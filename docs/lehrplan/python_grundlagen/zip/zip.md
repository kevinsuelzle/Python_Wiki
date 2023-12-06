# Einführung in die `zip()`-Funktion in Python

Die `zip()`-Funktion in Python ist ein nützliches Werkzeug, um mehrere iterierbare Objekte – wie Listen oder Tupel –
parallel zu durchlaufen. Sie fasst die Elemente mehrerer Iteratoren zu Tupeln zusammen und gibt einen Iterator über
diese Tupel zurück.

## Grundlegende Verwendung von `zip()`

Die einfachste Verwendung von `zip()` besteht darin, zwei oder mehr Listen (oder andere Iterables) zu kombinieren:

```python
zahlen = [1, 2, 3]
buchstaben = ['a', 'b', 'c']
resultat = zip(zahlen, buchstaben)
print(list(resultat))  # Gibt [(1, 'a'), (2, 'b'), (3, 'c')] aus
```

In diesem Beispiel werden die Elemente der beiden Listen `zahlen` und `buchstaben` zu Paaren zusammengefasst.

## Vorteile der `zip()`-Funktion

1. **Einfaches Iterieren über mehrere Listen**: `zip()` ermöglicht es, mehrere Listen gleichzeitig zu durchlaufen, was
   besonders bei Operationen nützlich ist, die Elemente aus mehreren Quellen benötigen.

2. **Kurzer und lesbarer Code**: Der Einsatz von `zip()` führt oft zu kürzerem und leichter verständlichem Code im
   Vergleich zu herkömmlichen Iterationsmethoden.

3. **Flexibilität**: `zip()` funktioniert mit jedem iterierbaren Objekt und ist nicht auf Listen beschränkt. Sie können
   damit auch Tupel, Strings, Sets oder Dictionaries kombinieren.

4. **Dynamische Handhabung**: Wenn die übergebenen Iterables unterschiedlich lang sind, wird `zip()` beendet, sobald das
   kürzeste Iterable erschöpft ist.

## Erweiterte Anwendungen von `zip()`

- **Zip mit unterschiedlich langen Iterables**: Wenn man `zip()` mit Iterables unterschiedlicher Länge verwendet, werden
  die überschüssigen Elemente des längeren Iterables ignoriert.

```python
zahlen = [1, 2, 3, 4]
buchstaben = ['a', 'b', 'c']
resultat = zip(zahlen, buchstaben)
print(list(resultat))  # Gibt [(1, 'a'), (2, 'b'), (3, 'c')] aus
```

- **Verwendung von `zip()` mit mehr als zwei Iterables**: Es ist möglich, mehr als zwei Iterables zu kombinieren.

```python
zahlen = [1, 2, 3]
buchstaben = ['a', 'b', 'c']
symbole = ['!', '@', '#']
resultat = zip(zahlen, buchstaben, symbole)
print(list(resultat))  # Gibt [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')] aus
```

- **Umkehren des Zippens**: Mit `zip(*zippped_list)` kann ein gezipptes Iterable wieder in seine einzelnen Bestandteile
  zerlegt werden.

```python
gepaart = [(1, 'a'), (2, 'b'), (3, 'c')]
zahlen, buchstaben = zip(*gepaart)
print(list(zahlen))  # Gibt [1, 2, 3] aus
print(list(buchstaben))  # Gibt ['a', 'b', 'c'] aus
```

## Komplexes Beispiel mit der `zip()`-Funktion in Python

### Szenario: Berechnung der Gesamtpunkte in einem Wettbewerb

Stellen wir uns vor, wir haben einen Wettbewerb, bei dem Teilnehmer in verschiedenen Kategorien Punkte sammeln. Am Ende
möchten wir die Gesamtpunktzahl jedes Teilnehmers berechnen.

Wir haben zwei Listen: eine mit den Namen der Teilnehmer und eine weitere mit Listen von Punkten, die jeder Teilnehmer
in den einzelnen Kategorien gesammelt hat. Unser Ziel ist es, die Gesamtpunktzahl für jeden Teilnehmer zu berechnen.

### Schritt-für-Schritt-Anleitung

- **Daten vorbereiten**:

```python
teilnehmer = ["Anna", "Bernd", "Carla"]
punkte = [[10, 20, 30], [15, 25, 35], [10, 30, 50]]
```

- **Verwendung von `zip()`**:
  Wir verwenden `zip()`, um die Namen der Teilnehmer mit ihren entsprechenden Punktelisten zu kombinieren.

```python
kombiniert = zip(teilnehmer, punkte)
```

- **Berechnung der Gesamtpunktzahl**:
  Für jeden Teilnehmer addieren wir die Punkte aus allen Kategorien, um die Gesamtpunktzahl zu ermitteln.

```python
gesamtpunktzahl = {name: sum(punkte) for name, punkte in kombiniert}
print(gesamtpunktzahl)
```

Diese Zeile erstellt ein Dictionary, in dem jeder Teilnehmername einem Gesamtpunktwert zugeordnet ist.

### Alternative Ansätze

- **Traditionelle for-Schleifen**:
  Anstelle von List Comprehensions und `zip()` hätten wir auch traditionelle for-Schleifen verwenden können:

```python
gesamtpunktzahl = {}
for i in range(len(teilnehmer)):
    gesamtpunktzahl[teilnehmer[i]] = sum(punkte[i])
```

Dieser Ansatz ist etwas länger und weniger Python-idiomatisch, erreicht aber dasselbe Ergebnis.

- **Einsatz von `enumerate()`**:
  Eine weitere Alternative wäre die Verwendung von `enumerate()`, wenn wir sowohl den Index als auch den Wert während
  der Iteration benötigen:

```python
gesamtpunktzahl = {}
for index, name in enumerate(teilnehmer):
    gesamtpunktzahl[name] = sum(punkte[index])
```

In diesem Beispiel sehen wir, wie `zip()` in Kombination mit List Comprehensions und Dictionary Comprehensions verwendet
werden kann, um eine elegante und effiziente Lösung für ein praktisches Problem zu bieten. Es zeigt, wie `zip()` dazu
beiträgt, den Code lesbar und prägnant zu halten, insbesondere bei der Handhabung von parallelen Datenstrukturen.

## Zusammenfassung

Die `zip()`-Funktion ist ein nützliches Werkzeug in Python, das effiziente und lesbare Lösungen für häufige Probleme
beim parallelen Durchlaufen von mehreren Iterables bietet. Von der einfachen Paarung von Listen bis hin zu komplexeren
Iterationen über mehrere Datenstrukturen hinweg ist `zip()` eine vielseitige Funktion, die in vielen Situationen
nützlich sein kann.

# Aufgaben
[50min]

### 1: Einführung in `zip`

Schreibe ein Python-Programm, das zwei Listen `liste1` und `liste2` nimmt und sie mithilfe von `zip` zusammenführt.

### 2: Liste der Tupel

Erstelle eine Liste von Tupeln aus den Elementen von `liste1` und `liste2` unter Verwendung von `zip`.

### 3: Elementweise Addition

Nimm zwei Listen von Ganzzahlen und addiere sie elementweise mithilfe von `zip`.

### 4: Parallele Zuweisung

Verwende `zip`, um Werte aus zwei Listen `namen` und `alter` parallel zuzuweisen.

### 5: Elemente filtern

Schreibe eine Funktion, die mithilfe von `zip` alle geraden Zahlen aus zwei Listen `liste1` und `liste2` filtert.

### 6: Dictionary erstellen

Erstelle ein Dictionary aus zwei Listen `schlüssel` und `werte` mithilfe von `zip`.

### 7: Sortierte Paare

Nimm zwei Listen von Zahlen und verwende `zip`, um Paare zu erstellen und sie nach der Summe der Paare zu sortieren.

### 8: Zusammenführen von Wörtern

Gegeben sind zwei Listen von Strings `adjektive` und `nomen`. Verwende `zip`, um alle möglichen Kombinationen von
Adjektiven und Nomen zu erstellen.

### 9: Elemente multiplizieren

Erstelle eine Liste, in der jedes Element das Produkt der entsprechenden Elemente aus `liste1` und `liste2` ist, indem
du `zip` verwendest.

### 10: Elemente vergleichen

Schreibe eine Funktion, die mithilfe von `zip` die Unterschiede zwischen zwei Listen `liste1` und `liste2` ermittelt und
zurückgibt.

### 11: Maximaler Wert pro Position

Gegeben sind zwei Listen von Zahlen `liste1` und `liste2`. Verwende `zip`, um eine Liste der maximalen Werte pro
Position zu erstellen.

### 12: Mittelwert berechnen

Berechne den Mittelwert von zwei Listen `liste1` und `liste2`, indem du `zip` und eine Schleife verwendest.

### 13: Elemente gruppieren

Gegeben ist eine Liste von Tupeln. Verwende `zip`, um die Tupel nach ihrem ersten Element zu gruppieren.

### 14: Teile und erobere

Nimm eine Liste von Zahlen `zahlen`. Verwende `zip`, um die Liste in zwei Teillisten aufzuteilen - eine für gerade und
eine für ungerade Zahlen.

### 15: Prüfung von Bedingungen

Schreibe eine Funktion, die mithilfe von `zip` überprüft, ob die Elemente zweier Listen `liste1` und `liste2` eine
bestimmte Bedingung erfüllen.

### 16: Entfernen von Duplikaten

Gegeben ist eine Liste von Elementen. Verwende `zip`, um Duplikate aus der Liste zu entfernen.

### 17: Anzahl der Übereinstimmungen zählen

Erstelle eine Funktion, die mithilfe von `zip` die Anzahl der Übereinstimmungen zwischen zwei Listen `liste1`
und `liste2` zählt.

### 18: Slices erstellen

Nimm eine Liste von Zahlen `zahlen` und verwende `zip`, um Slices dieser Liste zu erstellen, die bestimmten Bedingungen
entsprechen.

### 19: Elemente tauschen

Vertausche die Plätze der Elemente in den Listen `liste1` und `liste2` mithilfe von `zip`.

### 20: Verschlüsselung mit `zip`

Erstelle eine einfache Verschlüsselungsfunktion, die Text mithilfe von `zip` verschlüsselt und dann entschlüsselt.

[Lösungen](solutions.md#lösungen)

# Komplex-Aufgaben
[75min]

### Aufgabe 1: Datenanalyse mit `zip` und Bedingungen

Gegeben sind zwei Listen `temperaturen` und `städte`, wobei `temperaturen` die aktuellen Temperaturen in verschiedenen
Städten enthält und `städte` die zugehörigen Stadtnamen. Schreibe ein Programm, das die heißeste Stadt (mit der höchsten
Temperatur) und die kälteste Stadt (mit der niedrigsten Temperatur) identifiziert und ausgibt.

### Aufgabe 2: Wörter zählen mit `zip` und Dictionaries

Gegeben ist ein Text in Form eines Strings. Schreibe eine Funktion, die die Anzahl der Vorkommen jedes Worts im Text
zählt und ein Dictionary zurückgibt, in dem die Wörter als Schlüssel und die Anzahl der Vorkommen als Werte gespeichert
sind. Verwende `zip`, um den Text in Wörter aufzuteilen und die Zählung durchzuführen.

### Aufgabe 3: Multi-dimensionale Datenanalyse

Du erhältst eine Liste von Schülern, die in verschiedenen Fächern Noten erhalten haben. Jeder Schüler ist durch seinen
Namen und eine Liste von Noten in verschiedenen Fächern repräsentiert. Schreibe ein Programm, das den Durchschnitt für
jedes Fach berechnet und die Namen der Schüler ausgibt, deren Durchschnittsnote unter einem bestimmten Schwellenwert
liegt. Verwende `zip`, um die Daten effizient zu verarbeiten.

Diese komplexeren Aufgaben erfordern die Anwendung verschiedener Konzepte, die in den vorherigen Aufgaben behandelt
wurden, und demonstrieren die Flexibilität und Leistungsfähigkeit der `zip`-Funktion in Python.