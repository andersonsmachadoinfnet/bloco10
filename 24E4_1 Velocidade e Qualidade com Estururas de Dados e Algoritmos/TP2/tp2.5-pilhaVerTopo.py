# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

class TPilha:
    FItens = []

    def adicionaNaPila(self, pItm):
        self.FItens.append(pItm)
    
    def tarefa_no_topo(self):
        if self.FItens.count==0:
            raise Exception("A pilha está vazia!")
        return self.FItens[len(self.FItens)-1]

pilha = TPilha()
pilha.adicionaNaPila("Trabalhar")
pilha.adicionaNaPila("Estudar")
pilha.adicionaNaPila("Fazer o TP2!")
print(pilha.tarefa_no_topo())

