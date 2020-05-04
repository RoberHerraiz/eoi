from django.contrib import admin

from . import models

# Register your models here.

class PowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')

<<<<<<< HEAD
admin.site.register(models.Power, PowerAdmin)

class MetaHumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'active' ,'level', 'ally')
    list_filter = ('active', 'level', 'powers', 'ally')

admin.site.register(models.MetaHuman, MetaHumanAdmin)
=======

admin.site.register(models.Power, PowerAdmin)


class MetaHumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'active', 'level')
    list_filter = ('active', 'level', 'powers') 

admin.site.register(models.MetaHuman, MetaHumanAdmin)

>>>>>>> 6948fa3ec2bf31c512f81f78cab02690591b5d62
