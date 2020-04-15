from django.dispatch import Signal, receiver

from .models import HashTag


parsed_hashtags = Signal(providing_args=['hashtag_list'])


@receiver(parsed_hashtags, dispatch_uid='hashtag')
def create_hashtags(sender, hashtag_list, *args, **kwargs):
    for tag in hashtag_list:
        obj, __ = HashTag.objects.get_or_create(tag=tag)
