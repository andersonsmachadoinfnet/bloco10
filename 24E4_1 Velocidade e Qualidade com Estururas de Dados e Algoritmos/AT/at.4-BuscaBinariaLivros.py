# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 08/12/2024

def buscaBinaria(pLista, pItm):
    lIdxMenor = 0
    lTamanho  = len(pLista)
    lIdxMaior = lTamanho-1
    lIteracoes=0

    while (lIdxMaior-lIdxMenor)>=0:
        lIdxMeio  = (lIdxMenor + lIdxMaior) // 2 
        lItmMeio  = pLista[lIdxMeio]
        lIteracoes+=1
                
        if lItmMeio==pItm:
            return f"Busca Binária   : {pItm} encontrado na posição {lIdxMeio} na iteração {lIteracoes}"
        
        elif lItmMeio>pItm:
            lIdxMaior = lIdxMeio-1
        
        elif lItmMeio<pItm:
            lIdxMenor = lIdxMeio+1
    
    return "Item inexistente"

def buscaSequencial(pLista, pItm):
    for lIteracoes in range(len(pLista)-1):
        if pLista[lIteracoes]==pItm:
            return f"Busca Sequêncial: {pItm} encontrado na posição {lIteracoes} na iteração {lIteracoes}"

# Criando lista de 100mil livros padrao ISBN-13
lista = []
for i in range(100000):
    lista.append(9870000000000+i)
print(buscaBinaria(lista, 9870000055006))
print(buscaSequencial(lista, 9870000055006))