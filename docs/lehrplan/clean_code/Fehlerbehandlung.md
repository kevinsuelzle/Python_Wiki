# Fehlerbehandlung

```python
def divide(a, b):
    return a / b
```

Es ist wichtig, Ausnahmen zu behandeln, um unerwartete Abstürze zu vermeiden.

Im Fall einer Division sollten wir insbesondere eine Division durch `0` abfangen.

Beim Abfangen könnten wir den Code weiter laufen lassen:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        return None
```

oder wir lassen das programm abbrechen:

```python
import sys

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        sys.exit(1)
```

Anderfalls wird die Exeption als Rückgabe der Methode nach außen weitergeleitet und der Aufrufer von `devide` ist für diese verantworlich.
Entweder er fängt sie selbt in einem Try-Catch block oder gibt sie weiter.

## Finally

Um sicherzustellen, dass alles in definierten Bahnen abläuft, kann es daher sinnvoll sein, den "finally" Block
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
    return daten

print(datei_bearbeiten("beispieldatei.txt"))
```
## Aufgabe: 
Was würde passieren, wenn man den Code im `finally`-Block nach dem `except`-Block schreibt, also ohne den die `finally`-Zeile

$$$ Task 5:
* Erinnern, dass man das in Python mit `with` macht.
* Zeige, wie man Klassen so definiert, dass sie mit `with` arbeiten können.
* Überarbeite den bestehenden Text der Datei, damit das flüssig wird.
* Mache ein beispiel, in dem gezeigt wird, dass ein try-block so klein wie möglich sein sollte. und ggf. in eine funktion ausgelagert wird.
* Optional: Definiere aufgabe, in der man eine klasse definiert, die mit `with` funktioniert
* ÜBerarbeite den Text dieser Datei, damit das insgesamt flüssig ist.

[zurück](../TheGoodPractices)