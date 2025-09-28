# TUPEL
# Ein Tupel ist eine unveränderliche (immutable) Datenstruktur, die eine geordnete Sammlung von Elementen speichert. So ähnlich wie Listen, aber im Gegensatz zu Listen können Tupel nach ihrer Erstellung nicht mehr verändert werden (keine Elemente hinzufügen, entfernen oder ändern).

print(())                 # leeres Tupel
print(len(()))            # leere Tupel hat Länge 0
print(len((1, 2, 3)))     # Tupel mit 3 Elementen hat Länge 3

test = (42, 1, 11, 7, 99)
print(test[2])              # Ausgabe: 11
print(test[-2])             # Ausgabe: 7

print((42, 1, 11, 7, 99)[-3])   # Ausgabe: 11

def addieren(a, b):
  summe = a + b
  return a, b, summe         # Immer wenn mehrere Werte zurückgegeben werden sollen, wird ein Tupel verwendet

ergebnis = addieren(1, 4)
print(ergebnis)              # Ausgabe: (1, 4, 5)
print(type(ergebnis))        # Ausgabe: <class 'tuple'>

def addieren2(*summanden):   # * bedeutet: beliebig viele Argumente
  print(type(summanden))     # Ausgabe: <class 'tuple'>

addieren2()                  # Ausgabe: <class 'tuple'>