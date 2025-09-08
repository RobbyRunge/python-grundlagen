# Datentypen in Python
name = "Florian"      # String (Text)
age = 30              # Integer (Ganzzahl)
number = 100_000      # Integer mit Unterstrichen zur besseren Lesbarkeit der Zahl
height = 1.75         # Float (Gleitkommazahl)
is_student = False    # Boolean (Wahrheitswert)

# Funktion zur Überprüfung des Datentyps
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(number))      # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Konvertierung zwischen Datentypen
str()     # Konvertierung zu String
int()     # Konvertierung zu Integer
float()   # Konvertierung zu Float
bool()    # Konvertierung zu Boolean

# Beispiel für Konvertierung
print((str(age)))        # "30"
print((str(name)))       # "Florian"
print((str(number)))     # "100000"
print((int(height)))     # 1
print((int(is_student))) # 0
print((int(False)))      # 0
print((float(age)))      # 30.0
print((float(number)))   # 100000.0
print((float("3.14")))   # 3.14
print(float(True))       # 1.0
print(float(False))      # 0.0
print((bool(height)))    # True
print((bool(0)))         # False
print((bool("")))        # False
