from django.shortcuts import render
def view(request):
    subjects={'s1':"Python",'s2':"Django",'s3':"MySQL",'s4':"MongoDB"}
    return render(request,'testapp/index.html', subjects)