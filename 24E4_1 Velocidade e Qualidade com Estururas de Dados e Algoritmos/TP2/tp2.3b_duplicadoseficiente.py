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

def temItemDuplicado(pLista):
    lDuplicados = set()
    quick_sort(pLista, 0, len(pLista)-1) #primeiro eu ordeno a lista
    for i in range(len(pLista)-2):
        if pLista[i]==pLista[i+1]:
            lDuplicados.add(pLista[i])
    
    print(f"Os seguintes itens estão duplicados na lista: {lDuplicados}")

Lista = [2,6,2,1,0,5,7,9,8,10]
temItemDuplicado(Lista)