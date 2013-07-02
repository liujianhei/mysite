from django.contrib import admin
from deploy.models import Project, CommonSetting, Operation

class ProjectAdmin(admin.ModelAdmin):
    fields=('name', 'cappath', 'logfile', 'dlock', 'rlock', 'lastupdatetime')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(CommonSetting)
admin.site.register(Operation)
