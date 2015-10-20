"""Urls for Zinnia Hashids"""
from django.conf.urls import url

from zinnia_hashids.views import EntryHashids


urlpatterns = [
    url(r'^(?P<token>\w+)/$',
        EntryHashids.as_view(),
        name='entry_hashids'),
]
