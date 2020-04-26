from django.db import models

from tweets.models import Tweet


class HashTag(models.Model):

    tag = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_tweets(self):
        return Tweet.objects.filter(text__icontains='#'+self.tag)
