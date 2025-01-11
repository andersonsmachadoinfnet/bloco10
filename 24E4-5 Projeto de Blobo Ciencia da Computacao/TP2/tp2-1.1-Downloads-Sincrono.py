#Aluno: Anderson S M Machado
# Código usado somente para comparações de tempo

import requests
import time

start_time = time.time()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s segundos ---" % (time.time() - start_time))