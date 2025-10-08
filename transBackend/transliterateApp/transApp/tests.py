import requests

url = "http://127.0.0.1:8000/api/extract-text/Devanagari/"

with open("C:\\Users\\Disha\\Downloads\\board.jpg", "rb") as img_file:
    files = {"image": img_file}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)


json_data = response.json()
print(json_data)
