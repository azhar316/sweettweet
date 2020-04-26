import os

from sweettweet import settings


def get_file_path(instance, filename):
    file_extension = os.path.splitext(filename)[1]  # [0] is filename along with path
    if file_extension.lower() in settings.VALID_VIDEO_EXTENSIONS:
        path = os.path.join('videos', str(instance.user.id), filename)
    else:
        path = os.path.join('images', str(instance.user.id), filename)
    return path
