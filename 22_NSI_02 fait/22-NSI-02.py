# exo 1
def moyenne(note):
    tmp = 0
    tmp2 = 0
    for i in range (len(note)):
        tmp += note[i][0] * note[i][1]
        tmp2 += note[i][1]
    return tmp/tmp2

    
# exo 2
def pascal(n): 
    C= [[1]] 
    for k in range(1,n+1): 
        Ck = [1] 
        for i in range(1,k): 
            Ck.append(C[k-1][i-1]+C[k-1][i]) 
        Ck.append(1) 
        C.append(Ck) 
    return C
