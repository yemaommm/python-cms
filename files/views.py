#codeing=utf-8
from django.shortcuts import render,HttpResponse
from django.db import connection,transaction
from django.template import loader,Context
from django import forms
from files.models import *
import json
import os
import HTMLParser
import cgi
import shutil

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def delfile(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        filename=request.POST['filename']
        nowpath=request.POST['nowpath']
        filename=html_parser.unescape(filename)
        nowpath=html_parser.unescape(nowpath)
        request.session['nowpath']=nowpath
        stmp=nowpath+'\\'+filename
        if os.path.isdir(stmp):
            shutil.rmtree(stmp,True)
        elif os.path.isfile(stmp):
            os.remove(stmp)
        return HttpResponse('ok')
    except Exception as err:
        return HttpResponse(err)

def mkfile(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        mkname=request.POST['mkname']
        mktext=request.POST['mktext']
        nowpath=request.POST['nowpath']
        mkname=html_parser.unescape(mkname)
        mktext=html_parser.unescape(mktext)
        nowpath=html_parser.unescape(nowpath)
        request.session['nowpath']=nowpath
        f=open(nowpath+'\\'+mkname,'w')
        f.write(mktext)
        f.close()
        return HttpResponse('ok')
    except Exception as err:
        return HttpResponse(err)


def mkdir(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        path=request.POST['nowpath']
        filename=request.POST['filename']
        path=html_parser.unescape(path)
        request.session['nowpath']=path
        filename=html_parser.unescape(filename)
        os.mkdir(path+"\\"+filename)
        return HttpResponse('ok')
    except Exception as err:
        return HttpResponse(err)

def readfile(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        path=request.POST['path']
        path=html_parser.unescape(path)
        str=open(path,'r')
        #str=cgi.escape(str.read())
        str=str.read()
        return HttpResponse(str)
    except Exception as err:
        return HttpResponse(err)

def find(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        path=request.POST['path']
        select=request.POST['select']
        path=html_parser.unescape(path)
        select=html_parser.unescape(select)
        if select=='fist':
            path=path[0:path.rfind('\\')]
            if path.find(request.session['basepath'])==-1:
                path=request.session['basepath']
        elif select=='home':
            path=request.session['basepath']
        #print path
        file=os.listdir(path)
        request.session['nowpath']=path
        isdir=[]
        isfile=[]
        for f in range(len(file)):
            if os.path.isdir(path+"\\"+file[f]):
                isdir.append(file[f])
            else:
                isfile.append(file[f])
        #filepath = os.path.join(path,file[0])
        filepath=os.path.abspath(path)
        #print filepath
        t=loader.get_template('fileList.html')
        c=Context({'isfile':isfile,'isdir':isdir,'path':path})
        return HttpResponse(t.render(c))
    except Exception as err:
        return HttpResponse(err)

def fileList(request):
    try:
        html_parser = HTMLParser.HTMLParser()
        path=request.POST['path']
        basepath=request.POST['basepath']
        path=html_parser.unescape(path)
        basepath=html_parser.unescape(basepath)
        if basepath!="":
            request.session['basepath']=basepath
        file=os.listdir(path)
        request.session['nowpath']=path
        isdir=[]
        isfile=[]
        for f in range(len(file)):
            if os.path.isdir(path+"\\"+file[f]):
                isdir.append(file[f])
            else:
                isfile.append(file[f])
        #filepath = os.path.join(path,file[0])
        filepath=os.path.abspath(path)
        #print filepath
        t=loader.get_template('fileList.html')
        c=Context({'isfile':isfile,'isdir':isdir,'path':path})
        return HttpResponse(t.render(c))
    except Exception as err:
        return HttpResponse(err)

def one(request):
    cursor = connection.cursor()
    cursor.execute('select username from auth_user')
    names = cursor.fetchall()
    #names=FilePath.objects.filter(name='idk')
    #names=FilePath.objects.all()
    re=()
    for name in names:
        re+=(((name[0],name[0]),))
        print re
    #re=json.dumps(re)
    #print json.loads(re)['123']
    return HttpResponse(re)

def index(request):
    #print 123
    posts=FilePath.objects.all()
    t=loader.get_template('files.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))


def upload(request):

   # A nested FieldStorage instance holds the file
   #print request.POST.get('nowpath')
   fileitem = request.FILES.getlist('file')
   for f in fileitem:
       #print f.read()
       wf=open(request.session['nowpath']+'\\'+f.name,'wb')
       wf.write(f.read())
       wf.close();
   #print request.FILES.getlist('file')

   return HttpResponse("error")
