from socket import *
serverPort = 14000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()
exit_flag = False

while not exit_flag:
    data = connectionSocket.recv(1024).decode()
    # print(data)
    data_list = data.split('_')[:-1]
    for s in data_list:
        if s == "EXIT":
            exit_flag = True
            break
        print(s, end='\n')
connectionSocket.close()
serverSocket.close()
