from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Course
from .forms import CourseForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
class course_overview(generic.ListView):
    queryset = Course.objects.all()
    template_name = "course_overview.html"
    
    
def course_detail(request, slug):
    queryset = Course.objects.all()
    course = get_object_or_404(queryset, slug=slug)
    lessons = course.lessons.all()
    
    return render(
        request,
        "course_detail.html",
        {
            "course": course,
            "lessons": lessons,
        }
    )
    
    
def course_add(request):
    # Handle the POST request from the course form
    if request.method == "POST":
        course_form = CourseForm(data=request.POST)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.save()
            # display success message string:
            messages.add_message(
                request, messages.SUCCESS,
                'Course successfully added'
            )
            
    course_form = CourseForm()
    
    return render(
        request,
        "course_add.html",
        {
            "course_form": course_form,
        }
    )
    
def course_edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        course_form = CourseForm(data=request.POST, instance=course)
        
        if course_form.is_valid():
            course_form.save()
            messages.add_message(request, messages.SUCCESS, 'Course Updated!')
            return HttpResponseRedirect(reverse('course_overview'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating course!')
    else:
        # If it's a GET request, initialize the form with the instance data
        course_form = CourseForm(instance=course)

    return render(request, 'course_edit.html', {'course_edit_form': course_form, 'course': course})
        
    
    
    
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    course.delete()
    messages.add_message(request, messages.SUCCESS, 'Course deleted!')
    
    return HttpResponseRedirect(reverse("course_overview"))