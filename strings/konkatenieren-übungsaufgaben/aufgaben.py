# Übungsaufgaben:

# Was wird von dem folgenden Programm ausgegeben? Gib, wenn es zu einem Fehler kommt, an, welcher Fehler auftritt und warum.
a = "Developer"
b = "Akademie"
c = '.'
d = "com"

print(a + b)            # DeveloperAkademie
print(a + b + c + d)    # DeveloperAkademie.com
print(a + b -b)         # TypeError (subtrahieren von Strings nicht möglich)
print(5 * c)            # .....
print(3d)               # SyntaxError (Zahl und Variable ohne Operator)
print(a + d)            # Developercom
print(a + b + d)        # DeveloperAkademiecom
print(d**2)             # TypeError (Exponentiation von Strings nicht möglich)
print(2 * (c + d))      # .com.com
print(3 * c + 2 * d)    # ...comcom