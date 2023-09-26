from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# index.html 처리
def index(request):
    return render(request,
                  'jeapp/index.html',
                  {})