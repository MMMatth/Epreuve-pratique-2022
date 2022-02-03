def maxi(tab):
    maxi = 0
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
    for i in range(len(tab)):
        if tab[i] == maxi:
            return maxi,i
    

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2