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