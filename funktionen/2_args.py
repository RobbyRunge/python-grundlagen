# ARGS - ARGUMENTS
# Funktionen können eine beliebige Anzahl an Argumenten empfangen

def addieren(*summanden):   # * bedeutet, dass eine beliebige Anzahl an Argumenten übergeben werden kann (wird als Tupel empfangen) / args = arguments
  print(sum(summanden))     # Summe aller übergebenen Argumente wird berechnet und ausgegeben

addieren(1, 2, 5, 6, 7)     # kann beliebig viele Argumente übergeben, Ausgabe: 21 
addieren()                  # keine Argumente übergeben, Ausgabe: 0     

def addieren2(vorname, nachname, *summanden):     # Kombination aus einem normalen Argument und beliebig vielen Argumenten (Reihenfolge beachten: normale Argumente immer zuerst, dann *args)
  print(f"Hallo {vorname} {nachname}")
  print(f"Deine Zahlen lauten: {summanden}")

addieren2("Max", "Mustermann", 1, 2, 5, 6, 7)       # Ausgabe: Hallo Max Mustermann \n Deine Zahlen lauten: (1, 2, 5, 6, 7)
addieren2("Max", 8, 1, 2, 5, 6, 7)                  # Ausgabe: Hallo Max 8 \n Deine Zahlen lauten: (1, 2, 5, 6, 7) - funktioniert, aber nicht sinnvoll