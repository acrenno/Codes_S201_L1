from classesBD import Motorista, Corridas, Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nota = int(input("Qual a nota do motorista?: "))
        corridas = []
        while True:
            add_corrida = input("Adicionar outra corrida?: ")
            if add_corrida.lower() == "nao":
                break
            nota_corrida = int(input("Nota da corrida: "))
            distancia_corrida = float(input("Distancia da corrida: "))
            valor_corrida = float(input("Valor da corrida: "))
            nome_passageiro = input("Nome do passageiro: ")
            documento_passageiro = input("Documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corridas(nota_corrida, distancia_corrida, valor_corrida, passageiro)
            corridas.append(corrida)
        self.motorista_model.create_motorista(nota, corridas)

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nota: {motorista.nota}")
            print("Corridas:")
            for corrida in motorista.corridas:
                print(f"Nota: {corrida.nota}")
                print(f"Distancia: {corrida.distancia}")
                print(f"Valor: {corrida.valor}")
                print(f"Nome do passageiro: {corrida.passageiro.nome}")
                print(f"Documento do passageiro: {corrida.passageiro.documento}")

    def update_motorista(self):
        id = input("Entre com o id: ")
        nota = int(input("Nova nota (1-5): "))
        corrida_nota = int(input("Nova nota da corrida (1-5): "))
        distancia = float(input("Nova distancia da corrida: "))
        valor = float(input("Novo valor da corrida: "))
        nome = input("Novo nome do passageiro: ")
        documento = input("Novo documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        corrida = Corridas(corrida_nota, distancia, valor, passageiro)
        self.motorista_model.update_motorista(id, nota, corrida)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()