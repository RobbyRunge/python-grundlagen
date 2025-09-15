# VARIABLEN IN PYTHON
name = "Markus"                                     # String (Zeichenkette)
age = 28                                            # Integer (Ganzzahl)
is_student = True                                   # Boolean (Wahrheitswert)

var1, var2, var3 = False, 2.5, "Hallo"              # Mehrere Variablen in einer Zeile
var2 = "Welt"                                       # Variable neu zuweisen, Typ ändert sich dynamisch

print(name)                                         # Ausgabe: Markus
print(f"Hallo {name}, ich bin {age} Jahre alt!")    # Ausgabe: Hallo Markus, ich bin 28 Jahre alt!

# ----------------------------------------------------------------

# FALSCHE BEISPIELE FÜR VARIABLEN
wrong_name = 20
wrong_age = "Max"

wrong_name, wrong_age = wrong_age, wrong_name                   # Variablen tauschen

print(f"Hallo {wrong_name}, ich bin {wrong_age} Jahre alt!")    # Ausgabe: Hallo 20, ich bin Max Jahre alt!

# ----------------------------------------------------------------

# RESERVIERTE SCHLÜSSELWÖRTER IN PYTHON
import keyword

print(keyword.kwlist)       # Ausgabe aller reservierten Schlüsselwörter in Python ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']