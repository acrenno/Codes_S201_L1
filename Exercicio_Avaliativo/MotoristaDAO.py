class MotoristaDAO:
    def __init__(self,database):
        self_db = database

    def newMotorista(self, nota: int, corridas:list):
        corridas = []
        for corrida in corridas:
            corrida = {
               "Nota da corrida" : corrida.nota,
               "Distancia percorrida" : corrida.distancia,
               "Valor total" : corrida.valor,
               "Passageiro" : {
                    "Nome do passageiro" : corrida.passageiro.nome,
                    "Documento" : corrida.passageiro.documento
               }

            }
            corridas.append(corrida)

        try:
             result = self.db.collection.insert_one({
                "Nota" : nota,
                "Corridas" : corridas
             })
             print(f"Id do motorista: {result.inserted_id}")
             return result.inserted_id
        except Exception as e:
            print(f"Nao criou o motorista {e}")
            return None

    def read_motorista(self, id:str):
        try:
            motoristas = self.db.collection.find_one({"_id": ObjectId(id)})
            if(motoristas):
                notas = motoristas['nota_motorista']
                corridas = motoristas['corridas']
                corrida = [Corridas(corridas['nota_corrida'], corridas['distancia'], corridas['preco'],
                           Passegeiro(corridas['passagerio']['nome'], corridas['passageiro']['documento'])) for corridas in corridas]
            print(f"Motorista found: {motoristas}")
            return Motorista(notas, corridas)
        except Exception as e:
            print(f"ERRO AO LER MOTORISTA {e}")
            return None

    def update_motorista(self, id: str, nota: int, corridas:list):
        corridas = []
        for corrida in corridas:
            corrida = {
               "Nota da corrida" : corrida.nota,
               "Distancia percorrida" : corrida.distancia,
               "Valor total" : corrida.valor,
               "Passageiro" : {
                    "Nome do passageiro" : corrida.passageiro.nome,
                    "Documento" : corrida.passageiro.documento
               }

            }
            corridas.append(corrida)
        
        try:
            result = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set" : {"nota": nota, "corridas": corridas}})
            print (f"Motorista atualizado: {result.modified_count} documnetos(s) modificado(s)")
            return result.modified_count
        except Exception as e:
            print(f"ERRO AO ATUALIZAR MOTORISTA {e}")
            return None

    def delete_motorista(self,id:str):
        try:
            result = self.db.collection.delete_one({"_id":ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documentos deletados")
            return result.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista")
            return
        
