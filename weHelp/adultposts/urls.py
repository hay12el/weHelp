from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'adultposts'

urlpatterns = [
    url(r'^create_post/$', views.post_create, name='post_create'),
    path('post/<str:pk>/', views.current_post, name='current_post'),
]
