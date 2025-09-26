# MATCH-CASE ANWEISUNGEN (VERZWEIGUNGEN)
# Nutze match-case für übersichtliche Vergleiche mit festen Werten.

# Hinweise zu match-case:
# - prüft auf Muster/Werte
# - klar strukturierter als if-elif-else bei vielen festen Werten
# - jeder Fall ein eigener case-Zweig

note = int(input("Gib deine Note ein: "))       # Eingabe-Funktion input() und Umwandlung in int mit int()

match note:
  case 1:                                       # Vergleichsoperator == (gleich) (Bedingung)
    print("Das ist eine sehr gute Note!")       # Einrückung (Indentation) ist wichtig!
  case 2:                                       # elif-Zweig (Bedeutung: else if) (optional)
    print("Das ist eine gute Note!")            # Einrückung (Indentation)
  case 3:
    print("Das ist eine befriedigende Note!")
  case 4:
    print("Das ist eine ausreichende Note!")
  case 5:
    print("Das ist eine mangelhafte Note!")
  case _:                                       # else-Zweig (Bedeutung: sonst) (optional)
    print("Das ist eine schlechte Note!")       # Einrückung (Indentation)