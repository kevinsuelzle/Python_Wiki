$$$ Task 4: Erweiteres Beispiel statt dem jetzigen ausdenken, bei dem eine Globale Variable in einem anderen skript für probleme sorgt.

# Verwendung von Funktionsparametern statt globaler Variablen

## Beispiel

```python
x = 10

def increment():
    global x
    x += 1
```

Anstatt eine globale Variable zu verwenden, sollte die Funktion einen Wert als Argument annehmen und den modifizierten
Wert zurückgeben.

```python
def increment(x):
    return x + 1
```

**Frage**: Warum ist das ein schlechter Stil?

**Antwort**:

- **Beeinträchtigung von Lesbarkeit und Wartbarkeit:**
    
    Globale Variablen können von überall im Code geändert werden, was zu unerwartetem Verhalten und schwer zu findenden Fehlern führen kann.

- **Erschwerte Nachvollziehbarkeit des Datenflusses:** 

    Da ihre Werte an vielen Stellen verändert werden können, ohne dass dies offensichtlich ist, wird der Datenfluss im Programm unklar.

- **Probleme in größeren Projekten:** 

    In umfangreichen Projekten wird die Nachverfolgung der Verwendung und Änderung globaler Variablen fast unmöglich, was die Komplexität unnötig erhöht.

- **Erschwerte Testbarkeit:** 

    Globale Variablen erschweren das isolierte Testen von Codeabschnitten, da Änderungen an ihnen unerwartete Seiteneffekte in anderen Teilen des Programms haben können.

- **Risiko von Seiteneffekten:** 

    Änderungen an globalen Variablen können unerwartete Auswirkungen auf andere Teile des Programms haben, was die Fehlersuche und -behebung erschwert.
[zurück](../TheGoodPractices)
