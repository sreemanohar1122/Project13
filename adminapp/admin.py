from django.contrib import admin
from .models import Jobs

class JobsModelAdmin(admin.ModelAdmin):
    list_display = ['jobid,title,skills,description']
    list_filter = ['title']
    class Meta:
        model=Jobs
admin.site.register(Jobs,JobsModelAdmin)


# Register your models here.
