"""Urls for Zinnia Hashids"""
from django.conf.urls import url

from zinnia_hashids.views import EntryHashids
from zinnia_hashids.settings import HASHIDS_MIN_LENGTH


urlpatterns = [
    url(r'^(?P<token>\w{%i,})/$' % HASHIDS_MIN_LENGTH,
        EntryHashids.as_view(),
        name='entry_hashids'),
]
