from django.http import HttpResponse
def views1(response):
    m='<h1> This is fro views1 </h1>'
    return HttpResponse(m)