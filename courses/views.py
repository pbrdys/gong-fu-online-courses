from django.shortcuts import render

# Create your views here.
def course_overview(request):
    return render(
        request,
        "course_overview.html",
    )