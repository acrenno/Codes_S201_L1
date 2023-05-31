class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    #descobrir quem é neto de determinado avo
    def get_casado(self, casado_name):
        query = "MATCH (p:Pessoa {nome: $casado_name})-[:CASADO_COM]->(n:Pessoa) return n"
        parameters = {"casado_name": casado_name}
        self.db.execute_query(query, parameters)


    #descobrir filhos de determinado pai/mae
    def get_pai(self, pai_name):
        query = "MATCH (p:Pessoa {nome: $pai_name})-[:PAI_DO]->(n:Pessoa) return n"
        parameters = {"pai_name": pai_name}
        self.db.execute_query(query, parameters)


    #descobrir quem é dono de determinado pet
    def get_pet(self, pet_name):
        query = " MATCH (n:Pessoa)-[:DONO_DE]-> (p:Animal {nome: $pet_name}) return n"
        parameters = {"pet_name": pet_name}
        self.db.execute_query(query, parameters)
