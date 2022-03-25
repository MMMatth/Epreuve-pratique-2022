def moyenne(tab):
    a=0
    b=0
    if len(tab) == 0:
        return "erreur"
    for i in range(len(tab)):
        a += tab[i]
        b += 1
    return a/b

print(moyenne([]) )

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j= j -1
    return tab