from django.db import models
from django.utils.timezone import now
from rest_framework_api_key.models import AbstractAPIKey

class NationalIDAPIKey(AbstractAPIKey):
    class Meta:
        verbose_name = "National ID API Key"
        verbose_name_plural = "National ID API Keys"

class APICallLog(models.Model):
    api_key = models.ForeignKey(
        NationalIDAPIKey, on_delete=models.SET_NULL, null=True, blank=True, related_name="api_calls"
    )
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    response_status = models.IntegerField()

    def __str__(self):
        return f"{self.endpoint} - {self.timestamp} - {self.response_status}"
