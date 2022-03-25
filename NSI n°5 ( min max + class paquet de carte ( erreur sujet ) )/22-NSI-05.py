def RechercheMinMax(tab):
    if len(tab) == 0:
        return {"min" : None,"max" : None}
    d = {"min" : 0,"max" : 0}
    for i in range(len(tab)):
        if d["max"] < tab[i]:
            d["max"] = tab[i]
    for i in range(len(tab)):
        if d["min"] > tab[i]:
            d["min"] = tab[i]
    return(d)










class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range (1, 4):
            for j in range(1, 14):
                self.contenu.append(Carte(i,j).getNom()+" de "+Carte(i,j).getCouleur())# on ajoute le "nombre" puis la "couleur" avec un "de" entre les deux

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        for i in range(len(self.contenu)): # on parcour la liste
            print(i+1,self.contenu[i],"\n") #probleme dans l'exo ?
            if i+1 == pos: # on presise i+1 car on commence à 0 en python
                return self.contenu[i] # on renvoie notre contenu

        
        
unPaquet = PaquetDeCarte() 
unPaquet.remplir() 
print(unPaquet.getCarteAt(20))