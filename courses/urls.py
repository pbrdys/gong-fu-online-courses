from . import views
from django.urls import path

urlpatterns = [
    path('', views.course_overview.as_view(), name='course_overview'),

    path('add/',
         views.course_add, name="course_add"),

    path('edit_course/<int:course_id>',
         views.course_edit, name='course_edit'),

    path('delete_course/<int:course_id>',
         views.course_delete, name='course_delete'),

    path('<slug:slug>/',
         views.course_detail, name='course_detail'),

    # Lesson Urls
    path('<slug:course_slug>/add_lesson/',
         views.lesson_add, name="lesson_add"),

    path('<slug:course_slug>/<slug:lesson_slug>/',
         views.lesson_detail, name='lesson_detail'),

    path('<slug:course_slug>/<slug:lesson_slug>/edit/',
         views.lesson_edit, name='lesson_edit'),

    path('<slug:course_slug>/delete/<int:lesson_id>/',
         views.lesson_delete, name='lesson_delete'),
]
