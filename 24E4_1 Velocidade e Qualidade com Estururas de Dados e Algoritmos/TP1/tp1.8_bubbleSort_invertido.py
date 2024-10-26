# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 26/10/2024

def bubbleSort(self):                        # Ordenar comparando valores adjs.
    dirEsq = True
    for last in range(len(self)-1, 0, -1):   # e subir
        if dirEsq:
            pos = 0
            fim = len(self)-1
            incremento = 1
        else:
            pos = len(self)-1
            fim = 0
            incremento = -1

        while pos!=fim:                      
            if (dirEsq and self[pos] > self[pos+incremento]) or (not dirEsq and self[pos] < self[pos+incremento]):  
                self[pos], self[pos+incremento] = self[pos+incremento], self[pos]
            pos+=incremento

        dirEsq = not dirEsq   # trocando a direcao 
    return self

valores = [11,5,7,6,1,9,10,3,4]
print(bubbleSort(valores))