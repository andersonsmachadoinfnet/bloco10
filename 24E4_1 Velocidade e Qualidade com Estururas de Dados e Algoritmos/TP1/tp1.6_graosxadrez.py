# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 26/10/2024

def calculaPosicao(qtdGraos):
    posicao=0
    while (qtdGraos>0):
        qtdGraos = qtdGraos // 2
        posicao=posicao+1
    return posicao

qtdGraos = int(input('Informe a quantidade de grãos?'))
print('Essa quantidade será guardada em '+str(calculaPosicao(qtdGraos))+' quadrado(s) de xadrez.')