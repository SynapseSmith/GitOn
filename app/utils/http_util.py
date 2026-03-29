# app/utils/http_util.py
from typing import Union

import requests
from fastmcp.server.dependencies import get_http_headers
import os

giton_url = os.getenv("giton_url")

def export_token():
    headers = get_http_headers()
    return headers.get("authorization", "").strip()

def giton_get(endpoint: str):
    token = export_token()
    if not token:
        return {"error": "Missing Authorization token"}

    url = f"{giton_url.rstrip('/')}/{endpoint.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error {e.response.status_code}", "details": e.response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request exception: {str(e)}"}


def giton_post(endpoint: str, json_body: Union[dict, str] = None, ):
    token = export_token()
    if not token:
        return {"error": "Missing Authorization token"}

    url = f"{giton_url.rstrip('/')}/{endpoint.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=json_body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error {e.response.status_code}", "details": e.response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request exception: {str(e)}"}