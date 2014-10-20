from django.shortcuts import render,HttpResponse
from django.db import connection,transaction
from django.template import loader,Context
from files.models import *
import json

# Create your views here.

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
    posts=FilePath.objects.all()
    t=loader.get_template('files.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))
    
