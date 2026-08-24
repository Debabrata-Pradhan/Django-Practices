from django.shortcuts import render

from testapp.models import hyd_jobs
def hyd_jobs_view(request):
    jobs_list=hyd_jobs.objects.all()
    return render(request,'testapp/index.html',{'jobs_list':jobs_list})
