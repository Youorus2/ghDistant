# hello_world.py

import tkinter as tk
from constantes import HELLO_WORLD_TITLE, HELLO_WORLD_TEXT

def fonction_principale():
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title(HELLO_WORLD_TITLE)
    fenetre.geometry("400x400")
    fenetre.configure(bg="cyan")  # Fond d’écran vert

    
    # Création du label de texte
    label = tk.Label(fenetre, text=HELLO_WORLD_TITLE, fg="green", bg="black")
    label.pack(expand=True)  # Centrage vertical et horizontal
    
    # Finalisation
    fenetre.mainloop()

# Appel de la fonction principale
if __name__ == "__main__":
    fonction_principale()
