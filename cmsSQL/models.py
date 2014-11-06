from django.db import models
from django.contrib import admin

# Create your models here.
class sqlconection(models.Model):
    name=models.CharField(max_length=150)
    host=models.CharField(max_length=150)
    user=models.CharField(max_length=150)
    passwd=models.CharField(max_length=150,blank=True)
    port=models.CharField(max_length=150)
    db=models.CharField(max_length=150,blank=True)

class sqlconectionAdmin(admin.ModelAdmin):
    list_display=('name','host','user','passwd','port','db')