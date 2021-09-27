import socket
import threading

encryption = 'utf-8'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
serverSocket.bind(('', 5555))
serverSocket.listen(5)

clients = []
nicknames = []


def broadcast(message):  # Фукнция для отправки сообщения всем клиентам
    for client in clients:
        client.send(message)


def handle(client):  # Функция для обработки трафика отдельного клиента
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode(encryption))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = serverSocket.accept()
        print("Connected with: {}\n".format(str(address)))
        client.send('NICKNAME'.encode(encryption))
        nickname = client.recv(1024).decode(encryption)
        nicknames.append(nickname)
        clients.append(client)
        print('Nickname is {}'.format(nickname))
        broadcast('{} joined to the server\n'.format(nickname).encode(encryption))
        client.send('Connected to the server!\n'.encode(encryption))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
