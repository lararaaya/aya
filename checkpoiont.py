# Question 1
liste = [2, 3, 6]
resultat = 1
for nombre in liste:
    resultat *= nombre
print(resultat)  
# Question 2
liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
liste.sort(key=lambda x: x[-1])
print(liste)
# Question 3
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
resultat = d1.copy()
for cle, valeur in d2.items():
    if cle in resultat:
        resultat[cle] += valeur
    else:
        resultat[cle] = valeur
print(resultat)
# Question 4
n = int(input("entrer un nombre"))
d = {}
for i in range(1, n+1):
    d[i] = i*i
print(d)
# Question 5
liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
liste.sort(key=lambda x: float(x[1]), reverse=True)
print(liste)
#Question 6
# Créer un ensemble
ensemble = {0, 1, 2, 3, 4}
print(ensemble)
# Itérer
for element in ensemble:
    print(element)
# Ajouter / retirer
ensemble.add(5)
ensemble.remove(0)
print(ensemble)