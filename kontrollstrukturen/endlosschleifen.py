# ENDLOSSCHLEIFEN
# Eine Endlosschleife ist eine Schleife, die niemals endet, weil die Bedingung immer wahr ist.

# Hinweise zu Endlosschleifen:
# - Schleifenbedingung ist immer True
# - nützlich für Programme, die kontinuierlich laufen sollen (z.B. Server)
# - Schleife kann nur durch externe Eingriffe (z.B. Tastenkombination) beendet werden

teilnehmerListe = []                                                                  # Leere Liste für Teilnehmer erstellen                   
teilnehmer = input("Gib den Namen des Teilnehmers ein (oder 'exit' zum Beenden): ")   # Eingabe-Funktion input()

while teilnehmer != "exit":             # Schleifenbedingung (Bedingung)
  teilnehmerListe.append(teilnehmer)    # Teilnehmer zur Liste hinzufügen
  print(teilnehmer)                     # Aktuellen Teilnehmer ausgeben

print(teilnehmerListe)                  # Gesamte Teilnehmerliste ausgeben
