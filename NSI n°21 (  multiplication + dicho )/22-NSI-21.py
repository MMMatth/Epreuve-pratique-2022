def multiplication(n1,n2):
    if n1 == 0 or n2 == 0:
        return 0
    c1,c2 =n1,n2
    if n1 < 0:
        n1 = n1 * -1
    if n1 < 0:
        n2 = n2 * -1
    res = 0
    for i in range(n2):
        res += n1
    if c1 > 0 and c2 > 0 or c1 < 0 and c2 < 0:
        return res
    else:
        return -res

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin+debut) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1			
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True