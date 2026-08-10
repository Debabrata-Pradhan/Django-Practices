from django.http import HttpResponse
def views2(response):
    m='<h1> This is fro views2</h1>'
    return HttpResponse(m)