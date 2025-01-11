# Anderson S M Machado
import time

def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        #print(f"Mova o disco 1 de {origem} para {destino}")
        return 1
    movimentos = torre_hanoi(n-1, origem, auxiliar, destino)
    #print(f"Mova o disco {n} de {origem} para {destino}")
    movimentos += 1
    movimentos += torre_hanoi(n-1, auxiliar, destino, origem)
    return movimentos

discos = [2,4,8,16]
for n in discos:
    tempo_inicial=time.time()
    total_movimentos = 0
    total_movimentos = torre_hanoi(n, "A", "C", "B")
    tempo_final=time.time()
    print(f"Total de movimentos realizados com {n} discos: {total_movimentos} no tempo: {tempo_final-tempo_inicial}")