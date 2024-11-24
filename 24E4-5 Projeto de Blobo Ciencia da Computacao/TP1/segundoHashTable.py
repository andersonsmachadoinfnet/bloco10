# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_5
# Disciplina: Projeto de bloco: Ciencia da Computacao
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

# classe hashtable
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
    self.size+1

  def buscar(self, chave):
    indice=self.hash(chave)
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

# carregando lista de arquivos
lista = carregarLista("lista.txt")
tabela= THashTable(10400)
tempo_inicial = time.time()
for i, itm in enumerate(lista):
  tabela.inserir(str(i), itm)
tempo_final=time.time()
print(f"Carregamento Lista: {tempo_final-tempo_inicial}")

# Inserindo dados do arquivo do professor
lista = carregaOperacoes()
tempo_inicial = time.time()
for itm in lista:
  tabela.inserir( str(int(itm[0])//10), itm[2] )
tempo_final=time.time()
print(f"Inserindo dados   : {tempo_final-tempo_inicial}")

# Removendo dados do arquivo do professor
tempo_inicial = time.time()
for itm in lista:
  tabela.remover(str(int(itm[3])//10))
tempo_final=time.time()
print(f"Deletando dados   : {tempo_final-tempo_inicial}")

# Mostrando dados 1, 100, 1000 e 5000
print("Arquivo 0001      : "+tabela.buscar("1"))
print("Arquivo 0100      : "+tabela.buscar("100"))
print("Arquivo 1000      : "+tabela.buscar("1000"))
print("Arquivo 5000      : "+tabela.buscar("5000"))
