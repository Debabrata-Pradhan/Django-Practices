from django.http import HttpResponse
import datetime
def greeting(response):
    hour=datetime.datetime.now()
    h=int(hour.strftime('%H'))
    m='<h1>Hello!'
    if h<12:
        m+='Good Morning</h1>'
    elif h<16:
        m+='Good Afternoon</h1>'
    elif h<21:
        m+='Good Evening</h1>'
    else:
        m+='Good Night</h1>'
    return HttpResponse(m)

