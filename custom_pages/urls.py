from . import views
from django.urls import path

urlpatterns = [
    path('access-denied/', views.access_denied, name='access_denied'), 
    path('500/', views.custom_500),
]