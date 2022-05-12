from socket import *

serverName = gethostbyname(gethostname()) 
serverPort = 16002
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

welcomeString = clientSocket.recv(1024).decode()
print(welcomeString)

while True:
    User = input('Usuário: ')
    Password = input('Senha: ')
    data = User + chr(31) + Password

    clientSocket.send(data.encode())

    sentence = clientSocket.recv(1024).decode()
    print("\n\n" + sentence)
    break


clientSocket.close()
