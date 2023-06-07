from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Issue(models.Model):
    title = models.CharField(max_length=50, help_text="Type of exception")
    url = models.CharField(max_length=50, help_text="Url endpoint")
    headers = models.TextField()
    body = models.TextField()
    method = models.CharField(max_length=10, help_text="Type of http method")
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    response = models.TextField(help_text="Error log")
    description = models.TextField(help_text="Reason of error")
    status_code = models.CharField(max_length=10, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
