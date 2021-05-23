from pybluez import bluetooth

# this code shows how to establish a connection using an RFCOMM socket, transfer some data, and disconnect.

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  # создаем канал связи

# BluetoothSocket(), выделяет ресурсы для канала связи на основе RFCOMM.
#RFCOMM BluetoothSocket, используемый для приема входящих подключений,
# должен быть подключен к ресурсам операционной системы с помощью метода привязки bind()

port = 1
server_sock.bind(("",port))  # пустая строка показывает, что любой локальный адаптер приемлем для привязки
# После привязки сокета вызов listen() переводит сокет в режим прослушивания, и он готов принимать входящие соединения.
server_sock.listen(1)

client_sock, address = server_sock.accept()
print("Accepted connection from ",address)

data = client_sock.recv(1024)
print(f"received {data}")

client_sock.close()
server_sock.close()