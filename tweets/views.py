from django.shortcuts import render

from .models import Tweet


def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/home.html', {'tweets': tweets})
