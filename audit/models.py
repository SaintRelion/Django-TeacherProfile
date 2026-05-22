from django.db import models
from django.utils import timezone


class AuditLog(models.Model):
    class Action(models.TextChoices):
        CREATE = "create", "Create"
        UPDATE = "update", "Update"
        DELETE = "delete", "Delete"
        CUSTOM = "custom", "Custom"

    user = models.ForeignKey(
        "accounts.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="audit_logs",
    )
    action = models.CharField(max_length=16, choices=Action.choices)
    model_name = models.CharField(max_length=128)  # e.g. "DocumentFolder"
    object_id = models.CharField(max_length=64, null=True, blank=True)
    event = models.CharField(max_length=128, blank=True)  # e.g. "user.login"
    data = models.JSONField(default=dict, blank=True)  # snapshot / diff / extra payload
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M}] {self.action} {self.model_name} ({self.object_id})"
