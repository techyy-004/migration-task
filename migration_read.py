import requests

API_TOKEN = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="  
USER_ID = "223e32e4-7a9f-4a69-ba9a-5f201c00dbda" 
BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

headers = {
    "api_token": API_TOKEN,
    "User-ID": USER_ID
}

def get_all_folders():
    response = requests.get(BASE_URL, headers=headers)
    print("Status:", response.status_code)

    try:
        print("Response:", response.text)
    except requests.exceptions.JSONDecodeError:
        print("Non-JSON response:", response.text)
        return None

get_all_folders()