from django.http import HttpResponse
def hyd_jobs(response):
    m='<h1>This is Hyd job notifications </h1>'
    return HttpResponse(m)
def blr_jobs(response):
    m='<h1>This is Blr job notifications </h1>'
    return HttpResponse(m)
