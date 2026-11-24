import os

import requests
from dotenv import load_dotenv

TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"

load_dotenv()


def get_partner_token():
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": os.environ["TESLA_CLIENT_ID"],
            "client_secret": os.environ["TESLA_CLIENT_SECRET"],
            "audience": os.environ["TESLA_API_BASE"],
            "scope": "openid vehicle_device_data vehicle_location",
        },
        timeout=30,
    )

    if response.status_code != 200:
        print("Eroare", response.status_code, response.text)
        raise SystemExit(1)

    return response.json()["access_token"]


if __name__ == "__main__":
    token = get_partner_token()
    print("token received")
