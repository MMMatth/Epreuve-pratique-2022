


a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre, racine):
    if racine == '':
        return 0
    elif arbre[racine][0] != '' or arbre[racine][1] != '':
        return 1 + taille(arbre, arbre[racine][0]) + taille(arbre, arbre[racine][1])
    elif arbre[racine][0] == '' and arbre[racine][1] == '':
        return 1 

assert taille(a, 'F')== 9

def tri_iteratif(tab):
    for k in range(len(tab)-1 , 0, -1):
        imax = k
        for i in range(0 , k):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab

assert tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]