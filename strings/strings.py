# VERSCHIEDENE MÖGLICHKEITEN, ZEICHENKETTEN ZU DEFINIEREN
name_test = "John"
name_test1 = 'Doe'
# Ausgabe der Zeichenketten bleibt Struktur erhalten
print("""Lieber Hacker,
      
      Hackers gonna hack 00111010 00101001

      Viele Grüße
  """)

# LEN FUNKTION (LÄNGE EINER ZEICHENKETTE)
name = "Robby"

print(len("Robby"))   # Direkte Ausgabe der Länge
print(len(name))      # Ausgabe der Länge der Zeichenkette

print("Robby"[4])     # Zugriff auf ein einzelnes Zeichen in der Zeichenkette
print("Robby"[-4])    # Zugriff auf ein einzelnes Zeichen von hinten (letzte Position ist -1)

# Fehlerbeispiele
print("Robby"[8])     # Zugriff auf ein einzelnes Zeichen in der Zeichenkette (Index außerhalb des Bereichs) 
print("Robby"[-8])    # Zugriff auf ein einzelnes Zeichen von hinten (Index außerhalb des Bereichs)

n = len("Robby")
print("Robby"[n])     # Zugriff auf ein einzelnes Zeichen in der Zeichenkette (Index außerhalb des Bereichs)
print("Robby"[-1])    # Zugriff auf das letzte Zeichen in der Zeichenkette

# ----------------------------------------------------------------

# SLICING (AUSSCHNEIDEN) VON ZEICHENKETTEN

name_slicing = "Robby"

print(name_slicing[0:3])          # Ausgabe der ersten drei Zeichen (Index 0 bis 2), Endindex ist exklusiv (ausschließend) - Ausgabe: Rob
print(name_slicing[:3])           # Startindex weglassen, wenn von Anfang an geschnitten werden soll - Ausgabe: Rob
print(name_slicing[2:])           # Endindex weglassen, wenn bis zum Ende geschnitten werden soll - Ausgabe: bby

print(name_slicing[-1000:1000])   # Start- und Endindex außerhalb des Bereichs - Ausgabe: Robby

print(name_slicing[:])            # Start- und Endindex weglassen, um die gesamte Zeichenkette zu erhalten - Ausgabe: Robby

# ----------------------------------------------------------------

# STRINGS KONKATENIEREN (VERKETTEN)

x = "Apfel"
y = "Baum"
print(x + y)              # Ausgabe: ApfelBaum

a = "Hallo" 
b = ' '
c = "Python"
d = "!"
print(a + b + c + d)      # Ausgabe: Hallo Python!

print(a - b)              # Fehler: Subtraktion von Zeichenketten ist nicht erlaubt
print(a / b)              # Fehler: Division von Zeichenketten ist nicht erlaubt
print(3 * d)              # Ausgabe: !!! # Zeichenkette wird 3 Mal wiederholt, geht nur mit Zahl und Zeichenkette

# ----------------------------------------------------------------

# STRING METHODEN (FUNKTIONEN, DIE AUF ZEICHENKETTEN ANGEWENDET WERDEN KÖNNEN)

print(dir(str))                                   # Ausgabe aller Methoden, die auf Zeichenketten angewendet werden können

print("Robby".zfill(10))                          # Füllt die Zeichenkette mit Nullen auf eine Gesamtlänge von 10 auf, Ausgabe: 00000Robby

print("Robby123!".upper())                        # Wandelt die Zeichenkette in Großbuchstaben um, Ausgabe: ROBBY123!
print("Robby123!".lower())                        # Wandelt die Zeichenkette in Kleinbuchstaben um, Ausgabe: robby123!

print("rObbY123!".capitalize())                   # Wandelt den ersten Buchstaben in Großbuchstaben um und den Rest in Kleinbuchstaben, Ausgabe: Robby123!

print("Robby123!".isupper())                      # Prüft, ob alle Buchstaben in Großbuchstaben sind, Ausgabe: False
print("ROBBY123!".islower())                      # Prüft, ob alle Buchstaben in Kleinbuchstaben sind, Ausgabe: False

print("Robby123!".isnumeric())                    # Prüft, ob die Zeichenkette nur aus Zahlen besteht, Ausgabe: False
print("Robby!".isalpha())                         # Prüft, ob die Zeichenkette nur aus Buchstaben besteht, Ausgabe: True

print("Robby;Pamela;Mia;Tokage".split(";"))       # Teilt die Zeichenkette an jedem Semikolon und gibt eine Liste zurück, Ausgabe: ['Robby', 'Pamela', 'Mia', 'Tokage']
print("Robby\nPamela\nMia\nTokage".splitlines())  # Teilt die Zeichenkette an jedem Zeilenumbruch und gibt eine Liste zurück, Ausgabe: ['Robby', 'Pamela', 'Mia', 'Tokage']
print("Robby\nPamela\nMia\nTokage".split("\n"))   # Teilt die Zeichenkette an jedem Zeilenumbruch und gibt eine Liste zurück, Ausgabe: ['Robby', 'Pamela', 'Mia', 'Tokage']

print("   Robby   ".strip())                      # Entfernt Leerzeichen am Anfang und Ende der Zeichenkette, Ausgabe: Robby
print("   Rob  by   ".strip())                    # Entfernt Leerzeichen am Anfang und Ende der Zeichenkette, Ausgabe: Rob  by

print("   Robby   ".replace(" ", ""))             # Ersetzt alle Leerzeichen durch nichts (" "  ersetzt durch ""), Ausgabe: Robby
print("   Rob  by   ".replace(" ", ""))           # Ersetzt alle Leerzeichen durch nichts (" "  ersetzt durch ""), Ausgabe: Robby
print("   Robby   ".replace("b", "."))            # Ersetzt alle "b" durch ".", Ausgabe: Ro..y

print("Wasserfall".count("s"))                    # Zählt, wie oft "s" in der Zeichenkette vorkommt, Ausgabe: 2
print("168866553232158684765143".count("3"))      # Zählt, wie oft "3" in der Zeichenkette vorkommt, Ausgabe: 5

print("Wasserfall".index("e"))                    # Gibt den Index des ersten Vorkommens von "e" zurück, Ausgabe: 4
print("Wasserfall".index("Q"))                    # Gibt den Index des ersten Vorkommens von "Q" zurück, Ausgabe: ValueError, wenn das Zeichen nicht gefunden wird
print("Wasserfall".find("e"))                     # Gibt den Index des ersten Vorkommens von "e" zurück aber es wird kein Fehler ausgegeben, Ausgabe: 4
print("Wasserfall".find("Q"))                     # Gibt den Index des ersten Vorkommens von "Q" zurück aber es wird kein Fehler ausgegeben, Ausgabe: -1 (Fluchwert, wenn das Zeichen nicht gefunden wird)

print("Wasser" in "Wasserfall")                   # Prüft, ob "Wasser" in der Zeichenkette "Wasserfall" enthalten ist, Ausgabe: True