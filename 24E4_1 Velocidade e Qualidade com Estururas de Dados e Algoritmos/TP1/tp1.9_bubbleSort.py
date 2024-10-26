# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 26/10/2024

def bubbleSort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

valores = [11,5,7,6,1,9,10,3,4]
print(bubbleSort(valores))