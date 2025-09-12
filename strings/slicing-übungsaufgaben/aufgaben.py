# Übungsaufgaben:

# 1. Was wird von dem folgenden Programm ausgegeben?
a = "Buchhaltung"
b = "Python ist toll!"

print(a[5])         # Ausgabe: h
print(b[-1])        # Ausgabe: !
print(a[:4])        # Ausgabe: Buch
print(b[11:16])     # Ausgabe: toll!
print(a[-100:100])  # Ausgabe: Buchhaltung
print(a[-5])        # Ausgabe: l
print(a[-12])       # Ausgabe: string is out of range
print(a[4:8])       # Ausgabe: halt

# 2. Schneide mithilfe von Slicing aus dem String
wort = "Maximilian"
# die folgenden Substrings aus:
# 1 Max
print(wort[:3])
print(wort[-10:-7])

# 2 Maxi
print(wort[:4])
print(wort[-10:-6])

# 3 im
print(wort[3:5])
print(wort[-7:-5])

# 4 mili
print(wort[4:8])
print(wort[-6:-2])

# 5 ian
print(wort[7:])
print(wort[-3:])