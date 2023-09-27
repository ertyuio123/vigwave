from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# index.html 처리
def about(request):
    return render(request,
                  'mgapp/about.html',
                  {})
def index(request):
    return render(request,
                  'mgapp/index.html',
                  {})