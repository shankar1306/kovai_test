import requests
import json

api_key = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
headers = {
    "api_token": api_key
}


params = {
    "userId": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}
upt_data = {
    "id": "02299c42-6c1a-40d0-bf48-5b075c21f899",
    "title": "new_title",    
    "user_id": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}
response = requests.put("https://apihub.document360.io/v2/Drive/Folders", headers=headers,params=params , json=upt_data)
print(response.status_code)
if response.status_code == 200:
    updated = response.json()
    print(" Folder title updated successfully!")
    print(f" Updated Title: {updated.get('title')}")