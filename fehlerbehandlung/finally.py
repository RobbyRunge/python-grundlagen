# FINALLY
# Das finally-Statement wird immer ausgeführt, egal ob eine Ausnahme aufgetreten ist oder nicht.

liste = [1, 2, 3, "Flo", "Mia", "Robby"]

try:
  index2 = int(input("Bitte gib einen Index ein: "))
  print(liste[index2])
except Exception as ex:                                   # Fange alle Fehler ab (IndexError, ValueError, etc.)
  print(ex)                                               # Allgemeine Fehlermeldung
  print(f"Der Zugriff ist fehlgeschlagen.\n{ex}")
finally:                                                  # Dieser Block wird immer ausgeführt
  print("Das finally-Statement wird immer ausgeführt.")