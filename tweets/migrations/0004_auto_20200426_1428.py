# Generated by Django 3.0.5 on 2020-04-26 08:58

from django.db import migrations, models
import tweets.utils
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20200415_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='media',
        ),
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, help_text='Image', null=True, upload_to=tweets.utils.get_file_path, validators=[tweets.validators.validate_file_extension]),
        ),
    ]
