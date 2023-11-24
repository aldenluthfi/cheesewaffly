from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def handler400(request, exception):
    return HttpResponse(render(request, '400.html'), status=500)

def handler403(request, exception):
    return HttpResponse(render(request, '403.html'), status=403)

def handler404(request, exception):
    return HttpResponse(render(request, '404.html'), status=404)

def handler500(request):
    return HttpResponse(render(request, '500.html'), status=500)