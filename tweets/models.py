from django.db import models
from django.conf import settings

from . import validators
from . import utils


class TweetManager(models.Manager):

    def like_toggle(self, user, tweet):
        tweet_like = TweetLike.objects.filter(user=user, tweet=tweet)
        if tweet_like.exists():
            tweet_like.delete()
            liked = False
        else:
            __ = TweetLike.objects.create(user=user, tweet=tweet)
            liked = True
        return liked

    def retweet(self, user, tweet):
        tweet_retweet = TweetRetweet.objects.filter(user=user, tweet=tweet)
        if not tweet_retweet.exists():
            tweet_retweet = TweetRetweet.objects.create(user=user, tweet=tweet)
        return tweet_retweet


class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                             related_name='tweets')
    text = models.CharField(max_length=200, help_text='200 characters or fewer')
    image = models.ImageField(upload_to=utils.get_file_path,
                              blank=True, null=True,
                              validators=[validators.validate_file_extension],
                              help_text='Image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TweetManager()

    def __str__(self):
        return self.text


class TweetLike(models.Model):
    """A model for tweet likes. This model is used to know the
     time a tweet was liked and the user who liked it."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name="tweet_likes")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,
                              related_name="likes", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetRetweet(models.Model):
    """A model for retweets of tweets. This model is used to know the
    time a tweet was retweeted and the user who retweeted it."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name="tweet_retweets")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,
                              related_name="retweets", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetComment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tweetcomments")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=200, help_text='200 characters or fewer')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
