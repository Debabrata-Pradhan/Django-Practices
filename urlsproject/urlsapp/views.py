from django.http import HttpResponse
import datetime
def message1(response):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    return HttpResponse(h)
def message2(response):
    m='<h1>Its been so long to meet you</h1>'
    return HttpResponse(m)
def message3(response):
    m='<h1>Have a good time</h1>'
    return HttpResponse(m)
def message4(response):
    m='<h1>Awesome</h1>'
    return HttpResponse(m)