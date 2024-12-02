# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024
# Fonte     : Material do Professoror, Flávio da Silva Neves

def quickselect(array, low, high, k):
    # Caso base: se o array tiver apenas um elemento
    if low == high:
        return array[low]
    
    # Particiona o array e obtém o índice do pivô
    pivot_index = partition(array, low, high)
    
    # Caso em que o pivô é o k-ésimo menor elemento
    if k == pivot_index:
        return array[k]
    # Caso o k-ésimo elemento esteja à esquerda do pivô
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    # Caso o k-ésimo elemento esteja à direita do pivô
    else:
        return quickselect(array, pivot_index + 1, high, k)

def partition(array, low, high):
    # Escolhe o pivô como o último elemento
    pivot = array[high]
    i = low - 1  # Índice do menor elemento
    
    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Troca os elementos
    
    # Coloca o pivô na posição correta
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1

# Exemplo de uso
array = [10, 4, 5, 8, 6, 11, 26, 30, 35,12,14]
k = 3  # Queremos o 3º menor elemento
result = quickselect(array, 0, len(array) - 1, k - 1)  # k - 1 porque o índice é zero-based
print(f"O {k}-ésimo menor elemento é: {result}")