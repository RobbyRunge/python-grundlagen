# FOR-SCHLEIFEN-ANWEISUNG
# Mit einer for-Schleife kannst du über eine Liste von Elementen iterieren. (muss nicht nur Listen sein, sondern auch Strings, Tupel (unveränderliche Listen), Sets (ungeordnete Sammlungen), Dictionaries (Schlüssel-Wert-Paare))
# Wird verwendet, wenn ein vorgegebener Bereich durchlaufen werden soll.
# Wird verwendet, wenn der Durchlauf des vorgegebenen Bereichs nicht durch den Benutzer unterbrochen werden soll.
# Endet, sobald der vorgegebene Bereich vollständig durchlaufen wurde. Die bedingung wäre hier "so lange noch nicht am Ende angekommen".
# Kann nicht endloss laufen.
# Beispiele: Listen, Tupel (unveränderliche Listen), Strings, Zahlenbereiche, ...

# Hinweise zu for-Schleifen:
# - wiederholt Anweisungen für jedes Element in einer Sequenz
# - jedes Element wird nacheinander in der Schleife verarbeitet
# - Schleife endet automatisch, wenn alle Elemente durchlaufen wurden

passwörter = ["abc123", "gehe1m", "test", "123456"] # Liste von Passwörtern

for passwort in passwörter:     # for-Schleife (Schlüsselwort for)
  print(passwort)               # Einrückung (Indentation) ist wichtig!
  if len(passwort) < 5:         # if-Bedingung (Schlüsselwort if)
    break                       # Abbruch der Schleife (Schlüsselwort break)