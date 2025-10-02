# EINFÜHRUNG IN DIE OBJEKTORIENTIERUNG (OOP)
# Klassen sind Baupläne für Objekte

class Mammal:                                             # Definiere die Klasse "Mammal" - Säugetier (Eigenschaften, was mehrere Objekte gemeinsam haben werden vererbt)
  def __init__(self, farbe, rasse, name):                 # Initialisierungsmethode (oft als "Konstruktor" bezeichnet), wird aufgerufen, wenn ein neues Objekt der Klasse erstellt wird. Das self ist ein Verweis auf das aktuelle Objekt (die Instanz) der Klasse.
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

class Pokemon:
  def __init__(self,name, level):
    self.name = name
    self.__level = level                     # Private Variable, nicht direkt von außen zugreifbar
    self.vorstellen()                        # Aufruf der Methode innerhalb des Konstruktors (self muss angegeben werden, da es sich um eine Instanzmethode handelt) - macht die unteren Zeilen überflüssig 1*

  def vorstellen(self):
    print(f"{self.name}, {self.name}!")

  def get_level(self):                       # Getter-Methode
    return self.__level                      # Zugriff auf die private Variable

if __name__ == "__main__":
  bisasam = Pokemon("Bisasam", 5)            # Instanzierung eines Objekts der Klasse Pokemon Reihenfolge beachtet, davor kann nicht die bisasam.vorstellen() Methode aufgerufen werden
  schiggy = Pokemon("Schiggy", 8)
  
  print(bisasam.get_level())                 # Zugriff auf die private Variable über die Getter-Methode

  # schiggy.vorstellen()                     # 1*
  # bisasam.vorstellen()                     # 1*        