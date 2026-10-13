from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!", content_type="text/plain ; charset=utf-8")

def index(request):
    return render(request, 'index.html')

def my_html(request):
    return render(request, 'index.html')
