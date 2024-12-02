# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024

def quicksort(pArray):
    if len(pArray) <= 1:
        return pArray
    
    lPivot = pArray[0]
    lMenores = [x for x in pArray[1:] if x < lPivot]
    lMaiores = [x for x in pArray[1:] if x >= lPivot]
    return quicksort(lMenores) + [lPivot] + quicksort(lMaiores)

lista = [10, 7, 8, 9, 1, 5]
listaOrdenada = quicksort(lista)
print("Ordenado: "+str(listaOrdenada))