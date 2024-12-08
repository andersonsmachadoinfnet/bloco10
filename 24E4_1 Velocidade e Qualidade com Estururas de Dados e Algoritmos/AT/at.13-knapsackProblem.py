# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

# Variação do código: https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
def mochila(pPesos, pValores, pPesoMax, n): 
	if n == 0 or pPesoMax == 0: 
		return 0
	if Memorizacao[n][pPesoMax] != -1: 
		return Memorizacao[n][pPesoMax]     # <- Retorno memorizado evitando recursão

	# calculando... 
	if pPesos[n-1] <= pPesoMax: 
		Memorizacao[n][pPesoMax] = max(pValores[n-1] + mochila(pPesos, pValores, pPesoMax-pPesos[n-1], n-1), mochila(pPesos, pValores, pPesoMax, n-1)) 
		return Memorizacao[n][pPesoMax] 
	elif pPesos[n-1] > pPesoMax: 
		Memorizacao[n][pPesoMax] = mochila(pPesos, pValores, pPesoMax, n-1) 
		return Memorizacao[n][pPesoMax] 

valor = [15, 10, 12]    # Valor significativo do item
peso  = [1, 2, 3]       # Peso de cada item
pesoMax = 5             # Peso máximo que a mochila aguenta em kg
n = len(valor) 
	
# iniciando a matrix de memorizacao. 
Memorizacao = [[-1 for i in range(pesoMax + 1)] for j in range(n + 1)]
print("O valor máximo a ser levado na mochila é de: ") 
print(mochila(peso, valor, pesoMax, n)) 

