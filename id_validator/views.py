from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .utils import validate_national_id

class ValidateNationalIDView(APIView):
    permission_classes = [HasAPIKey]  # Require API Key authentication

    def post(self, request):
        national_id = request.data.get("national_id")
        if not national_id:
            return Response({"error": "Missing national_id"}, status=400)

        is_valid, result = validate_national_id(national_id)
        if not is_valid:
            return Response({"error": result}, status=400)

        return Response(result)