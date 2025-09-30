# SCOPING
# Gültigkeitsbereich von Variablen built-in, global, lokal

# built-in: in der gesamten Python-Umgebung gültig
# global: in der ganzen Datei gültig
# lokal: nur innerhalb einer Funktion gültig

level = 0          # globale Variable (global scope), kann überall im Modul verwendet werden

def level_up():
  level = 5                           # lokale Variable (local scope), kann nur innerhalb der Funktion verwendet werden               
  print(f"Dein Level ist: {level}")   # local scope, kann nur innerhalb der Funktion verwendet werden

level_up()                            # global scope, kann überall im Modul verwendet werden
print(level)                          # global scope, Ausgabe: 0, weil die globale Variable level nicht verändert wurde


def level_up2(level = 5):
  print(f"Dein Level ist: {level}")

level_up2(3)                           # Ausgabe: 3, weil der übergebene Wert 3 ist (überschreibt den Default-Wert 5)
print(level)                          # Ausgabe: 0, weil die globale Variable level nicht verändert wurde


level3 = 0

def level_up3():
  global level3                       # global wird verwendet, um die globale Variable level3 zu referenzieren
  level3 += 1

level_up3()                           
print(f"Dein Level ist: {level3}")    # Ausgabe: 1, weil die globale Variable level3 um 1 erhöht 