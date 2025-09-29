# DICTIONARIES
# Ein Dictionary (Wörterbuch) ist eine ungeordnete Sammlung von Schlüssel-Wert-Paaren. Die Schlüssel müssen eindeutig und unveränderlich (immutable) sein, während die Werte beliebige Datentypen haben können. Dictionaries sind veränderbar, d.h. Elemente können hinzugefügt, entfernt oder geändert werden.

# GRUNDLAGEN

dict()                   # Leeres Dictionary
print({
  "name": "Robby", 
  "age": 28
})                       # Dictionary mit Werten
print({
  "name": "Robby", 
  "age": 28
}["name"])               # Zugriff auf einen Wert über den Schlüssel, Ausgabe: "Robby"
print({
  "name": "Robby", 
  "age": 28
}["number"])             # KeyError: 'number' (Schlüssel existiert nicht)
print({
  "name": "Robby", 
  "age": 28
}["number"])             # KeyError: 'number' (Schlüssel existiert nicht)

# GET() - WERT ÜBER SCHLÜSSEL ABRUFEN (IMMER GET() VERWENDEN, UM KEYERROR ZU VERMEIDEN UND SICHERZUSTELLEN, DASS EIN WERT ZURÜCKGEGEBEN WIRD)

dict1 = {
  "name": "Robby",
  "age": 28
}
print(dict1.get("age"))            # Abrufen eines Werts über den Schlüssel, Ausgabe: 28
print(dict1.get("number"))         # Abrufen eines Werts über einen nicht existierenden Schlüssel, Ausgabe: None

dict2 = {
  1: "Robby",                      # Auch mit anderen Datentypen als Schlüssel möglich (integer)
  2.0: 28,                         # Auch mit anderen Datentypen als Schlüssel möglich (float)
  []: "Hallo",                     # TypeError: unhashable type: 'list' (Listen sind veränderlich und können daher nicht als Schlüssel verwendet werden)
  True: "Wahr"                     # Auch mit anderen Datentypen als Schlüssel möglich (boolean)
}
print(dict2.get(1))                # Abrufen eines Werts über den Schlüssel, Ausgabe: "Robby"
print(dict2.get(2.0))              # Abrufen eines Werts über den Schlüssel, Ausgabe: 28
print(dict2.get([]))               # TypeError: unhashable type: 'list' (Listen sind veränderlich und können daher nicht als Schlüssel verwendet werden)
print(dict2.get(True))             # Abrufen eines Werts über den Schlüssel, Ausgabe: "Wahr"

# LEN() - LÄNGE DES DICTIONARY

dict3 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
print(len(dict3))                 # Länge des Dictionary, Ausgabe: 3

# DEFAULT-WERT BEI GET()

dict4 = {
  "abc123": "a2d134dsa36d32sa1asd32",
  "def456": "f4g5h6j7k8l9m0n1o2p3q4r5",
  "ghi789": "i8j9k0l1m2n3o4p5q6r7s8t9"
}
print(dict4.get("jkl456", "654das6as2f15sad2s1d"))   # Abrufen eines Werts über einen nicht existierenden Schlüssel, Ausgabe: "654das6as2f15sad2s1d". Default-Wert wird zurückgegeben, wenn der Schlüssel nicht existiert.

# OHNE METHODE UPDATE() - WERT ÜBER SCHLÜSSEL HINZUFÜGEN ODER ÄNDERN

dict5 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
dict5["name"] = "Max"              # Fügt ein neues Schlüssel-Wert-Paar hinzu
print(dict5)                       # Ausgabe: {'name': 'Max', 'age': 28, 'city': 'Berlin'}

dict6 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
dict6["address"] = "Hauptstraße 5"      # Fügt ein neues Schlüssel-Wert-Paar hinzu
print(dict6)                            # Ausgabe: {'name': 'Robby', 'age': 28, 'city': 'Berlin', 'address': 'Hauptstraße 5'}

# UPDATE() - WERT ÜBER SCHLÜSSEL HINZUFÜGEN ODER ÄNDERN

dict7 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
dict7.update({"name": "Max"})           # Ändert den Wert eines bestehenden Schlüssels
print(dict7)                            # Ausgabe: {'name': 'Max', 'age': 28, 'city': 'Berlin'}

# DEL - ENTFERNT EIN SCHLÜSSEL-WERT-PAAR

dict8 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
del dict8["age"]              # Entfernt ein Schlüssel-Wert-Paar
print(dict8)                  # Ausgabe: {'name': 'Robby', 'city': 'Berlin'}

# CLEAR() - ENTFERNT ALLE SCHLÜSSEL-WERT-PAARE

dict9 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
dict9.clear()               # Entfernt alle Schlüssel-Wert-Paare
print(dict9)                # Ausgabe: {}

# COPY() - DICTIONARY KOPIEREN

dict10 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
kopie = dict10                    # Keine Kopie, sondern nur eine Referenz auf das gleiche Dictionary
kopie2 = dict10.copy()            # Echte Kopie des Dictionary
print(kopie2)                     # Ausgabe: {'name': 'Robby', 'age': 28, 'city': 'Berlin'}

# KEYS() - GIBT EINE LISTE ALLER SCHLÜSSEL ZURÜCK

dict11 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
print(dict11.keys())              # Gibt den Datentyp der Schlüssel zurück, Ausgabe: <class 'dict_keys'> (das ist kein Listentyp, sondern ein spezieller dict_keys Typ) Ausgabe: dict_keys(['name', 'age', 'city'])
print(list(dict11.keys()))        # Wandelt die Schlüssel in eine Liste um, Ausgabe: ['name', 'age', 'city']

# VALUES() - GIBT EINE LISTE ALLER WERTE ZURÜCK

dict12 = {
  "name": "Robby",
  "age": 28,
  "city": "Berlin"
}
print(dict12.values())            # Gibt den Datentyp der Werte zurück, Ausgabe: <class 'dict_values'> (das ist kein Listentyp, sondern ein spezieller dict_values Typ) Ausgabe: dict_values(['Robby', 28, 'Berlin'])
print(list(dict12.values()))      # Wandelt die Werte in eine Liste um, Ausgabe: ['Robby', 28, 'Berlin']