from database import Database
from players_database import PlayersDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.213.128.181:7687", "neo4j", "maximum-rush-drip")
db.drop_all()

# Criando uma instância da classe players_database para interagir com o banco de dados
players_database = PlayersDatabase(db)

# Criando alguns players
players_database.create_player("João",100)
players_database.create_player("Anna", 200)
players_database.create_player("Maria", 300)


# Criando alguns jogos
players_database.create_match("CS")
players_database.create_match("Valorant")


# Criando algumas jogos e players
players_database.insert_player_match("Anna", "CS")
players_database.insert_player_match("Maria", "Valorant")


# Atualizando o nome de um player
players_database.update_player("Anna", "Pedro")

# Deletando um player
players_database.delete_player("Joao")


# Imprimindo todas as informações do banco de dados
print("Players:")
print(players_database.get_player())
print("Jogos:")
print(players_database.get_player())

# Fechando a conexão com o banco de dados
db.close()