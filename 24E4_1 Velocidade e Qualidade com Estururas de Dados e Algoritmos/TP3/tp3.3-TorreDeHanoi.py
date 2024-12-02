# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024
# Fonte     : https://www.bosontreinamentos.com.br/logica-de-programacao/algoritmo-torre-de-hanoi-em-python/

def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return 1
    movimentos = torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    movimentos += 1
    movimentos += torre_hanoi(n-1, auxiliar, destino, origem)
    return movimentos

n = int(input("Digite o número de discos: "))
total_movimentos = torre_hanoi(n, "A", "C", "B")
print(f"Total de movimentos realizados: {total_movimentos}")