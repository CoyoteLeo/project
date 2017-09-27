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
from django.conf.urls import url, include
from django.contrib import admin
from .views import meta, index, add, delete, modify, showcomplete, showuncomplete, showmiss, todolist

admin.autodiscover()

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r'^add/$', add, name='add'),
    url(r'^delete/$', delete, name='delete'),
    url(r'^showcomplete/$', showcomplete, name='showcomplete'),
    url(r'^showuncomplete/$', showuncomplete, name='showuncomplete'),
    url(r'^showmiss/$', showmiss, name='showmiss'),
    url(r'^(?P<title>.+)/$', modify, name='modify'),
]
