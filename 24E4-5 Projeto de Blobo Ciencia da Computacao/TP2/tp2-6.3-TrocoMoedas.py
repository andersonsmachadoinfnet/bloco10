# Anderson S M Machado

def troco(valor, moedas):
    lQtd = [0 for _ in range(len(moedas))]
    print(f"Troco para R$ {valor}:")
    for i in range(len(moedas)):
        if valor>=moedas[i]:
            q = valor // moedas[i]
            valor -= q*moedas[i]
            lQtd[i]= q
    
    for i in range(len(moedas)):
        if lQtd[i]>0:
            print(f"  {lQtd[i]} moeda(s) de R$ {moedas[i]}")


troco(0.94, [1.0, 0.5, 0.25, 0.10, 0.05, 0.01])
troco(1.30, [0.25, 0.01])
