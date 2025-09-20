# LOGISCHE OPERATOREN
# Diese Operatoren werden verwendet, um boolesche Werte zu kombinieren.

# Operatorrangfolge (von höher zu niedriger):
# 1. NOT (not)
# 2. AND (and) 
# 3. OR (or)
# Hinweis: XOR (^) hat eine andere Rangfolge und gehört zu den Bitwise-Operatoren

print(not(2 < 3))             # NOT: False, weil die Bedingung wahr ist (not kehrt das Ergebnis um)
print(not(2 > 3))             # NOT: True, weil die Bedingung falsch ist (not kehrt das Ergebnis um)

print(2 < 3 and 3 < 5)        # AND: True, weil beide Bedingungen wahr sind (beide müssen wahr sein, damit das Ergebnis wahr ist)
print(2 < 3 and 6 < 5)        # AND: False, weil die zweite Bedingung falsch ist (beide müssen wahr sein, damit das Ergebnis wahr ist)

print(2 < 3 or 3 < 5)         # OR: True, weil beide Bedingungen wahr sind (bei OR muss nur eine Bedingung wahr sein, damit das Ergebnis wahr ist)
print(4 < 3 or 6 < 5)         # OR: False, weil beide Bedingungen falsch sind (bei OR muss nur eine Bedingung wahr sein, damit das Ergebnis wahr ist)

print((2 < 3) ^ (3 < 5))      # XOR: False, weil beide Bedingungen wahr sind (bei XOR muss genau eine Bedingung wahr sein, damit das Ergebnis wahr ist)
print((2 < 3) ^ (3 > 5))      # XOR: True, weil nur eine Bedingung wahr ist (bei XOR muss genau eine Bedingung wahr sein, damit das Ergebnis wahr ist)