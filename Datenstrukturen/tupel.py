# TUPEL
# Ein Tupel ist eine unveränderliche (immutable) Datenstruktur, die eine geordnete Sammlung von Elementen speichert. So ähnlich wie Listen, aber im Gegensatz zu Listen können Tupel nach ihrer Erstellung nicht mehr verändert werden (keine Elemente hinzufügen, entfernen oder ändern).

# GRUNDLAGEN

print(())                 # leeres Tupel
print(len(()))            # leere Tupel hat Länge 0
print(len((1, 2, 3)))     # Tupel mit 3 Elementen hat Länge 3

# ZUGRIFF AUF ELEMENTE

test = (42, 1, 11, 7, 99)
print(test[2])              # Ausgabe: 11
print(test[-2])             # Ausgabe: 7
print((42, 1, 11, 7, 99)[-3])   # Ausgabe: 11

# RETURN VON MEHREREN WERTEN (BEISPIEL AN EINER FUNKTION)

def addieren(a, b):
  summe = a + b
  return a, b, summe         # Immer wenn mehrere Werte zurückgegeben werden sollen, wird ein Tupel verwendet
ergebnis = addieren(1, 4)
print(ergebnis)              # Ausgabe: (1, 4, 5)
print(type(ergebnis))        # Ausgabe: <class 'tuple'>

def addieren2(*summanden):   # * bedeutet: beliebig viele Argumente
  print(type(summanden))     # Ausgabe: <class 'tuple'>
addieren2()                  # Ausgabe: <class 'tuple'>

# KONKATENATION VON TUPELN

print((1, 2, 3) + (4, 5))    # Konkatenation von Tupeln mit dem + Operator

# COUNT() - ELEMENTE ZÄHLEN

tupel1 = (1, 2, 3, 7, 5, 9, 6, 4, 8)
count1 = tupel1.count(5)                   # Zählt, wie oft ein Element in einem Tupel vorkommt
count2 = tupel1.count(-5)                  # Gibt den Index des ersten Vorkommens eines Elements zurück
print(count1)                              # Ausgabe: 1 (da 5 einmal im Tupel ist)
print(count2)                              # Ausgabe: 0 (da -5 nicht im Tupel ist)

# INDEX() - INDEX EINES ELEMENTS FINDEN

tupel2 = (1, 2, 3, 7, 5, 9, 6, 4, 8)
index = tupel2.index(5)               # Gibt den Index des ersten Vorkommens eines Elements zurück
print(index)                          # Ausgabe: 4 (da 5 an Index 4 ist)

# COPY() - TUPEL KOPIEREN

tupel3 = (1, 2, 3)                    
kopie = tupel3.copy()                 # Funktioniert nicht, da Tupel keine copy() Methode haben 

# SORT() - LISTEN SORTIEREN

tupel4 = (1, 5, 4, 2, 3)
liste = list(tupel4)         # Wandelt das Tupel in eine Liste um
liste.sort()                 # Sortiert die Liste
print(liste)                 # Ausgabe: [1, 2, 3]