import numpy as np
from numba import jit, prange

# Função de soma paralelizada com OpenMP via Numba
@jit(nopython=True, parallel=True)
def soma_paralela(lista):
    soma = 0
    # O 'prange' é utilizado para criar um loop paralelizado
    for i in prange(len(lista)):
        soma += lista[i]
    return soma

# Exemplo de uso
if __name__ == '__main__':
    lista = np.random.randint(1, 100, size=1000000)  # Lista com 1 milhão de elementos
    resultado = soma_paralela(lista)
    print(f"A soma dos elementos da lista é: {resultado}")
