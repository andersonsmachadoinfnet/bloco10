# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

def quick_sort(lista, inicio, fim):
    if inicio > fim:
        return
    anterior = inicio
    posterior = fim
    pivo = lista[inicio]

    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivo:
            posterior = posterior - 1

        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior = anterior + 1

        while anterior < posterior and lista[anterior] <= pivo:
            anterior = anterior + 1

        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior = posterior - 1

        lista[anterior] = pivo

    quick_sort(lista, inicio, anterior - 1)
    quick_sort(lista, anterior + 1, fim)

lista = [2,8,7,6,5,10,15,14,13,11,12]
quick_sort(lista, 0, len(lista)-1)
print(f"A lista ordenada é {lista}")