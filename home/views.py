from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Gong Fu Online Courses. Learn step by step from your own place at your own pace")