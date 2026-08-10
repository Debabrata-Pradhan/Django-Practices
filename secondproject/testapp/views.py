from django.http import HttpResponse
import datetime
def timing(response):
    date=datetime.datetime.now()
    m='<h1> The current  time is: '+ str(date) + '</h1>'
    return HttpResponse(m)
