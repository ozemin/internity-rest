from django.contrib import admin

from jobs.models import Job, JobApplication

# Register your models here.
admin.site.register(Job)
admin.site.register(JobApplication)
