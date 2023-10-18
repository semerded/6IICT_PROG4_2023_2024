import tkinter as tk

APP = tk.Tk()

text = tk.Label(APP, text="lengte berekenaar in cm", padx=50, pady=10)
text.pack()

input = tk.Entry(APP)
input.pack()

def bereken():
    output = tk.Tk()
    outputText = tk.Label(output, text=f"u bent {input.get()}cm groot!", width=20, height=5)
    outputText.pack()

knop = tk.Button(APP, text="bereken", command=bereken)
knop.pack()

APP.mainloop()