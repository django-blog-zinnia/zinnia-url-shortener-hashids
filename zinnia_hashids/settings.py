"""Settings for Zinnia Hashids"""
from django.conf import settings

HASHIDS_SALT = getattr(settings, 'ZINNIA_HASHIDS_SALT', 'Zinnia rocks')
