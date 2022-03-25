def RechercheMin(tab):
    mini = tab[0]
    for i in range(1,len(tab)):
        if mini > tab[i]:
            mini = tab[i]
    for j in range(len(tab)):
        if mini == tab[j]:
            return j
    
assert RechercheMin([5]) == 0

assert RechercheMin([5, 3, 2, 2, 4]) == 2

assert RechercheMin([5, 3, 2, 2, 4]) == 2

def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i + 1
        else :
            tab[i], tab[j] = tab[j],tab[i]
            j = j - 1
    return tab

assert (separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]