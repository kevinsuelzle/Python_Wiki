# Debugger

Programmieren ist ein komplexer Prozess, der Präzision und Aufmerksamkeit erfordert. Trotzdem sind Fehler beim 
Programmieren allgegenwärtig. Um diese Fehler zu finden, hilft es oft, den Code Schritt für Schritt ablaufen zu lassen,
sodass wir den Programmablauf als Menschen verstehen können. Ein **Debugger** erlaubt einem genau diese Art der 
Codedurchführung. Wir werden in diesem Kapitel sehen, wie man den Debugger nutzen kann.


### Aufgabe: Käferalarm🐞
Schau dir deises [🎦Video](https://youtube.com/shorts/P9ZkTIgsByk?si=FtUJerw9KcRIy9Tx) an und erkläre,
wie der Begriff "Bug" für Fehler in der Informatik entstanden ist. Warum heißt das Entfernen von Fehlern dann "Debugging"?


### Aufgabe: Von diesen sieben Tricks sollt ihr nichts wissen🌶

<iframe width="560" height="315" src="https://www.youtube.com/embed/X3jw1JVNdPE?si=I_RzovjKKbkQVRkC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Schau dir das [Video von Fireship](https://youtu.be/X3jw1JVNdPE?si=qHCernkCvp5gb8dK) an und beantworte die folgenden
Fragen:

* Welche Gründe werden am Anfang des Videos als Gründe für das Auftreten von Fehlern beim Programmieren genannt.
  Sortiere diese Fehler nach der Häufigkeit.
* Welche sieben Tipps gibt das Video, um Fehler zu vermeiden, finden und zu korrigieren?

[Lösung](solution.md#aufgabe-von-diesen-sieben-tricks-sollt-ihr-nichts-wissen)

### Der Debugger

Ein Debugger ist ein wesentliches Werkzeug in der Softwareentwicklung, das Programmierern hilft, den Code Schritt für 
Schritt auszuführen, um Fehler (Bugs) zu finden und zu beheben. Debugger bieten die Möglichkeit, den Zustand eines 
Programms zu einem bestimmten Zeitpunkt zu überprüfen, Variablenwerte zu inspizieren und den Programmfluss zu 
kontrollieren. 

Debugger haben alle ähnliche Funktionen:
* **Haltepunkte setzen**: Erlaubt es dem Entwickler, die Ausführung des Programms an bestimmten Punkten anzuhalten.
* **Schrittweise Ausführung**: Führt das Programm Zeile für Zeile aus, um die Auswirkungen jeder Anweisung zu beobachten.
* **Variablen inspizieren**: Zeigt die aktuellen Werte von Variablen im Programm an.
* **Programmfluss steuern**: Erlaubt es, den Ablauf des Programms zu steuern, beispielsweise durch Fortsetzen der Ausführung oder Rückkehr zu einem früheren Punkt.

Im Folgenden werden wir 3 Varianten den Debugger zu benutzen ansehen:

* Eingebauter Debugger von **VSCode**
* Eingebauter Debugger von **PyCharm**
* Konsolendebugger mit `pdb` 

### Verwendung von `pdb`

Python bietet mit `pdb` einen Debugger, der mit Python direkt mitgeliefert wird. `pdb` ist ein interaktives Tool.

Das `pdb`-Modul (Python Debugger) ermöglicht es, den Code interaktiv zu durchlaufen, Haltepunkte zu setzen und den 
Zustand des Programms zu inspizieren. Dadurch können wir während der Entwicklung Einblick in den Zustand des Programms
erhalten und Befehle Schritt für Schritt ausführen. Das ermöglicht es uns sehr gut nachvollzuziehen, was im Programm 
passiert. 

Hier sind einige grundlegende Befehle:

- `import pdb`: Importiert das pdb-Modul.
- `pdb.set_trace()`: Setzt einen Haltepunkt im Code.
- `c`: Fährt mit der Ausführung fort, bis zum nächsten Haltepunkt.
- `n`: Führt die nächste Zeile aus.
- `s`: Tritt in eine Funktion oder Methode ein.
- `p`: Druckt den Wert eines Ausdrucks.
- `q`: Beendet den Debugger und das Programm.

#### Beispiel zur Nutzung von `pdb`
[45min]
```python
import pdb

def berechne_summe(a, b):
    pdb.set_trace()
    summe = a + b
    return summe

ergebnis = berechne_summe(3, 4)
print(ergebnis)
```

In diesem Beispiel wird `pdb.set_trace()` verwendet, um einen Haltepunkt zu setzen. Wenn das Programm diesen Punkt 
erreicht, wird die Ausführung pausiert und der Benutzer kann mit den pdb-Befehlen den Zustand des Programms 
inspizieren und steuern. 

### Aufgaben
[60min]

### 1. **Haltepunkt setzen**: 🌶️️
Füge in der folgenden Funktion einen Haltepunkt hinzu und führe das Programm aus. 

Untersuche die Werte von `a` und `b`, bevor die Summe berechnet wird.
```python
def addiere(a, b):
    # Füge hier einen Haltepunkt ein
    return a + b

ergebnis = addiere(5, 7)
print(ergebnis)
```

###  2. **Nächste Zeile ausführen**: 🌶️️
Betrachte das folgende Python-Skript. Führe es mit pdb aus und benutze den Befehl n (next), um die Ausführung bis zur 
print-Anweisung Zeile für Zeile zu durchlaufen.
```python 
import pdb

def quadriere(zahl):
    pdb.set_trace()
    ergebnis = zahl * zahl
    return ergebnis

print(quadriere(4))
```

### 3. **In eine Funktion eintreten**: 🌶️️
In dem folgenden Code, tritt mit dem s (step) Befehl in die Funktion berechne_differenz 
ein. Prüfe die Variablen innerhalb der Funktion.
```python
import pdb

def berechne_differenz(x, y):
    return x - y

pdb.set_trace()
ergebnis = berechne_differenz(10, 5)
print(ergebnis)
```

### 4. **Werte ausdrucken**: 🌶️️
Verwende p (print), um den Wert von ergebnis in dem folgenden Programm auszugeben, bevor es mit 
dem c (continue) Befehl fortgesetzt wird.
```python
import pdb

def multipliziere(a, b):
    return a * b

pdb.set_trace()
ergebnis = multipliziere(6, 7)
print(ergebnis)
```

### 5. **Haltepunkte dynamisch setzen**: 🌶️️🌶️️
Anstatt pdb.set_trace() direkt im Code zu verwenden, starte das folgende Programm mit 
dem Python-Interpreter im Debug-Modus (`python -m pdb script.py`). Setze dann einen Haltepunkt bei der Zeile, die die 
Multiplikation ausführt. Führe das Programm bis zu diesem Haltepunkt aus und überprüfe die Werte von x und y.
```python
def multipliziere(x, y):
    ergebnis = x * y
    return ergebnis

ergebnis = multipliziere(3, 3)
print(ergebnis)
```
[Lösungen](solution.md)



## Nutzen von Logs zur Fehlersuche
[60min]

Die meisten Programme, erzeugen sogenannte Logs. Das sind meist Textdateien die während der Programmausführung angelegt
werden und darüber Auskunft geben, welche Abläufe im Programm passiert sind. Geschieht ein Fehler, kann in den Logs
verhältnismäßig einfach nachvollzogen werden, was vorher passiert ist.

Oftmals sind Logs aber nur ein erster Hinweis darauf in welchen Programmteilen bestimmte Fehler passiert sind und welche
Auswirkungen sie auf das Programm hatten. 

Software, die für einen Produktiveinsatz entwickelt wird, sollte immer eine Form von Logging beinhalten.

### Warum ist Logging wichtig?

1. **Fehleridentifikation**: 
    Logging ermöglicht die Erfassung von Fehlern und Ausnahmen zur Laufzeit. Diese Logs bieten wichtige Hinweise zur 
   Fehlerursache.

2. **Verhaltensanalyse**: 
    Durch das Protokollieren von Aktivitäten und Ereignissen kann das Verhalten des Programms verstanden und 
   analysiert werden.

3. **Historische Daten**: 
    Logs bieten eine Historie der Programmausführung, die hilfreich sein kann, um Probleme, die zu einem früheren
   Zeitpunkt aufgetreten sind, zu diagnostizieren.

4. **Leistungsmessung**: 
    Performance-relevante Informationen können geloggt werden, um Engpässe und Leistungsprobleme zu identifizieren.

### Logging in der Praxis

- **Logging-Level**: 
   Verschiedene Logging-Levels (wie INFO, DEBUG, ERROR) ermöglichen es, die Menge und den Detailgrad der 
  Log-Nachrichten zu steuern.

- **Kontextreiche Informationen**: 
   Gute Log-Nachrichten enthalten Kontext, wie Zeitstempel, Ausführungspfad, Variablenwerte usw.

- **Nicht-intrusiv**: 
   Logging ist eine nicht-intrusive Methode, die den normalen Ablauf des Programms nicht unterbricht.

- **Werkzeuge und Bibliotheken**: 
   Es gibt viele Tools und Bibliotheken (Python's `logging`-Modul), die das Logging unterstützen und 
  erleichtern.
