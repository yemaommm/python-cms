from django.db import models
from django.contrib import admin

# Create your models here.

class FilePath(models.Model):
    name=models.CharField(max_length=150)
    path=models.CharField(max_length=150)

class FilePathAdmin(admin.ModelAdmin):
    list_display=('name','path')
