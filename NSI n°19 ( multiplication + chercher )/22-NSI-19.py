from re import I


def multiplication(n1,n2):
    res = 0
    if n1 == 0 or n2 == 0:
        return res
    if n1 > 0 and n2 > 0:
        for i in range(n2):
            res+=n1
        return res
    if n1 < 0 and n2 < 0:
        for i in range(-n2):
            res-=n1
        return res
    if n1 < 0 and n2 > 0:
        for i in range(n2):
            res-=n1
        return -res
    if n1 > 0 and n2 < 0:
        for i in range(-n2):
            res+=n1
        return -res
    
    assert multiplication(3,5) == 15 
    assert multiplication(-4,-8) == 32 
    assert multiplication(-2,6) == -12 
    assert multiplication(-2,0) == 0


def chercher(T,n,i,j):
    if i < 0 or j > len(T) :
        print("Erreur")
        return None    
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, i+1 , j)
    elif T[m] > n  :
        return chercher(T, n, i, j-1 )
    else :
        return m

print(chercher([1,5,6,6,9,12],6,0,5))
