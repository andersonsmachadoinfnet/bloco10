# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024
 
def ehPalindromo(palavra):
    l = len(palavra)
    if l==1:
        return True
    elif palavra[l-1]!=palavra[0]:
        return False
    else:
        return ehPalindromo(palavra[1:l-1])

palavra=input("Digite uma palavra para ver se é um palíndromo: ")
print(ehPalindromo(palavra))
