def nb_repetitions(elt,tab):
    tmp = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            tmp += 1
    return tmp


def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a