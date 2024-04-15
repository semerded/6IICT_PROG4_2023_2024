# Los de vragen uit oefen mee 2 op.

def optellen(eindGetal, getal = 1):
    if getal == eindGetal:
        print(getal)
        return
    optellen(eindGetal, getal + 1)
    print(getal)

optellen(3)