# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_1
# Disciplina: Velocidade e qualidade com estruturas de dados e algoritmos
# Professor : Flávio da Silva Neves
# Data      : 01/12/2024
 
def contarCaracter(palavra, letra):
    return _contarCaracter(palavra, letra, 0)

def _contarCaracter(palavra, letra, soma):
    l = len(palavra)
    if l==0:
        return soma
    
    if palavra[0]==letra:
        soma += 1
    
    return _contarCaracter(palavra[1:l], letra, soma)

print(contarCaracter("banana","a"))