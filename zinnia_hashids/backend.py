"""URL Shortener backend for Zinnia Hashids"""
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from zinnia.settings import PROTOCOL

from zinnia_hashids.factory import hashids


def backend(entry):
    """
    Hashids URL shortener backend for Zinnia.
    """
    hashed_pk = hashids.encode(entry.pk)
    url = '%s://%s%s' % (
        PROTOCOL, Site.objects.get_current().domain,
        reverse('entry_hashids', kwargs={'token': hashed_pk}))
    return url
