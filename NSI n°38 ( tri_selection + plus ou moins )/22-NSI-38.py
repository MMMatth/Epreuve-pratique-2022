def tri_selection(tab):
    n = len(tab) - 1
    for i in range(0,n):
        mini = i
        for j in range(i,n+1):
            if tab[j] < tab[mini]:
                mini = j
        if mini != i:
            save = tab[i]
            tab[i] = tab[mini]
            tab[mini] = save
    return tab


from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre etait ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre etait ",nb_mystere)

plus_ou_moins()
