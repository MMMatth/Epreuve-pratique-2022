def conv_bin(n):
    L = []
    while n >= 1:
        if n%2 == 1:
            L.append(1 )
            n = n//2
        if n == 0 :
            return(L,len(L))
        if n%2 == 0:
            L.append(0)
            n = n//2
    
    return(L.reverse(),len(L))





def tri_bulles(T):
    n = len(T)
    for i in range(0,-n,-1):
        for j in range(n-1):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

print(tri_bulles([5,7,1,2,9,8,7,1,0]))