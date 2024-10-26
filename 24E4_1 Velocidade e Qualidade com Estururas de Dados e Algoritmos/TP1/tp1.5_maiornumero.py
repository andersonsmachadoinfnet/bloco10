# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 26/10/2024

def maiorNumeroDaLista(pLista):
    maior = None
    for i in pLista:
        if (maior==None) or (i>maior):
            maior=i
    return maior

valores = [2,5,7,6,0,9,10,3,4]
print(f"Dado a lista de valores: {valores}")
print("O maior número é: "+str(maiorNumeroDaLista(valores)))