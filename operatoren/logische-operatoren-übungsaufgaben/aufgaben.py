# Übungsaufgaben:

# 1. Welche Wahrheitswerte kommen bei den folgenden logischen Ausdrücken heraus?
True and False and True or False      # False
not False or not True                 # True
True and (False or not False)         # True
not (not False ^ True or not False)   # False
True and False ^ True and False       # False

# 2. Worin besteht der Unterschied zwischen den beiden Operatoren ^ und or?
# Bei XOR kann nur einer der beiden True ergeben und bei OR ist es egal ob beide True sind

# 3. Welche Wahrheitswerte kommen als Ergebnis heraus? 
2 < 3 and not 2 > 5                 # True
not True ^ False or 3 == 2 + 1      # True
not not not 2 % 5 == 7 % 5          # False
True and False ^ True and False     # False
True ^ False ^ 0 ^ 1 ^ (2 > 3)      # 0