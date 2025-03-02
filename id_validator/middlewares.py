from django.utils.timezone import now
from rest_framework_api_key.models import APIKey
from id_validator.models import APICallLog, NationalIDAPIKey

class APICallLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Log only API requests
        if request.path.startswith("/api/"):
            api_key = None
            api_key_header = request.headers.get("Authorization")

            if api_key_header and api_key_header.startswith("Api-Key "):
                key = api_key_header.split("Api-Key ")[1]

                # Validate API key
                if APIKey.objects.is_valid(key):
                    api_key = NationalIDAPIKey.objects.filter(hashed_key=APIKey.objects.get_from_key(key)).first()

            # Log API request
            APICallLog.objects.create(
                api_key=api_key,
                endpoint=request.path,
                timestamp=now(),
                ip_address=self.get_client_ip(request),
                response_status=response.status_code,
            )

        return response

    def get_client_ip(self, request):
        """Retrieve client IP address from request headers"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
