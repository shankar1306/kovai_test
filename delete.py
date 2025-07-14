import requests
from tabulate import tabulate

api_key = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
headers = {
    "api_token": api_key
}

params = {
    "userId": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}

response = requests.delete("https://apihub.document360.io/v2/Drive/Folders/f09ca62f-4f10-4ae6-994f-23e83ba8c38b", headers=headers, params=params)
print(response.status_code)
if response.status_code == 200:
    print("Folder deleted successfully!")