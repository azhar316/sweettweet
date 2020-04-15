from django.shortcuts import render
from django.views import View

from .models import HashTag


class HashTagView(View):

    def get(self, request, tag, *args, **kwargs):
        obj, __ = HashTag.objects.get_or_create(tag=tag)
        return render(request, 'hashtags/tag_view.html', {'obj': obj})
