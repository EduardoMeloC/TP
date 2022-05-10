from socket import *

#serverName = 'LAPA09'
serverName = '10.11.0.30'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lower case sentence:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
clientSocket.close()
