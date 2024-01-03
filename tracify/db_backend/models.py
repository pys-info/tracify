from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import JSONField

User = get_user_model()


class Issue(models.Model):
    title = models.CharField(max_length=64, help_text="Type of exception")
    description = models.TextField(help_text="Reason of error")
    created_at = models.DateTimeField(auto_now_add=True)
    data = JSONField(help_text="Additional data")

    def __str__(self):
        return self.title
