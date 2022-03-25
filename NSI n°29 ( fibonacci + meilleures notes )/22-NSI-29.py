def fibonacci(n):
    u1 = 1
    u2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n-2):
            total = u1 + u2
            u2 = u1
            u1 = total
        return total
         
assert fibonacci(1) == 1
assert fibonacci(25) == 75025
assert fibonacci(45) == 1134903170


liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi =  []
    
    for compteur in range(len(liste_notes)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]
            
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)

assert meilleures_notes() == (80, 3, ['c', 'f', 'h'])