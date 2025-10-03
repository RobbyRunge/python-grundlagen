# Python Grundlagen - Modul 3.0

Dieses Repository enthält umfassende Python-Lernmaterialien zu grundlegenden Konzepten der Programmierung. Es behandelt Datenstrukturen, Funktionen, Fehlerbehandlung und Objektorientierung.

---

## 📁 Projektstruktur

### 1. **Datenstrukturen**
- **Listen, Tupel, Sets, Dictionaries**
- Grundlegende Operationen und Methoden
- Best Practices für Datentypen

### 2. **Funktionen**
- Funktionsdefinitionen mit `def`
- Parameter und Rückgabewerte
- Module und Imports
- `if __name__ == "__main__"` Pattern
- **Beispiel:** Taschenrechner-Modul mit mathematischen Operationen

### 3. **Fehlerbehandlung**
- **Datei:** `fehlerbehandlung/finally.py`
- **try-except-finally Blocks:**
  - `try`: Überprüft Code auf Fehler
  - `except`: Fängt und behandelt Ausnahmen (z.B. `IndexError`, `ValueError`)
  - `finally`: Wird immer ausgeführt, ideal für Cleanup-Operationen
- **Beispiel:**
  ```python
  try:
      # Code der Fehler verursachen könnte
      index = int(input("Index eingeben: "))
      print(liste[index])
  except Exception as ex:
      print(f"Fehler: {ex}")
  finally:
      print("Wird immer ausgeführt")
  ```

### 4. **Objektorientierung (OOP)**
- **Datei:** `objektorientierung/einführung.py`
- **Konzepte:**
  - **Klassen und Objekte:** Baupläne für wiederverwendbare Strukturen
  - **Vererbung:** Klassen wie `Hund` und `Katze` erben von `Mammal`
  - **`self`:** Verweis auf die aktuelle Objektinstanz
  - **`__init__`:** Initialisierungsmethode (oft als Konstruktor bezeichnet)
  - **Magische Methoden:**
    - `__str__`: String-Repräsentation
    - `__gt__`: Größer-als-Vergleich
    - `__add__`, `__sub__`, `__eq__`, etc.
- **Beispielklassen:**
  - `Mammal`: Basisklasse mit gemeinsamen Eigenschaften
  - `Pokemon`: Klasse mit Level-System und Kampfmechanik

### 5. **Funktionen vs. Methoden**
- **Funktionen:** Unabhängige Codeblöcke außerhalb von Klassen
- **Methoden:** Funktionen innerhalb von Klassen, gebunden an Objekte
- Aufruf: `funktion()` vs. `objekt.methode()`

---

## 🚀 Ausführung

### Voraussetzungen
- Python 3.6 oder höher

### Beispielaufruf
```bash
# Fehlerbehandlung
python fehlerbehandlung/finally.py

# Objektorientierung
python objektorientierung/einführung.py

# Module
python funktionen/6_module-beispiel/main.py
```

---

## 📚 Wichtige Konzepte

### String-Formatierung
- **Modern (empfohlen):** f-Strings
  ```python
  print(f"Hallo {name}")
  ```
- **Alt:** String-Konkatenation
  ```python
  print("Hallo " + name)
  ```

### Tupel
- Unveränderlich (immutable)
- Keine `.copy()`-Methode nötig
- Verwendung: `tuple(original)` oder direkte Zuweisung

### `if __name__ == "__main__"`
- Prüft, ob Skript direkt ausgeführt wird
- Code wird nicht ausgeführt beim Import als Modul
- Nützlich für Tests und Hauptlogik

---

## ⚠️ Hinweise

- **`exec()`**: Vorsicht bei der Verwendung! Führt beliebigen Code aus und kann Sicherheitsrisiken bergen.
- **Best Practice**: Nutze f-Strings statt String-Konkatenation
- **Magische Methoden**: Ermöglichen natürliches Verhalten von Objekten (Addition, Vergleiche, etc.)

---

## 👤 Autor
**Robby**

Dieses Projekt dient als Lernressource für Python-Grundlagen im Rahmen der Developer Akademie.

---

## 📖 Lizenz
Dieses Projekt ist für Bildungszwecke bestimmt.