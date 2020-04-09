import os

from django.core.exceptions import ValidationError

from sweettweet import settings


def validate_file_extension(value):
    file_extension = os.path.splitext(value.name)[1]  # [0] is filename along with path
    if file_extension.lower() not in settings.VALID_FILE_EXTENSIONS:
        raise ValidationError('Unsupported File type.')
