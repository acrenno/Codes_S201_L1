class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (p:Teacher {name: $name}) RETURN p AS nome"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["nome"] for result in results]

    def delete(self, name):
        query = "MATCH (p:Teacher {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(self, name, novoCpf):
        query = "MATCH (p:Teacher {name: $name}) SET p.cpf = $novoCpf"
        parameters = {"name": name, "novoCpf": novoCpf}
        self.db.execute_query(query, parameters)