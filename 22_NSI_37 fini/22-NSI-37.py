def verifie(tab):
    res = False
    
    if len(tab) == 1:
        return True
    
    for i in range(len(tab)-1):
        if tab[i] < tab[i+1]:
            res = True
        else :
            res = False
    return res

assert verifie([0, 5, 8, 8, 9]) == True 
assert verifie([8, 12, 4]) == False 
assert verifie([-1, 4]) == True 
assert verifie([5]) == True


urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {"A":0,"B":0,"C":0}
    for bulletin in urne:
        if bulletin == 'A' or bulletin == "B" or bulletin == "C":
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            return False
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == election[vainqueur]]
    return liste_finale


