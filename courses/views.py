from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.
class course_overview(generic.ListView):
    queryset = Course.objects.all()
    template_name = "course_overview.html"