from django.contrib import admin
from .models import APICallLog

@admin.register(APICallLog)
class APICallLogAdmin(admin.ModelAdmin):
    list_display = ("endpoint", "timestamp", "api_key", "response_status", "ip_address")
    search_fields = ("api_key", "endpoint")
    list_filter = ("response_status", "timestamp")
