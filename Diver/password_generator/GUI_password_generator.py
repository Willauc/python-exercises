# Auteur : William Turbide Auclair
# Date : 26 juin 2025
# Description :  Générer un mot de passe aléatoire selon des critères (longueur, majuscules, chiffres, symboles).
#                modules standard (random, string), fonctions.
#                Interface utilisateur avec Tkinter ou CLI.
import tkinter as tk

import password_generator


class MyGui:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry('400x250')
        self.root.title('Password Generator')

        self.intro = tk.Label(self.root, text='Password Generator', font=('Arial', 18))
        self.intro.pack(padx=5, pady=10)

        self.placeholder = "Password"
        self.password_afficheur = tk.Entry(self.root, font=("Arial", 10), fg='grey', width=40)
        self.password_afficheur.insert(0, self.placeholder)
        self.password_afficheur.pack(padx=5, pady=10)

        self.size_val = tk.IntVar()
        self.size_check = tk.Spinbox(self.root, from_=1, to=30, width=5, textvariable=self.size_val)
        self.size_check.pack()

        self.digit_val = tk.BooleanVar()
        self.digit_check = tk.Checkbutton(self.root, text='Numero?', font=('Arial', 12), variable=self.digit_val)
        self.digit_check.pack()

        self.uppercase_val = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(self.root, text='Uppercase?', font=('Arial', 12),
                                              variable=self.uppercase_val)
        self.uppercase_check.pack()

        self.special_val = tk.BooleanVar()
        self.special_chack = tk.Checkbutton(self.root, text='Caractere special?', font=('Arial', 12),
                                            variable=self.special_val)
        self.special_chack.pack()

        self.bouton = tk.Button(self.root, text='Generate', command=self.generate)
        self.bouton.pack(padx=5, pady=10)

        self.root.mainloop()

    def generate(self):
        password = password_generator.generate_password(self.size_val.get(), self.special_val.get(),
                                                        self.digit_val.get(), self.uppercase_val.get())
        if self.password_afficheur.get() == self.placeholder:
            self.password_afficheur.delete(0, tk.END)
            self.password_afficheur.config(fg='black')
            self.password_afficheur.insert(0, password)
        else:
            self.password_afficheur.delete(0, tk.END)
            self.password_afficheur.insert(0, password)


MyGui()
