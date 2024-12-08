# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024


class TContato:
    def __init__(self, pNome, pTelefone):
        self.Nome = pNome
        self.Tel  = pTelefone
    
class TLista:
    def __init__(self):
        self.FLista = []
    
    def adicionar(self, pContato):
        self.FLista.append(pContato)
    
    def localizar(self, pNome):
        for lItem in self.FLista:
            if lItem.Nome==pNome:
                return lItem
        return None


# inicializando dados
lista = TLista()
lista.adicionar(TContato("Fulano","2222-2222"))
lista.adicionar(TContato("Ciclano","3333-3333"))
lista.adicionar(TContato("Beltrano","4444-4444"))

# Encontrado contato
item = lista.localizar("Ciclano")
if item!=None:
    print(f"O telefone de {item.Nome} é {item.Tel}")
else:
    print("Contato inexistente")