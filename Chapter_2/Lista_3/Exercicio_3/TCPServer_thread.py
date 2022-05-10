from socket import *
from threading import Thread

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

def thread_function(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == "":
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    t = Thread(target = thread_function, \
        args=(connectionSocket, addr))
    t.start()