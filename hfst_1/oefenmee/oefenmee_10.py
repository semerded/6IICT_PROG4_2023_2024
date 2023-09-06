# Vul eerst aan. Daarna pas uitvoeren!
dictionary = {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

""" Geef aan wat volgende code print"""
" Vul aan: "
print(dictionary)

" Vul aan: "
for x in dictionary:
    print(x)

" Vul aan: "
print( list(dictionary.keys()))

" Vul aan: "
print( dictionary.get("e", 4))

" Vul aan: "
print( list(dictionary.values()))

" Vul aan: "
print( dictionary.get("q", 4))

" Vul aan: "
for x, y in dictionary.items():
    print(y, x)

" Vul aan: "
for x in dictionary.values():
    print(x)

" Vul aan: "
print( dictionary.pop("c"))

"Vul aan: "
print( list(dictionary.items()) )
