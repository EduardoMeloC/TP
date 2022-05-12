from socket import *

serverName = gethostbyname(gethostname())
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

N = int(input('Input N: '))

for i in range(N):
    clientSocket.sendto(str(i+1).encode(), (serverName, serverPort))

clientSocket.sendto("EXIT".encode(), (serverName, serverPort))

clientSocket.close()
