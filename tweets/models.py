from django.db import models
from django.conf import settings

from . import validators
from . import utils


class TweetLike(models.Model):
    """A model for tweet likes. This model is used to know the
     time a tweet was liked and the user who liked it."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetRetweet(models.Model):
    """A model for retweets of tweets. This model is used to know the
    time a tweet was retweeted and the user who retweeted it."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name="retweets")
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                             related_name='tweets')
    text = models.CharField(max_length=200, help_text='200 characters or fewer')
    media = models.FileField(upload_to=utils.get_file_path,
                             blank=True, null=True,
                             validators=[validators.validate_file_extension],
                             help_text='Image or Video File')
    likes = models.ManyToManyField(TweetLike, blank=True)
    retweets = models.ManyToManyField(TweetRetweet, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
