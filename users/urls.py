from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('', views.UserProfileDetailView.as_view()),
    path('profile/', views.UserProfileDetailView.as_view(), name='user_detail'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/update/', views.UserProfileUpdateView.as_view(), name='user_update'),
]
