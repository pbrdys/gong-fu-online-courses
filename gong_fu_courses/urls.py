"""
URL configuration for gong_fu_courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('courses/', include('courses.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_view
from contact import views as contact_view
from courses import views as course_views

urlpatterns = [
    path("", include("home.urls"), name="home-urls"),
    path("custom/", include("custom_pages.urls"), name="custom-pages-urls"),
    path("courses/", include("courses.urls"), name="courses-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

handler404 = 'custom_pages.views.custom_404'
