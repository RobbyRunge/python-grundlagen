# HAUPTPROGRAMM
# Dieses Programm verwendet das Modul "taschenrechner", um grundlegende mathematische Operationen durchzuführen.

import taschenrechner as tr           # Importiere das Modul "taschenrechner" und gebe ihm den Kurznamen "tr"

from taschenrechner import *          # Importiere alle Funktionen aus dem Modul "taschenrechner", Probleme bei Namenskonflikten möglich

summe = tr.addieren(5, 3)                     # Verwende die Funktion "addiere" aus dem Modul "tr"
differenz = tr.subtrahieren(10, 4)            # Verwende die Funktion "subtrahiere" aus dem Modul "tr"
produkt = tr.multiplizieren(4, 5)             # Verwende die Funktion "multipliziere" aus dem Modul "tr"
quotient = tr.dividieren(20, 4)               # Verwende die Funktion "dividiere" aus dem Modul "tr"

summe_from_import = addieren(2, 2)            # Verwende die Funktion "addiere" direkt, da sie importiert wurde
differenz_from_import = subtrahieren(5, 3)    # Verwende die Funktion "subtrahiere" direkt
produkt_from_import = multiplizieren(3, 3)    # Verwende die Funktion "multipliziere" direkt
quotient_from_import = dividieren(8, 2)       # Verwende die Funktion "dividiere" direkt

print(f"Summe: {summe}, Differenz: {differenz}, Produkt: {produkt}, Quotient: {quotient}")

print(f"Summe (from import): {summe_from_import}, Differenz (from import): {differenz_from_import}, Produkt (from import): {produkt_from_import}, Quotient (from import): {quotient_from_import}")

# Erklärung: if __name__ == "__main__"

if __name__ == "__main__":
  print("Das Hauptprogramm wird direkt ausgeführt.")

# prüft, ob das aktuelle Python-Skript direkt ausgeführt wird (also z.B. mit python main.py) und nicht als Modul in ein anderes Skript importiert wurde.

# Bedeutung:
# Ist das Skript das Hauptprogramm, dann ist __name__ gleich "__main__" und der nachfolgende Code wird ausgeführt.
# Wird das Skript als Modul importiert, ist __name__ der Modulname und der Code wird nicht ausgeführt.

# Vorteil:
# So kannst du Code schreiben, der nur beim direkten Ausführen des Skripts läuft (z.B. Tests, Hauptlogik), aber nicht beim Importieren als Modul.