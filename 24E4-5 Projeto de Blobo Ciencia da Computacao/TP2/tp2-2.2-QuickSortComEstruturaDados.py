# Anderson S. M. Machado

class TEstudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def toString(self):
        return f"{self.nome} nota: {self.nota}"

def quicksort(pArray):
    if len(pArray) <= 1:
        return pArray
    
    lPivot = pArray[0]
    lMenores = [x for x in pArray[1:] if x.nota < lPivot.nota]
    lMaiores = [x for x in pArray[1:] if x.nota >= lPivot.nota]
    return quicksort(lMenores) + [lPivot] + quicksort(lMaiores)

lista = []
lista.append(TEstudante("Fulano", 9))
lista.append(TEstudante("Ciclano", 7))
lista.append(TEstudante("Beltrano", 10))
lista.append(TEstudante("Zultano", 8))
listaOrdenada = quicksort(lista)
for itm in listaOrdenada:
    print(itm.toString())
