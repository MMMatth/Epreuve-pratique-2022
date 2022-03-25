def fusion(tab1,tab2):
    n1 , n2 = len(tab1),len(tab2)
    res = [0]*(n1+n2) # on crée une liste des deux mais vide
    i1,i2,i = 0,0,0

    while i1 < n1 and i2 < n2 :
        if tab1[i1] < tab2[i2]:
            res[i] = tab1[i1]
            i1 = i1 + 1
        else:
            res[i] = tab2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        res[i] = tab1[i1]
        i1 = i1 + 1
        i += 1
    while i2 < n2:
        res[i] = tab2[i2]
        i2 = i2 + 1
        i += 1
    return res



def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(nombre) == 1:
        return dico[nombre]

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
		 ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre_droite)
        else:
            return rom_to_dec(nombre_droite) - dico[nombre[0]]

assert rom_to_dec("CXLII") == 142
