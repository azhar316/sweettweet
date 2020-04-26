from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse

from .models import HashTag


class HashTagView(generic.View):

    def get(self, request, tag, *args, **kwargs):
        tag = get_object_or_404(HashTag, tag=tag)
        return render(request, 'hashtags/tag_view.html', {'tag': tag})


def tag_list(request):
    print("tag_list")
    if request.is_ajax():
        tags = HashTag.objects.all().order_by('-created')[:10]
        return JsonResponse({'tags': tags})
    return redirect('hashtags:tag')
