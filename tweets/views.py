from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tweet
from .models import TweetComment
from .forms import TweetForm, TweetCommentForm


class IndexView(generic.ListView):

    model = Tweet
    template_name = 'tweets/home.html'
    context_object_name = 'tweets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweet_form'] = TweetForm()
        return context


class TweetCreateView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return redirect('tweets:index')

    def post(self, *args, **kwargs):
        tweet_form = TweetForm(self.request.POST)
        tweet = tweet_form.save(commit=False)
        tweet.user = self.request.user
        tweet.save()
        return HttpResponseRedirect(reverse('tweets:tweet_detail', args=(tweet.id,)))


class TweetDetailView(generic.DetailView):

    model = Tweet
    template_name = 'tweets/tweet_detail.html'
    context_object_name = 'tweet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = TweetCommentForm()
        return context


class TweetUpdateView(LoginRequiredMixin, generic.UpdateView):

    form_class = TweetForm
    template_name = 'tweets/tweet_update.html'

    def get_success_url(self):
        return reverse('tweets:tweet_detail', args=(self.object.id,))

    def get_queryset(self):
        return Tweet.objects.filter(user=self.request.user)


class TweetDeleteView(LoginRequiredMixin, generic.DeleteView):

    template_name = 'tweets/confirm_tweet_delete.html'
    success_url = reverse_lazy('tweets:home')

    def get_queryset(self):
        return Tweet.objects.filter(user=self.request.user)
