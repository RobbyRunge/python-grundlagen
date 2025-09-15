# VERGLEICHSOPERATOREN
# Vergleichsoperatoren werden verwendet, um zwei Werte zu vergleichen und einen booleschen Wert (True oder False) zurückzugeben.

2 < 3             # Kleiner als: True, weil 2 kleiner als 3 ist

a = 5
b = 10
a < b             # True, weil 5 kleiner als 10 ist
a <= b            # Kleiner oder gleich: True, weil 5 kleiner oder gleich 10 ist
a > b             # Größer als: False, weil 5 nicht größer als 10 ist
a >= b            # Größer oder gleich: False, weil 5 nicht größer oder gleich 10 ist

c = "Robby"
d = "Alice"
c == d            # Gleich: True, weil beide Strings identisch sind
c != d            # Ungleich: True, weil die Strings unterschiedlich sind
c < d             # Lexikographisch kleiner: False, weil "Robby" nicht vor "Alice" kommt (Länge und Buchstaben werden verglichen)
c > d             # Lexikographisch größer: True, weil "Robby" nach "Alice" kommt (Länge und Buchstaben werden verglichen)
c <= d            # Lexikographisch kleiner oder gleich: False, weil "Robby" nicht vor oder gleich "Alice" ist (Länge und Buchstaben werden verglichen)
c >= d            # Lexikographisch größer oder gleich: True, weil "Robby" nach oder gleich "Alice" ist (Länge und Buchstaben werden verglichen)