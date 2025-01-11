#Anderson S M Machado

def permutacoes(string):
	if len(string) == 1:
		return [string]

	permutations = []
	for i in range(len(string)):
		letra = string[i]
		resto = string[:i] + string[i+1:]
		for perm in permutacoes(resto):
			permutations.append(letra + perm)

	return permutations

string ='ABC'

Resultado = permutacoes(string)
z=set(Resultado)
for perm in z:
	print(perm)

