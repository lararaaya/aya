import pandas as pd

# Création du DataFrame
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Sexe': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Femme'],
    'Salaire': [50000, 60000, 45000, 55000, 70000, 55000],
    'Expérience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

# 1. iloc : sélectionner les 3 premières lignes
first_three_rows = employee_df.iloc[0:3]
print("1. Les 3 premières lignes :")
print(first_three_rows)

# 2. loc : sélectionner toutes les lignes où le département est "Marketing"
marketing_dept = employee_df.loc[employee_df['Department'] == 'Marketing']
print("\n2. Département Marketing :")
print(marketing_dept)

# 3. iloc : sélectionner les colonnes Age et Sexe pour les 4 premières lignes
age_sexe_subset = employee_df.iloc[0:4, [2, 3]]
print("\n3. Colonnes Age et Sexe (4 premières lignes) :")
print(age_sexe_subset)

# 4. loc : sélectionner Salaire et Expérience pour les lignes où Sexe = "Homme"
male_salary_exp = employee_df.loc[employee_df['Sexe'] == 'Homme', ['Salaire', 'Expérience']]
print("\n4. Salaire et Expérience (Hommes) :")
print(male_salary_exp)