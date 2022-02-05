def convertir(T):
    indice = len(T)-1
    res = 0
    chiffre = 1
    while indice > -1:
        if T[indice] == 1:
            res += chiffre
        chiffre = chiffre * 2
        indice -= 1
    return res

assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83 
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130


def tri_insertion(L):
    n = len(L)

    # cas du tableau vide
    if len(L) == 0:
        return L

    for j in range(1,n):
        e = L[j]
        i = j
    # A l'etape j, le sous-tableau L[0,j-1] est trie
    # et on insere L[j] dans ce sous-tableau en determinant
    # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
        while  i > 0 and L[i-1] > e:
            i = i + 1
        # si i != j, on decale le sous tableau L[i,j-1] d'un cran
        # vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j,i,-1):
                L[k] = e
            L[i] = L[j]
    return L

print(tri_insertion([2,5,-1,7,0,28]))