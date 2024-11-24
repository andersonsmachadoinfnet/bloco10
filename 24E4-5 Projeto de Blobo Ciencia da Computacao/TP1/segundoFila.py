# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_5
# Disciplina: Projeto de blobo: Ciencie da Computacao
# Professor : Francisco Benjamim Filho
# Data      : 23/11/2024

import csv
import time

# lendo o arquivo com a lista de arquivos no diretorio
def carregarLista(pNomeArq):
  with open(pNomeArq, "r") as arquivo:
    linhas = arquivo.readlines()
  return linhas

# lendo o arquivo de inclusoes e exclusoes do professor
def carregaOperacoes():
  with open("oprInsDel.csv", "r") as arquivo:
    arq_csv = csv.reader(arquivo, delimiter=",")
    saida   = []
    for i, linha in enumerate(arq_csv):
      if i!=0:
        saida.append(linha)
  return saida

# classe fila
class TFila:
  def __init__(self):
    self.FItens = []

  def adicionar(self, pItm):
    self.FItens.append(pItm)

  def quantidade(self):
    return len(self.FItens)

  def pop(self):
    if self.FItens.count==0:
      raise Exception("A fila esta vazia!")
    lItm = self.FItens[0]
    del self.FItens[0]
    return lItm

  def inserir(self, itm, posicao):
    lBuffer = TFila()
    while self.quantidade()>=posicao:
      lBuffer.adicionar(self.pop())
    self.adicionar(itm)
    while lBuffer.quantidade()>0:
      self.adicionar(lBuffer.pop())

  def remover(self, posicao):
    lBuffer = TFila()
    while self.quantidade()>posicao:
      lBuffer.adicionar(self.pop())
    lItemRemovido = self.pop()
    while lBuffer.quantidade()>0:
      self.adicionar(lBuffer.pop())

  def buscar(self, posicao):
    return self.FItens[posicao]

# Carregando lsta de arquivos
lista = carregarLista("lista.txt")
fila = TFila()
tempo_inicial = time.time()
for itm in lista:
  fila.adicionar(itm)
tempo_final=time.time()
print(f"Carregamento Lista: {tempo_final-tempo_inicial}")

# Inserindo dados do arquivo do professor
lista = carregaOperacoes()
tempo_inicial = time.time()
for itm in lista:
  fila.inserir(itm[2], int(itm[0])//10)
tempo_final = time.time()
print(f"Inserindo dados   : {tempo_final-tempo_inicial}")

# Removendo dados do arquivo do professor
tempo_inicial = time.time()
for itm in lista:
  fila.remover(int(itm[3])//10)
tempo_final = time.time()
print(f"Deletando dados   : {tempo_final-tempo_inicial}")

# Mostrando dados 1, 100, 1000 e 5000
print("Arquivo 0001      : "+fila.buscar(1))
print("Arquivo 0100      : "+fila.buscar(100))
print("Arquivo 1000      : "+fila.buscar(1000))
print("Arquivo 5000      : "+fila.buscar(5000))

