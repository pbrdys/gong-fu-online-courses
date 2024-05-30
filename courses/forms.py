from .models import Course, Lesson
from django import forms


class CourseForm(forms.ModelForm):
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
    class Meta:
        model = Lesson
        fields = (
            'title', 'slug', 'video_url',
            'description', 'recommendation', 'order')
