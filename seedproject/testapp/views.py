from django.shortcuts import render
from testapp.models import seed1
def display(request):
    seed_list = seed1.objects.all()
    return render(request,'testapp/index.html',{'seed_list':seed_list})
