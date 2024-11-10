# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

class TFila:
    def __init__(self, tamanho):
        self.fila = [''] * tamanho
        self.base = -1
        self.topo = -1
    
    def adicionar_cliente(self, pNome):
        if self.topo >= len(self.fila):
            raise Exception("Fila cheia")
        self.topo = self.topo + 1
        self.fila[self.topo] = pNome
        if self.base==-1:
            self.base=self.base+1
    
    def atender_cliente(self):
        if (self.base==-1) or (self.base>self.topo):
            raise Exception("Não há itens na fila!")
        lItm = self.fila[self.base]
        self.base=self.base+1
        return lItm
    
    def tamanho_fila(self):
        return self.topo-self.base+1
    

fila = TFila(10)
fila.adicionar_cliente('Fulano')
fila.adicionar_cliente('Beltrano')
fila.adicionar_cliente('Ciclano')
print(f"A fila tem {fila.tamanho_fila()} cliente(s)")
print(f"Atendendo o cliente {fila.atender_cliente()}")
print(f"A fila tem {fila.tamanho_fila()} cliente(s)")


    
