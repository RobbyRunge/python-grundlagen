# AUFRUFSREIHENFOLGE IN FUNKTIONEN
# Reihenfolge der Argumente bei Funktionsaufrufen sind:
# 1. positionelle Argumente
# 2. *args
# 3. **kwargs

def daten_erfasse(id, vorname, nachname, *geo, **daten):   # Reihenfolge der Argumente in der Funktion: normale Argumente, *args, **kwargs
  pass

daten_erfasse(1, "Max", "Mustermann",  geo=[52.5200, 13.4050], email="max@mustermann.de") 