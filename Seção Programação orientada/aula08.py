# Crie uma classe Tarefa com atributos descrição e status. 
# Adicione métodos para marcar a tarefa como concluída e exibir o status.

class Tarefa:
    def __init__(self, descricao, status='pendendte'):
        self.descricao = descricao
        self.status = status

    def conclude(self):
        self.status = 'concluído' 
        return self.status
    
    def alterar(self, novo_status):
        if novo_status in ["pendente", "concluída"]:
            self.status = novo_status
        else:
            raise ValueError("Status inválido")

    def show(self):
        print(f"A tarefa {self.descricao} está {self.status}.")

tasks = Tarefa('viajar')
tasks.show()
tasks.alterar()