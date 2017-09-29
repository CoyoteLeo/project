from django.conf.urls import url, include
from django.contrib import admin
from user.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls', namespace="user", app_name='user')),
    url(r'^todolist/', include('todolist.urls', namespace="todolist", app_name="todolist")),
    url(r"^self_introduction",
        include("self_introduction.urls", namespace="self_introduction", app_name="self_introduction")),
    url(r'^$', index, name='index')
]
