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
]
