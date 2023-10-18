"""
Volg de instructies van oefen mee 11.
Je zal een app maken om de kleur van een label aan te passen.
De app bestaat uit 1 entry, 1 label & 1 button.

    Tip! Je zal de methode .config() moeten gebruiken.
         Hiermee kan je de onderdelen (kleur, tekst, ...) van een widget wijzigen.

"""
COLOR = ["red", "green", "blue", "orange", "yellow", "purple", "gray", "grey", "black", "pink"]

import tkinter as tk

APP = tk.Tk()

def updateText():
    color = entry.get().lower() if entry.get().lower() in COLOR else "black"
    label.config(text="het label is %s" % entry.get(), fg=color)

entry = tk.Entry(APP)
button = tk.Button(APP, text="send", command=updateText)
label = tk.Label(APP, text="typ iets")

entry.grid(row=0, column=0, columnspan=2)
button.grid(row=0, column=2)
label.grid(row=1, column=0, columnspan=3)

APP.mainloop()