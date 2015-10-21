"""Factory for Zinnia Hashids"""
from hashids import Hashids

from zinnia_hashids.settings import HASHIDS_SALT


hashids = Hashids(
    salt=HASHIDS_SALT
)
