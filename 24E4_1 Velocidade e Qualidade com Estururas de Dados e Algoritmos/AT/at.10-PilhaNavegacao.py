# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

class TPilha:
    def __init__(self):
        self.FItens = []

    def adicionaNaPila(self, pItm):
        self.FItens.append(pItm)
    
    def pop(self):
        if self.FItens.count==0:
            raise Exception("A pilha está vazia!")
        lItm = self.FItens[len(self.FItens)-1]
        del self.FItens[len(self.FItens)-1]
        return lItm
    
    def ver_topo(self):
        if self.FItens.count==0:
            raise Exception("A pilha está vazia!")
        return self.FItens[len(self.FItens)-1]

class TNavegacao:
    def __init__(self):
        self.FVoltar = TPilha()
        self.FAvancar= TPilha()
    
    def visitar(self, site):
        self.FVoltar.adicionaNaPila(site)
        print(f"Acessando: {self.FVoltar.ver_topo()}")
    
    def voltar(self):
        self.FAvancar.adicionaNaPila(self.FVoltar.pop())
        print(f"Voltando para: {self.FVoltar.ver_topo()}")
    
    def avancar(self):
        self.FVoltar.adicionaNaPila(self.FAvancar.pop())
        print(f"Avançando para: {self.FVoltar.ver_topo()}")

Navegacao = TNavegacao()
Navegacao.visitar("www.google.com")
Navegacao.visitar("www.uol.com")
Navegacao.visitar("www.globo.com")
Navegacao.voltar()
Navegacao.avancar()