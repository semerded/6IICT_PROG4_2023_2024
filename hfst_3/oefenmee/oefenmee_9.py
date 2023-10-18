"""
Volg de instructies van oefen mee 9.
Je zal een app maken om letters toe te voegen aan een entry op een specifieke positie?
De app bestaat uit 3 entries & 1 button.

"""
import tkinter as tk

APP = tk.Tk()

def bereken():
    inputVeld2.insert(int(inputVeld0.get()), inputVeld1.get())

inputVeld0 = tk.Entry(APP)
inputVeld1 = tk.Entry(APP)
inputVeld2 = tk.Entry(APP)
button = tk.Button(APP, text="bereken", command=bereken)

inputVeld0.grid(row=0, column=0)
inputVeld1.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)
inputVeld2.grid(row=2, column=0, columnspan=2)


APP.mainloop()

