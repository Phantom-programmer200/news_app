# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse
from django.shortcuts import render
import requests
from .forms import SearchForm


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def home(request):
    return render(request, 'home.html')


def article_list(request):
    # This is a placeholder for the article list view
    return render(request, 'home.html')  # You can customize this as needed


def article_detail(request, article_id):
    # This is a placeholder for article detail view
    return render(request, 'article_detail.html', {'article_id': article_id})


def news_page(request):
    api_key = '35ce67ced2c2439aa90348a44a7931ec'  # Replace with your actual API key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])

    # Search functionality
    query = request.GET.get('query', '')
    if query:
        articles = [
            article for article in articles
            if (article.get('title') and query.lower() in article['title'].lower()) or
               (article.get('description') and query.lower()
                in article['description'].lower())
        ]

    return render(request, 'news_page.html', {'articles': articles, 'query': query})
