from django.shortcuts import render
def css_view(request):
    d={
        's1':'Django', 's2':'HTML', 's3':'CSS','s4':'Python','s5':'MySQL'
    }
    return render(request,'testapp/index.html',d)

