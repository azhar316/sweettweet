# Generated by Django 3.0.5 on 2020-04-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='tag',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]