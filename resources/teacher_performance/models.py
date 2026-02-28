from django.db import models


class TeacherPerformance(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user}: {self.rating}"
