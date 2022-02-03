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
    N = len(plan)                          
    for i in range(N):
        print(personne)
        if plan[personne] == personne:
            return False
        else:
            personne = plan[personne]
    return True

print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}))
