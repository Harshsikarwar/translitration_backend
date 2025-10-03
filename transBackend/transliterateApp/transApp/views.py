# transApp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import base64

# Configure Gemini API
genai.configure(api_key="AIzaSyCoeyMGqYHk2S4q1ifuPhwZVKBsUpz3ws4")

class ExtractTextAPI(APIView):
    def post(self, request):
        try:
            image_file = request.FILES.get("image")

            if not image_file:
                return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

            # Read image as base64
            image_bytes = image_file.read()
            image_b64 = base64.b64encode(image_bytes).decode("utf-8")

            # Call Gemini
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(
                [
                    "Extract all text from this image.",
                    {
                        "mime_type": "image/png",  # or "image/jpeg"
                        "data": image_b64,
                    },
                ]
            )

            return Response({"text": response.text}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
