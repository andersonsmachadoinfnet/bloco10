# Anderson S. M. Machado
from vetor import soma_serial
import numpy as np
import random
import time

numeros = []
for i in range(10000):
  numeros.append(random.randint(0,100000))
a = np.array(numeros)

time_ini = time.time()
r = soma_serial(a)
time_fim = time.time()-time_ini
print(f"Soma de 10000 numeros em {time_fim} no modo paralelo.")

time_ini = time.time()
r = 0
for i in range(len(numeros)-1):
  r += numeros[i]
time_fim = time.time()-time_ini
print(f"Soma de 10000 numeros em {time_fim} no modo sequencial")
