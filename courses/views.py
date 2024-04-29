from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Course

# Create your views here.
class course_overview(generic.ListView):
    queryset = Course.objects.all()
    template_name = "course_overview.html"
    
    
def course_detail(request, slug):
    queryset = Course.objects.all()
    course = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "course_detail.html",
        {
            "course": course
        }
    )