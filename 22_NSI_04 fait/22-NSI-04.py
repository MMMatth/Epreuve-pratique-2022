def recherche(tab):
    L= []
    for i in range (len(tab)-1):
        if tab[i] == tab[i+1]-1:
            L.append((tab[i],tab[i+1]))
    return L


def propager(M, i, j, val): 
    """[BAH ELLE PROPAGE GROS CON]

    Args:
        M ([int]): [M]
        i ([int]): [i]
        j ([int]): [j]
        val ([int]): [val]
    """
    if M[i][j]== val: 
        return 
 
    M[i][j]=val 
 
    # l'élément en haut fait partie de la composante 
    if ((i-1) >= 0 and M[i-1][j] == 1): 
        propager(M, i-1, j, val) 
 
    # l'élément en bas fait partie de la composante 
    if ((i+1) < len(M) and M[i+1][j] == 1): 
        propager(M, i+1, j, val) 
 
    # l'élément à gauche fait partie de la composante 
    if ((j-1) >= 0 and M[i][j-1] == 1): 
        propager(M, i, j-1, val) 
 
    # l'élément à droite fait partie de la composante 
    if ((j+1) < len(M) and M[i][j+1] == 1): 
        propager(M, i, j+1, val) 

M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]] 
propager(M,2,1,3) 
print(M)