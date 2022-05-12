from socket import *
serverPort = 16002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

serverStrings = {
    "init": "Servidor inicializado. Aguardando usuário...",
    "connect": f"Usuário não autenticado iniciou uma conexão.",
    "welcome": "Bem vindo ao nosso fantástico sistema de login!\n\nDigite seu usuário e senha.\n",
    "success": "Bem vinde, ",
    "failure": "Usuário não registrado ou senha incorreta.\n(Usuario: Sheronlyne // Senha: sheron123)\n",
    "attempt": "Tentativa de login não autenticado.\n",
    "successServer": "Usuário iniciou uma conexão. \n",
}

userDatabase = {
    "Sheronlyne": "sheron123"
}

print(serverStrings["init"])

connectionSocket, addr = serverSocket.accept()
print(serverStrings["connect"] + f" {addr}")

while True:
    connectionSocket.send(serverStrings["welcome"].encode())

    user, password = connectionSocket.recv(1024).decode().split(chr(31))

    if(user in userDatabase and userDatabase[user] == password):
        sentence = serverStrings["success"] + user + ".\n"
        connectionSocket.send(sentence.encode())
        print(serverStrings["successServer"] + f"({user}/{password} : {addr})")
    else:
        connectionSocket.send(serverStrings["failure"].encode())
        print(serverStrings["attempt"] + f"({user}/{password} : {addr})")
    break

connectionSocket.close()
serverSocket.close()
