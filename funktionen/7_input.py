# INPUT-FUNKTIONEN

name = input("Gib deinen Namen ein: ")               # Eingabeaufforderung (mit einem Leerzeichen) - Blockiert das Programm bis eine Eingabe erfolgt
# name = input("Gib deinen Namen ein:\n")            # Eingabeaufforderung (mit einem Zeilenumbruch - \n)

print(f"Hallo {name}!")                              # Ausgabe der Eingabe


# BEISPIEL MIT INT (GANZZAHLEN) ARBEITEN

jahr = int(input("In welchem Jahr wurdest du geboren? "))        # Eingabeaufforderung - Umwandlung in einen Integer (Ganzzahl)
alter = 2023 - jahr
print(f"Du bist {alter} Jahre alt.")                             # Ausgabe des Alters