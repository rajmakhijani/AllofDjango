from django.contrib import admin
from .models import inputmodel

class inputaddmin(admin.ModelAdmin):
    list_display=['inputa','inputb']
admin.site.register(inputmodel,inputaddmin)

# Register your models here.
