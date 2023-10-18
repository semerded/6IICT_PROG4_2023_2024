"""
Volg de instructies van oefen mee 10.
Je zal een app maken waarmee je de eerste/laatste letter uit een entry kan verwijderen.
De app bestaat uit 1 entry & 2 buttons.

"""
import tkinter as tk

APP = tk.Tk()

class delete:
    def delete(inhoud):
        inputveld.delete(0, tk.END)
        inputveld.insert(0, inhoud)
        
    def first():
        inhoud = inputveld.get()
        inhoud = inhoud[1:]
        delete.delete(inhoud)
    
    def last():
        inhoud = inputveld.get()
        inhoud = inhoud[:-1]
        delete.delete(inhoud)

inputveld = tk.Entry(APP)
button1 = tk.Button(APP, text="verwijder eerste!", command=delete.first)
button2 = tk.Button(APP, text="verwijder laatste!", command=delete.last)

inputveld.grid(row=0, column=0, columnspan=2)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

APP.mainloop()

