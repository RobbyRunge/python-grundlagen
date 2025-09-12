# Verschiedene Arten von Zeichenketten in Python
name_test = "John"
name_test1 = 'Doe'
# Ausgabe der Zeichenketten bleibt Struktur erhalten
print("""Lieber Hacker,
      
      Hackers gonna hack 00111010 00101001

      Viele Grüße
  """)

# len (Länge) einer Zeichenkette
name = "Robby"

print(len("Robby"))  # Direkte Ausgabe der Länge
print(len(name))  # Ausgabe der Länge der Zeichenkette

print("Robby"[4])  # Zugriff auf ein einzelnes Zeichen in der Zeichenkette
print("Robby"[-4])  # Zugriff auf ein einzelnes Zeichen von hinten (letzte Position ist -1)

# Fehlerbeispiele
print("Robby"[8])  # Zugriff auf ein einzelnes Zeichen in der Zeichenkette (Index außerhalb des Bereichs) 
print("Robby"[-8])  # Zugriff auf ein einzelnes Zeichen von hinten (Index außerhalb des Bereichs)

n = len("Robby")
print("Robby"[n])  # Zugriff auf ein einzelnes Zeichen in der Zeichenkette (Index außerhalb des Bereichs)
print("Robby"[-1])  # Zugriff auf das letzte Zeichen in der Zeichenkette

# Slicing (Ausschneiden) von Zeichenketten
name_slicing = "Robby"

print(name_slicing[0:3])  # Ausgabe der ersten drei Zeichen (Index 0 bis 2), Endindex ist exklusiv (ausschließend) - Ausgabe: Rob
print(name_slicing[:3])  # Startindex weglassen, wenn von Anfang an geschnitten werden soll - Ausgabe: Rob
print(name_slicing[2:])  # Endindex weglassen, wenn bis zum Ende geschnitten werden soll - Ausgabe: bby

print(name_slicing[-1000:1000])  # Start- und Endindex außerhalb des Bereichs - Ausgabe: Robby

print(name_slicing[:])  # Start- und Endindex weglassen, um die gesamte Zeichenkette zu erhalten - Ausgabe: Robby