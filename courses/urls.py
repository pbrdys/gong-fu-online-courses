from . import views
from django.urls import path

urlpatterns = [
    path('', views.course_overview.as_view(), name='course_overview'),
    path('add/', views.course_add, name="course_add"),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]