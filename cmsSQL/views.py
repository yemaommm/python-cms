#coding=utf-8
from django.shortcuts import render,HttpResponse
from django.template import loader,Context
from models import *
import json
import mysqlconn

# Create your views here.

def dbQ(request):
    cur=sqlconection.objects.all()
    t=loader.get_template('sql.html')
    c=Context({'posts':cur})
    return HttpResponse(t.render(c))
    #return HttpResponse('123')

def postConn(request):
    sqlname= request.POST.get('name')
    cur=sqlconection.objects.get(name=sqlname)
    request.session['sqlhost']=cur.host
    request.session['sqluser']=cur.user
    request.session['sqlpasswd']=cur.passwd
    request.session['port']=cur.port
    to=[]
    sql=[]
    sql.append("show databases")
    Q=mysqlconn.conn(cur.host,cur.user,cur.passwd,cur.port,sql)
    for stmp in Q:
        to.append(stmp[0])
    t=loader.get_template('sqldb.html')
    c=Context({'posts':to})
    return HttpResponse(t.render(c))
    #return HttpResponse('123')

def postdb(request):
    sqldb= request.POST.get('name')
    request.session['sqldb']=sqldb
    host=request.session['sqlhost']
    user=request.session['sqluser']
    passwd=request.session['sqlpasswd']
    port=request.session['port']
    to=[]
    sql=[]
    sql.append("use "+sqldb)
    sql.append("show tables")
    Q=mysqlconn.conn(host,user,passwd,port,sql)
    for stmp in Q:
        to.append(stmp[0])
    t=loader.get_template('sqltable.html')
    c=Context({'posts':to})
    return HttpResponse(t.render(c))
    #return HttpResponse('123')

def posttable(request):
    sqltable= request.POST.get('name')
    host=request.session['sqlhost']
    user=request.session['sqluser']
    passwd=request.session['sqlpasswd']
    port=request.session['port']
    sqldb=request.session['sqldb']
    #to=[]
    sql=[]
    sql.append("use "+sqldb)
    sql.append("select * from "+sqltable)
    dataQ=mysqlconn.conn(host,user,passwd,port,sql)
    sql.append("use "+sqldb)
    sql.append("show columns from "+sqltable)
    R=mysqlconn.conn(host,user,passwd,port,sql)
    #print dataQ
    #print R
    col=[]
    rows=[]
    for j in range(len(R)):
        if R[j][3]=='PRI':
            col.append({'field':'*'+R[j][0],'title':'*'+R[j][0]})
        else:
            col.append({'field':R[j][0],'title':R[j][0]})
    for i in range(len(dataQ)):
        stmp={}
        for j in range(len(col)):
            stmp[col[j]['field']]=str(dataQ[i][j])
        rows.append(stmp)

    t=loader.get_template('tables.html')
    c=Context({'col':json.dumps(col),'rows':json.dumps(rows)})
    print len(t.render(c))
    return HttpResponse(t.render(c))
    #return HttpResponse('123')