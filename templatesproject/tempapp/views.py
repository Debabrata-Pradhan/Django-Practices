from django.shortcuts import render


def temp(request):
    return render(request,'testapp/index.html')
