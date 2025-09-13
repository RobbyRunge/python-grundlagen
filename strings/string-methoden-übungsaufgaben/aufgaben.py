# Übungsaufgaben:

# 1. Was wird von dem folgenden Programm ausgegeben?
passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper())                  # Ausgabe: ABC123
print(passwort2.lower())                  # Ausgabe: pass wort
print(passwort3.islower())                # Ausgabe: True
print(passwort2.isupper())                # Ausgabe: False
print(passwort1.zfill(8))                 # Ausgabe: 000abc123
print(passwort2.strip())                  # Ausgabe: PassWort
print(len(passwort3))                     # Ausgabe: 10
print(passwort1.isalpha())                # Ausgabe: False
print(passwort1[3:].isnumeric())          # Ausgabe: True
print("a;b;c;d;e".split(';'))             # Ausgabe: ['a', 'b', 'c', 'd', 'e']
print("01.23.45.67.89".split(';'))        # Ausgabe: ['01.23.45.67.89']
print(passwort2.replace("Pass",'.'))      # Ausgabe: . Wort
print(passwort3.count('3'))               # Ausgabe: 2
print(passwort2.count('s'))               # Ausgabe: 2
print(passwort3.find(2+2))                # Ausgabe: 4
print(passwort1.index("4"))               # Ausgabe: ValueError

# 2. Verwende passende String-Methoden, um die vorgegebenen Strings in die umzuwandeln, die als Kommentar vorgegeben sind:
"passw0r7"      # PASSw0r72
"Anime"         # 000000Anime3
"florian"       # Florian
"Kaguya"        # kaguya
"0123456789"    # 9876543210

print("passw0r7".upper().replace("7","72").replace("W", "w").replace("R", "r"))   # Ausgabe: PASSW0R72
print("Anime".zfill(11).replace("e", "e3"))                                       # Ausgabe: 000000Anime3
print("florian".capitalize())                                                     # Ausgabe: Florian
print("Kaguya".lower())                                                           # Ausgabe: kaguya
print("0123456789".replace("0123456789", "9876543210"))                           # Ausgabe: 9876543210