from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse("hi")