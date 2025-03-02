from rest_framework_api_key.models import AbstractAPIKey

class NationalIDAPIKey(AbstractAPIKey):
    class Meta:
        verbose_name = "National ID API Key"
        verbose_name_plural = "National ID API Keys"
