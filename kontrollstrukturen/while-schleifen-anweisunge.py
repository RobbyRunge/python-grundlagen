# WHILE-SCHLEIFEN-ANWEISUNG
# Wird verwenden, wenn kein vorgegebener Bereich durchlaufen werden soll, sondern der Abbruch von einer Bedingung abhängt.
# Wird verwendet, wenn der Benutzer den Abbruch der Schleife steuern können soll.
# Endet, sobald die Bedingung nicht mehr erfüllt ist.
# Kann endloss laufen.
# Beispiele: Hauptereignisschleife in Spielen, Viedospiele, Client-/Server-Programmierung, ...

# Hinweise zu while-Schleifen:
# - wiederholt Code, solange Bedingung True ist
# - nützlich, wenn Anzahl der Wiederholungen nicht feststeht
# - Schleifenbedingung am Anfang der Schleife

maxRound = 25                 # Maximale Rundenanzahl
round = 1                     # Startwert für Rundenanzahl

while maxRound > 0:           # Schleifenbedingung (Bedingung)
  print(f"Runde: {round}")    # f = Format-String für Variablen-Einbindung
  round += 1                  # Erhöhung der Rundenanzahl um 1
  maxRound -= 1               # Verringerung der maximalen Rundenanzahl um 1, weil sonst Endlosschleife


name = input("Gib deinen Namen ein! X zum Abbruch: ")     # Eingabe-Funktion input()
namelist = []                                             # Leere Liste für Namen erstellen

while name != "X":                                        # Schleifenbedingung (Bedingung)
  namelist.append(name)                                   # Namen zur Liste hinzufügen
  print(namelist)                                         # Aktuelle Namensliste ausgeben
  name = input("Gib deinen Namen ein! X zum Abbruch: ")   # Neue Eingabe für Namen, damit Schleifenbedingung irgendwann False wird - sonst Endlosschleife