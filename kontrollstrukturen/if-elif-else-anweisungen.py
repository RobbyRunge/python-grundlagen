# IF-ELIF-ELSE ANWEISUNGEN (VERZWEIGUNGEN)
# Nutze if-elif-else für komplexe Bedingungen und logische Ausdrücke.

# Hinweise zu if-elif-else:
# - prüft beliebige Bedingungen (True/False)
# - flexibel für komplexe logische Ausdrücke
# - mehrere elif-Zweige möglich

note = input("Gib deine Note ein: ")          # Eingabe-Funktion input()

if note == "1":                               # Vergleichsoperator == (gleich) (Bedingung)
  print("Das ist eine sehr gute Note!")       # Einrückung (Indentation) ist wichtig!
elif note == "2":                             # elif-Zweig (Bedeutung: else if) (optional)
  print("Das ist eine gute Note!")            # Einrückung (Indentation) ist wichtig! 
elif note == "3":
  print("Das ist eine befriedigende Note!")
elif note == "4":
  print("Das ist eine ausreichende Note!")    
elif note == "5":
  print("Das ist eine mangelhafte Note!")
else:                                         # else-Zweig (Bedeutung: sonst) (optional)
  print("Das ist eine schlechte Note!")       # Einrückung (Indentation) ist wichtig!