
# Variablen und Datentypen

In diesem Abschnitt lernen wir die Grundlagen von Variablen und verschiedenen Datentypen in Python kennen. Variablen 
sind wie Behälter, in denen wir Daten speichern können, während Datentypen die Art der Daten bestimmen, die in diesen 
Variablen gespeichert werden können.

## Bedeutung von Variablen in der Programmierung

Variablen sind ein unverzichtbarer Bestandteil der meisten Programmiersprachen, einschließlich Python. Sie erfüllen
mehrere wichtige Funktionen:

1. **Daten speichern**: 
   Variablen dienen als Speicherorte im Arbeitsspeicher eines Computers, in denen Daten gespeichert werden können. 
   Diese Daten können Zahlen, Texte, Listen, Objekte oder andere Datentypen sein. 

2. **Lesbarkeit und Wartbarkeit**: 
   Variablen helfen, den Code verständlicher zu machen. Durch sinnvolle Namen wird der Zweck des Codes klarer, was die 
   Wartung und Fehlerbehebung vereinfacht.

3. **Berechnungen durchführen und Ergebnisse speichern**: 
   Variablen ermöglichen die Durchführung von Berechnungen mit gespeicherten Werten. So können beispielsweise 
   mathematische Operationen ausgeführt und das Ergebnis in einer anderen Variablen gespeichert werden.

4. **Daten wiederverwenden**: 
   Variablen werden eingesetzt, um Daten in verschiedenen Teilen eines Programms zu nutzen. 

5. **Speichern von Zuständen**: 
   In komplexeren Anwendungen dienen Variablen dazu, den Zustand einer Anwendung zu speichern und zu verwalten. 
   Beispiele hierfür sind der Login-Status eines Nutzers oder die Anzahl der Artikel in einem Warenkorb.

Variablen sind somit essenziell für die Erstellung flexibler, effizienter und verständlicher Programme und bilden die 
Grundlage für fast alle Operationen und Logiken in der Programmierung.


## Variablen

Eine Variable in Python kann erstellt werden, indem man ihr einen Namen gibt und 
ihr einen Wert zuweist.

**Beispiel:**
```python
meine_variable = 10
alter = 23
Geburtsjahr = 1940
willkommens_text = "Hey du!"
```

### Namenskonventionen: 

- Variablennamen sollten klar und beschreibend sein. In Python verwenden wir oft Snake-Case, 
bei dem Wörter durch Unterstriche getrennt werden (z.B. `meine_variable`).
- Variablennamen dürften nicht mit einer Zahl anfangen und keine Sonderzeichen außer dem Unterstrich enhalten

Kurze Variablennamen sind nur in absoluten Ausnahmefällen zu verwenden, z.B. als Laufvariable in einer Schleife. Es
kostet keine Ressourcen und kein Geld aussagekräftige Variablen zu nutzen. 

Eine Variable `a` könnte alles sein, während die Variable `zinssatz` recht sicher ein Zinssatz darstellen wird.

## Datentypen

In Python gibt es verschiedene Datentypen, aber hier konzentrieren wir uns auf die grundlegendsten.

### Integers (Ganzzahlen):
Integers repräsentieren ganze Zahlen, positiv oder negativ, ohne Dezimalstellen. 

Möchte man andere Datentypen in Integers umwandeln, nutzt man die `int`-Funtkion, wie wir unten im Beispiel sehen 
können.

Beispiel:

```python
alter = 30
anzahl_der_aepfel = -3
zahl_von_zeichenkette = int("20")
```

### Floats (Gleitkommazahlen):

Dezimalzahlen werden durch den Datentyp `float` dargestellt und sind im IEEE 754 Format codiert. Beim Umgang mit floats
kann es zu Ungenauigkeiten kommen, da sich nicht alle Dezimalzahlen perfekt darstellen lassen. Das sollte aber hier
für uns noch keine große Rolle spielen.

Beispiel:

```python
preis = 19.99
temperatur = -2.5
floaty = float(2)
```

#### Aufgaben / Diskussionen:
1. Diskutiert, für welche Anwendungen float und integer jeweils besser geeignet sind und wo es keine Rolle spielt!
2. Kann man mit Fließkommazahlen jede Dezimalzahl darstellen? Begründet eure Antworten.

### Booleans (Boolesche Werte):

Booleans repräsentieren nur zwei Werte: True (wahr) oder False (falsch). 

Sie sind sehr nützlich in Bedingungen und Schleifen, da sie das zum Beispiel das Ergebnis von Vergleichen sind
(später mehr dazu).

Ein anderer praktischer Anwendungsfall ist die Nutzung als 'flag', ob zum Beispiel jemand Student ist oder nicht.

Beispiel:

```python
ist_student = True
ist_sonnig = False
```

Von Booleans werden wir um Laufe der Woche noch mehr hören und sie auch schon direkt in unserem eigenen Programm nutzen.

### Strings (Zeichenketten):
Strings werden verwendet, um Text zu speichern. In Python gibt es eine Vielzahl von Funktionen und Methoden, die es
erlauben Strings zu verarbeiten. Strings in Python sind Unicode, das heißt so ziemlich jedes Zeichen, was es gibt kann
gespeichert werden, auch Emojis zum Beipiel!


###  Eigenschaften

1. **Definition**: 
   - Ein String ist eine unveränderliche (immutable) Sequenz von Zeichen.
   - Strings werden in einfachen (`'...'`), doppelten (`"..."`) oder dreifachen (`'''...'''` oder `"""..."""`) 
   Anführungszeichen definiert.

2. **Unveränderlichkeit**: 
   - Der Inhalt eines Strings kann nach seiner Erstellung nicht mehr verändert werden.
   - Veränderungen erzeugen immer einen neuen String.

3. **Zugriff und Slicing**: 
   - Zugriff auf einzelne Zeichen über Indizes (beginnend mit 0).
   - Unterstützt Slicing für das Extrahieren von Teilstrings (`"hello"[1:3] # "el"`).

4. **Escape-Zeichen**: 
   - Beinhaltet Escape-Zeichen wie `\n` (neue Zeile) und `\t` (Tabulator).

5. **String-Operationen**: 
   - Bietet Operationen wie Konkatenation, Repetition und Methoden für Transformation, Suche, Ersatz usw.

6. **Formatierung**: 
   - Es gibt mehrere Möglichkeiten zur Formatierung, einschließlich `format()` und f-Strings (seit Python 3.6).

**Beispiel**:

```python
name = "Anna"
begruessung = 'Hallo Welt!'
zahl_als_text = "1234"
```

Strings sind für uns sehr wichtig. Der Datentyp ist sehr universell und typischerweise werden jegliche Eingaben und
Ausgaben eine Art String sein.

Eine kleine Übersicht an häufig verwendeten Funktionen:

| Operation             | Beschreibung                                                                                  | Beispiel                       |
|-----------------------|-----------------------------------------------------------------------------------------------|--------------------------------|
| `s.upper()`           | Konvertiert alle Zeichen des Strings `s` in Großbuchstaben.                                   | `'hello'.upper() # 'HELLO'`    |
| `s.lower()`           | Konvertiert alle Zeichen des Strings `s` in Kleinbuchstaben.                                  | `'Hello'.lower() # 'hello'`    |
| `s.strip()`           | Entfernt führende und abschließende Leerzeichen im String `s`.                                | `'  hello '.strip() # 'hello'` |
| `s.startswith(sub)`   | Überprüft, ob der String `s` mit dem Unterstring `sub` beginnt.                               | `'Hello'.startswith('He')`     |
| `s.endswith(sub)`     | Überprüft, ob der String `s` mit dem Unterstring `sub` endet.                                 | `'Hello'.endswith('lo')`       |
| `s.split(sep)`        | Teilt den String `s` an jedem Vorkommen des Separators `sep`.                                 | `'a,b,c'.split(',')`           |
| `sep.join(iter)`      | Fügt eine Sammlung von Strings `iter` mit dem Separator `sep` zusammen.                       | `','.join(['a', 'b', 'c'])`    |
| `s.replace(old, new)` | Ersetzt alle Vorkommen von `old` in `s` durch `new`.                                          | `'hello'.replace('l', 'r')`    |
| `s.find(sub)`         | Gibt den niedrigsten Index von `sub` in `s` zurück, oder -1, falls `sub` nicht gefunden wird. | `'hello'.find('l')`            |
| `s.count(sub)`        | Zählt, wie oft der Unterstring `sub` in `s` vorkommt.                                         | `'hello'.count('l')`           |
| `len(s)`              | Gibt die Länge des Strings `s` zurück.                                                        | `len('hello')`                 |
| `s[index]`            | Greift auf das Zeichen an Position `index` in `s` zu.                                         | `'hello'[1] # 'e'`             |
| `s + t`               | Konkateniert (verbindet) die Strings `s` und `t`.                                             | `'Hello ' + 'world!'`          |
| `s * n`               | Wiederholt den String `s` `n`-mal.                                                            | `'Hello' * 3`                  |
| `s.isnumeric()`       | Überprüft, ob alle Zeichen im String `s` numerisch sind.                                      | `'123'.isnumeric()`            |

Diese Tabelle bietet einen Überblick über einige der am häufigsten verwendeten Operationen, die auf Strings in Python 
angewendet werden können. Diese Operationen ermöglichen es, Strings zu manipulieren, zu analysieren und Informationen 
aus ihnen zu extrahieren.

### Listen

Listen in Python sind eine der vielseitigsten Datenstrukturen und werden verwendet, um eine geordnete Sammlung von 
Elementen zu speichern. Hier sind einige Schlüsseleigenschaften:

#### Eigenschaften von Listen

1. **Geordnet**: 
   - Listen speichern Elemente in einer festgelegten Reihenfolge.
   - Der Zugriff auf Elemente erfolgt über deren Position oder Index.

2. **Veränderlich (Mutable)**: 
   - Die Inhalte einer Liste können nach ihrer Erstellung verändert werden.
   - Elemente können hinzugefügt, entfernt oder geändert werden.

3. **Vielseitig**: 
   - Listen können verschiedene Datentypen enthalten, einschließlich Zahlen, Strings und andere Listen.
   - Sie sind nicht auf einen einzelnen Datentyp beschränkt.

4. **Dynamisch**: 
   - Listen können in ihrer Größe dynamisch wachsen oder schrumpfen.
   - Sie passen sich automatisch der neuen Größe an, wenn Elemente hinzugefügt oder entfernt werden.

5. **Duplikate erlaubt**: 
   - Listen können Duplikate von Elementen enthalten, d.h., ein Element kann mehrmals in einer Liste vorkommen.

#### Erstellung und Nutzung von Listen

Listen werden mit eckigen Klammern `[]` erstellt, und die Elemente werden durch Kommata getrennt. 


**Beispiel:**
```python
fruechte = ["Apfel", "Banane", "Kirsche"]
zahlen = [1, 2, 3, 4, 5]
gemischt = [3.14, "Hallo", True]
```

Elemente einer Liste können über ihren Index angesprochen werden, wobei der erste Index 0 ist. Listen bieten eine 
Vielzahl von Methoden für verschiedene Operationen, wie `append()`, `extend()`, `pop()` und `remove()`, was sie zu einem 
flexiblen und nützlichen Werkzeug in der Programmierung macht.

Ganz häufig werden Listen mit Elementen des selben Datentyps genutzt und fungieren als eine 'Sammlung' (engl. Collection)
dieser Elemente.

Eine kleine Übersicht an häufig verwendeten Funktionen:

| Funktion       | Beschreibung                                                   | Beispiel                    |
|----------------|----------------------------------------------------------------|-----------------------------|
| `[index]`      | Greift auf das Element am Index `index` zu .                   | `liste[0]`                  |
| `append(x)`    | Fügt ein Element `x` am Ende der Liste hinzu.                  | `liste.append(5)`           |
| `extend(iter)` | Erweitert die Liste um alle Elemente des iterierbaren Objekts. | `liste.extend([6, 7, 8])`   |
| `insert(i, x)` | Fügt ein Element `x` an der Stelle `i` ein.                    | `liste.insert(2, 'neu')`    |
| `remove(x)`    | Entfernt das erste Vorkommen von `x` aus der Liste.            | `liste.remove('neu')`       |
| `pop(i)`       | Entfernt das Element an der Stelle `i` und gibt es zurück.     | `element = liste.pop(2)`    |
| `clear()`      | Entfernt alle Elemente aus der Liste.                          | `liste.clear()`             |
| `index(x)`     | Gibt den Index des ersten Vorkommens von `x` zurück.           | `index = liste.index(5)`    |
| `count(x)`     | Zählt, wie oft `x` in der Liste vorkommt.                      | `anzahl = liste.count(5)`   |
| `sort()`       | Sortiert die Elemente der Liste.                               | `liste.sort()`              |
| `reverse()`    | Kehrt die Reihenfolge der Elemente in der Liste um.            | `liste.reverse()`           |
| `copy()`       | Erstellt eine flache Kopie der Liste.                          | `neue_liste = liste.copy()` |

Diese Tabelle gibt einen Überblick über gängige Methoden, die mit Listen in Python verwendet werden. Jede Methode hat 
ihre spezifischen Anwendungsfälle und hilft bei der effizienten Manipulation von Listendaten.


### Tupel (Tuples):
Tupel sind ähnlich wie Listen, aber unveränderbar (immutable). Sie können also weder erweitert noch können ihre Elemente
verändert werden

Um ein Tupel zu erstellen, verwenden wir runde Klammern ().

**Beispiel**:

```python
koordinaten = (4, 5)
print(koordinaten[5])
gemischtes_tupel = ("Katze", 42, False)
```

Auch hier gibt es eine Übersicht häufiger Funktionen, die wir auf Tupel anwenden können:


| Funktion          | Beschreibung                                                  | Beispiel                   |
|-------------------|---------------------------------------------------------------|----------------------------|
| `[index]`         | Greift **lesend** auf das Element am Index `index` zu .       | `tupel[0]`                 |
| `count(x)`        | Zählt, wie oft `x` im Tupel vorkommt.                         | `tupel.count(5)`           |
| `index(x)`        | Gibt den Index des ersten Vorkommens von `x` im Tupel zurück. | `index = tupel.index(5)`   |
| `len(tupel)`      | Gibt die Länge des Tupels zurück.                             | `laenge = len(tupel)`      |
| `max(tupel)`      | Gibt das größte Element des Tupels zurück.                    | `max_element = max(tupel)` |
| `min(tupel)`      | Gibt das kleinste Element des Tupels zurück.                  | `min_element = min(tupel)` |
| `sum(tupel)`      | Berechnet die Summe aller Elemente des Tupels.                | `gesamtsumme = sum(tupel)` |
| `sorted(tupel)`   | Erstellt eine sortierte Liste aus den Elementen des Tupels.   | `sortiert = sorted(tupel)` |

Diese Tabelle stellt die grundlegenden Methoden und Funktionen dar, die bei der Arbeit mit Tupeln in Python verwendet 
werden können. Da Tupel unveränderlich (immutable) sind, gibt es weniger Methoden zur direkten Manipulation als bei 
Listen. Die meisten Operationen erzeugen daher neue Tupel oder andere Datentypen.

Ein häufiger Anwendungsfall für Tupel ist die Rückgabe mehrerer Elemente aus einer Funktion.


## Zusammenfassung und Tipps

- Variablen sind unerlässlich, um Daten in einem Programm zu speichern und zu manipulieren. 
- Die Wahl des richtigen Datentyps ist wichtig, um den Code klar und effizient zu gestalten. 
- Python ist dynamisch typisiert, was bedeutet, dass sich der Datentyp einer Variable ändern kann. 
  Trotzdem ist es eine gute Praxis, den Datentyp im Auge zu behalten.
- Mit Listen und Tupels kann man mehrere Elemente in einer Variable speichern.
- Jeder Datentyp hat seine eigenen Besonderheiten und Verwendungen. Listen und Tupel sin für geordnete Sammlungen 
  geeignet.
- Die Wahl des richtigen Datentyps hängt von den Anforderungen des jeweiligen Programms ab.

## Aufgaben
1. **Variable zuweisen**: Weise der Variable `a` den Wert 5 zu.
2. **Text in Variable speichern**: Speichere den Text "Hallo Python" in einer Variable namens `begrüßung`.
3. **Variable verändern**: Ändere den Wert der Variable `a` auf 10.
4. **Mehrere Variablen**: Erstelle zwei Variablen `name` und `alter` mit deinem Namen und deinem Alter.
5. **Variablennamen**: Erstelle eine Variable `anzahl_aepfel` und weise ihr den Wert 5 zu.
6. **Textverkettung**: Verbinde zwei Textvariablen `vorname` und `nachname` zu einem vollständigen Namen.
7. **Datentypen**: Speichere den Wert 15.5 in einer Variable und gib den Typ dieser Variable aus.
8. **Boolesche Variable**: Erstelle eine Variable `ist_schüler` und weise ihr den Wert `True` zu.
9. **Liste erstellen**: Erstelle eine Liste namens `farben` mit den Elementen "Rot", "Grün" und "Blau".
10. **Element aus Liste**: Greife auf das zweite Element der Liste `farben` zu.
11. **Tupel erstellen**: Erstelle ein Tupel `koordinaten` mit den Werten (4, 5).
12. **Element aus Tupel**: Gib das erste Element des Tupels `koordinaten` aus.
13. **Variable umwandeln**: Konvertiere die String-Variable `zahl_string` mit dem Wert "10" in einen Integer.
14. **Listenelement hinzufügen**: Füge der Liste `farben` die Farbe "Gelb" hinzu.

## Neue Begriffe

| Begriff  | Kurzerklärung                                      | Link zur Referenz                                                                           |
|----------|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| Variable | Name, mit dem man Werte wiederholt nutzen kann     |                                                                                             |
| Integer  | Datentyp für Ganzzahlen                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) |
| Float    | Datentyp für Fließkommazahlne                      | [Referenz](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) |
| Boolean  | Datentyp für Wahrheitswerte (`True`/`False`)       | [Referenz](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)               |
| String   | Datentyp für Zeichenketten                         | [Referenz](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)          |
| List     | Veränderliche Kollektion verschiedener Elemente    | [Referenz](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) |
| Tupel    | Unveränderliche Kollektion verschiedener Elementen | [Referenz](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) |

## Lösungen

1. `a = 5`
2. `begrüßung = "Hallo Python"`
3. `a = 10`
4. `name = "Dein Name"; alter = Dein Alter`
5. `anzahl_aepfel = 5`
6. 
```python 
vorname = "Max"
nachname = "Mustermann"
voller_name = vorname + " " + nachname
print(voller_name)
```
7. 
```python
meine_variable = 15.5
print(type(meine_variable))
```
8. `ist_schüler = True`
9.`farben = ["Rot", "Grün", "Blau"]`
10`print(farben[1])`
11`koordinaten = (4, 5)`
12`print(koordinaten[0])`
13.
```python
zahl_string = "10"
zahl_int = int(zahl_string)
print(zahl_int)
```
14. `farben.append("Gelb")`