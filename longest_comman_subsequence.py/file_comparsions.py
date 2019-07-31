def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n + 1) for i in range(m + 1)]
    directions={}
    
    for i in range(m + 1):
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
                directions[i, j] = "E"#empty
                
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
                directions[i, j] = "D" #diagonal
            else: 
                #L[i][j] = max(L[i-1][j], L[i][j-1])
                if(L[i - 1][ j] >= L[i][ j - 1]):
                    L[i][j] = L[i - 1][ j]
                    directions[i, j] = "L" #left
                else:
                    L[i][ j] = L[i][j - 1]
                    directions[i, j] = "U" #up
    
    print(directions)

    sub_sequence = []

    i = m
    j = n

    while i > 0 and j > 0:
        if  directions[i, j] == 'D':
            sub_sequence.append("LCS " + X[i - 1])
            i -= 1
            j -= 1
        elif directions[i, j] == 'U':
            # print 'add', B[j-1]
            sub_sequence.append('ADD ' + B[j - 1])
            j -= 1
        elif directions[i, j] == 'L':
            # print 'remove', A[i-1]
            sub_sequence.append('REM ' + A[i - 1])
            i -= 1
        elif directions[i, j] == 'E':
            if i == 0:
                # print 'add', B[j-1]
                operations.append('ADD ' + B[j - 1])
                j -= 1
            elif j == 0:
                # print 'remove', A[j-1]
                operations.append('REM ' + A[j - 1])
                i -= 1
            
            
    result="".join(sub_sequence[::-1])        
    print("  ".join(sub_sequence[::-1]))
    return L[m][n]



def getFileContent(path):
    with open(path) as f:
        return list(f)
    
A = getFileContent(r'C:\Users\AG29527\Desktop\file.txt')
B = getFileContent(r'C:\Users\AG29527\Desktop\table.txt')
#res=lcs(list("AGGTAB"),list("GXTXAYB"))
res=lcs(A,B) 
print(res)