from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    msg = 'Start Page'
    return HttpResponse(msg)

def hello(request):
    msg = 'Hi'
    return HttpResponse( msg)
