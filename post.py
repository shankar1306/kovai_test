import requests
import json

api_key = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
headers = {
    "api_token": api_key
}

params = {
    "userId": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}
data = {
    "title": "Title",
    "user_id": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}
response = requests.post("https://apihub.document360.io/v2/Drive/Folders", headers=headers,params=params , json=data)
print(response.status_code)
print(response.json())
if response.status_code == 200 or response.status_code == 201:
    result = response.json()
    folder_id = result.get("id")
    folder_title = result.get("title")
    print(f" Folder created successfully!")
    print(f" Folder Name: {folder_title}")
    print(f" Folder ID: {folder_id}")
else:
    print(f" Failed to create folder. Status code: {response.status_code}")