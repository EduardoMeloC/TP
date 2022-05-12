from socket import *

serverName = gethostbyname(gethostname()) 
serverPort = 12006
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

is_running = True

while is_running:
    server_msg = clientSocket.recv(1024).decode()
    if "EXIT" in server_msg:
        server_msg = server_msg.replace("EXIT", "")
        is_running = False
    print(server_msg)

    if(not is_running):
        break
    user_input = input()
    clientSocket.send(user_input.encode())

clientSocket.close()
