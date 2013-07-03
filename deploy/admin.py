from django.contrib import admin
from deploy.models import Project, IntervalsSetting, Operation, Person

class ProjectAdmin(admin.ModelAdmin):
    fields=('name', 'cappath', 'logfile', 'dlock', 'rlock', 'lastupdatetime')

class IntervalsSettingAdmin(admin.ModelAdmin):
    list_display=('name', 'deploytimeintervals', 'rollbacktimeintervals',)

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(IntervalsSetting, IntervalsSettingAdmin)
admin.site.register(Operation)
admin.site.register(Person)
