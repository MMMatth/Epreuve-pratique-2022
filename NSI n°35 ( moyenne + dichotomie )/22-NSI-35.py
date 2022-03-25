def moyenne (tab): 
    ''' 
        moyenne(list) -> float 
        Entrée : un tableau non vide d'entiers 
        Sortie : nombre de type float  
        Correspondant à la moyenne des valeurs présentes dans le 
        tableau 
    '''       
    a = 0
    b = 0
    for i in range(len(tab)):
        a += tab[i]
        b += 1
    return a/b

assert moyenne([1]) == 1 
assert moyenne([1,2,3,4,5,6,7]) == 4 
assert moyenne([1,2]) == 1.5



def dichotomie(tab, x):
    """
        tab : tableau trie dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab) == 0:
        return False,1

    # cas ou x n'est pas compris entre les valeurs extremes
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False,2
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = fin - 1			
    return False, 3

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True 
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == (False, 3) 
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1) == (False, 2) 
assert dichotomie([],28) == (False, 1) 
