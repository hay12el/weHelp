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
    url(r'^helper/$', views.young_hompage, name='young_homepage'),
    url(r'^saved_posts/$', views.young_saved_posts, name='saved_posts'),
    path('success/<str:pk>/', views.got_helped, name='got_helped'),
    url(r'^admin_homepage/$', views.admin_homepage, name="admin_homepage"),
    url(r'^admin_young/$', views.admin_young, name="admin_young"),
    url(r'^admin_adult/$', views.admin_adult, name="admin_adult"),
    url(r'^admin_posts/$', views.admin_posts, name="admin_post"),
    path('delete_young/<str:pk>/', views.delete_young, name='delete_young'),
    path('delete_adult/<str:pk>/', views.delete_adult, name='delete_adult'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    path('success_check/<str:pk>/',
         views.admin_got_helped, name='admin_got_helped'),
]
