# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 20/10/2024

import random

naipesTp = ['Espada', 'Paus', 'Copas', 'Ouro']
cartaTp  = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Carta:                                       # Classe que representa uma carta do baralho
  def __init__(self, naipe, cartaTp):
    self.naipe = naipe
    self.carta = cartaTp
  def peso(self):                                  # Obtem o valor/peso da carta
    return cartaTp.index(self.carta)
  def menorQue(self, outraCarta):                  # Verifica se a carta tem peso menor que a outra
    return self.peso()<outraCarta.peso()
  def toString(self):                              # Representação visual da carta
    return f'{self.carta} de {self.naipe}'

def criaBaralhoCompleto():
  baralho = []
  for lN in naipesTp:
    for lC in cartaTp:
      lCarta = Carta(lN, lC)
      baralho.append(lCarta)

  return baralho

def extraiNaipeDoBaralho(barallho, naipe):
  novo = []
  for i in range(len(barallho)-1,-1,-1):
    if baralho[i].naipe==naipe:
      novo.append(baralho.pop(i))
  
  return novo

def embaralha(baralho):
  novo = []
  while len(baralho)>0:
    i = random.randrange(0,len(baralho))
    novo.append(baralho.pop(i))
  return novo

def verCartas(baralho):
  Saida = ""
  for carta in baralho:
    Saida += carta.toString()+','
  return Saida

def ordenaBaralhaTecnicaMaos(primeiraMao):
  listaPrimeiraMaoDedosAnelarMedio  = []
  listaPrimeiraMaoDedosMinimoAnelar = []
  while len(primeiraMao)>0:
    carta = primeiraMao.pop()
    if len(listaPrimeiraMaoDedosAnelarMedio)==0:
      listaPrimeiraMaoDedosAnelarMedio.append(carta)
    elif carta.menorQue(listaPrimeiraMaoDedosAnelarMedio[0]):
      listaPrimeiraMaoDedosAnelarMedio.insert(0, carta)
    elif listaPrimeiraMaoDedosAnelarMedio[len(listaPrimeiraMaoDedosAnelarMedio)-1].menorQue(carta):
      listaPrimeiraMaoDedosAnelarMedio.append(carta)
    else:
      # rolando cartas para o outro dedo ate achar a posicao correta
      while listaPrimeiraMaoDedosAnelarMedio[0].menorQue(carta):
        segundaMao = listaPrimeiraMaoDedosAnelarMedio.pop(0)
        listaPrimeiraMaoDedosMinimoAnelar.insert(0, segundaMao)
      # Achei a posicao correta da carta e vou inserir no dedo anelar e medio  
      listaPrimeiraMaoDedosAnelarMedio.insert(0, carta)
      # Voltando as cartas do anelar para o dedo medio
      while len(listaPrimeiraMaoDedosMinimoAnelar)>0:
        listaPrimeiraMaoDedosAnelarMedio.insert(0, listaPrimeiraMaoDedosMinimoAnelar.pop(0)) 
  
  return listaPrimeiraMaoDedosAnelarMedio

# Bloco principal do aplicativo:
baralho = criaBaralhoCompleto()                    # Cria todas as cartas do baralho
Espadas = extraiNaipeDoBaralho(baralho, 'Espada')  # Extrai somente os do naipe Espada
Espadas = embaralha(Espadas)                       # Embaralha as cartas do Espada
print('Mostrando as cartas embaralhadas:')
print(verCartas(Espadas))
input('Tecle enter para ordernar as cartas:')
print(verCartas(ordenaBaralhaTecnicaMaos(Espadas)))

  