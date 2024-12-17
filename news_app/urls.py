"""
URL configuration for news_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import news_home

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the articles app URLs
    path('articles/', include('articles.urls')),
    path('', include('articles.urls')),  # Assuming you have articles URLs
    # path('users/', include(('users.urls', 'users'), namespace='users')),  # Add namespace here
    path('users/', include('users.urls')),  # Include users URLs
    path('', news_home, name='news_home'),
]
