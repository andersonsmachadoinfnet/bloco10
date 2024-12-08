# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

class TFila:
    def __init__(self, tamanho):
        self.fila = [''] * tamanho
        self.base = -1
        self.topo = -1
    
    def adicionar_chamado(self, pNome):
        if self.topo >= len(self.fila):
            raise Exception("Fila cheia")
        self.topo = self.topo + 1
        self.fila[self.topo] = pNome
        if self.base==-1:
            self.base=self.base+1
    
    def atender_chamado(self):
        if (self.base==-1) or (self.base>self.topo):
            raise Exception("Não há itens na fila!")
        lItm = self.fila[self.base]
        self.base=self.base+1
        return lItm
    
    def tamanho_fila(self):
        return self.topo-self.base+1
    

fila = TFila(10)
fila.adicionar_chamado('Fulano deseja formatar windows')
fila.adicionar_chamado('Beltrano instalar anti-vírus')
fila.adicionar_chamado('Ciclano trocar tonner da impressora')
print(f"A fila tem {fila.tamanho_fila()} chamados(s)")
print(f"Atendendo: {fila.atender_chamado()}")
print(f"A fila tem {fila.tamanho_fila()} chamados(s)")
print(f"Atendendo: {fila.atender_chamado()}")
print(f"A fila tem {fila.tamanho_fila()} chamados(s)")


    
