class Query:
    def __init__(self, database):
        self.db = database


    #QUESTAO 1

    #buscando teacher renzo
    def teacher_renzo(self):
        query = "MATCH (p:Teacher) WHERE p.name = 'Renzo' RETURN p.ano_nasc AS ano, p.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["ano"], result["cpf"]) for result in results]


    #buscando todos os profs que comecam com m
    def comeca_m(self):
        query = "MATCH (p:Teacher) WHERE p.name STARTS WITH 'M' RETURN p.name AS name, p.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["cpf"]) for result in results]


    #sair com os nomes de todas as cidades
    def cidades(self):
        query = "MATCH (c:City) RETURN c.name AS cidades"
        results = self.db.execute_query(query)
        return [result["cidades"] for result in results]

    #escolas com numero maior/igual a 150 e menor/igual a 550

    def escolami(self):
        query = "MATCH (e:School) WHERE e.number >= 150 AND e.number <= 550 RETURN e.name AS nome, e.address AS address, e.number AS number"
        results = self.db.execute_query(query)
        return [(result["nome"], result["address"], result["number"]) for result in results]




    #QUESTAO 2

    #ANO PROF MAIS JOVEM E PROF MAIS VELHO
    def oldyoung(self):
        query = "MATCH (p:Teacher) RETURN MAX(p.ano_nasc) AS young, MIN(p.ano_nasc) AS old"
        results = self.db.execute_query(query)
        return [(result["young"], result["old"]) for result in results]

    #MA hab das cidades
    def mahabtantes(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS mahab"
        results = self.db.execute_query(query)
        return [result["mahab"] for result in results]

    #qual cidade tem o cep 37540000?

    def srsalterado(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS nomealter"
        results = self.db.execute_query(query)
        return [result["nomealter"] for result in results]

    #retorne um caracter do nome dos professores

    def caracnomeprof(self):
        query = "MATCH (p:Teacher) RETURN SUBSTRING(p.name, 2, 1) AS caracter"
        results = self.db.execute_query(query)
        return [result["caracter"] for result in results]


