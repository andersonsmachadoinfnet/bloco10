import numpy as np
from numba import jit, prange

@jit(nopython=True, parallel=True)
def maximo_paralela(lista):
    maximo = lista[0]
    # O 'prange' é utilizado para criar um loop paralelizado
    for i in prange(1,len(lista)):
        if lista[i]>maximo:
            maximo = lista[i]
    return maximo

# Exemplo de uso
if __name__ == '__main__':
    lista = np.random.randint(1, 100, size=1000000)  # Lista com 1 milhão de elementos
    resultado = maximo_paralela(lista)
    print(f"O valor máximo na lista é: {resultado}")
