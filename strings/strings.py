# Verschiedene Arten von Zeichenketten in Python
name_test = "John"
name_test1 = 'Doe'

# Ausgabe der Zeichenketten bleibt Struktur erhalten
print("""Lieber Hacker,
      
      Hackers gonna hack 00111010 00101001

      Viele Grüße
  """)

# Länge einer Zeichenkette ermitteln
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