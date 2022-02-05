def occurrence_max(chaine):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
    occurrence = [0]*len(alphabet)
    for i in range(len(alphabet)):
        for j in chaine:
            if alphabet[i] == j:
                occurrence[i] += 1
    maxi = 0
    for i in range(len(occurrence)):
        if  maxi < occurrence[i]:
            maxi = occurrence[i]
    for k in range(len(occurrence)):
        if occurrence[k] == maxi:
            return alphabet[k]
        
ch="je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique"
assert occurrence_max(ch) == "e"


def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
# on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            L[i][j] = 255 - image[i][j] 
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inferieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < seuil :
                L[i][j] = 1
            else:
                L[i][j] = 0
    return L
img=[[20, 34, 254, 145, 6], [23, 124, 287, 225, 69], [197, 
174, 207, 25, 87], [255, 0, 24, 197, 189]]
assert nbLig(img) == 4 
assert nbCol(img) == 5 
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, -32, 30, 186], [58, 81, 48, 
230, 168], [0, 255, 231, 58, 66]] 
assert binaire(img,120) == [[1, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 1, 1, 0, 0]]