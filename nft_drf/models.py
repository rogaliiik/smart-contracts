from django.db import models
import os
from binascii import hexlify


def _createHashId():
    return hexlify(os.urandom(10))


class Token(models.Model):
    unique_hash = models.CharField(max_length=20, default=_createHashId().decode('ascii'), unique=True)
    tx_hash = models.CharField(max_length=100, blank=True)
    media_url = models.URLField()
    owner = models.CharField(max_length=100)
