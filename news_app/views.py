from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def news_home(request):
    # Replace with your news homepage template
    return render(request, 'news/home.html')
