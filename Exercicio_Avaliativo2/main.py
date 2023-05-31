from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

db = Database("bolt://3.231.95.226:7687", "neo4j", "stretches-pointers-dedications")

query_db = Query(db)
teacher_db = TeacherCRUD(db)

# QUESTAO 1
print(query_db.teacher_renzo())
print(query_db.comeca_m())
print(query_db.cidades())
print(query_db.escolami())

# Questão 2
print(query_db.oldyoung())
print(query_db.mahabtantes())
print(query_db.srsalterado())
print(query_db.caracnomeprof())

# Questão 3
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

# Fechando a conexão com o banco de dados
db.close()