# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

class TPedido:
    def __init__(self, id, nome, valor):
        self.id   = id
        self.nome = nome
        self.valor= valor

class TPilha:
    def __init__(self):
        self.FItens = []

    def adicionaNaPila(self, pItm):
        self.FItens.append(pItm)

    def tarefa_no_topo(self):
        if self.FItens.count==0:
            raise Exception("A pilha está vazia!")
        return self.FItens[len(self.FItens)-1]
    
    def quantidade(self):
        return len(self.FItens)
    
    def pop(self):
        if self.FItens.count==0:
            raise Exception("A pilha está vazia!")
        lItm = self.FItens[len(self.FItens)-1]
        del self.FItens[len(self.FItens)-1]
        return lItm
    
    def pedidosImpares(self):
        lQtd = 0
        for lPedido in self.FItens:
            if (lPedido.id % 2 != 0):
                lQtd=lQtd+1
        return lQtd


# Criando instâncias
pilha = TPilha()
# Adicionando notas
pilha.adicionaNaPila(TPedido(1,"Fulano", 100.00))
pilha.adicionaNaPila(TPedido(2,"Ciclano", 150.00))
pilha.adicionaNaPila(TPedido(3,"Beltrano", 60.00))

print("O número de pedidos ímpares é: "+str(pilha.pedidosImpares()))
