# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

def totalDeItensImpares(pFila):
    qImpar = 0
    for i in range(len(pFila)):
        if (pFila[i]%2!=0):
            qImpar=qImpar+1
    return qImpar

fila = [1,2,3,4,5]
print(f"Dado a fila {fila}")
print(f"Existe(m) {totalDeItensImpares(fila)} número(s) ímpar(es)")