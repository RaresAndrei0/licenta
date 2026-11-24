import os

import requests
from dotenv import load_dotenv

from partner_token import get_partner_token

load_dotenv()

API_BASE = os.environ["TESLA_API_BASE"]
DOMAIN = os.environ["TESLA_DOMAIN"]

token = get_partner_token()
headers = {"Authorization": f"Bearer {token}"}

# 1. Point tesla to the public key
response = requests.post(
    f"{API_BASE}/api/1/partner_accounts",
    headers=headers,
    json={"domain": DOMAIN},
    timeout=30,
)
print("Sign:", response.status_code, response.text)

# 2. Check what was saved
response = requests.get(
    f"{API_BASE}/api/1/partner_accounts/public_key",
    headers=headers,
    params={"domain": DOMAIN},
    timeout=30,
)
print("Seen key: ", response.status_code, response.text)
