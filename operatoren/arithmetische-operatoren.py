# ARITHMETISCHE OPERATOREN (PUNKTRECHNUNG VOR STRICHRECHNUNG)
# +, -, *, /, //

print(30 + 15)      # Ausgabe: 45
print(30 - 15)      # Ausgabe: 15
print(30 * 15)      # Ausgabe: 450
print(30 / 15)      # Ausgabe: 2.0    # Division ergibt immer eine Gleitkommazahl (float)

print(30 // 15)     # Ausgabe: 2      # Ganzzahlige Division (Ergebnis wird abgerundet, float wird zu int)
print(7 // 2)       # Ausgabe: 3      # Ganzzahlige Division (Ergebnis wird abgerundet, float wird zu int)

print(30 % 15)      # Ausgabe: 0      # Modulo (Rest der Division)
print(7 % 2)        # Ausgabe: 1      # Modulo (Rest der Division)
print(8 % 3)        # Ausgabe: 2      # Modulo (Rest der Division)

print(2 ** 3)       # Ausgabe: 8      # Exponentiation (2 hoch 3)
print(9 ** 0.5)     # Ausgabe: 3.0    # Exponentiation (Quadratwurzel von 9)

print(2 + 3 * 4)    # Ausgabe: 14     # Multiplikation hat höhere Priorität als Addition
print((2 + 3) * 4)  # Ausgabe: 20     # Klammern ändern die Priorität
print(10 / 2 + 5)   # Ausgabe: 10.0   # Division hat höhere Priorität als Addition (10 : 2 + 5)

# BEISPIELE:
print(5**3 + 2)         # Ausgabe: 127
print (4 + 3 - 5)       # Ausgabe: 2
print(6 + 8 / 2)        # Ausgabe: 10.0
print(10 * 2**3)        # Ausgabe: 80
print(5 * 9 *2 / 10)    # Ausgabe: 9.0
print(5 % 3 * 7)        # Ausgabe: 14
print(6 % 5 + 3)        # Ausgabe: 4
print(10 % 2**2)        # Ausgabe: 2