# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024

import os

def listarDir(pPath):
    os.chdir(pPath)
    for arquivo in os.listdir():
        if os.path.isfile(arquivo):
            print(pPath+os.sep+arquivo)
        elif os.path.isdir(arquivo):
            listarDir(pPath+os.sep+arquivo)
            os.chdir(pPath)


print("O diretorio atual é: "+os.getcwd())
iniciarDe = input("Digite o diretório a ser pesquisado: ")
if (iniciarDe=="") or (iniciarDe==None):
    iniciarDe = os.getcwd()

listarDir(iniciarDe)