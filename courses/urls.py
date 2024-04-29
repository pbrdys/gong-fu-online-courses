from . import views
from django.urls import path

urlpatterns = [
    path('', views.course_overview.as_view(), name='course_overview'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]