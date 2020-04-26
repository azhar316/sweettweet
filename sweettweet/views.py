from django.shortcuts import render

from tweets.models import Tweet
from users.models import User
from hashtags.models import HashTag


def search_view(request):
    query = request.GET.get('q')
    tweets = Tweet.objects.filter(text__contains=query)
    users = User.objects.filter(username__contains=query)
    tags = HashTag.objects.filter(tag__contains=query)
    return render(request, 'sweettweet/search.html',
                  {'tweets': tweets, 'users': users, 'tags': tags})
