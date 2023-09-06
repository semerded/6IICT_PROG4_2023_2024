# Gebruik onderstaande code om deze opdracht op te lossen.

# Pad naar het bestand (Plak in variabele het relatieve pad)
pad = "VUL AAN"

# Open het tekstbestand met lied & zet inhoud van lied in string.
with open(pad, "r") as fp:
    lied = fp.read()

# Haal witregels weg uit string & zet string om naar lijst.
lied = lied.replace("\n","")
lied = lied.split()

# Print lied (om te testen dat het werkt)
print(lied)


