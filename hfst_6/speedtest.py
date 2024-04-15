from time import perf_counter

def facul(n):
    if n == 1:
        return 1
    
    vorige_faculteit = facul( n-1 )
    return n * vorige_faculteit

def forfacul(n):
    fac = 1
    for i in range(n):
        fac *= i + 1
    return fac

def whilefacul(n):
    fac = 1
    while n > 0:
        fac *= n
        n -= 1

starttime = perf_counter()

for i in range(100000):
    test = (facul(900)) 



stoptime = perf_counter()

forstarttime = perf_counter()

for i in range(100000):
    test = (forfacul(900))


forstoptime = perf_counter()

whilestarttime = perf_counter()

for i in range(100000):
    test = (whilefacul(900))
    
whilestoptime = perf_counter()


print(f"recursion:  {stoptime - starttime}")
print(f"for loop:   {forstoptime - forstarttime}")
print(f"while loop: {whilestoptime - whilestarttime}")