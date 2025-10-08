# transApp/urls.py
# transApp/urls.py
from django.urls import path
from .views import ExtractTransliterateAPI

urlpatterns = [
    path("extract-text/<str:transLang>/", ExtractTransliterateAPI.as_view(), name="extract_text"),
]

