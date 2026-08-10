from django.http import HttpResponse
def display(request):
    m='<h1>Hello </h1>'
    return HttpResponse(m)