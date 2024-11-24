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

# Classe Pilha
class TPilha:
  def __init__(self):
    self.FItens = []

  def adicionar(self, pItm):
    self.FItens.append(pItm)

  def quantidade(self):
    return len(self.FItens)

  def pop(self):
    if self.FItens.count==0:
      raise Exception("A pilha esta vazia!")
    lItm = self.FItens[len(self.FItens)-1]
    del self.FItens[len(self.FItens)-1]
    return lItm

  def inserir(self, itm, posicao):
    lBuffer = TPilha()
    while self.quantidade()>=posicao:
      lBuffer.adicionar(self.pop())
    self.adicionar(itm)
    while lBuffer.quantidade()>0:
      self.adicionar(lBuffer.pop())

  def remover(self, posicao):
    lBuffer = TPilha()
    while self.quantidade()>posicao:
      lBuffer.adicionar(self.pop())
    lItemRemovido = self.pop()
    while lBuffer.quantidade()>0:
      self.adicionar(lBuffer.pop())

# Carregando lsta de arquivos
lista = carregarLista("lista.txt")
pilha = TPilha()
tempo_inicial = time.time()
for itm in lista:
  pilha.adicionar(itm)
tempo_final=time.time()
print(f"Carregamento Lista: {tempo_final-tempo_inicial}")

# Inserindo dados do arquivo do professor
lista = carregaOperacoes()
tempo_inicial = time.time()
for itm in lista:
  pilha.inserir(itm[2], int(itm[0])//10)
tempo_final = time.time()
print(f"Inserindo dados   : {tempo_final-tempo_inicial}")

# Removendo dados do arquivo do professor
tempo_inicial = time.time()
for itm in lista:
  pilha.remover(int(itm[3])//10)
tempo_final = time.time()
print(f"Deletando dados   : {tempo_final-tempo_inicial}")

# Mostrando dados 1, 100, 1000 e 5000:
while pilha.quantidade()>0:
  lItm = pilha.pop()
  if (pilha.quantidade()==1) or (pilha.quantidade()==100) or (pilha.quantidade()==1000) or (pilha.quantidade()==5000):
    print(f"Arquivo {pilha.quantidade()} : {lItm}")
