from django.db import models
import os
from binascii import hexlify


def _createHashId():
    return hexlify(os.urandom(10))


class Token(models.Model):
    unique_hash = models.CharField(max_length=500, default=_createHashId().decode('utf-8'), unique=True)
    tx_hash = models.CharField(max_length=500, blank=True)
    media_url = models.CharField(max_length=500)
    owner = models.CharField(max_length=500)
