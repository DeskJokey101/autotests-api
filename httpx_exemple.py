import httpx
from sqlalchemy.sql.coercions import expect

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title":"Новая задача",
#     "completed": False,
# 'user_id': 1
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.status_code)
# print(response.json())
#
#
# data = {"user_name": "test_user", "password": "123456"}
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json())
#
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.request.headers)
# print(response.json())
#
# params = {"userId": 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos?userId=1', params=params)
#
# print(response.url)
# print(response.json())
#
# files = {"file": ("exemple.txt", open("exemple.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
#
# print(response.json())
#
#
# with httpx.Client() as clients:
#     response_1 = clients.get('https://jsonplaceholder.typicode.com/todos/1')
#     response_2 = clients.get('https://jsonplaceholder.typicode.com/todos/2')
#
#
# print(response_2.json())
# print(response_2.json())
#
#
# clients = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = clients.get("https://httpbin.org/get")
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print(f"Запрос превысил лимит времени")
