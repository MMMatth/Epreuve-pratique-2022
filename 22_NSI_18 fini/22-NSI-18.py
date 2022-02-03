from pickle import FALSE


def mini(releve,date):
    mini = 20
    indice = 0
    for i in range(len(releve)):
        if releve[i] < mini:
            mini  = releve[i]
    for i in range(len(releve)):
        if mini == releve[i]:
            return mini,date[i]
        
        



def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return True if inverse == chaine else False
    
def est_nbre_palindrome(nbre):
    chaine = inverse_chaine(str(nbre))
    return True if str(nbre) == chaine else False