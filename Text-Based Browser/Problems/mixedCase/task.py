x = input()

liste = x.split(' ')
el_ind = 1
for _ in liste:
    if el_ind < len(liste):
        liste[el_ind] = liste[el_ind].capitalize()
        el_ind += 1
z = ''.join(liste)
print(z)


