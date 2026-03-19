from django.contrib.auth.models import AbstractUser
from sr_libs.dal.mixins import ArchiveMixin


class User(AbstractUser, ArchiveMixin):
    pass
