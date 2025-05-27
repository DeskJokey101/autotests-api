import socket

data_list = list()

def user_server():
    #Создаем TCP-Socket для работы с сетевыми соединениями
    user_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Привязываем его к порту и адрессу
    user_server_address = ('localhost', 12345)
    user_server_socket.bind(user_server_address)


    # Слушаем входящие подключения (10 шт)
    user_server_socket.listen(10)
    print('Сервер работает в штатном режиме и ждет подключений...')

    while True:
        # Принимаем соединение от клиента
        user_client_socket, user_client_address = user_server_socket.accept()
        print(f'{user_client_address} подключился к серверу')

        # Получаем данные от клиента
        data = user_client_socket.recv(1024).decode()


        print(f'Пользователь c адрессом: {user_client_address} отправил сообщение: {data}')


        # Ответ от сервера со всеми сообщениями получаемыми от клиента
        data_list.append(data)
        user_client_socket.send('\n' .join(data_list).encode())

        # Закрываем сообщение
        user_client_socket.close()


if __name__ == '__main__':
    user_server()