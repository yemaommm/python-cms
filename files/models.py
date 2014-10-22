#coding=utf-8
from django.db import models
from django.contrib import admin
from django.db import connection

# Create your models here.

class FilePath(models.Model):
    cursor = connection.cursor()
    cursor.execute('select username from auth_user')
    names = cursor.fetchall()
    re=()
    for name in names:
        re+=(((name[0],name[0]),))
    print names
    
    name=models.CharField(max_length=150)
    path=models.CharField(max_length=150)
    user=models.CharField(verbose_name='用户'
                          ,choices=re,max_length=100)

class FilePathAdmin(admin.ModelAdmin):
    list_display=('name','path','user')
