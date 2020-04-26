from django.urls import path

from . import views

app_name = 'hashtags'
urlpatterns = [
    path('<str:tag>/', views.HashTagView.as_view(), name='tag'),
    path(r'^ajax/list/$', views.tag_list, name='tag_list'),
]
