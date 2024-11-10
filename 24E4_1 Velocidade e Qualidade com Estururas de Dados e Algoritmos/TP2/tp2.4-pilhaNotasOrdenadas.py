# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

class TPilha:
    def __init__(self):
        self.FItens = []

    def adicionaNaPila(self, pItm):
        self.FItens.append(pItm)

    def quick_sort(self, lista, inicio, fim):
        if inicio > fim:
            return
        anterior = inicio
        posterior = fim
        pivo = lista[inicio]

        while anterior < posterior:
            while anterior < posterior and lista[posterior] > pivo:
                posterior = posterior - 1

            if anterior < posterior:
                lista[anterior] = lista[posterior]
                anterior = anterior + 1

            while anterior < posterior and lista[anterior] <= pivo:
                anterior = anterior + 1

            if anterior < posterior:
                lista[posterior] = lista[anterior]
                posterior = posterior - 1

            lista[anterior] = pivo

        self.quick_sort(lista, inicio, anterior - 1)
        self.quick_sort(lista, anterior + 1, fim)
    
    def ordena(self):
        self.quick_sort(self.FItens, 0, len(self.FItens) - 1)

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


# Criando instâncias
pilha = TPilha()
pilhaordenada = TPilha()
# Adicionando notas
pilha.adicionaNaPila(5)
pilha.adicionaNaPila(6)
pilha.adicionaNaPila(9)
pilha.adicionaNaPila(8)
pilha.adicionaNaPila(3)
# Ordenando
pilha.ordena()
# Invertendo notas
while pilha.quantidade()>0:
    pilhaordenada.adicionaNaPila(pilha.pop())
# Imprimindo valores ordenados da nova pilha
while pilhaordenada.quantidade()>0:
    print(pilhaordenada.pop())

