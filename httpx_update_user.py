import httpx

from tools.facers import get_random_email


create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response_user = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
response_user_data = response_user.json()
print("Статус код:",response_user.status_code)
print(response_user_data)

log_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}

log_resp_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=log_payload)
log_resp_user_data = log_resp_user.json()

print("Статус код:", log_resp_user.status_code)
print(log_resp_user_data)

path_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
path_user_headers = {
    "Authorization": f"Bearer {log_resp_user_data["token"]["accessToken"]}"
}

path_user_resp = httpx.patch(f"http://localhost:8000/api/v1/users/{response_user_data["user"]["id"]}", headers=path_user_headers, json=path_payload)
path_user_resp_data = path_user_resp.json()
print("Статус код:", path_user_resp.status_code)
print(path_user_resp_data)