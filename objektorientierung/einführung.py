# EINFÜHRUNG IN DIE OBJEKTORIENTIERUNG (OOP)
# Klassen sind Baupläne für Objekte

class Mammal:                                             # Definiere die Klasse "Mammal" - Säugetier (Eigenschaften, was mehrere Objekte gemeinsam haben werden vererbt)
  def __init__(self, farbe, rasse, name):                 # Konstruktor-Methode, wird aufgerufen, wenn ein neues Objekt der Klasse erstellt wird
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