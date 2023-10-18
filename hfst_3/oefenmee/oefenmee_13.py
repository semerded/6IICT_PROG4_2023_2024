"""
Herneem oefen mee 8 en oefen mee 11.
Zorg ervoor dat de apps ook werken zonder button.
Update hiervoor de app manueel via de methode .update().
"""
COLOR = ["red", "green", "blue", "orange", "purple", "gray", "grey", "black", "pink"]

import tkinter as tk

APP = tk.Tk()

colorLabel = tk.Label(APP, text="textkleur: ")
colorInput = tk.Entry(APP)
input1 = tk.Entry(APP)
input2 = tk.Entry(APP)
antwoord = tk.Label(APP, text="")

colorLabel.grid(row=0, column=0)
colorInput.grid(row=0, column=1)
input1.grid(row=1, column=0)
input2.grid(row=1, column=1)
antwoord.grid(row=2, column=0, columnspan=2)




while True:
    if colorInput.get().lower() in COLOR:
        color = colorInput.get()
    else:
        color = "black"
    
    try:
        _input1 = int(input1.get())
        _input2 = int(input2.get())
    except ValueError:
        antwoord.config(text="geef een getal in graag", fg=color)
    else:
        uitkomst = _input1 + _input2
        antwoord.config(text=uitkomst, fg=color)
    colorLabel.config(fg=color)
    
    APP.update()