# SETS
# Eine Menge (Set) ist eine ungeordnete Sammlung von eindeutigen Elementen. Sets sind veränderbar, d.h. Elemente können hinzugefügt oder entfernt werden, aber die Elemente selbst müssen unveränderlich (immutable) sein, z.B. Zahlen, Strings oder Tupel. Es gibt keine Duplikate in einem Set, d.h. jedes Element kann nur einmal vorkommen.

# GRUNDLAGEN

set()                                       # Leeres Set
print({12, 28, True, 38, 29, "Robby"})      # Set mit Werten (Reihenfolge der Elemente kann variieren)
print({12, 28, True, 38, 29, "Robby"}[0])   # TypeError: 'set' object is not subscriptable (Sets sind ungeordnet, daher kein Zugriff über Index möglich)

print({1, 1, 1, 1, 1})                      # Duplikate werden entfernt, Ausgabe: {1}
print(len({1, 1, 1, 1, 1}))                 # Duplikate werden entfernt, Länge ist 1

# IN - SUCHEN VON ELEMENTEN

set1 = {1, 2, 5, 6, 9}
print(6 in set1)                            # Überprüft, ob ein Element im Set ist, Ausgabe: True
print(10 in set1)                           # Überprüft, ob ein Element im Set ist, Ausgabe: False

# ADD() - HINZUFÜGEN VON ELEMENTEN

set2 = {1, 2, 5, 6, 9}
set2.add(10)                                # Fügt ein Element zum Set hinzu
print(set2)                                 # Ausgabe: {1, 2, 5, 6, 9, 10}
set2.add(5)                                 # Fügt ein Element zum Set hinzu, das bereits existiert (keine Änderung)

# REMOVE() - ENTFERNEN VON ELEMENTEN

set3 = {1, 2, 5, 6, 9}
set3.remove(5)                              # Entfernt ein Element aus dem Set, wenn es existiert
print(set3)                                 # Ausgabe: {1, 2, 6, 9}

# CLEAR() - ALLE ELEMENTE ENTFERNEN

set4 = {1, 2, 5, 6, 9}
set4.clear()                                # Entfernt alle Elemente aus dem Set
print(set4)                                 # Ausgabe: set()

# COPY() - SET KOPIEREN

set5 = {1, 2, 3}
kopie = set5.copy()                          # Erstellt eine flache Kopie des Sets
print(kopie)                                 # Ausgabe: {1, 2, 3}

# SORT() - LISTEN SORTIEREN

set6 = {3, 1, 4, 2, 15, 13, 24, 5}
liste = list(set6)                           # Wandelt das Set in eine Liste um
liste.sort()                                 # Sortiert die Liste
print(liste)                                 # Ausgabe: [1, 2, 3, 4, 5, 13, 15, 24]