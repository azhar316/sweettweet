from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('', views.UserProfileDetailView.as_view()),
    path('profile/', views.UserProfileDetailView.as_view(), name='user_detail'),
    path('profile/update/', views.UserProfileUpdateView.as_view(), name='user_update'),
]
