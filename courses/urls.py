from . import views
from django.urls import path

urlpatterns = [
    path('', views.course_overview, name='course_overview'),
]