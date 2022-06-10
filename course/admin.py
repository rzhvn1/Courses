from django.contrib import admin

from .models import Course, Category, Contact, Branch
# Register your models here.

admin.site.register([Course, Category, Contact, Branch])
