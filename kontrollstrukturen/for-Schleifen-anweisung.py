# FOR-SCHLEIFEN-ANWEISUNG
# Mit einer for-Schleife kannst du über eine Liste von Elementen iterieren. (muss nicht nur Listen sein, sondern auch Strings, Tupel, Sets, Dictionaries)

# Hinweise zu for-Schleifen:
# - wiederholt Anweisungen für jedes Element in einer Sequenz
# - jedes Element wird nacheinander in der Schleife verarbeitet
# - Schleife endet automatisch, wenn alle Elemente durchlaufen wurden

passwörter = ["abc123", "gehe1m", "test", "123456"] # Liste von Passwörtern

for passwort in passwörter:     # for-Schleife (Schlüsselwort for)
  print(passwort)               # Einrückung (Indentation) ist wichtig!
  if len(passwort) < 5:         # if-Bedingung (Schlüsselwort if)
    break                       # Abbruch der Schleife (Schlüsselwort break)