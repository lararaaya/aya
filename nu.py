import numpy as np

# 1. Créer le tableau "grades"
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 2. Moyenne, médiane et écart type
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_grade = np.std(grades)

# 3. Maximum et minimum
max_grade = np.max(grades)
min_grade = np.min(grades)

# 4. Indice de la note la plus élevée
max_index = np.argmax(grades)

# 5. Nombre d'étudiants ayant obtenu une note supérieure à 90
count_above_90 = np.sum(grades > 90)

# 6. Pourcentage d'étudiants ayant obtenu une note supérieure à 90
percentage_above_90 = np.mean(grades > 90) * 100

# 7. Tableau des notes supérieures à 75
passing_grades = grades[grades > 75]

# 8. Affichage des résultats
print("Tableau des notes :", grades)
print("Moyenne :", mean_grade)
print("Médiane :", median_grade)
print("Écart type :", std_grade)
print("Note maximale :", max_grade)
print("Note minimale :", min_grade)
print("Indice de la note la plus élevée :", max_index)
print("Nombre d'étudiants > 90 :", count_above_90)
print("Pourcentage d'étudiants > 90 :", percentage_above_90, "%")
print("Notes supérieures à 75 :", passing_grades)