#Anderson S M Machado
def PinturaCadeiras(qtdCadeiras, qtdCores):
    if qtdCadeiras == 1:
        return qtdCores
    if qtdCadeiras == 0:
        return qtdCores
    
    dp = [0] * (qtdCadeiras + 1)
    dp[1] = qtdCores     
    for i in range(2, qtdCadeiras + 1):
        dp[i] = dp[i - 1] * (qtdCores - 1)
    return dp[qtdCadeiras]

QTDCADEIRAS = 4
QTDCORES    = 3 
print(f"Com {QTDCADEIRAS} cadeiras e {QTDCORES} cores há {PinturaCadeiras(QTDCADEIRAS, QTDCORES)} possibilidade de pintar sem repetir cores adjacentes")  
