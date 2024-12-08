# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

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


nomes = ["Miguel","Helena","Gael","Theo","Arthur","Heitor","Maria Alice","Alice","Davi","Laura","Miguel","Ciclano"]
tabela = THashTable(len(nomes))
qDup  = 0
for i in range(len(nomes)-1):
    if tabela.buscar(nomes[i])==None:
        tabela.inserir(nomes[i],'chave'+str(i))
    else:
        qDup += 1
        print(f"O {nomes[i]} está duplicado na lista.")
print(f"Total de nomes duplicados: {qDup}")