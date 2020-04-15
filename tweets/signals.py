import re

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Tweet
from hashtags.signals import parsed_hashtags


@receiver(post_save, sender=Tweet, dispatch_uid='tweet_save')
def create_hashtags(sender, instance, created, **kwargs):
    if created:
        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.text)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
