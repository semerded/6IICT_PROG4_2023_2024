# Draai een woord om.

def draaiom(input: str):
    if len(input) == 1:
        return input
    return input[-1] +  draaiom(input[:-1])
    

print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI
