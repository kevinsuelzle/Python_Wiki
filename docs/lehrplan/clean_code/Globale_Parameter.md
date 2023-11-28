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

**Frage**: Kann es unter diesem Aspekt Funktionen ohne Argumente ([nyladische Funktionen](../Funktionsparameter)) überhaupt geben?

**Antwort**:

- **Nutzung von Umgebungsvariablen:**

    Nyladische Funktionen können auf Umgebungsvariablen zugreifen, die außerhalb der Funktion definiert sind, aber nicht als globale Variablen im Code selbst. Dies ermöglicht den Zugriff auf Konfigurationen oder Systemeigenschaften.

- **Rückgriff auf statische Daten:** 

    Solche Funktionen können auch statische Daten verwenden, die innerhalb ihrer Klasse oder Moduls definiert sind. Diese Daten sind zwar global zugänglich, aber im Kontext der Klasse oder des Moduls gekapselt.

- **Einsatz von Singleton-Mustern:** 

    In objektorientierten Sprachen können nyladische Funktionen Teil eines Singleton-Objekts sein, das globalen Zustand in einer kontrollierten Weise verwaltet.

- **Verwendung von Diensten oder Ressourcen:** 

    Sie können auf externe Dienste oder Ressourcen zugreifen, wie z.B. Datenbankverbindungen oder Dateisysteme, die außerhalb des Funktionsumfangs definiert sind.

- **Erzeugung von Daten basierend auf internem Zustand:** 

    In einigen Fällen können nyladische Funktionen Daten generieren oder verarbeiten, die auf ihrem internen Zustand basieren, wie z.B. ein Zufallszahlengenerator.

- **Ausführung von Operationen ohne externe Abhängigkeiten:** 

    Manchmal führen solche Funktionen Operationen aus, die keine externen Daten benötigen, wie das Zurücksetzen eines internen Zustands oder das Ausführen einer festgelegten Routine.

**Aufgabe**: Geben sie Beispiele von nyladischen Funktionen.

**Aufgabe**: Schreiben sie eine sinnvolle Funktion, die ohne Parameter auskommt.

[zurück](../TheGoodPractices)
