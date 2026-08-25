from django.contrib import admin
from testapp.models import hyd_jobs
class hyd_jobs_admin(admin.ModelAdmin):
    list_display=['title','eligibility','company','salary','location','contact']
admin.site.register(hyd_jobs,hyd_jobs_admin)
