from django.db import models
from sr_libs.dal.mixins import ArchiveMixin

from ..document_folder.models import DocumentFolder


class TeacherDocument(ArchiveMixin):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    folder = models.ForeignKey(DocumentFolder, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    extension = models.CharField(max_length=20)
    file_size_in_mb = models.DecimalField(max_digits=10, decimal_places=2)
    file_base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.document_title} ({self.user})"
