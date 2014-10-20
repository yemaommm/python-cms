from django.shortcuts import render,HttpResponse
from django.db import connection,transaction
from django.template import loader,Context
from files.models import *
import json
import os
import HTMLParser

# Create your views here.

def fileList(request):
    html_parser = HTMLParser.HTMLParser()
    path=request.GET['path']
    path=html_parser.unescape(path)
    print path
    file=os.listdir(path)
    isdir=[]
    isfile=[]
    for f in range(len(file)):
        if os.path.isdir(path+"\\"+file[f]):
            isdir.append(file[f])
        else:
            isfile.append(file[f])
    #filepath = os.path.join(path,file[0])
    filepath=os.path.abspath(path)
    print filepath
    t=loader.get_template('fileList.html')
    c=Context({'isfile':isfile,'isdir':isdir,'path':filepath})
    return HttpResponse(t.render(c))

def one(request):
    #cursor = connection.cursor()
    #cursor.execute('select * from auth_user')
    #names = cursor.fetchall()
    #names=FilePath.objects.filter(name='idk')
    names=FilePath.objects.all()
    re={}
    for name in names:
        re[name.name]=name.path
    re=json.dumps(re)
    #print json.loads(re)['123']
    return HttpResponse(re)

def index(request):
    #print 123
    posts=FilePath.objects.all()
    t=loader.get_template('files.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))
    
