def lcs(X, Y): 
 
    m = len(X) 
    n = len(Y) 

    L = [[None]*(n + 1) for i in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1])

    sub_sequence = []
    i = m
    j = n

    # find the lcs
    while i > 0 and j > 0:
        if L[i][j] != L[i - 1][j]:
            sub_sequence.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            i -= 1
    print("".join(sub_sequence[::-1]))
    return L[m][n]


res=lcs("AGGTAB","GXTXAYB")   
print(res)