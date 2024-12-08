# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

from random import randint
import time

def bubbleSort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Gerando listas
ListaMil = []
ListaDezMil =[]

for i in range(10000):
    numero = randint(0,10000)
    if i<=1000:
        ListaMil.append(numero)
    ListaDezMil.append(numero)

tempo_inicial = time.time()
lista = bubbleSort(ListaMil)
tempo_final = time.time()
print(f"Ordenando  1000 itens: {tempo_final-tempo_inicial}")

tempo_inicial = time.time()
lista = bubbleSort(ListaDezMil)
tempo_final = time.time()
print(f"Ordenando 10000 itens: {tempo_final-tempo_inicial}")