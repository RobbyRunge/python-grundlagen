# EINFÜHRUNG IN DIE OBJEKTORIENTIERUNG (OOP)
# Klassen sind Baupläne für Objekte

class Mammal:                                             # Definiere die Klasse "Mammal" - Säugetier (Eigenschaften, was mehrere Objekte gemeinsam haben werden vererbt)
  def __init__(self, farbe, rasse, name):                 # Initialisierungsmethode (oft als "Konstruktor" oder "magische Methode" bezeichnet), wird aufgerufen, wenn ein neues Objekt der Klasse erstellt wird. Das self ist ein Verweis auf das aktuelle Objekt (die Instanz) der Klasse.
    self.farbe = farbe                                    # Instanzvariable "farbe"
    self.rasse = rasse                                    # Instanzvariable "rasse"
    self.name = name                                      # Instanzvariable "name"

  def vorstellen(self):                                                                 # Aufrufbare Methode der Klasse
    print(f"Ich bin ein {self.farbe}er {self.rasse} und heiße {self.name}.")

  def essen(self):       # Beispielmethode
    pass

  def laufen(self):
    pass

class Hund(Mammal):      # Definiere die Klasse "Hund" und erbe von der Klasse "Mammal"
  def bellen(self):
    pass

class Katze(Mammal):     # Definiere die Klasse "Katze" und erbe von der Klasse "Mammal"
  def miauen(self):
    pass


dog1 = Hund("braun", "Dackel", "Bello")                   # Erstelle ein Objekt der Klasse "Hund"
dog2 = Hund("schwarz", "Labrador", "Hasso")               # Erstelle ein weiteres Objekt der Klasse "Hund"

cat1 = Katze("weiß", "Perser", "Miezi")                   # Erstelle ein Objekt der Klasse "Katze"
cat2 = Katze("getigert", "Europäisch Kurzhaar", "Tiger")  # Erstelle ein weiteres Objekt der Klasse "Katze"

dog1.vorstellen()
dog2.vorstellen()
cat1.vorstellen()
cat2.vorstellen()

# ----------------------------------------

# Die Klasse "Pokemon" modelliert ein Pokémon mit Namen, Level und Lebenspunkten.
# Sie bietet Methoden, um das Pokémon vorzustellen, Lebenspunkte und Level anzuzeigen,
# es weiterzuentwickeln und andere Pokémon anzugreifen.
class Pokemon:
  def __init__(self, name):
    self.__name = name
    self.__level = 1                         # Private Variable, nicht direkt von außen zugreifbar
    self.__lebenspunkte = 42
    
    # self.vorstellen()                      # Aufruf der Methode innerhalb des Konstruktors (self muss angegeben werden, da es sich um eine Instanzmethode handelt)

  def __str__(self):
    return f"Name: {self.__name}\nLebenspunkte: {self.__lebenspunkte}\nLevel: {self.__level}"        # Definiere die String-Repräsentation des Objekts (magische Methode)
  
  def __gt__(self, other):                   # Definiere die Größer-als-Methode (magische Methode)
    return self.__level > other.__level

  def vorstellen(self):
    print(f"{self.__name}, {self.__name}!")

  def zeige_lebenspunkte(self):
    return self.__lebenspunkte               # Zugriff auf die private Variable durch eine Methode

  def zeige_level(self):
    print(f"{self.__name} : {self.__level}")
    return self.__level

  def entwicklen(self):
    self.__level += 1

  def attackieren(self, other, schaden):     # "other" wird als gängiges Wort für das andere Objekt verwendet (in dem Fall ein anderes Pokemon)
    other.__lebenspunkte -= schaden

if __name__ == "__main__":                   # Teste die Klasse nur, wenn das Skript direkt ausgeführt wird
  # Erstelle zwei Pokémon-Objekte
  p1 = Pokemon("Pikachu")                  
  p2 = Pokemon("Bisasam")

  # Test für öffentliche Methoden
  p1.attackieren(p2, 10)
  print(p2.zeige_lebenspunkte())

  # Test für magische Methoden __str__ und __gt__
  p1.entwicklen()
  p2.attackieren(p1, 5)
  print(p1)                                 # Gibt die String-Repräsentation des Objekts aus (magische Methode __str__ wird automatisch aufgerufen)
  print(p2)                                 # Gibt die String-Repräsentation des Objekts aus (magische Methode __str__ wird automatisch aufgerufen)

  print(p1 > p2)                            # Vergleicht die Level der beiden Pokémon (magische Methode __gt__ wird automatisch aufgerufen)

# Magische Methoden (Methoden, die mit __ beginnen und enden) ermöglichen es, das Verhalten von Objekten in bestimmten Situationen zu definieren, z.B. wie sie dargestellt werden oder wie sie miteinander verglichen werden. Es gibt:
# +  | __add__(self, other)          | Addition
# -  | __sub__(self, other)          | Subtraktion
# *  | __mul__(self, other)          | Multiplikation
# /  | __truediv__(self, other)      | Division
# == | __eq__(self, other)           | Gleichheit
# <  | __lt__(self, other)           | Kleiner als
# >  | __gt__(self, other)           | Größer als


# Funktionen vs. Methoden

# Funktionen sind unabhängige Codeblöcke, die außerhalb von Klassen definiert werden und beliebig aufgerufen werden können.
# Methoden sind Funktionen, die innerhalb einer Klasse definiert sind und immer auf ein Objekt (meist über self) zugreifen.
# Sie werden mit einem Punkt an einem Objekt aufgerufen, z.B. objekt.methode().
# Kurz:
# Funktionen = allgemein,
# Methoden = an Klassen/Objekte gebunden.