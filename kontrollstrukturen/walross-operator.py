# WALROSS-OPERATOR (:=)
# Der Walross-Operator (:=) ermöglicht es, eine Variable innerhalb eines Ausdrucks zuzuweisen und gleichzeitig zu verwenden.

teilnehmerListe = []                                                                                       # Leere Liste für Teilnehmer erstellen

while (teilnehmer := input("Gib den Namen des Teilnehmers ein (oder 'exit' zum Beenden): ")) != "exit":    # Eingabe-Funktion input() und Zuweisung mit Walross-Operator
  teilnehmerListe.append(teilnehmer)                                                                       # Teilnehmer zur Liste hinzufügen

print(teilnehmerListe)                                                                                     # Gesamte Teilnehmerliste ausgeben