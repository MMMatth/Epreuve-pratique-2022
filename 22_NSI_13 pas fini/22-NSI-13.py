def rendu(somme_a_rendre):
    L = [5,2,1]
    L2 = [0,0,0]
    for i in range (len(L)):
        if somme_a_rendre // L[i] != 0:
            L2[i] = somme_a_rendre // L[i]
            somme_a_rendre = somme_a_rendre % L[i] 
    return L2

assert rendu(13) == [2,1,1] 
assert rendu(64) == [12,2,0] 
assert rendu(89) == [17,2,0]






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
        while maillon != None : 
            print(maillon.valeur) 
            maillon = maillon.suivant
 
    def defile(self) : 
        if not self.est_vide() : 
            if self.dernier_file.suivant == None : 
                resultat = self.dernier_file.valeur 
                self.dernier_file = None 
                return resultat 
            maillon = self.dernier_file.suivant
            while maillon.suivant.suivant != None : 
                maillon = maillon.suivant 
            resultat = maillon.valeur  
            maillon.suivant = None 
            return resultat 
        return None
    

F = File() 
assert F.est_vide() == True 
F.enfile(2) 
F.enfile(5) 
F.enfile(7)
F.enfile(2) 
F.enfile(7)  

print(F.defile(),F.defile())

