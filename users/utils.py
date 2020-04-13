import os


def get_image_path(instance, filename):
    return os.path.join('images', 'profile_pics', str(instance.user.id), filename)
