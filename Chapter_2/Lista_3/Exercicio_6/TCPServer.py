from socket import *
serverPort = 12006
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

class StateMachine:
    def __init__(self, states, transitions, initialState, connectionSocket):
        self.connectionSocket = connectionSocket
        self.states = {}
        for _, (stateName, stateMsg) in enumerate(states.items()):
            self.states[stateName] = State(stateName, stateMsg)
            if initialState == stateName:
                self.current = self.states[stateName]
                self.connectionSocket.send(self.current.msg.encode())

        for transition in transitions:
            tfrom, to = transition.tfrom, transition.to
            for stateName in self.states:
                if transition.tfrom == stateName:
                    self.states[stateName].transitions.append(transition)

    def setState(self, nextState):
        for transition in self.current.transitions:
            if transition.to == nextState:
                self.current = self.states[transition.to]
                self.connectionSocket.send(self.current.msg.encode())
                return
        raise ValueError(f"Inexistent transition from {current} to {nextState}")

class State:
    def __init__(self, name, msg):
        self.transitions = []
        self.name = name
        self.msg = msg

class Transition:
    def __init__(self, tfrom, to):
        self.tfrom = tfrom
        self.to = to

nome = "Null"

STATES = {
    "Boas-vindas": "Olá! Bem-vindo! Qual o seu nome?",
    "Serviços": "Certo, {}! Como posso te ajudar? Digite o número que corresponde à opção desejada:\n1 - Agendar um horário de monitoria\n2 - Listar as próximas atividades da disciplina\n3 - E-mail do professor",
    "Agendar Monitoria": "Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br",
    "Atividades Pendentes": "Fique atento para datas das próximas atividades. Confira o que vem por aí!\n\nP1: 26 de maio de 2022\nLista 3: 29 de maio de 2022",
    "E-mail do Professor": "Quer falar com o professor?\nO e-mail dele é sadoc@dcc.ufrj.br",
    "Finalizar": "\nObrigado por utilizar nosso serviços! Até logo!",
}


TRANSITIONS = [
    Transition("Boas-vindas", "Serviços"),
    Transition("Serviços", "Agendar Monitoria"),
    Transition("Serviços", "Atividades Pendentes"),
    Transition("Serviços", "E-mail do Professor"),
    Transition("Serviços", "Finalizar"),
    Transition("Agendar Monitoria", "Finalizar"),
    Transition("Atividades Pendentes", "Finalizar"),
    Transition("E-mail do Professor", "Finalizar"),
]

connectionSocket, addr = serverSocket.accept()
stateMachine = StateMachine(STATES, TRANSITIONS, "Boas-vindas", connectionSocket)
while True:
    if stateMachine.current.name == "Boas-vindas":
        nome = connectionSocket.recv(1024).decode()
        stateMachine.states["Serviços"].msg = stateMachine.states["Serviços"].msg.format(nome)
        stateMachine.setState("Serviços")
    if stateMachine.current.name == "Serviços":
        user_input = connectionSocket.recv(1024).decode()
        if user_input == "1":
            stateMachine.setState("Agendar Monitoria")
        if user_input == "2":
            stateMachine.setState("Atividades Pendentes")
        if user_input == "3":
            stateMachine.setState("E-mail do Professor")
    stateMachine.setState("Finalizar")
    break

connectionSocket.send("EXIT".encode())
connectionSocket.close()
