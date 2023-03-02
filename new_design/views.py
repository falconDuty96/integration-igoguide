from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def home(request):
    return render(request, 'index.html')


# def user_connect(request):
# def connect_pro(request):
