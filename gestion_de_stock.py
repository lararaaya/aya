import pandas as pd
import tkinter as tk 
from tkinter import messagebox
import csv
import numpy as np

#1
class produit:
    def __init__(self, id_produit, nom, categorie, quantite, seuil, prix):
        self.id_produit = id_produit
        self.nom = nom
        self.categorie = categorie
        self.quantite = quantite
        self.seuil = seuil
        self.prix = prix  
#2
liste_produits = []
prochaine_id = 1
#3
def ajouter_produit(nom, categorie, quantite, seuil, prix):
    global prochaine_id
    p = produit(prochaine_id, nom, categorie, quantite, seuil, prix)
    liste_produits.append(p)
    prochaine_id += 1
    return p
def trouver_produit(id_produit):
    for p in liste_produits:
        if p.id_produit == id_produit:
            return p
    return None # si on ne trouve rien    
def entree_stock(id_produit, quantite):
    p = trouver_produit(id_produit)
    if p is None:
        raise Exception("Produit introuvable")
    p.quantite += quantite
def sortie_stock(id_produit, quantite):
    p = trouver_produit(id_produit)
    if p is None:
        raise Exception("produit introuvable")
    if quantite > p.quantite:
        raise Exception("stock insuffisant")
    p.quantite -= quantite
    if p.quantite <= p.seuil:
        print(f"ALERTE : le stock de '{p.nom}' est bas (reste {p.quantite})")
        # if NOTIF_DISPONIBLE:
        #     notification.notify(
        #         title="stock bas",
        #         message=f"'{p.nom}' : reste seulment {p.quantite}",
        #         timeout=60,   #la notification reste 60 secandes
        #     )
#4
def recharcher_par_nom(nom):
    resultats = [] 
    for p in liste_produits:
        if nom.lower() in p.nom.lower():
            resultats.append(p)
    return resultats
def trier_par_quantite():
    liste = liste_produits.copy()
    n = len(liste)  
    for i in range(n):
        for j in range(n - 1 - i):
            if liste[j].quantite > liste[j + 1].quantite:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste                           
#5
def sauvegarder_scv(nom_fichier):
    with open(nom_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nom", "categorie", "quantite", "seuil", "prix"])
        for p in liste_produits:
            writer.writerow([p.id_produit, p.nom, p.categorie, p.quantite, p.seuil, p.prix])
def lire_csv(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8")as f:
            reader = csv.reader(f) 
            next(reader)
            for ligne in reader:
                ajouter_produit(ligne[1], ligne[2], int(ligne[3]), int(ligne[4]), float(ligne[5]))
    except FileNotFoundError:
        print("le fichier n'existe pas encore.")
#6
def afficher_statistique():
    donnees = []
    for p in liste_produits:
        donnees.append([p.id_produit, p.nom, p.categorie, p.quantite, p.seuil, p.prix])
        df = pd.DataFrame(donnees, columns=["id", "nom", "categorie", "quantite", "seuil", "prix"])
        df["valeur"] = df["quantite"] * df["prix"]
        print(df)
        print("Quantite total :", np.sum(df["quantite"]))
        print("Quantite moyenne :", np.mean(df["quantite"]))
        print("Valeur total du stock :", np.sum(df["valeur"])) 
#7
def rafraichir(liste_affichage, window):
    liste_affichage.delete(0, tk.END)
    for p in liste_produits:
        liste_affichage.insert(
            tk.END,
            f"{p.id_produit} - {p.nom} - {p.categorie} - Qte: {p.quantite}"
        )


def sortie_depuis_interface(champ_id, champ_quantite, liste_affichage, window):
    try:
        id_produit = int(champ_id.get())
        quantite = int(champ_quantite.get())

        sortie_stock(id_produit, quantite)
        rafraichir(liste_affichage, window)

        messagebox.showinfo("Succes", "Sortie de stock effectuee !")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def lancer_interface():
    window = tk.Tk()
    window.title("Gestion de stock")
    window.geometry("700x500")
    window.configure(bg="#F8EAEA")

    # TITRE
    tk.Label(
        window,
        text="GESTION DE STOCK",
        font=("Arial", 18, "bold"),
        bg="#EAF2F8",
        fg="#1F4E79"
    ).pack(pady=10)

    # LISTE
    cadre_liste = tk.LabelFrame(
        window,
        text="Liste des produits",
        font=("Arial", 11, "bold"),
        bg="white",
        padx=10,
        pady=10
    )
    cadre_liste.pack(fill="both", expand=True, padx=20, pady=5)

    liste_affichage = tk.Listbox(
        cadre_liste,
        width=70,
        height=8,
        font=("Arial", 10)
    )
    liste_affichage.pack()

    # SORTIE DE STOCK
    cadre_sortie = tk.LabelFrame(
        window,
        text="Sortie de stock",
        font=("Arial", 11, "bold"),
        bg="white",
        padx=10,
        pady=8
    )
    cadre_sortie.pack(padx=20, pady=5)

    champ_id = tk.Entry(cadre_sortie, width=8, fg="black")
    champ_id.pack(side="left", padx=5)
    champ_quantite = tk.Entry(cadre_sortie, width=8)
    champ_quantite.pack(side="left", padx=5)

    tk.Button(
        cadre_sortie,
        text="Sortie stock",
        command=lambda: sortie_depuis_interface(champ_id, champ_quantite, liste_affichage, window),
        bg="#E74C3C",
        fg="white"
    ).pack(padx=10)

    # BOUTONS (maintenant bien à l'intérieur de lancer_interface)
    cadre_boutons = tk.Frame(window, bg="#EAF2F8")
    cadre_boutons.pack(pady=8)

    tk.Button(
        cadre_boutons,
        text="Rafraichir",
        command=lambda: rafraichir(liste_affichage, window),
        bg="#17A589",
        fg="white",
        width=18
    ).pack(padx=5)

    rafraichir(liste_affichage, window)  # affiche la liste dès l'ouverture
    window.mainloop()
#8
if __name__ == "__main__":
    ajouter_produit("Produit A", "Categorie 1", 20, 5, 800)
    ajouter_produit("Produit B", "Categorie 2", 10, 3, 350)
    ajouter_produit("Produit C", "Categorie 1", 2, 5, 120)
    ajouter_produit("Produit test", "Test", 50, 5, 200)
    try:
        sortie_stock(1, 15)
    except Exception as e:
        print("Erreur :", e)
    print("--- Produits triés par quantité ---")
    for p in trier_par_quantite():
        print(p.nom, "-", p.quantite)
    print("--- Recherche 'produit b' ---")
    for p in recharcher_par_nom("produit b"):
        print(p.nom)
    sauvegarder_scv("stock.csv")
    print("--- Statistiques ---")
    afficher_statistique()
 
    lancer_interface()
