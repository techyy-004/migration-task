import requests

API_TOKEN = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
USER_ID = "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

headers = {
    "api_token": "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ==",
    "User Id": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda",
    "Content-Type": "application/json"
}

def create_folder(folder_name):
    data = {
        "Title": folder_name
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
        if response.status_code == 200:
            folder_id = response.json().get("id")
            print(f"✅ Folder created successfully! ID: {folder_id}")
            return folder_id
    except:
        print("Non-JSON response:", response.text)
    return None

if __name__ == "__main__":
    folder_name = input("Enter the folder name to create: ")
    create_folder(folder_name)