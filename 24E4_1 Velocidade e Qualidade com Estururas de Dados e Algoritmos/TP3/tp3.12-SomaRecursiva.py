# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024

def soma(lista):
    if len(lista)>1:
        i = lista.pop(0)+lista.pop(0)
        lista.append(i)
        return soma(lista)
    else:
        return lista.pop(0)
    
lista = [1,2,3,4,5,6,7,8,9,10]
print(soma(lista))