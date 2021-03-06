from django.urls import path

from . import views


app_name = 'tweets'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('home/', views.IndexView.as_view(), name='home'),
    path('tweet/create/', views.TweetCreateView.as_view(), name='tweet_create'),
    path('tweet/detail/<int:pk>/', views.TweetDetailView.as_view(), name='tweet_detail'),
    path('tweet/update/<int:pk>/', views.TweetUpdateView.as_view(), name='tweet_update'),
    path('tweet/delete/<int:pk>/', views.TweetDeleteView.as_view(), name='tweet_delete'),
    path('tweet/comment/create/', views.TweetCommentCreateView.as_view(), name='tweet_comment_create'),
    path('tweet/comment/update/<int:pk>/', views.TweetCommentUpdateView.as_view(), name='tweet_comment_update'),
    path('tweet/comment/delete/', views.TweetCommentDeleteView.as_view(), name='tweet_comment_delete'),
    path('tweet/like/', views.tweet_like, name='tweet_like'),
    path('tweet/retweet/', views.tweet_retweet, name='tweet_retweet'),
    path('tweet/retweet/delete/', views.delete_retweet, name='tweet_retweet_delete'),
]
