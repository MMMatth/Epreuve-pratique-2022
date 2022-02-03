def rendu(somme_a_rendre):
    L = [5,2,1]
    L2 = [0,0,0]
    for i in range (len(L)):
        if somme_a_rendre // L[i] != 0:
            L2[i] = somme_a_rendre // L[i]
            somme_a_rendre = somme_a_rendre % L[i] 
    return L2
# print(rendu(89))







class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element) 
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != self.est_vide() :
            print(maillon.valeur)
            maillon = Maillon(self.defile()).valeur

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon
            maillon.suivant = None
            return resultat
        return None 
F = File() 
F.enfile(2) 
F.enfile(5)
F.enfile(7)
F.defile()
print(F.affiche())

# >>> F.defile() 
# 2 
# >>> F.defile() 
# 5 
# >>> F.affiche() 
# 7 