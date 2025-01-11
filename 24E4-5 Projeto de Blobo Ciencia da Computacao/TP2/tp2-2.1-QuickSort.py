# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado

import time

def quicksort(pArray):
    if len(pArray) <= 1:
        return pArray
    
    if pivotTipo==0:
        lPivotIdx = 0
    elif pivotTipo==1:
        lPivotIdx = len(pArray)-1
    else:
        lPivotIdx = len(pArray)//2
    
    lPivot = pArray[lPivotIdx]
    lMenores = []
    lMaiores = []
    for i in range(len(pArray)):
        if i!=lPivotIdx and pArray[i]<lPivot:
            lMenores.append(pArray[i])
        if i!=lPivotIdx and pArray[i]>=lPivot:
            lMaiores.append(pArray[i])
    return quicksort(lMenores) + [lPivot] + quicksort(lMaiores)

pivotTipo = 0
tempo_inicial=time.time()
for i in range(10000):
    lista = [10, 7, 8, 9, 1, 5, 20, 15, 17, 12, 6, 18, 16, 13, 14, 2]
    listaOrdenada = quicksort(lista)
tempo_final=time.time()
print(f"Pivot primeiro elemento: {tempo_final-tempo_inicial}")


pivotTipo = 1
tempo_inicial=time.time()
for i in range(10000):
    lista = [10, 7, 8, 9, 1, 5, 20, 15, 17, 12, 6, 18, 16, 13, 14, 2]
    listaOrdenada = quicksort(lista)
tempo_final=time.time()
print(f"Pivot último elemento  : {tempo_final-tempo_inicial}")

pivotTipo = 2
tempo_inicial=time.time()
for i in range(10000):
    lista = [10, 7, 8, 9, 1, 5, 20, 15, 17, 12, 6, 18, 16, 13, 14, 2]
    listaOrdenada = quicksort(lista)
tempo_final=time.time()
print(f"Pivot elemento mediano : {tempo_final-tempo_inicial}")

print("Ordenado: "+str(listaOrdenada))
