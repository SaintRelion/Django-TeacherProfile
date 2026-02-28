from django.db import models


class Notification(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.user})"
