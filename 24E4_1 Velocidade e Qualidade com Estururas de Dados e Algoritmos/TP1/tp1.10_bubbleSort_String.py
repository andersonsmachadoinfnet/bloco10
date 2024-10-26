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

valores = ["Manuel Oliver Francisco da Conceição",
           "Thales Benício Araújo",
           "Letícia Antonella Nina Nascimento",
           "Simone Mariah Sales",
           "Emanuelly Adriana Giovanna Barbosa",
           "Eliane Mariah das Neves",
           "Fernanda Olivia Sabrina Dias",
           "Benício Vinicius Paulo Rodrigues",
           "Eduardo Luís Carvalho",
           "Priscila Lívia Lúcia Viana"]

print(bubbleSort(valores))