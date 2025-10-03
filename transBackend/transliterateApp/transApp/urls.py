# transApp/urls.py
from django.urls import path
from .views import ExtractTextAPI

urlpatterns = [
    path("extract-text/", ExtractTextAPI.as_view(), name="extract_text"),
]

