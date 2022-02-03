#Exo 1

def recherche(caractere,mot):
    tmp = 0
    for i in range(len(mot)):
        if caractere == mot[i]:
            tmp += 1
    return tmp


#Exo 2
def rendu_glouton(arendre, solution=[], i=0):
    Pieces = [100,50,20,10,5,2,1]
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)
