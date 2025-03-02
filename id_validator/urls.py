from django.urls import path
from .views import ValidateNationalIDView

urlpatterns = [
    path('validate/', ValidateNationalIDView.as_view(), name='validate_national_id'),
]
