from django.contrib.auth.models import AbstractUser
from sr_libs.dal.mixins import ArchiveMixin
from django.db import models


class User(AbstractUser, ArchiveMixin):
    pds = models.JSONField(default=dict, blank=True, null=True)
