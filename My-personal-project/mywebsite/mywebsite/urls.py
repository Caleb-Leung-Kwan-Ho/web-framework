"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Interest/',include('Interest.urls')),
    path('technical_skills/',include('technical_skills.urls')),
    path('homepage/',include('homepage.urls')),
    path('softskills/',include('softskills.urls')),
    path('Certification/',include('Certification.urls')),
    path('CV/',include('CV.urls')),
    re_path(r'^$',views.homepage),
]
    
urlpatterns += staticfiles_urlpatterns()