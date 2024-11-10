# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

def inverter_fila(pFila):
    lSaida = []
    for i in range(len(pFila)-1, -1, -1):
        lSaida.append(pFila[i])
    return lSaida

fila = [1,2,3,4,5,6,7,8,9]
filaInvertida = inverter_fila(fila)

print(f"Fila normal   : {fila}")
print(f"Fila Invertida: {filaInvertida}")