import httpx


login_payload = {
  "email": "user@root.com",
  "password": "str123"
}

log_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
log_response_data = log_response.json()
print("Status code:", log_response.status_code)
print(f"Login response:", log_response_data)


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI1LTA1LTI1VDIwOjQ0OjI0Ljk1NjMwOCIsInVzZXJfaWQiOiIyM2Y2MzdmOS0xMTA0LTRhNTQtODgwYS0zY2FlYTQ2NWRmOGUifQ._3vHjxjEfcYzz1T1Unm3jJlKD1diQXnpyKYd_m3RN9U"}
refresh_resp = httpx.get("http://localhost:8000/docs#/users/get_user_me_view_api_v1_users_me_get", headers=headers)
print("Status code:", refresh_resp.status_code)
print(refresh_resp.request.headers)



