from re import S


def delta(tab):
    L = [tab[0]]
    for i in range(len(tab)-1):
        L.append(tab[i+1]-tab[i])
    return L



class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ""
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    if e.est_une_feuille():
        return s
    return '('+ s +')'


e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), 
'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', 
Noeud(None, 1, None)))

print(expression_infixe(e))