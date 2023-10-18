"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""
import tkinter as tk

APP = tk.Tk()

veld_1 = tk.Entry(APP)
veld_1.grid(row=0, column=0)

veld_2 = tk.Entry(APP)
veld_2.grid(row=0, column=1)

antwoord = tk.Label(APP, text=f"de som van de 2 getallen is ...")
antwoord.grid(row=1, column=0, columnspan=2)

def bereken():
    uitkomst = int(veld_1.get()) + int(veld_2.get())
    antwoord.config(text=f"de som van de 2 getallen is {uitkomst}")

getKnop = tk.Button(APP, text="bereken", command=bereken)
getKnop.grid(row=2, column=0, columnspan=2)



APP.mainloop()