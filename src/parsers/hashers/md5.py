# -*- coding: utf-8 -*-
"""The MD5 hasher implementation.
   This is a port from Plaso to OpenRelik.
"""

import hashlib

from .interface import BaseHasher
from .manager import HashersManager


class MD5Hasher(BaseHasher):
  """This class provides MD5 hashing functionality."""

  NAME = 'md5'
  ATTRIBUTE_NAME = 'md5_hash'
  DESCRIPTION = 'Calculates an MD5 digest hash over input data.'

  def __init__(self):
    """Initializes the MD5 hasher."""
    super(MD5Hasher, self).__init__()
    self._md5_context = hashlib.md5()

  def GetStringDigest(self):
    """Returns the digest of the hash function expressed as a Unicode string.

    Returns:
      str: string hash digest calculated over the data blocks passed to
          Update(). The string consists of printable Unicode characters.
    """
    return self._md5_context.hexdigest()

  def Update(self, data):
    """Updates the current state of the hasher with a new block of data.

    Repeated calls to update are equivalent to one single call with the
    concatenation of the arguments.

    Args:
      data(bytes): block of data with which to update the context of the hasher.
    """
    self._md5_context.update(data)


HashersManager.RegisterHasher(MD5Hasher)