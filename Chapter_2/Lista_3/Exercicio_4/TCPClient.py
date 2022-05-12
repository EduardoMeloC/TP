from socket import *

serverName = gethostbyname(gethostname()) 
serverPort = 14000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

N = int(input('Input N:'))

for i in range(N):
    sentence = str(i+1) + '_'
    clientSocket.send(sentence.encode())

clientSocket.send("EXIT_".encode())

clientSocket.close()
