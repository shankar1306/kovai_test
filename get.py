import requests
from tabulate import tabulate

api_key = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
headers = {
    "api_token": api_key
}

params = {
    "userId": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}

response = requests.get("https://apihub.document360.io/v2/Drive/Folders", headers=headers, params=params)

print(response.status_code)
print(response.json())

response_data = response.json()
table_data = []

for folder in response_data["data"]:
    table_data.append([
        folder["id"],
        folder["title"],
        folder["parent_folder_id"],
        folder["items_count"]
    ])
    
    for sub in folder.get("sub_folders", []):
        table_data.append([
            sub["id"],
            f"└─ {sub['title']}",
            sub["parent_folder_id"],
            sub["items_count"]
        ])

headers = ["ID", "Title", "Parent Folder", "Items Count"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))