from .models import Course, Lesson
from django import forms


class CourseForm(forms.ModelForm):
    """
    Form for creating and updating Course objects.

    Attributes:
        title (str): The title of the course.
        slug (str): The slug of the course.
        description (str): The description of the course.
        category (int): The category of the course.
        featured_image (str): The URL of the featured image for the course.
        content (str): The content of the course.
        level (int): The level of the course.
        order (int): The order of the course.
    """

    class Meta:
        model = Course
        fields = (
            'title', 'slug', 'description',
            'category', 'featured_image', 'content', 'level', 'order')

        error_messages = {
            '__all__': {
                'required': "This field is required. LOL",
            },
        }


class LessonForm(forms.ModelForm):
    """
    Form for creating and updating Lesson objects.

    Attributes:
        title (str): The title of the lesson.
        slug (str): The slug of the lesson.
        video_url (str): The URL of the video for the lesson.
        description (str): The description of the lesson.
        recommendation (str): Recommendations for the lesson.
        order (int): The order of the lesson.
    """

    class Meta:
        model = Lesson
        fields = (
            'title', 'slug', 'video_url',
            'description', 'recommendation', 'order')
