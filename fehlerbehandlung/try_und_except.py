# TRY UND EXCEPT
# try wird immer in Kombination mit except verwendet.

liste = [1, 2, 3, "Flo", "Mia", "Robby"]

# Fehlerbehandlung mit spezifischen Exception-Handlern 

try:
  index = int(input("Bitte gib einen Index ein: "))
  print(liste[index])
except IndexError as ex:                            # Fange den Fehler ab, wenn der Index nicht existiert (mit "as" wird die Fehlermeldung von Python in einer Variable gespeichert, üblich mit dem Namen "ex" - except)
  print(ex)                                         # Index existiert nicht
  print(f"Der Zugriff ist fehlgeschlagen.\n{ex}")
except ValueError as ex:                            # Fange den Fehler ab, wenn der Input kein Integer ist
  print(ex)                                         # Input war kein Integer
  print(f"Bitte gib eine Zahl ein.\n{ex}")

# Allgemeiner Exception-Handler (fängt alle Fehler ab, auch wenn sie nicht vorhergesehen wurden)

try:
  index2 = int(input("Bitte gib einen Index ein: "))
  print(liste[index2])
except Exception as ex:                             # Fange alle Fehler ab (IndexError, ValueError, etc.)
  print(ex)                                         # Allgemeine Fehlermeldung
  print(f"Der Zugriff ist fehlgeschlagen.\n{ex}")