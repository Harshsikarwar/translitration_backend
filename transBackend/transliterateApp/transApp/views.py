from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
import google.generativeai as genai
from aksharamukha import transliterate

genai.configure(api_key="AIzaSyCoeyMGqYHk2S4q1ifuPhwZVKBsUpz3ws4")  # <-- Replace this with your actual key

def extract_text_from_image(image_file):
    try:
        image_bytes = image_file.read()
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")

        prompt = '''You are a helpful assistant. Extract all the meaningful text from the input image and return only the extracted text, no JSON or explanation, remove escape characters.'''

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": "image/png",  # Adjust if needed
                    "data": image_b64,
                },
            ]
        )

        if hasattr(response, "text") and response.text:
            text = response.text.strip()
            return text
        else:
            raise ValueError("Gemini API returned no text.")

    except Exception as e:
        print("Error during Gemini extraction:", str(e))
        raise



def transliterate_text(text, target_script):
    return transliterate.process("Malayalam", target_script, text)

class ExtractTransliterateAPI(APIView):
    def post(self, request, transLang):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            extracted_text = extract_text_from_image(image_file)
            transliterated_text = transliterate.process("Malayalam", transLang, extracted_text)

            return Response({
                "extracted_text": extracted_text,
                "transliteration": transliterated_text
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
