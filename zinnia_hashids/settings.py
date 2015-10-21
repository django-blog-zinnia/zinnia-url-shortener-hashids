"""Settings for Zinnia Hashids"""
from django.conf import settings

HASHIDS_SALT = getattr(settings, 'ZINNIA_HASHIDS_SALT', 'Zinnia rocks')

HASHIDS_MIN_LENGTH = getattr(settings, 'ZINNIA_HASHIDS_MIN_LENGTH', 6)

HASHIDS_ALPHABET = getattr(settings, 'ZINNIA_HASHIDS_ALPHABET', '')
