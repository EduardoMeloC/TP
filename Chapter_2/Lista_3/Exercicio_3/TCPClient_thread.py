from socket import *

serverName = gethostbyname(gethostname()) 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    if sentence == '':
        break
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
clientSocket.close()
