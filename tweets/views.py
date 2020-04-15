from django.shortcuts import (render, HttpResponseRedirect,
                              redirect, reverse, get_object_or_404)
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Tweet,  TweetComment, TweetRetweet
from .forms import TweetForm, TweetCommentForm


class IndexView(generic.ListView):

    model = Tweet
    template_name = 'tweets/home.html'
    context_object_name = 'tweets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweet_form'] = TweetForm()
        return context


# CRUD views of Tweet Model

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


# CRUD views of TweetComment

class TweetCommentCreateView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return reverse('tweets:home')

    def post(self, *args, **kwargs):
        tweet_comment_form = TweetCommentForm(self.request.POST)
        tweet_comment = tweet_comment_form.save(commit=False)
        tweet_comment.user = self.request.user
        tweet = get_object_or_404(Tweet, id=self.request.POST.get('tweet_id'))
        tweet_comment.tweet = tweet
        tweet_comment.save()
        return redirect(self.request.POST.get('previous_page', '/'))


# No need of Detail View for TweetComment

class TweetCommentUpdateView(LoginRequiredMixin, generic.UpdateView):

    form_class = TweetCommentForm
    template_name = 'tweets/tweet_comment_update.html'

    def get_queryset(self):
        return TweetComment.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('tweets:tweet_detail', args=(self.object.tweet.id,))


class TweetCommentDeleteView(LoginRequiredMixin, generic.DeleteView):

    # Use javascript confirmation for deleting a TweetComment.
    # Use the form post method to bypass django's delete confirmation
    # process.

    # template_name = 'tweets/confirm_tweet_comment_delete.html'
    context_object_name = 'tweet_comment'

    def get_object(self, queryset=None):
        queryset = TweetComment.objects.filter(user=self.request.user)
        object = get_object_or_404(queryset, id=self.request.POST.get('comment_id'))
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_page'] = self.request.POST.get('previous_page', '/')
        return context

    def get_success_url(self):
        return self.request.POST.get('previous_page', '/')


@login_required
def tweet_like(request):
    if request.method == "GET":
        return redirect('/')
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    liked = Tweet.objects.like_toggle(request.user, tweet)
    return redirect(request.POST.get('previous_page'))


@login_required
def tweet_retweet(request):
    if request.method == "GET":
        return redirect('/')
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    retweet = Tweet.objects.retweet(request.user, tweet)
    return redirect(request.POST.get('previous_page'))


@login_required
def delete_retweet(request):
    if request.method == "GET":
        return redirect('/')
    tweet = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    retweet = get_object_or_404(TweetRetweet, user=request.user, tweet=tweet)
    retweet.delete()
    return redirect(request.POST.get('previous_page'))
