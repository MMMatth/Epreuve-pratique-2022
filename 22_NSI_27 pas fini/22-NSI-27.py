


a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre, racine):
    if racine == '':
        return 0
    elif arbre[racine][0] != '' or arbre[racine][1] != '':
        return 1 + taille(arbre, arbre[racine][0]) + taille(arbre, arbre[racine][1])
    elif arbre[racine][0] == '' and arbre[racine][1] == '':
        return 1 

print(taille(a, 'F'))

def tri_iteratif(tab):
    for k in range(len(tab)-1 , 0, -1):
        imax = k
        for i in range(0 , len(tab) ):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > i :
            tab[i] , tab[imax] = tab[imax] , tab[i]
    return tab

# print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))