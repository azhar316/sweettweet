# Generated by Django 3.0.5 on 2020-04-15 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0002_tweetcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='retweets',
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='tweets.Tweet'),
        ),
        migrations.AddField(
            model_name='tweetretweet',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retweets', to='tweets.Tweet'),
        ),
        migrations.AlterField(
            model_name='tweetlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweetretweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet_retweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
