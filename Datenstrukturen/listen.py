# LISTEN
# Listen sind veränderbare, geordnete Sammlungen von Elementen, die verschiedene Datentypen enthalten können.

# GRUNDLAGEN

liste = []                            # Leere Liste
listeMitWerten = [1, "Mia", True]     # Liste mit Werten

print(len(listeMitWerten))            # Länge der Liste

# ZUGRIFF AUF ELEMENTE

print(listeMitWerten[1])              # Zugriff auf Elemente der Liste (Index beginnt bei 0)
print(listeMitWerten[-1])             # Zugriff auf das letzte Element der Liste

# SLICING (TEILLISTEN)

print(listeMitWerten[0:2])            # Slicing (Teilliste von Index 0 bis 1)
print(listeMitWerten[1:2])            # Slicing von Anfang bis Index 1
print(listeMitWerten[1:10])           # Slicing von Anfang bis Index 9 (überschreitet die Listenlänge nicht)
print(listeMitWerten[15])           # IndexError: list index out of range

# + OPERATOR (KONKATENATION)

liste1 = [1, 2, 5, 6, 9]
weiterenZahlen = [0, 10 , 12, 15]
ergebnis = liste1 + weiterenZahlen  # Listen können mit dem + Operator verbunden werden (Konkatenation), geht auch mit "ergebnis = liste1 + [10, 20]"
print(ergebnis)                     # Ausgabe: [1, 2, 5, 6, 9, 0, 10, 12, 15]

# * OPERATOR (WIEDERHOLUNG)

liste2 = [0, 1]
print(liste2 * 3)                   # Liste wird 3 Mal wiederholt, Ausgabe: [0, 1, 0, 1, 0, 1]

# APPEND() - ELEMENT HINZUFÜGEN

liste3 = [1, 2, 5, 6, 9]
liste3.append(20)                   # Fügt eine Zahl am Ende der Liste hinzu (wird immer nur 1 Element hinzugefügt)
print(liste3)                       # Ausgabe: [1, 2, 5, 6, 9, 20]

# SORT() - LISTEN SORTIEREN

liste4 = [1, 2, 5, 6, 9, 11, 4]
liste4.sort()                       # Sortiert die Liste in aufsteigender Reihenfolge, wird direkt in der Liste gespeichert
print(liste4)                       # Ausgabe: [1, 2, 4, 5, 6, 9, 11]
liste4.sort(reverse=True)           # Sortiert die Liste in absteigender Reihenfolge, wird direkt in der Liste gespeichert
print(liste4)                       # Ausgabe: [11, 9, 6, 5, 4, 2, 1]

# COUNT() - ELEMENTE ZÄHLEN

liste5 = [1, 2, 5, 6, 9, 5]
liste5.count(5)                     # Zählt, wie oft ein Element in der Liste vorkommt
print(liste5.count(5))              # Ausgabe: 2

# REMOVE() - ELEMENT ENTFERNEN

liste6 = [1, 2, 5, 6, 9, 5, True, False, "Hallo"]
liste6.remove(5)                                      # Entfernt das ERSTE Vorkommen eines Elements aus der Liste
liste6.remove(True)
print(liste6)                                         # Ausgabe: [1, 2, 6, 9, 5, False, "Hallo"]

# INSERT() - ELEMENT AN BESTIMMTER POSITION EINFÜGEN

liste7 = [0, 1, 2, 4, 5, 6]
liste7.insert(3, 3)                 # Fügt ein Element an einem bestimmten Index ein (Index, Wert)
print(liste7)                       # Ausgabe: [0, 1, 2, 3, 4, 5, 6]

# COPY() UND CLEAR() - KOPIEREN UND LEEREN

liste8 = [0, 1, 2, 3, 4, 5, 6]
kopie = liste8                      # Keine Kopie, sondern nur eine Referenz auf die gleiche Liste
kopie2 = liste8.copy()              # Echte Kopie der Liste
liste8.clear()                      # Entfernt alle Elemente aus der Liste, aber auch in der Kopie sind alle Elemente weg, weil es nur eine Referenz ist
print(liste8)                       # Ausgabe: []
print(kopie)                        # Ausgabe: []
print(kopie2)                       # Ausgabe: [0, 1, 2, 3, 4, 5, 6]

# INDEX() UND IN-OPERATOR - ELEMENT SUCHEN

liste9 = [0, 1, 2, 3, 4, 5, 6]
position = liste9.index(4)          # Speichert den Index eines Elements in einer Variable
print(position)                     # Ausgabe: 4
print(3 in liste9)                  # Prüft, ob ein Element in der Liste enthalten ist, Ausgabe: True
print(10 in liste9)                 # Prüft, ob ein Element in der Liste enthalten ist, Ausgabe: False

# JOIN() - LISTE ZU STRING VERBINDEN

liste10 = [0, 1, 2, 3, 4, 5, 6]
print(";".join(liste10))                        # Fehler: join() funktioniert nur mit Zeichenketten (Strings)
liste11 = ["0", "1", "2", "3", "4", "5", "6"]
print(";".join(liste11))                          # Verbindet alle Elemente der Liste zu einer Zeichenkette, Ausgabe: 0;1;2;3;4;5;6
liste12 = ["M", "i", "a"]
print("".join(liste12))                           # Verbindet alle Elemente der Liste zu einer Zeichenkette, Ausgabe: Mia