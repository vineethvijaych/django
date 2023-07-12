from django.contrib import admin
from . models import *
from . models import pictures

# Register your models here.

admin.site.register(student)
admin.site.register(pictures)