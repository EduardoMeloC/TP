from socket import *
from threading import Thread
from time import sleep

def thread_function(msg,addr):
    modifiedMessage = msg.decode().upper()
    sleep(5)
    serverSocket.sendto(modifiedMessage.encode(), addr)


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    t = Thread(target = thread_function, args=(message,clientAddress, ))
    t.start()