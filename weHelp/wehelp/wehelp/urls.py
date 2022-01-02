from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
