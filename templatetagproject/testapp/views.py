from django.shortcuts import render
import datetime
def tags(request):
    date=datetime.datetime.now()
    my_dict={'date':date}
    return render(request,'testapp/index.html',context=my_dict)
def msg(request):
    return render(request,'testapp/message.html')