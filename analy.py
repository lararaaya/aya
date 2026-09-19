import numpy as np

fichier = open("Loan_prediction_dataset.csv", "r")

data = np.genfromtxt(fichier, delimiter=",")

fichier.close()

print(data)
print(data.dtype.names)


montants = data[8]

moyenne = np.nanmean(montants)
mediane = np.nanmedian(montants)
ecart_type = np.nanstd(montants)

print("Moyenne :", moyenne)
print("Médiane :", mediane)
print("Écart type :", ecart_type)
