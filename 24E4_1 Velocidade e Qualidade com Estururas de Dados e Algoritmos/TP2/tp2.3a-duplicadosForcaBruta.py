# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

def temItemDuplicado(pLista):
    lDuplicados = set()
    for i in range(len(pLista)-1):
        for j in range(len(pLista)-1):
            if (i!=j) and (pLista[i]==pLista[j]):
                lDuplicados.add(pLista[i])
    
    print(f"Os seguintes itens estão duplicados na lista: {lDuplicados}")

Lista = [0,1,2,3,4,5,6,7,8,9,10,3,11,8]
temItemDuplicado(Lista)