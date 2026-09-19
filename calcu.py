import math
class Calculatrice:
    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }
    def add_operation(self, symbole, fonction):
        self.operations[symbole] = fonction

    def calculate(self, nombre1, symbole, nombre2):
        try:
            # Vérification des nombres
            if not isinstance(nombre1, (int, float)) or \
               not isinstance(nombre2, (int, float)):
                raise TypeError("Les valeurs doivent être des nombres.")  
            
            # Vérification de l'opération
            if symbole not in self.operations:
                raise ValueError("Opération invalide.")

            # Division par zéro
            if symbole == "/" and nombre2 == 0:
                raise ZeroDivisionError("Division par zéro impossible.")

            fonction = self.operations[symbole]
            return fonction(nombre1, nombre2)

        except (TypeError, ValueError, ZeroDivisionError) as e:
            print("Erreur :", e)
            raise


# Fonctions des opérations avancées
def puissance(a, b):
    return a ** b


def racine(a, b):
    if a < 0:
        raise ValueError("La racine carrée d'un nombre négatif est impossible.")
    return math.sqrt(a)


def logarithme(a, b):
    if a <= 0:
        raise ValueError("Le logarithme nécessite un nombre positif.")
    return math.log(a)


# Programme principal
calculatrice = Calculatrice()

# Ajout des opérations avancées
calculatrice.add_operation("**", puissance)
calculatrice.add_operation("sqrt", racine)
calculatrice.add_operation("log", logarithme)

while True:
    print("\n--- CALCULATRICE ---")
    print("Opérations disponibles :", ", ".join(calculatrice.operations))
    print("Tapez 'q' pour quitter.")

    operation = input("Entrez l'opération : ")

    if operation.lower() == "q":
        print("Au revoir !")
        break

    try:
        nombre1 = float(input("Entrez le premier nombre : "))

        # sqrt et log n'utilisent qu'un seul nombre
        if operation in ["sqrt", "log"]:
            nombre2 = 0
        else:
            nombre2 = float(input("Entrez le deuxième nombre : "))

        resultat = calculatrice.calculate(
            nombre1, operation, nombre2
        )

        print("Résultat :", resultat)

    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")
    except Exception as e:
        print("Erreur :", e)
