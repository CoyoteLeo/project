"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done, password_reset, \
    password_reset_done, password_reset_confirm, password_reset_complete
from .views import Login, logout_action, ProfileView, Register, PasswordChange

admin.autodiscover()

urlpatterns = [
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logout_action, name='logout'),
    url(r'^password_change/$', PasswordChange.as_view(), name='password_change'),
    url(r'^password_change/done/$', password_change_done, name='password_change_done'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', password_reset_complete, name='password_reset_complete'),
]
