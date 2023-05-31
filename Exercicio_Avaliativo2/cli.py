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


class PersonCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.createp)
        self.add_command("read", self.readp)
        self.add_command("update", self.updatep)
        self.add_command("delete", self.deletep)

    def createp(self):
        name = input("Enter the name: ")
        ano_nasc = int(input("Enter the year of birth: "))
        cpf = input("Enter the cpf: ")
        self.person_model.create(name, ano_nasc, cpf)

    def readp(self):
        name = input("Enter the name: ")
        person = self.person_model.readp(name)
        if person:
                print(f"Name: {person['name']}")
                print(f"Ano nascimento: {person['ano_nasc']}")
                print(f"CPF: {person['cpf']}")


def updatep(self):
    name = input("Enter the name: ")
    novo_cpf = input("Enter the new cpf: ")
    self.person_model.updatep(name, novo_cpf)


def deletep(self):
    name = input("Enter the name: ")
    self.person_model.deletep(name)


def run(self):
    print("Welcome to the book CLI!")
    print("Available commands: create, read, update, delete, quit")
    super().run()