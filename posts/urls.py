from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
    post_delete,
    
    post_edit,
    PostLikeToggle,
    PostLikeAPIToggle,
    )

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^edit/(?P<slug>[\w-]+)/$', post_edit, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]