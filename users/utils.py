import os


def get_image_path(instance, filename):
    return os.path.join('images', 'profile_pics', str(instance.user.id), filename)


def recent_activity_sort_helper(instance):
    try:
        return instance.updated
    except AttributeError:
        return instance.timestamp
