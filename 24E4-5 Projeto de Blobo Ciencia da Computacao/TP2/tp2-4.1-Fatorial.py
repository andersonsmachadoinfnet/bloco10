def fatorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fatorial(n - 1) * n

numeros = [3,6,9]
for i in numeros:
    print("O fatorial de "+str(i)+" é: "+str(fatorial(i)))