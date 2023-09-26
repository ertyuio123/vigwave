from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# imsi.html 처리
def imsi(request):
    return render(request,
                  'mainapp/imsi.html',
                  {})

# index.html 처리
def index(request):
    return render(request,
                  'mainapp/index.html',
                  {})