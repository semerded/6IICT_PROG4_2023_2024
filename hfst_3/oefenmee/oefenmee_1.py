""" 
Maak een app aan die 3 labels bevat.
De inhoud van de 3 labels is:
    - Label 1: hallo
    - Label 2: klas
    - Label 3: 6iict
"""
import tkinter as tk

APP = tk.Tk()

label1 = tk.Label(APP, text="hallo")
label1.pack()
label2 = tk.Label(APP, text="klass")
label2.pack()
label3 = tk.Label(APP, text="6IICT")
label3.pack()

APP.mainloop()