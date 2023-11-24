# Fehlerbehandlung

![Fehlerbehandlung](../clean_code/pictures/BrokenDishes.jpg)

```python
def divide(a, b):
    return a / b
```

Es ist wichtig, Ausnahmen zu behandeln, um unerwartete Abstürze zu vermeiden.

Im Fall einer Division sollten wir insbesondere eine Division durch null abfangen.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        return None
```

**Frage**: Gibt es noch weitere Verbesserungen an dieser Funktion?

**Antwort**:

- Die Programmiererin muss entscheiden, ob der Code weiter ausgeführt werden darf. Ist das der Fall, so ist der obige
  Code geeignet.
- Soll das Programm angehalten werden, so ist der folgende Code zu verwenden. Dabei ist zu beachten, dass möglicherweise
  das bis dahin abgelaufene Programm nicht vollständig aufgeräumt werden kann.

```python
import sys

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        sys.exit(1)
```

- Um sicherzustellen, dass alles in definierten Bahnen abläuft, kann es daher sinnvoll sein, den "finally" Block
  einzufügen. Der finally-Block in Python ist besonders nützlich, wenn Sie sicherstellen möchten, dass bestimmte
  Aufräumarbeiten oder Abschlussaktionen ausgeführt werden, unabhängig davon, ob eine Ausnahme auftritt oder nicht. Dies
  ist besonders hilfreich bei der Arbeit mit Ressourcen wie Dateien oder Netzwerkverbindungen, die ordnungsgemäß
  geschlossen oder freigegeben werden müssen, um Ressourcenlecks zu vermeiden.

```python
def datei_bearbeiten(dateipfad):
    try:
        datei = open(dateipfad, 'r')
        daten = datei.read()
        # Weiterverarbeitung der Daten
    except IOError:
        print("Fehler beim Lesen der Datei.")
    finally:
        # Dieser Block wird immer ausgeführt
        datei.close()
        print("Die Datei wurde geschlossen.")


datei_bearbeiten("beispieldatei.txt")
```

Wenn sie eine Ausnahmebehandlung vorsehen, sollte nichts vor dem "try" stehen und nach dem "except" Block sollte auch
kein weiterer Code mehr folgen. Ausnahme: der "finally" Block.

Diese Regel erklärt sich aus der Tatsache, dass eine Funktion nur eine Aufgabe tun soll. Die Funktion
Try ... Except ... Finally ist ebenfalls eine Funktion, die nur eine Aufgabe machen soll.

[zurück](../TheGoodPractices)