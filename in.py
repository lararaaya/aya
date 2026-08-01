def calculator(num1, num2):
    op = input("Etrez l'operateur (+, -, *, /) : ")
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "entrez : division par zero"
        return num1 / num2    
    else:
        return "operation non valide"
num1 = float(input("entrez le premier nombre :")) 
num2 = float(input("entrez le deuxieme nomnbre : ")) 
resultat = calculator(num1, num2)
print("le resultat est :", resultat)                      