# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

class THashTable:
    def __init__(self, capacidade):
        self.capacidade=capacidade
        self.tabela    = [[] for _ in range(capacidade)]
        self.size      = 0

    def hash(self, chave):
        return hash(chave) % self.capacidade
    
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return

        self.tabela[indice].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        indice =self.hash(chave)
        for par in self.tabela[indice]:
            if par[0]==chave:
                return par[1]
        return None

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0]==chave:
                del self.tabela[indice][i]
                self.size-=1
                return True
        return False
    
    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " +", ".join(resultado)+" }"

tabela = THashTable(10)
tabela.inserir('chave1','nome1')
tabela.inserir('chave2','nome2')