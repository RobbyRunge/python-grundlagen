# KWARGS - KEYWORD ARGUMENTS
# Funktionen können eine beliebige Anzahl an benannten Argumenten empfangen

# GRUNDLAGEN

def kwargs_test(**kwargs):        # ** bedeutet, dass eine beliebige Anzahl an benannten Argumenten übergeben werden kann (wird als Dictionary empfangen) / kwargs = keyword arguments
  print(kwargs)

kwargs_test(a = 1, b = 2, c = 3)  # Schlüssel-Wert-Paare übergeben, Ausgabe: {'a': 1, 'b': 2, 'c': 3}

# GET() METHODE BEI KWARGS

def teilnehmer(**daten):                                # beliebig viele benannte Argumente empfangen
  # Immer besser Default-Werte zu setzen, falls ein Argument nicht übergeben wird
  vorname = daten.get("name", "Max")                    # Können über den Schlüssel abgefragt werden, hier ist der Schlüssel "name" (Default-Wert "Max")
  nachname = daten.get("nachname", "Mustermann")        # wenn der Schlüssel nicht existiert, wird als Default-Wert "Mustermann" gesetzt
  alter = daten.get("alter", 0)
  geschlecht = daten.get("geschlecht", "unbekannt")
  nummer = daten.get("nummer", 123456789)               # wenn der Schlüssel nicht existiert, wird None zurückgegeben. Hier wird als Default-Wert 123456789 gesetzt
  print(f"Hallo {vorname} {nachname}, du bist {alter} Jahre alt und dein Geschlecht ist {geschlecht}. Seine Telefonnnummer ist {nummer}.") 

teilnehmer(name = "Max", nachname = "Mustermann", alter = 30, geschlecht = "männlich")   # Argumente werden benannt übergeben, Reihenfolge egal