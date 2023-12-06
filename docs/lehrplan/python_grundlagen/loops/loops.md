# Schleifen

In der Programmierung sind **Schleifen** ein grundlegendes Konzept, welches verwendet wird, um einen bestimmten Block
von
Anweisungen wiederholt auszuführen. Man sagt auch, dass Schleifen über etwas iterieren. Dies kann zum Beispiel ein
Zahlenbereich sein oder auch eine Menge an Elementen in einer Liste.

## Die Bedeutung von Schleifen

Schleifen sind ein wesentlicher Bestandteil der Programmierung und haben eine breite Anwendung in verschiedenen
Situationen:

1. **Wiederholung:** Schleifen ermöglichen es, einen Satz von Anweisungen mehrmals auszuführen, bis eine bestimmte
   Bedingung erfüllt ist oder solange eine Bedingung wahr ist.

2. **Datenverarbeitung:** In vielen Fällen müssen Sie alle Elemente einer Datenstruktur (wie eine Liste oder ein Array)
   durchgehen und auf jedes Element eine bestimmte Operation anwenden. Schleifen erleichtern diese Iteration und
   Verarbeitung.

3. **Benutzereingabe:** Schleifen ermöglichen eine dauerhafte Interaktion mit Benutzern, indem sie auf Eingaben warten
   und je nach Eingabe unterschiedliche Aktionen ausführen.

## Arten von Schleifen in Python

In Python gibt es zwei Hauptarten von Schleifen:

1. **`for`-Schleife:** Die `for`-Schleife wird verwendet, um über eine Sequenz (z. B. eine Liste, ein Tupel oder eine
   Zeichenkette) zu iterieren und den Codeblock für jedes Element in der Sequenz auszuführen.

2. **`while`-Schleife:** Die `while`-Schleife wird so lange ausgeführt, wie eine angegebene Bedingung wahr ist. Sie wird
   verwendet, wenn die Anzahl der Schleifendurchläufe im Voraus nicht bekannt ist.

## Beispiel einer `for`-Schleife

Hier ist ein einfaches Beispiel für eine `for`-Schleife in Python:

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
for frucht in fruechte:
    print(frucht)
```

Diese Schleife iteriert über die Liste `fruechte` und gibt jede Frucht nacheinander aus. Für jeden Durchlauf der
Schleife nimmt `frucht` ein anderes Element der Liste an und steht im Schleifenkörper zur Verfügungn.

## Beispiel einer `while`-Schleife

Hier ist ein einfaches Beispiel für eine `while`-Schleife in Python:

```python
zaehler = 0
while zaehler < 5:
    print("Schleife Nr.", zaehler)
    zaehler += 1
```

Diese Schleife wird so lange ausgeführt, wie `zaehler` kleiner als 5 ist, und gibt die Nachricht "Schleife Nr." gefolgt
von der aktuellen Schleifennummer aus.

Schleifen sind ein mächtiges Werkzeug in der Programmierung und ermöglichen die Automatisierung von Aufgaben und die
effiziente Verarbeitung von Daten. Es ist wichtig, Schleifen mit Bedacht zu verwenden, um Endlosschleifen und
unerwünschte Ergebnisse zu vermeiden.

# Einführung in `for`-Schleifen

Eine `for`-Schleife in Python ist eine Kontrollstruktur, die verwendet wird, um über eine Sequenz von Elementen (z. B.
eine Liste, ein Tupel oder eine Zeichenkette) zu iterieren und eine Gruppe von Anweisungen für jedes Element in der
Sequenz auszuführen. `for`-Schleifen sind sehr nützlich, um Aufgaben zu automatisieren, die eine wiederholte
Verarbeitung von Daten erfordern.

## Eigenschaften von `for`-Schleifen

Hier sind einige wichtige Eigenschaften von `for`-Schleifen in Python:

1. **Klare Struktur:** `for`-Schleifen haben eine klare und gut definierte Struktur, die die Wiederholung von Code
   erleichtert.

2. **Durchlaufen einer Sequenz:** Sie iterieren über eine Sequenz von Elementen, eins nach dem anderen, bis alle
   Elemente durchlaufen wurden.

3. **Feste Anzahl von Durchläufen:** Im Gegensatz zu `while`-Schleifen haben `for`-Schleifen eine feste Anzahl von
   Durchläufen, die von der Länge der Sequenz bestimmt werden.

4. **Automatische Aktualisierung:** Der Index oder das Element, über das iteriert wird, wird automatisch aktualisiert,
   wodurch die Wahrscheinlichkeit von Endlosschleifen verringert wird.

## Syntax einer `for`-Schleife

Die grundlegende Syntax einer `for`-Schleife in Python lautet:

```python
for element in sequenz:
# Anweisungen, die für jedes Element ausgeführt werden
```

- `element`: Eine Variable, die den aktuellen Wert aus der Sequenz repräsentiert.
- `sequenz`: Die Sequenz, über die iteriert wird (z. B. eine Liste, ein Tupel, eine Zeichenkette).

## Beispiel einer `for`-Schleife

Hier ist ein einfaches Beispiel für eine `for`-Schleife, die über eine Liste von Zahlen iteriert und sie ausgibt:

```python
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print(zahl)
```

In diesem Beispiel durchläuft die `for`-Schleife die Liste `zahlen` und gibt jede Zahl nacheinander aus.

## Anwendung von `for`-Schleifen

`for`-Schleifen sind äußerst vielseitig und werden in verschiedenen Anwendungsfällen eingesetzt, wie:

- Iteration über Daten in Listen, Tupeln oder Zeichenketten.
- Verarbeitung von Elementen in Datenstrukturen wie Listen und Dictionaries.
- Ausführung von Code für eine feste Anzahl von Durchläufen.
- Automatisierung von Aufgaben, bei denen eine wiederholte Aktion erforderlich ist.

## Aufgaben
[25min]

### 1. Zählen
Schreibe eine `for`-Schleife, die die Zahlen von 1 bis 10 ausgibt.
### 2. Städtetrip
Erstelle eine Liste von Städten und verwenden Sie eine `for`-Schleife, um jede Stadt auszugeben.
### 3. Summierung
Schreibe eine `for`-Schleife, die die Summe aller Zahlen von 1 bis 100 berechnet.
### 4. Längster Name
Erstelle eine Liste von Namen und verwenden Sie eine `for`-Schleife, um den längsten Namen in der Liste zu
   finden
### 5. Quadratzahlen
Schreibe eine `for`-Schleife, die die Quadratzahlen von 1 bis 10 ausgibt.
### 6. Suchen einer Frucht
Erstelle eine Liste von Früchten und verwenden Sie eine `for`-Schleife, um nach einer bestimmten Frucht zu
   suchen und sie auszugeben, wenn sie gefunden wird.
### 7. Verdreht
Schreibe eine `for`-Schleife, die die Buchstaben eines Wortes in umgekehrter Reihenfolge ausgibt.
### 8. Fakultät
Schreibe eine `for`-Schleife, die die Fakultät (n!) einer gegebenen Zahl `n` berechnet.
### 9. Thermometer für Amerikaner 
Erstelle eine Liste von Temperaturen in Celsius und verwenden Sie eine `for`-Schleife, um sie in Fahrenheit
    umzuwandeln und auszugeben.
### 10. Vokale
Schreibe eine `for`-Schleife, die die Anzahl der Vokale in einem gegebenen Wort zählt.
### 11. Häufigkeit
Schreibe eine `for`-Schleife, die einen Text durchläuft und zählt, wie oft ein bestimmtes Wort in diesem Text
    vorkommt.

[Lösungen](solutions.md#for-schleifen)

# Einführung in While-Schleifen in Python

While-Schleifen sind eine grundlegende Kontrollstruktur in Python, die es ermöglicht, einen Block von Anweisungen
wiederholt auszuführen, solange eine bestimmte Bedingung erfüllt ist. Sie sind besonders nützlich, wenn die Anzahl der
Wiederholungen nicht im Voraus bekannt ist. Dies ist zum Beispiel bei einer wiederholten Eingabeaufforderung an den
Nutzer der Fall.

## Eigenschaften von While-Schleifen

1. **Bedingungsabhängig**: Die Schleife wird fortgesetzt, solange die Bedingung wahr (`True`) ist.

2. **Initialisierung notwendig**: Vor der Schleife sollte die Variable, die in der Bedingung verwendet wird,
   initialisiert werden.

3. **Aktualisierung innerhalb der Schleife**: Es ist wichtig, die Bedingungsvariable innerhalb der Schleife zu
   aktualisieren, um eine endlose Schleife zu vermeiden.

4. **Flexibilität**: While-Schleifen sind flexibel und können für eine Vielzahl von Situationen verwendet werden,
   insbesondere wenn die Anzahl der Durchläufe nicht bekannt ist.

5. **Risiko endloser Schleifen**: Wenn die Bedingung nie falsch wird, entsteht eine endlose Schleife, was zu Problemen
   führt (z.B. das Programm friert ein).

6. **Break-Statement**: Durch das `break`-Statement kann eine While-Schleife vorzeitig beendet werden, selbst wenn die
   Bedingung noch wahr ist.

7. **Continue-Statement**: Mit `continue` kann der aktuelle Durchlauf der Schleife übersprungen und zur
   Bedingungsüberprüfung zurückgekehrt werden.

## Beispiel

```python
# Zählt von 1 bis 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Wichtig, um die Schleife zu beenden
```

Natürlich können wir auch sehr einfach Endlosschleifen erzeugen in dem wir die Bedingung einfach immer auf `True`
lassen:

```python
# Frage endlos nach Nutzereingaben
while True:
    eingabe = input()
    # Mache etwas mit der Nutzereingabe
```

Wie wir die Endlosschleife doch verlassen können, lernen wir dann gleich.

## Aufgaben
[25min]

### 1. Zählen
Schreibe eine While-Schleife, die Zahlen von 1 bis 10 ausgibt.
### 2. Gerade Zahlen
Verwende eine While-Schleife, um alle geraden Zahlen zwischen 1 und 20 auszugeben.
### 3. Liste von hinten ausgeben
Erstelle eine Schleife, die eine Liste von Zahlen rückwärts ausgibt (z.B. von 5 bis 1).
### 4. Die ersten Fünf
Schreibe eine Schleife, die die ersten 5 Elemente einer gegebenen Liste ausgibt.
### 5. Summe von 1 bis 100
Nutze eine While-Schleife, um die Summe der Zahlen von 1 bis 100 zu berechnen.
### 6. Fast endlose Schleife
Erstelle eine Schleife, die solange Zufallszahlen zwischen 1 und 10 generiert und ausgibt, bis die Zahl 5
   erscheint.
### 7. Fakultät
Verwende eine While-Schleife, um die Fakultät einer gegebenen Zahl zu berechnen.
### 8. Wiederholung nach Länge
Schreibe eine Schleife, die eine gegebene Zeichenkette so oft ausgibt, wie ihre Länge beträgt.
### 9. Fibonacci
Nutze eine While-Schleife, um die Fibonacci-Reihe bis zum zehnten Element zu berechnen. Recherchiere, was die
Fibonacci-Reihe ist.
### 10. Stopp-Bedingung
Erstelle eine Schleife, die eine Liste durchläuft und bei Erreichen eines bestimmten Wortes (z.B. "
    Stopp") beendet wird.

[Lösungen](solutions.md#while-schleifen)

# Vorzeitiges Abbrechen einer Schleife

In vielen Fällen sucht man einfach einen Wert in einem Bereich oder ein bestimmtes Element in einer List. Sobald man
dieses gefunden hat, kann man die Schleife eigentlich abbrechen. Dafür nutzt man das Keyword `break`:

```python
for i in range(0, 10):
    if i == 5:
        break

    print(i)
```

Dieser Code gibt folgendes aus:

```bash
0
1
2
3
4
```

Sobald die Bedingung `i == 5` wahr wird, sorgt `break` dafür, dass wir die Schleifen verlassen. Damit sparen wir uns 5
weitere Durchläufe. Bei kompexen Problemstellungen kann man damit sehr viel Zeit und damit auch Energie sparen.

Auf der anderen Seite gibt es aber auch Fälle in denen man nicht die ganze Schleife beenden will, sondern nur den
aktuellen Durchlauf. Dafür nutzt man das Keyword `continue`.

```python
for i in range(0, 10):
    if i != 5:
        continue

    print(i)
```

Im Gegesatz dazu ist die Ausgabe hier:

```bash
5
```

Wieso? Für jeder Zahl zwischen 0 und 10 wird überprüft, ob diese Zahl ungleich 5 ist. Ist sie ungleich 5, springen wir
direkt zum nächsten Durchlauf. Nur für den Fall, das die Zahl gleich 5 ist, erreichen wir die print-Funktion überhaupt.

Sehr häufig wird break in Kombination mit while-Schleifen verwendet. Wieso? Weil es sehr einach ist damit
Endlosschleifen zu erzeugen, die man unter bestimmten Bedinungen beenden will.

Zum Beispiel:

```python
while True:
    eingabe = input()
    if eingabe == "C":
        break

    # irgendwas mit der Eingabe machen
```

Durch `while True:` läuft diese Schleife theoretisch endlos lange, weil die Bedingung immer wahr ist. Bei jedem
Schleifen durchlauf wird der Nutzer nach einer Eingabe gefragt. Sobald der Nutzer "C" eingibt, wird die Schleife durch
den Befehl `break` verlassen und das Programm kann normal weiterlaufen.

## Else-Zweig bei While- und For-Schleifen in Python

In Python können sowohl `while`- als auch `for`-Schleifen mit einem optionalen `else`-Zweig versehen werden. Dieser Teil
der Schleife wird ausgeführt, wenn die Schleife auf normale Weise beendet wird, d.h., nicht durch ein `break`-Statement
unterbrochen wird.

### Else-Zweig bei For-Schleifen

Ähnlich wie bei `while`-Schleifen wird der `else`-Zweig einer `for`-Schleife ausgeführt, wenn die Schleife alle Elemente
der Sequenz durchlaufen hat, ohne durch ein `break`-Statement unterbrochen zu werden.

**Beispiel:**

```python
for i in range(1, 5):
    print(i)
else:
    print("Die Schleife ist regulär beendet worden")
```

Hier wird der `else`-Zweig ausgeführt, da die Schleife alle Elemente der Sequenz durchläuft.

### Else-Zweig bei While-Schleifen

Der `else`-Zweig einer `while`-Schleife wird ausgeführt, nachdem die Bedingung der Schleife zu `False` wird. Wenn die
Schleife durch ein `break`-Statement verlassen wird, wird der `else`-Zweig nicht ausgeführt.

**Beispiel:**

```python
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("Die Schleife ist regulär beendet worden")
```

In diesem Beispiel wird der `else`-Zweig ausgeführt, da die Schleife durch das Erreichen des Endes der
Schleifenbedingung beendet wird.

## Anwendungsfälle

- **Suchoperationen**: Der `else`-Zweig kann nützlich sein, um nach der Durchführung einer Suchoperation in einer
  Schleife eine Meldung auszugeben, falls das gesuchte Element nicht gefunden wurde.
- **Validierung**: Bei Validierungsprozessen kann der `else`-Zweig verwendet werden, um zu bestätigen, dass keine
  Bedingungen verletzt wurden.

## Wichtig zu wissen

- Der `else`-Zweig wird nur dann ausgeführt, wenn die Schleife nicht durch ein `break`-Statement verlassen wird.
- Er ist optional und wird nicht häufig verwendet, aber in bestimmten Situationen kann er den Code klarer und
  verständlicher machen.

# Komplex-Aufgaben

[60min]

## Aufgabe 1: Benutzerdefinierte Passwortüberprüfung

Schreibe ein Programm, das den Benutzer zur Eingabe eines Passworts auffordert. Das Passwort muss bestimmte Kriterien
erfüllen (z.B. mindestens 8 Zeichen lang, enthält sowohl Zahlen als auch Buchstaben). Das Programm soll dem Benutzer
mitteilen, ob das eingegebene Passwort gültig ist oder nicht. Wenn das Passwort nicht gültig ist, soll das Programm
spezifizieren, welche Kriterien nicht erfüllt wurden.

## Aufgabe 2: Textbasierter Quiz

Entwickle ein kleines Quizspiel. Das Programm stellt dem Benutzer fünf verschiedene Fragen, auf die er antworten muss.
Für jede richtige Antwort erhält der Benutzer einen Punkt. Nachdem alle Fragen beantwortet wurden, zeigt das Programm
die Gesamtpunktzahl und eine entsprechende Bewertung (z.B. "Anfänger", "Fortgeschritten", "Experte") basierend auf der
erreichten Punktzahl.

## Aufgabe 3: Einfacher Zahlenraten

Erstelle ein Spiel, bei dem der Benutzer versuchen muss, eine zufällig generierte Zahl zwischen 1 und 100 zu erraten.
Nach jeder Eingabe gibt das Programm an, ob die geratene Zahl zu hoch oder zu niedrig ist. Der Benutzer hat eine
begrenzte Anzahl von Versuchen (z.B. 10). Nach dem Spiel gibt das Programm an, ob der Benutzer gewonnen hat und wie
viele Versuche benötigt wurden.

## Aufgabe 4: Bestellung in einem virtuellen Café

Simuliere ein einfaches Bestellsystem für ein Café. Das Programm listet verschiedene Getränke und Speisen mit ihren
Preisen auf. Der Benutzer kann Artikel auswählen und die gewünschte Menge angeben. Das Programm führt eine laufende
Summe der Bestellung. Nachdem der Benutzer seine Auswahl abgeschlossen hat, zeigt das Programm die Gesamtsumme der
Bestellung an und fragt, ob der Benutzer bar oder mit Karte zahlen möchte.

[Lösungen](solutions.md#komplex-aufgaben)