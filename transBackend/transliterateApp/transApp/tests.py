#from django.test import TestCase

# Create your tests here.
import requests

url = "http://127.0.0.1:8000/api/extract-text/"
files = {"image": open("C:\\Users\\Disha\\Downloads\\Traffic-Sign-Board.jpg", "rb")}
response = requests.post(url, files=files)

print(response.json())
