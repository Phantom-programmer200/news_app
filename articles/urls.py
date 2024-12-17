from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet
from .views import home
from .views import article_list, article_detail, news_page
from django.shortcuts import redirect


urlpatterns = [

    path('', home, name='home'),  # This maps the root URL to the home view
    path('', article_list, name='article_list'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('news/', news_page, name='news_page'),  # New URL for the news page
    path('users/', include('users.urls')),
    # Redirect root URL to news homepage
    path('', lambda request: redirect('news_home')),
]
