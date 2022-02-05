def correspond(mot,mot_a_trous):
    Find = True
    for i in range(len(mot)):
        if mot[i] == mot_a_trous[i]:
            Find = True
        elif mot_a_trous[i] == "*":
             Find = True
        else:
            return False
    return Find




def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'
    N = len(plan)-1                          
    for i in range(N):
        if plan[personne] == "A":
            return False
        else:
            personne = plan[personne]
    return True

assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}) == False 
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}) == True 
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}) == True 
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}) == False 
 