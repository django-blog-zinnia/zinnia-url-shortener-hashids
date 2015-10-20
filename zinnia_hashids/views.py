"""Views for Zinnia Hashids"""
from hashids import Hashids

from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from zinnia.models.entry import Entry

from zinnia_hashids.settings import HASHIDS_SALT


class EntryHashids(RedirectView):
    """
    View for handling the hashids of an Entry,
    simply do a redirection.
    """
    permanent = True

    def get_redirect_url(self, **kwargs):
        """
        Get entry corresponding to 'pk' encoded by hashids
        in the 'token' variable and return the get_absolute_url
        of the entry.
        """
        hashids = Hashids(salt=HASHIDS_SALT)
        unhashed_pk = hashids.decode(kwargs['token'])[0]
        entry = get_object_or_404(Entry.published, pk=unhashed_pk)
        return entry.get_absolute_url()
