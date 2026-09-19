import tkinter as tk


def fahrenheit_to_celsius():
    """Convertit une température de Fahrenheit en Celsius."""
    fahrenheit = float(ent_temperature.get())
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    lbl_result.config(text=f"{celsius}\N{DEGREE CELSIUS}")


# Créer la fenêtre
window = tk.Tk()
window.title("Convertisseur de Température")
window.resizable(width=False, height=False)

# Créer le cadre
frm_entry = tk.Frame(master=window)

# Entrée pour la température Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Label Fahrenheit
lbl_temp = tk.Label(
    master=frm_entry,
    text="\N{DEGREE FAHRENHEIT}"
)

# Disposer les widgets dans le cadre
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Bouton de conversion
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)

# Label pour afficher le résultat
lbl_result = tk.Label(
    master=window,
    text="\N{DEGREE CELSIUS}"
)

# Disposer les widgets
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Lancer l'application
window.mainloop()
