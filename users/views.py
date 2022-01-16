from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPage(request):
    return HttpResponse("i am starting page")

def prem(request):
    return HttpResponse("hello mate this is prem sai vittal")