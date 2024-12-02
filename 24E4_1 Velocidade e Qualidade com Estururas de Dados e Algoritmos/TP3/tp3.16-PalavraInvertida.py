# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024
 
def palavraInvertida(palavra):
    return _palavraInvertida(palavra, '')

def _palavraInvertida(palavra, invertida):
    if len(palavra)==len(invertida):
        return invertida
    
    l = len(invertida)
    invertida = invertida + palavra[0-(l+1)]
    return _palavraInvertida(palavra, invertida)

print(palavraInvertida("recursao"))