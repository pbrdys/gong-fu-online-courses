from . import views
from django.urls import path

urlpatterns = [
    path('', views.course_overview.as_view(), name='course_overview'),
    path('add/', views.course_add, name="course_add"),
    path('edit_course/<int:course_id>', views.course_edit, name='course_edit'),
    path('delete_course/<int:course_id>', views.course_delete, name='course_delete'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]