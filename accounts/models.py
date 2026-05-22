from django.contrib.auth.models import AbstractUser
from sr_libs.dal.mixins import ArchiveMixin
from django.db import models

from audit.mixins import AuditMixin


class User(AbstractUser, ArchiveMixin, AuditMixin):
    pds = models.JSONField(default=dict, blank=True, null=True)

    ignore_fields = [
        "date_joined",
        "pds",
        "is_active",
        "is_staff",
        "password",
        "last_login",
        "is_superuser",
    ]
