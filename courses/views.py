from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Course, Lesson
from .forms import CourseForm, LessonForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from custom_pages.views import user_has_permission, user_is_superuser, access_denied


# Create your views here.
class course_overview(generic.ListView):
    """
    View for displaying an overview of all courses.

    Attributes:
        queryset: Queryset of all Course objects.
        template_name: The name of the template used for rendering the view.
    """
    queryset = Course.objects.all()
    template_name = "course_overview.html"
    paginate_by = 8


@login_required
def course_detail(request, slug):
    """
    View for displaying details of a specific course.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the course.

    Returns:
        HttpResponse: Rendered course detail template.

    Raises:
        Http404: If the requested course does not exist.
    """
    if user_has_permission(request.user):
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
    else:
        return access_denied(request)


@login_required
def course_add(request):
    """
    View for adding a new course.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered course add template.
    """
    if user_is_superuser(request.user):
        # Handle the POST request from the course form
        if request.method == "POST":
            course_form = CourseForm(data=request.POST, files=request.FILES)
            if course_form.is_valid():
                course = course_form.save(commit=False)
                course.save()
                # Display success message
                messages.add_message(
                    request, messages.SUCCESS,
                    'Course successfully added'
                )
                return redirect('course_overview')
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Form not valid'
                )
        else:
            course_form = CourseForm()

        return render(
            request,
            "course_add.html",
            {
                "course_form": course_form,
            }
        )
    else:
        return access_denied(request)


@login_required
def course_edit(request, course_id):
    """
    View for editing an existing course.

    Args:
        request (HttpRequest): The HTTP request object.
        course_id (int): The ID of the course to be edited.

    Returns:
        HttpResponse: Rendered course edit template.

    Raises:
        Http404: If the requested course does not exist.
    """
    if user_is_superuser(request.user):
        course = get_object_or_404(Course, pk=course_id)
        if request.method == "POST":
            course_form = CourseForm(
                data=request.POST,
                files=request.FILES,
                instance=course)

            if course_form.is_valid():
                course_form.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Course Updated!')

                return HttpResponseRedirect(reverse('course_overview'))
            else:
                messages.add_message(
                    request, messages.ERROR, 'Error updating course!')
        else:
            # If it's a GET request, initialize the form with the instance data
            course_form = CourseForm(instance=course)

        return render(
            request, 'course_edit.html',
            {'course_edit_form': course_form, 'course': course})

    else:
        return access_denied(request)


@login_required
def course_delete(request, course_id):
    """
    View for deleting an existing course.

    Args:
        request (HttpRequest): The HTTP request object.
        course_id (int): The ID of the course to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the course overview page.

    Raises:
        Http404: If the requested course does not exist.
    """
    if user_is_superuser(request.user):
        course = get_object_or_404(Course, pk=course_id)
        if request.method == "POST":
            course.delete()
            messages.add_message(request, messages.SUCCESS, 'Course deleted!')
            return HttpResponseRedirect(reverse('course_overview'))
        else:
            return render(
                request,
                'course_delete.html',
                {'course': course})

    else:
        return access_denied(request)


@login_required
def lesson_detail(request, course_slug, lesson_slug):
    """
    View for displaying details of a specific lesson.

    Args:
        request (HttpRequest): The HTTP request object.
        course_slug (str): The slug of the course to which the lesson belongs.
        lesson_slug (str): The slug of the lesson.

    Returns:
        HttpResponse: Rendered lesson detail template.

    Raises:
        Http404: If the requested course or lesson does not exist.
    """
    if user_has_permission(request.user):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course)
        return render(
            request,
            'lesson_detail.html',
            {
                'lesson': lesson,
                'course': course
            })
    else:
        return access_denied(request)


@login_required
def lesson_add(request, course_slug):
    """
    View for adding a new lesson to a course.

    Args:
        request (HttpRequest): The HTTP request object.
        course_slug (str): The slug of the course

    Returns:
        HttpResponse: Rendered lesson add template.
    """
    if user_is_superuser(request.user):
        course = get_object_or_404(Course, slug=course_slug)

        if request.method == "POST":
            lesson_form = LessonForm(data=request.POST)
            if lesson_form.is_valid():
                lesson = lesson_form.save(commit=False)
                lesson.course = course
                lesson.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Lesson successfully added'
                )
                return redirect('course_detail', slug=course_slug)
        else:
            lesson_form = LessonForm()

        return render(
            request,
            "lesson_add.html",  # Ensure the template path is correct
            {
                "lesson_form": lesson_form,
                "course": course,
            }
        )
    else:
        return access_denied(request)


@login_required
def lesson_edit(request, course_slug, lesson_slug):
    """
    View for editing an existing lesson.

    Args:
        request (HttpRequest): The HTTP request object.
        course_slug (str): The slug of the course to which the lesson belongs.
        lesson_slug (str): The slug of the lesson to be edited.

    Returns:
        HttpResponse: Rendered lesson edit template.

    Raises:
        Http404: If the requested course or lesson does not exist.
    """
    if user_is_superuser(request.user):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course)

        if request.method == "POST":
            lesson_form = LessonForm(data=request.POST, instance=lesson)
            if lesson_form.is_valid():
                lesson_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Lesson successfully updated'
                )
                return redirect('course_detail', slug=course_slug)

        else:
            lesson_form = LessonForm(instance=lesson)

        return render(
            request,
            'lesson_edit.html',
            {
                'lesson_form': lesson_form,
                'course': course,
                'lesson': lesson
            }
        )
    else:
        return access_denied(request)


@login_required
def lesson_delete(request, lesson_id, course_slug):
    """
    View for deleting an existing lesson.

    Args:
        request (HttpRequest): The HTTP request object.
        lesson_id (int): The ID of the lesson to be deleted.
        course_slug (str): The slug of the course

    Returns:
        HttpResponseRedirect: Redirects to the course detail page.

    Raises:
        Http404: If the requested lesson does not exist.
    """
    if user_is_superuser(request.user):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        if request.method == "POST":
            lesson.delete()
            messages.add_message(request, messages.SUCCESS, 'Lesson deleted!')
            return redirect('course_detail', slug=course_slug)
        else:
            return render(
                request,
                'lesson_delete.html',
                {
                    'lesson': lesson,
                    'course': course
                }
            )
    else:
        return access_denied(request)
