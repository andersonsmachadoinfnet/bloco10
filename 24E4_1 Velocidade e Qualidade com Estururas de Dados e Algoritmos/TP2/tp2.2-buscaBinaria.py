# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 09/11/2024

def buscaBinaria(pLista, pItm):
    lIdxMenor = 0
    lTamanho  = len(pLista)
    lIdxMaior = lTamanho-1

    while (lIdxMaior-lIdxMenor)>=0:
        lIdxMeio  = (lIdxMenor + lIdxMaior) // 2 
        lItmMeio  = pLista[lIdxMeio]
                
        if lItmMeio==pItm:
            return f"Encontrado na posição {lItmMeio}"
        
        elif lItmMeio>pItm:
            lIdxMaior = lItmMeio-1
        
        elif lItmMeio<pItm:
            lIdxMenor = lItmMeio+1
    
    return "Item inexistente"

lista = [0,1,2,3,4,5,6,7,8,9,10]
print(buscaBinaria(lista, 6))

