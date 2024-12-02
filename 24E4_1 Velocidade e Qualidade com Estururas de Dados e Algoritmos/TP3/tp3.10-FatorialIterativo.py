# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024


def fatorial(n):
    valor = 1
    for i in range(1, n+1):
        valor = valor * i
    return valor

numero = int(input("Digite o número fatorial: "))
print(f"O fatorial de {numero} é: "+str(fatorial(numero)))