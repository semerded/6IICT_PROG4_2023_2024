# Bepaal de faculteit van een getal met behulp van een while-loop.
def facul(n):
    fac = 1
    for i in range(n):
        fac *= i + 1
    return fac
        


print( facul(1) ) # 1
print( facul(2) ) # 2
print( facul(3) ) # 6
print( facul(4) ) # 24
print( facul(5) ) # 120