from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^my_posts/$', views.adult_page, name="my_posts"),
    url(r'^checking/$', views.check, name='check_page'),
    url(r'^adult_login/$', views.adult_login, name='Alogin'),
    url(r'^young_login/$', views.young_login, name='Ylogin'),
    path('success/<str:pk>/', views.got_helped, name='got_helped'),
]
