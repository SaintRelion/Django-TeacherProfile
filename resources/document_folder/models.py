from django.db import models

from sr_libs.dal.mixins import ArchiveMixin

from audit.mixins import AuditMixin


class DocumentFolder(ArchiveMixin, AuditMixin):
    name = models.CharField(max_length=255)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    has_expiry = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
