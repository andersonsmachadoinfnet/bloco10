import numpy as np
from numba import jit, prange

# Função auxiliar para particionar a lista
def partition(arr, low, high):
    pivot = arr[high]  # Escolhe o pivô como o último elemento
    i = low - 1  # Índice do menor elemento
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Função Quicksort com paralelismo
@jit(nopython=True, parallel=True)
def quicksort(arr, low, high):
    if low < high:
        # Particiona o vetor
        pi = partition(arr, low, high)

        # Chama recursivamente para as duas metades, em paralelo
        prange_low = prange(low, pi - 1)  # Para a parte esquerda
        prange_high = prange(pi + 1, high)  # Para a parte direita
        for _ in prange_low:
            quicksort(arr, low, pi - 1)
        for _ in prange_high:
            quicksort(arr, pi + 1, high)

# Criando uma lista de números aleatórios
arr = np.random.randint(0, 1000000, size=1000000)

# Chamando a função quicksort
quicksort(arr, 0, len(arr) - 1)

# Imprimindo os primeiros 10 elementos para verificar se está ordenado
print("Os primeiros 10 elementos ordenados:", arr[:10])
