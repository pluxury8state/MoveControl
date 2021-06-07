from version_with_pybluez.pybluez import bluetooth

# RFCOMM BluetoothSocket, используемый для установления исходящего соединения,
# подключается к своей цели с помощью метода подключения,
# который также принимает кортеж, определяющий адрес и номер порта.

bd_addr = "01:23:45:67:89:AB"

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()