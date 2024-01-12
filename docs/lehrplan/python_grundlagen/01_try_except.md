# Exception Handling in Python
[90min]

Beim Programmieren in Python ist es wichtig, Ausnahmen ordnungsgemäß zu behandeln, um robusten und fehlerresistenten Code zu schreiben. Ausnahmen sind Ereignisse, die während der Ausführung eines Programms auftreten und den normalen Ablauf unterbrechen. Du kannst durch korrektes Handling von Ausnahmen Fehler auf elegante Weise bewältigen und so die Gesamtzuverlässigkeit deines Codes verbessern.

## Grundlagen des Exception Handlings

### Try-Except-Block

Die Blöcke `try` und `except` werden verwendet, um Ausnahmen in Python zu behandeln. Der `try`-Block enthält den Code, der eine Ausnahme auslösen könnte, und der `except`-Block gibt an, wie die Ausnahme behandelt werden soll.

```python
    try:
        # Code, der eine Ausnahme auslösen könnte
        ergebnis = 10 / 0
    except ZeroDivisionError as e:
        # Behandlung der spezifischen Ausnahme
        print(f"Fehler: {e}")
```

### Mehrere Except-Blöcke

Du kannst mehrere `except`-Blöcke verwenden, um verschiedene Arten von Ausnahmen zu behandeln.

```python
try:
    wert = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / wert
except ValueError:
    print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")
except ZeroDivisionError as e:
    print(f"Fehler: {e}")
```

### Finally-Block

Der `finally`-Block wird unabhängig davon ausgeführt, ob eine Ausnahme auftritt oder nicht. Er wird oft für Aufräumarbeiten verwendet.

```python
try:
    datei = open("beispiel.txt", "r")
    # Operationen auf der Datei durchführen
except FileNotFoundError:
    print("Datei nicht gefunden.")
finally:
    datei.close()
```

## Fortgeschrittenes Exception Handling

### Eigene Ausnahmen

Du kannst benutzerdefinierte Ausnahmen erstellen, indem du eine neue Klasse definierst, die von der Klasse `Exception` erbt.

```python
class BenutzerdefinierterFehler(Exception):
    pass

try:
    raise BenutzerdefinierterFehler("Dies ist eine benutzerdefinierte Ausnahme.")
except BenutzerdefinierterFehler as e:
    print(f"Fehler gefangen: {e}")
```

### Else-Block

Der `else`-Block wird ausgeführt, wenn keine Ausnahmen im `try`-Block ausgelöst werden.

```python
try:
    wert = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / wert
except ValueError:
    print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")
except ZeroDivisionError as e:
    print(f"Fehler: {e}")
else:
    print(f"Ergebnis: {ergebnis}")
```

## Achtung: Exception Handling und Ablaufsteuerung

Es ist wichtig zu betonen, dass Exception Handling nicht als Mechanismus zur Ablaufsteuerung genutzt werden sollte. Ausnahmen sollten nicht für die Kontrolle des normalen Programmflusses verwendet werden, sondern ausschließlich für die Behandlung von unerwarteten Ereignissen und Fehlerzuständen.

# Aufgaben

[180min]

### 1. Division durch Null verhindern 🌶️️
   - Schreibe einen Python-Code, der eine einfache Division durch Null in einem `try`-Block enthält. Behandle die `ZeroDivisionError`-Ausnahme im `except`-Block, indem du eine aussagekräftige Fehlermeldung ausgibst.

### 2. Benutzereingabe und Integer-Konvertierung 🌶️️
   - Erstelle ein Programm, das den Benutzer nach einer Zahl fragt. Verwende einen `try`-Block, um die eingegebene Zeichenkette in einen Integer umzuwandeln. Behandle mögliche `ValueError`-Ausnahmen im `except`-Block und gib eine entsprechende Meldung aus.

### 3. Datei öffnen mit Fehlerbehandlung 🌶️️
   - Schreibe einen Code, der versucht, eine Datei mit dem Namen "beispiel.txt" zu öffnen. Verwende einen `try`-Block und behandle die `FileNotFoundError`-Ausnahme im `except`-Block, indem du eine Meldung ausgibst.

### 4. Benutzerdefinierte Ausnahme 🌶️️🌶️️
   - Erstelle eine benutzerdefinierte Ausnahme mit dem Namen `NegativeZahlFehler`. Schreibe einen Code, der eine Zahl entgegennimmt. Wenn die Zahl negativ ist, löse die `NegativeZahlFehler`-Ausnahme aus und gib eine entsprechende Meldung aus.

### 5. Dynamisches Laden von Modulen 🌶️️🌶️️
   - Schreibe eine Funktion, die den Benutzer nach dem Namen eines Python-Moduls fragt und es dann dynamisch lädt. Behandle mögliche `ModuleNotFoundError`-Ausnahmen im `except`-Block und gib eine Meldung aus.

### 6. Fortgeschrittene Benutzereingabe 🌶️️🌶️️🌶️️
   - Implementiere einen interaktiven Taschenrechner. Lass den Benutzer nacheinander zwei Zahlen und einen Operator (+, -, *, /) eingeben. Verwende `try`- und `except`-Blöcke, um mögliche `ValueError`-Ausnahmen und unbekannte Operationen zu behandeln. Gib das Ergebnis aus.

### 7. Komplexes Exception Handling 🌶️️🌶️️🌶️️
   - Erstelle einen Code, der eine Datei öffnet, ihren Inhalt liest und in eine andere Datei schreibt. Behandle dabei `FileNotFoundError`, `PermissionError` und `IOError` mit spezifischen Ausnahmen. Gib eine Meldung aus, wenn eine Ausnahme auftritt.

### 8. Fehlerbehandlung bei Dateioperationen 🌶️️🌶️️🌶️️
   - Schreibe einen Code, der versucht, den Inhalt einer Datei zu lesen und in eine andere Datei zu schreiben. Behandle mögliche `FileNotFoundError` und `PermissionError`-Ausnahmen im `except`-Block und gib entsprechende Meldungen aus.


### 9. Fehlerbehandlung in Rekursion 🌶️️🌶️️🌶️️
   - Schreibe eine rekursive Funktion zur Berechnung der Fakultät einer Zahl. Behandle den Basisfall und mögliche `RecursionError`-Ausnahmen durch eine angemessene Fehlerbehandlung.
