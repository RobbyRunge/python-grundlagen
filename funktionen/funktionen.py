# FUNKTIONEN
# Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe ausführen.

# GRUNDLAGEN

def sag_hallo1(name):         # Funktionskopf / def = Definition der Funktion, name = positionelles Argument
  pass                        # Platzhalter, wenn die Funktion noch keinen Code hat

def sag_hallo2(vorname, nachname):          # Funktionskopf
  print(f"Hallo {vorname} {nachname}")      # Funktionskörper

sag_hallo2("Max", "Mustermann")             # Funktionsaufruf, Ausgabe: Hallo Max Mustermann


def addieren(a, b):
  summe = a + b
  return summe            # Rückgabewert der Funktion (Terminal von VSCode zeigt an, dass die Funktion einen Wert zurückgibt, in dem Fall 42. Wird aber nicht angezeigt im normalen Terminal)

addieren(10, 32)
print(addieren(10, 32))      # Ausgabe: 42 - Rückgabewert wird ausgegeben

s = addieren(10, 32)         # Rückgabewert wird in Variable gespeichert (s hat jetzt den Wert 42)
print(f"Summe: {s}")         # Ausgabe: Summe: 42