from socket import *

serverName = gethostbyname(gethostname()) 
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    sentence = input('Input lowercase sentence:')
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    clientSocket.close()
