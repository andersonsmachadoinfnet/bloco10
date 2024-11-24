# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_5
# Disciplina: Projeto de bloco: Ciencia da Computacao
# Professor : Francisco Benjamim Filho
# Data      : 23/11/2024

import time
def carregarLista(pNomeArq):
  with open(pNomeArq, "r") as arquivo:
    linhas = arquivo.readlines()
  return linhas

# metodo de ordenacao
# complexidade: O(n*n)
def bubbleSort(lista):
  for i in range(len(lista)-1):
    for j in range(len(lista)-1):
      if lista[j]>lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista

# metodo de ordenacao selectionSort
# complexidade: O(n*n)
def selectionSort(lista, tamanho):
  for ind in range(tamanho):
    min_index = ind
    for j in range(ind+1, tamanho):
      # selecione o elemento minimo
      if lista[j]<lista[min_index]:
        min_index = j
    # troca os elementos
    lista[ind], lista[min_index] = lista[min_index], lista[ind]
  return lista

# metodo de ordenacao Insert Sort
# complexidade: o(n*n)
def insertionSort(lista):
  n=len(lista)
  if n<=1:
    return # nada a ordenar
  for i in range(1, n):
    key=lista[i]
    j=i-1
    while j>=0 and key<lista[j]:
      lista[j+1]=lista[j]
      j-=1
    lista[j+1]=key
  return lista

lista = carregarLista("lista.txt")
tempo_inicial=time.time()
listaOrdenada = bubbleSort(lista)
tempo_final=time.time()
print(f"bubbleSort   : {tempo_final-tempo_inicial}")

lista = carregarLista("lista.txt")
tempo_inicial=time.time()
listaOrdenada = selectionSort(lista, len(lista))
tempo_final=time.time()
print(f"selectionSort: {tempo_final-tempo_inicial}")

lista = carregarLista("lista.txt")
tempo_inicial=time.time()
listaOrdenada = insertionSort(lista)
tempo_final=time.time()
print(f"InsertionSort: {tempo_final-tempo_inicial}")
