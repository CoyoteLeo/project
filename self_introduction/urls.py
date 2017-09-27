from django.conf.urls import url
import self_introduction.views as self_introduction

urlpatterns = [
    url(r'^$', self_introduction.index, name="index")
]
