from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

is_running = True

while is_running:
    data, clientAddress = serverSocket.recvfrom(2048)
    data = data.decode()
    if data == "EXIT":
        is_running = False
        break
    print(data)

serverSocket.close()
