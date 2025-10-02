# EXEC
# Bedeutet, dass eine Funktion eine andere Funktion als Argument annimmt

cmd = "name = input('Gib deinen Namen ein: ');print(f'Hallo {name}')"    # String mit Python-Code, kann auch mehrere Befehle enthalten

exec(cmd)    # Führt den übergebenen String als Python-Code aus

# Gefahren: 
# - Unsicher, da beliebiger Code ausgeführt werden kann, daher nur mit vertrauenswürdigem Code verwenden!
# - Weil der fehlender Input-Prüfung potienziell Schadcode ausgeführt werden kann.