"""Factory for Zinnia Hashids"""
from hashids import Hashids

from zinnia_hashids.settings import HASHIDS_SALT
from zinnia_hashids.settings import HASHIDS_MIN_LENGTH


hashids = Hashids(
    salt=HASHIDS_SALT,
    min_length=HASHIDS_MIN_LENGTH
)
