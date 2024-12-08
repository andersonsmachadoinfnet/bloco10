# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

def selectionSort(array, size):  # Fonte: https://www.geeksforgeeks.org/python-program-for-selection-sort/
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# seleciona o elemento mínimo de cada iteração
			if array[j] < array[min_index]:
				min_index = j
		# troca os elementos
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('A lista ordenada é:')
print(arr)
