# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024


def fatorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fatorial(n - 1) * n

print("O fatorial de 3 é: "+str(fatorial(3)))