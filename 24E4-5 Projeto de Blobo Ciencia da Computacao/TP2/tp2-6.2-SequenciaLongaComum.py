def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    Seq = ""
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                Seq = Seq + X[i-1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n], Seq

X = "AGGTAB"
Y = "GXTXAYB"
print(f"Comprimento da LCS de {X}x{Y}: {lcs(X, Y)}")

X = "AC"
Y = "ABC"
print(f"Comprimento da LCS de {X}x{Y}: {lcs(X, Y)}")
