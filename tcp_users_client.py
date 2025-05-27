import socket


# Создаем TCP сокет
user_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_client_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу 1 клиента
user_server_address = ('localhost', 12345)
user_client_socket.connect(user_server_address)


# Создаем и отправляем сообщение
message = f'Привет, сервер!'
user_client_socket.send(message.encode())

# Подключение к серверу и отправка сообещния 2 клиента
user_client_socket_2.connect(user_server_address)
message_2 = f'Как дела?'
user_client_socket_2.send(message_2.encode())

# Реализация ответа от сервера
response = user_client_socket.recv(1024).decode()
print(f'Ответ от сервера: {response}')
response_2 = user_client_socket_2.recv(1024).decode()
print(f'Ответ от сервера: {response_2}')

# Зкравем соединение
user_client_socket.close()
user_client_socket_2.close()