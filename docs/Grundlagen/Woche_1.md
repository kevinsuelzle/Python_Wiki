# Week 1

Inhalt:

- Einführung Programmierumgebung
- Variablen & Datentypen
- input + output
- Mathematische Operationen
- Debugger
- Boolean & Verzweigungen (if, else, elif)

# Einführung

# Was ist Programmierung?

Programmierung ist für uns ein Prozess der Erstellung von Anweisungen, die von einem Computer ausgeführt werden, um bestimmte 
Aufgaben zu erfüllen oder Probleme zu lösen. 

Diese Anweisungen werden als Code bezeichnet und in einer Programmiersprache geschrieben. 

Programmierung ermöglicht es uns, Softwareanwendungen, Websites, mobile Apps und andere digitale Tools zu 
entwickeln. 

Im professionellen Umfeld steht die Wertschöpfung durch Software-Entwicklung an erster Stelle. Mit Programmierung werden
Probleme gelöst, die ein Unternehmen oder dessen Kunden haben. 

## Kernaspekte der Programmierung

1. **Algorithmisches Denken**: Programmierung basiert auf der Entwicklung von Algorithmen – Schritt-für-Schritt-Anweisungen zur Lösung eines Problems oder zur Durchführung einer Aufgabe.

2. **Code-Schreiben**: Das Schreiben von Code ist nur ein kleiner Teil der Programmierung. Hierbei wird ein Algorithmus in eine Sprache übersetzt, die der Computer verstehen und ausführen kann.

3. **Fehlerbehebung (Debugging)**: Kein Code ist perfekt. Programmierer verbringen viel Zeit damit, Fehler zu finden und zu beheben, um sicherzustellen, dass ihr Code wie beabsichtigt funktioniert.

4. **Datenmanipulation**: Programme werden oft entwickelt, um Daten zu sammeln, zu verarbeiten und auszugeben. Das Verständnis der Datenverarbeitung ist daher ein wesentlicher Aspekt der Programmierung.

5. **Benutzerinteraktion**: Viele Programme erfordern Interaktionen mit Benutzern. Das Design dieser Interaktionen ist ein wichtiger Teil der Entwicklung einer benutzerfreundlichen Software.

Das Schreiben von Code ist für die Programmierung zwar unerlässlich, aber eigentlich nur ein kleiner, aber wichtiger
Teil.

## Die Rolle von Python in der Programmierung

Python ist eine weit verbreitete und vielseitige Programmiersprache, die sich durch ihre klare Syntax und Lesbarkeit 
auszeichnet. Python ist eine Skriptsprache, das heißt der Code wird während der Ausführung in Maschinensprache
übersetzt. Im Gegensatz dazu gibts es sogenannte kompilierte Sprachen, bei denen diese Übersetzung unmittelbar nach dem
Schreiben des Codes stattfindet. Beide Ansätze haben Vor- und Nachteile.

Hier sehen wir einige Gründe, warum Python in der Welt der Programmierung eine wichtige Rolle spielt:

1. **Vielseitigkeit**: Python wird in vielen Bereichen verwendet, von Web-Entwicklung über Datenanalyse und maschinelles Lernen bis hin zur Automatisierung.

2. **Große Community**: Python hat eine große und aktive Community, die eine Fülle von Ressourcen, Bibliotheken und Frameworks bietet, die die Entwicklung von Anwendungen erleichtern.

3. **Plattformunabhängigkeit**: Python-Programme können auf verschiedenen Betriebssystemen ohne Änderung des Codes ausgeführt werden.

4. **Wissenschaft und Forschung**: Python ist aufgrund seiner starken Unterstützung in wissenschaftlichen Berechnungen und Forschungsprojekten eine bevorzugte Sprache in der akademischen Welt.

Zusammenfassend ist Programmierung ein kreativer und logischer Prozess, der es ermöglicht, Lösungen für komplexe 
Probleme zu entwickeln. Python spielt dabei eine Schlüsselrolle, indem es Zugänglichkeit und Flexibilität bietet, 
die es zu einer der beliebtesten Sprachen in der modernen Programmierung machen.

# Integrated Development Environments (IDEs) in der Programmierung

## Was ist ein IDE?

Ein Integrated Development Environment (IDE) ist eine Softwareanwendung, die umfangreiche Werkzeuge für Programmierer 
bereitstellt, um die Entwicklung von Software zu erleichtern. Ein typisches IDE umfasst einen Code-Editor, 
#Compiler/Interpreter, Debugger und oft weitere hilfreiche Werkzeuge.

Das Hauptziel einer IDE ist die Vereinfachung des Entwicklungsprozesses, sodass wir uns auf die eigenltichen Kernaufgaben
konzentrieren können. 

Auf euren Rechnern sind sowohl VSCode als auch PyCharm vorinstalliert, sodass wir direkt loslegen können.

## Beliebte IDEs für Python

### 1. Visual Studio Code (VSCode)

Visual Studio Code, entwickelt von Microsoft, ist ein kostenloser, leistungsfähiger und leichtgewichtiger Code-Editor. 
Er ist erweiterbar und anpassbar, was ihn zu einer beliebten Wahl für viele Programmiersprachen, einschließlich Python, 
macht.
  
- **Features**:
  - Unterstützung für zahlreiche Programmiersprachen und Frameworks.
  - Integrierter Git-Support.
  - Große Auswahl an Erweiterungen für erweiterte Funktionen wie Auto-Completion, Code-Linting, Themes und mehr.

VSCode kann durch die Python-Erweiterung, die Features wie IntelliSense, Debugging, Jupyter Notebooks und mehr umfasst,
effektiv für Python-Entwicklung genutzt werden.

### 2. PyCharm

PyCharm ist eine IDE, die speziell für Python entwickelt wurde und von JetBrains angeboten wird. Sie ist deutlich 
umfangreicher als VSCode.

- **Features**:
  - Integrierte Tools für professionelle Python-Entwicklung.
  - Smart Code Navigation, Refactoring-Tools und ein leistungsstarker Debugger.
  - Integration mit gängigen Frameworks und Tools wie Django, Flask, Google App Engine, und mehr.

PyCharm bietet eine tiefe Integration mit Python-spezifischen Werkzeugen und eine reichhaltige Entwicklungsumgebung, 
ie besonders für größere Projekte nützlich ist.

### 3. Jupyter Notebooks

Jupyter Notebooks bieten eine webbasierte interaktive Entwicklungsumgebung, die es ermöglicht, 
Code auszuführen, Ergebnisse in Echtzeit zu sehen und gleichzeitig Erklärungen, Formeln und Visualisierungen einzubinden.

- **Einsatzgebiete**:
  - Besonders beliebt in der Datenanalyse, wissenschaftlichen Forschung und Lehre.
  - Ermöglicht das Teilen von lebendigen Code-Dokumenten, was die Zusammenarbeit und das Lernen erleichtert.

Jupyter Notebooks sind ideal für exploratives Programmieren und die Visualisierung von Daten. 
Sie unterstützen eine Mischung aus Code, Text, Bildern und Diagrammen.

Sowohl VSCode als auch PyCharm bieten die Möglichkeit direkt mit Jupyter Notebook zu arbeiten.

## Aufgabe: Das erste Programm 
Zeitrahmen: 30 min + 15 min Diskussion

1. Findet euch in Gruppen von 3 Personen. Die Häälfte der Gruppen wird PyCharm und die andere Hälfte VSCode nutzen.
2. Macht euch mit PyCharm bzw. VSCode vertraut in dem hier folgenden Code programmiert und ausführt:
```python
print("Hello Wolfsburg! Das ist mein erstes Programm!")
```
3. Erklärt einer Gruppe, welche die andere IDE genutzt hat, wie eure IDE aufgebaut ist.

## Zusammenfassung

IDEs sind ein wesentlicher Bestandteil des Werkzeugkastens eines jeden Entwicklers. 
Während VSCode und PyCharm umfassende Entwicklungsplattformen bieten, eignen sich Jupyter Notebooks hervorragend für 
interaktive und explorative Programmierung, insbesondere in der Datenwissenschaft. Die Wahl des richtigen IDE hängt 
von den spezifischen Anforderungen des Projekts und den persönlichen Vorlieben des Entwicklers ab.

----------------------------------

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


-----------------------------------------

# Input und Output

## Die `print`-Funktion

Die `print`-Funktion ist eines der grundlegendsten und nützlichsten Werkzeuge in Python. Sie wird verwendet, um Werte 
auszugeben, sei es Text, Zahlen oder den Inhalt von Variablen. Ein einfacher Aufruf von `print` sieht wie folgt aus:
`print("Hallo, Welt!")`. 

Die Verwendung von Formatierungs-Strings, auch bekannt als f-Strings, macht die Arbeit mit der `print`-Funktion sehr
angenehm. Mit f-Strings können wir Werte von Variablen direkt in einen String einfügen, indem wir die Variable in 
geschweifte Klammern `{}` setzen und dem String ein `f` voranstellen.

**Beispiel**: 

```python
name = "Anna"
alter = 30
print(f"Mein Name ist {name} und ich bin {alter} Jahre alt.")
```

Diese Methode der String-Formatierung ist nicht nur effizient, sondern verbessert auch die Lesbarkeit des Codes 
erheblich. Sie ermöglicht es, dynamisch Werte in Strings einzubetten, was besonders nützlich ist, wenn es darum geht, 
komplexe Ausgaben zu generieren oder Benutzerinteraktionen zu gestalten.

## Die `input`-Funktion

Die `input`-Funktion in Python ist ein wesentliches Werkzeug, um Benutzereingaben zu erhalten. Sie ermöglicht es einem
Programm, während der Ausführung Daten vom Benutzer zu erfragen. Wenn `input()` aufgerufen wird, hält das Programm an
und wartet auf eine Eingabe von der Tastatur. Nachdem der Benutzer seine Eingabe bestätigt hat (üblicherweise 
durch Drücken der Enter-Taste), gibt `input()` diese Eingabe als String zurück. Optional kann `input()` einen 
String als Argument erhalten, der als Eingabeaufforderung (Prompt) dient. Hier ein einfaches Beispiel:

```python
name = input("Bitte gib deinen Namen ein: ")
print(f"Hallo, {name}!")
```

In diesem Beispiel wird der Benutzer aufgefordert, seinen Namen einzugeben. Nach der Eingabe wird der eingegebene 
Name mit einer Begrüßung ausgegeben. Es ist wichtig zu beachten, dass input() immer einen String zurückgibt. Wenn wir 
Zahlen oder andere Datentypen erwarten, müssen wir die Eingabe entsprechend konvertieren:

```python
alter_string = input("Gib dein Alter an: ")
alter = int(alter_string)
```

Damit haben wir bereits eine Menge Grundlagen gelernt, mit denen wir kleine Programme schreiben können. Damit wir das 
nicht nur theoretisch besprechen folgen jetzt erstmal eine Reihe an Übungsaufgaben.

## Aufgaben
1. **Einfache Ausgabe**: Verwende `print`, um "Hallo Welt" auszugeben. 
2. **Variable ausgeben**: Erstelle eine Variable `text` mit dem Wert "Python" und gib sie mit `print` aus.
3. **Zahlen ausgeben**: Gib mit `print` die Zahl 100 aus. 
4. **Mehrere Argumente**: Verwende `print`, um "Hallo" und "Welt" in derselben Zeile mit einem Leerzeichen dazwischen
auszugeben. 
5. **Zeilenende ändern**: Benutze `print`, um "Hallo", gefolgt von einem "!", ohne Zeilenumbruch auszugeben. 
6. **Eingabeaufforderung**: Verwende `input`, um den Benutzer nach seinem Namen zu fragen und speichere das Ergebnis in
einer Variablen. 
7. **Begrüßung**: Frage den Benutzer mit `input` nach seinem Namen und begrüße ihn anschließend mit `print`. 
8. **Numerische Eingabe**: Frage den Benutzer nach seinem Alter und gib es mit `print` aus. 
9. **Kombinierte Eingabe und Ausgabe**: Frage den Benutzer nach seinem Lieblingsessen und sage ihm mit `print`, dass du 
es auch magst. 
10. **Formatierte Ausgabe**: Frage den Benutzer nach seinem Namen und Alter und gib beides formatiert mit einem
f-String aus. 
11. **Mehrere Eingaben**: Frage den Benutzer nacheinander nach seinem Vornamen und Nachnamen und gib dann den
vollständigen Namen aus. 
12. **Rechnung mit Eingabe**: Bitte den Benutzer, zwei Zahlen einzugeben, addiere sie und gib das Ergebnis aus. 
13. **Fehlerkorrektur**: Frage den Benutzer nach einer Zahl, konvertiere die Eingabe in einen Integer und fange dabei 
Fehler mit einer Fehlermeldung ab. 
14. **Eingabe in Liste speichern**: Bitte den Benutzer um drei Lieblingsfarben und speichere sie in einer Liste. Gib 
dann die Liste aus. 
15. **Benutzereingaben vergleichen**: Frage den Benutzer zweimal nach einem Passwort. Gib eine Erfolgsmeldung aus, 
wenn beide Eingaben übereinstimmen, ansonsten eine Fehlermeldung.

## Komplex-Aufgaben

**Aufgabe 1: Persönliche Statistik**

Zeit: 45min

Aufgabenstellung:

- Schreibe ein Python-Programm, das verschiedene persönliche Informationen von einem Benutzer erfragt: Name (String), Alter (Integer), Größe in Metern (Float) und Lieblingsfarben (Liste von Strings).
- Das Programm soll dann diese Informationen jeweils in einem formatierten String ausgeben.
- Für die Lieblingsfarben soll der Benutzer mehrere Farben eingeben können, getrennt durch Kommas.
- Das Programm soll die Anzahl der eingegebenen Lieblingsfarben berechnen und ausgeben.

## Neue Begriffe

| Begriff  | Kurzerklärung                                                         | Link zur Referenz                                                                                   |
|----------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `print`  | Funktion um Variablen als Text auf der Konsole auszugeben             | [Referenz](https://docs.python.org/3/library/functions.html?highlight=print#print)                  |
| `input`  | Funktion, um Nutzereingaben von der Konsole zu lesen                  | [Referenz](https://docs.python.org/3/library/functions.html?highlight=input#input)                  |
| f-String | Möglichkeit, Strings zu formatieren                                   | [Referenz](https://docs.python.org/3/tutorial/inputoutput.html?highlight=f%20strings#tut-f-strings) |
| `int`    | Funktion, um Strings, die nur Zahlen enthalten in Integer umzuwandlen | [Referenz](https://docs.python.org/3/library/functions.html?highlight=int#int)                      |
----------------------------

# Mathematische Operationen
In Python können wir alle einfachen mathematischen Operationen durchführen. Dieses sind grundlegend für die Entwicklung 
von Algorithmen und der Lösung von Problemen. In diesem Abschnitt soll es nur um mathematische Operationen gehen,
die wir mit Ganzzahlen und Fließkommazahlen verwenden können.

## Abschnitt 1: Grundoperationen

1. **Addition (`+`)**: Addiert zwei Zahlen.
```python
summe = 5 + 3  # Ergibt 8
```
2. **Subtraktion (`-`)**: Subtrahiert eine Zahl von einer anderen.

```python
differenz = 10 - 2  # Ergibt 8
```

3. **Multiplikation (`*`)**: Multipliziert zwei Zahlen.

```python
produkt = 4 * 2  # Ergibt 8
```

4. **Division (`/`)**: Teilt eine Zahl durch eine andere.

```python
quotient = 16 / 2  # Ergibt 8
```

5. **Ganzzahlige Division (`//`)**: Teilt eine Zahl durch eine andere und rundet das Ergebnis auf die nächste ganze Zahl ab.

```python
ganzzahliger_quotient = 17 // 2  # Ergibt 8
```

6. **Modulo (`%`)**: Gibt den Rest einer Division zurück.

```python
rest = 18 % 10  # Ergibt 8
```

7. **Potenzierung (`**`)**: Erhebt eine Zahl in die Potenz einer anderen.

```python
potenz = 2 ** 3  # Ergibt 8
```

## Erweiterte Operationen

Für komplexere mathematische Operationen wie Wurzeln oder trigonometrische Funktionen benötigen Sie das `math`-Modul, 
das viele nützliche Funktionen bietet. 

Um das `math`-Modul nutzen zu können, muss es importiert werden:
```python
import math
```

Hier sind einige Beispiele:

1. **Quadratwurzel (`math.sqrt(x)`)**: Berechnet die Quadratwurzel einer Zahl.

```python
import math
wurzel = math.sqrt(64)  # Ergibt 8
```

2. **Exponentialfunktion (`math.exp(x)`)**: Berechnet e^x, wobei e die Basis des natürlichen Logarithmus ist.

```python
import math
exponent = math.exp(3)  # Berechnet e^3
```

3. **Logarithmus (`math.log(x, base)`)**: Berechnet den Logarithmus einer Zahl zu einer bestimmten Basis.

```python
import math
log_nat = math.log(8, 2)  # Berechnet den Logarithmus von 8 zur Basis 2
```

## Reihenfolge der Operationen

In Python, wie in den meisten Programmiersprachen, ist die Reihenfolge der mathematischen Operationen wichtig und folgt 
etablierten mathematischen Konventionen. Diese Reihenfolge bestimmt, in welcher Reihenfolge die Operationen in einem 
Ausdruck ausgeführt werden.

1. **Klammern (`()`)** haben die höchste Priorität und werden zuerst ausgewertet. Sie können verwendet werden, um die 
Ausführungsreihenfolge zu ändern. Zum Beispiel wird in `(3 + 4) * 5` zuerst die Addition innerhalb der Klammern 
durchgeführt und dann die Multiplikation.

2. **Potenzierung (`**`)** wird als nächstes ausgeführt. Sie hat eine höhere Priorität als Multiplikation und Division.

3. **Multiplikation (`*`) und Division (`/`)** folgen danach. Sie haben die gleiche Priorität und werden von links nach
rechts ausgeführt.

4. **Addition (`+`) und Subtraktion (`-`)** haben die niedrigste Priorität und werden zuletzt ausgeführt, ebenfalls von 
links nach rechts.

Es ist wichtig, sich die Reihenfolge der Operationen zu merken, um Fehler in Berechnungen zu vermeiden und den Code 
klar und präzise zu gestalten. Die gute Nachricht: Die Reihenfolge entspricht exakt dem was wir aus der normalen 
Mathematik kennen!

Üben wir das Ganz:


## Aufgabe
1. **Addition**: Addiere 5 und 3. Gib das Ergebnis aus.
2. **Subtraktion**: Subtrahiere 2 von 10. Gib das Ergebnis aus.
3. **Multiplikation**: Multipliziere 4 mit 2. Gib das Ergebnis aus.
4. **Division**: Teile 16 durch 2. Gib das Ergebnis aus.
5. **Ganzzahlige Division**: Führe eine ganzzahlige Division von 17 durch 2 durch. Gib das Ergebnis aus.
6. **Modulo**: Finde den Rest der Division von 18 durch 10. Gib das Ergebnis aus.
7. **Potenzierung**: Erhebe 2 in die 3. Potenz. Gib das Ergebnis aus.
8. **Quadratwurzel**: Berechne die Quadratwurzel von 64. Gib das Ergebnis aus.
9. **Exponentialfunktion**: Berechne e^3 (e ist die Basis des natürlichen Logarithmus). Gib das Ergebnis aus.
10. **Natürlicher Logarithmus**: Berechne den natürlichen Logarithmus von 8. Gib das Ergebnis aus.

11. **Komplexe Rechnung**: Berechne das Ergebnis von (3 + 4) * 5. Gib das Ergebnis aus.
12. **Vergleich**: Überprüfe, ob das Produkt von 2 und 3 gleich 6 ist. Gib das Ergebnis aus.
13. **Runden**: Runde die Zahl 2.7 auf die nächste ganze Zahl. Gib das Ergebnis aus.
14. **Negative Zahlen**: Berechne das Produkt von -3 und 3. Gib das Ergebnis aus.
15. **Variable in Rechnung**: Definiere eine Variable `x` mit dem Wert 5 und berechne `x * x`. Gib das Ergebnis aus.
16. **Verschiedene Operationen**: Berechne das Ergebnis von `2 + 3 * 5`.
17. **Einsatz von Klammern**: Ändere den Ausdruck `2 + 3 * 5` so ab, dass zuerst die Addition und dann die 
Multiplikation ausgeführt wird.
18. **Potenzierung und Division**: Berechne das Ergebnis von `4 ** 2 / 8`.
19. **Mehrere Operationen**: Finde das Ergebnis von `3 + 4 * 2 - 1`.
20. **Komplexer Ausdruck**: Berechne den Wert von `(3 + 4) * (5 - 2) ** 2`.

## Komplex-Aufgaben
**Zinsrechner**

Zeit: 40 min 

Aufgabenstellung:

- Schreibe ein Python-Programm, das als einfacher Zinsrechner fungiert. 
- Das Programm soll vom Benutzer das Anfangskapital (Hauptsumme), den Zinssatz (in Prozent) und die Anlagedauer in 
Jahren abfragen. 
- Berechne die Endsumme, die sich aus der Formel Endsumme = Anfangskapital * (1 + Zinssatz/100 * Jahre) ergibt. 
- Gib das berechnete Ergebnis aus.

**Umrechner für Temperaturen**

Zeit: 40 min

Aufgabenstellung:
- Erstelle ein Python-Programm zur Umrechnung von Temperaturen zwischen Celsius und Fahrenheit. 
- Das Programm soll zuerst nach der Eingabetemperatur (als Zahl) fragen und dann, ob diese in Celsius oder Fahrenheit ist. 
- Führe die entsprechende Umrechnung durch: Von Celsius nach Fahrenheit (`F = C * 9/5 + 32`) oder von Fahrenheit nach 
- Celsius (`C = (F - 32) * 5/9`).
- Gib das Ergebnis der Umrechnung aus.

## Neue Begriffe

| Begriff     | Kurzerklärung                       | Link zur Referenz                                                                       |
|-------------|-------------------------------------|-----------------------------------------------------------------------------------------|
| `+`         | Addition von zwei Variablen         |                                                                                         |
| `-`         | Subtraktion von zwei Variablen      |                                                                                         |
| `*`         | Multiplikation von zwei Variablen   |                                                                                         |
| `/`         | Divison von zwei Variablen          |                                                                                         |
| `//`        | Ganzzahldivision von zwei Variablen |                                                                                         |
| `%`         | Module von zwei Variablen           |                                                                                         |
| `**`        | Potenzieren                         |                                                                                         |
| `math.sqrt` | Ziehen der Quadratwurzel            | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.sqrt) |
| `math.exp`  | Exponentailfunktion                 | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.exp)  |
| `math.log`  | Logartihmus zur angegeben Basis     | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.log)  |


-------------------

# Wie gehen wir mit Fehlern beim Programmieren um?

Programmieren ist ein komplexer Prozess, der Präzision und Aufmerksamkeit erfordert. Trotzdem sind Fehler beim 
Programmieren allgegenwärtig. Hier sind einige Gründe, warum Fehler entstehen, und die möglichen Auswirkungen, 
die sie haben können.

### Gründe für Programmierfehler

1. **Komplexität des Codes**: 
   - Je komplexer ein Programm ist, desto schwieriger ist es, alle Aspekte zu überblicken und Fehler zu vermeiden.

2. **Menschliche Fehler**: 
   - Programmierer sind Menschen und können Übersehen, Missverständnisse oder Irrtümer begehen.

3. **Zeitdruck und Arbeitsbelastung**: 
   - Unter Zeitdruck oder bei hoher Arbeitsbelastung können wichtige Details leicht übersehen werden.

Fehler sind beim Programmieren unvermeidbar. Es gibt keine Software auf der Welt, die fehlerfrei ist. Dafür gibt es zu
viele potentielle Fehlerquellen. 

#### Aufgabe / Diskussion
Zeit: 30 min

Aufgabenstellung:
- Diskutiert in 2er Gruppen, welche weiteren Gründe zu Fehlern führen können.
- Welche Auswirkungen können Fehler in Software haben? Geht sowohl auf technische als auch auf Auswirkungen für 
die Firma ein.
     
## Debugging von Python Anwendungen

Als Debugging bezeichnet man das Finden und Beseitigen von Fehlern.

Wieso nennt sich das Debugging? Früher, als Computer noch mit Röhren funktioniert haben, haben es sich wohl ab und an
echte Käfer (engl. Bugs) in diesen Röhren gemütlich gemacht und zu Fehlern geführt. Dementsprechend hat man diese dann 
'entkäfert'.

Effizientes Debuggen besteht aus einer Mischung aus Erfahrung, Nutzen der vorhandenen Tools und systematischen Vorgehen.

### Nutzen der `print`-Funktion

Die einfachste Form des Debuggings kann durch das Einfügen von `print`-Anweisungen im Code erfolgen, um Werte von 
Variablen zu einem bestimmten Zeitpunkt auszugeben. Dies wird sehr häufig verwendet, ist jedoch nicht optimal. Deswegen
gehen wir hier auch nicht weiter darauf ein.

### Nutzen von Logging-Funktionen

Logging spielt eine entscheidende Rolle im Debugging-Prozess, indem es Entwicklern Einblicke in den 
Ablauf eines Programms bietet. 

Oftmals sind Logs ein erster Hinweis darauf in welchen Programmteilen bestimmte Fehler passiert sind und welche
Auswirkungen sie auf das Programm hatten. 

Software, die für einen Produktiveinsatz entwickelt wird, sollte immer eine Form von Logging beinhalten.

#### Warum ist Logging wichtig?

1. **Fehleridentifikation**: 
   - Logging ermöglicht die Erfassung von Fehlern und Ausnahmen zur Laufzeit. Diese Logs bieten wichtige Hinweise zur 
   Fehlerursache.

2. **Verhaltensanalyse**: 
   - Durch das Protokollieren von Aktivitäten und Ereignissen kann das Verhalten des Programms verstanden und 
   analysiert werden.

3. **Historische Daten**: 
   - Logs bieten eine Historie der Programmausführung, die hilfreich sein kann, um Probleme, die zu einem früheren
   Zeitpunkt aufgetreten sind, zu diagnostizieren.

4. **Leistungsmessung**: 
   - Performance-relevante Informationen können geloggt werden, um Engpässe und Leistungsprobleme zu identifizieren.

#### Logging in der Praxis

- **Logging-Level**: 
  - Verschiedene Logging-Levels (wie INFO, DEBUG, ERROR) ermöglichen es, die Menge und den Detailgrad der 
  Log-Nachrichten zu steuern.

- **Kontextreiche Informationen**: 
  - Gute Log-Nachrichten enthalten Kontext, wie Zeitstempel, Ausführungspfad, Variablenwerte usw.

- **Nicht-intrusiv**: 
  - Logging ist eine nicht-intrusive Methode, die den normalen Ablauf des Programms nicht unterbricht.

- **Werkzeuge und Bibliotheken**: 
  - Es gibt viele Tools und Bibliotheken (wie log4j, Python's logging-Modul), die das Logging unterstützen und 
  erleichtern.

### Der Debugger

Ein Debugger ist ein wesentliches Werkzeug in der Softwareentwicklung, das Programmierern hilft, den Code Schritt für 
Schritt auszuführen, um Fehler (Bugs) zu finden und zu beheben. Debugger bieten die Möglichkeit, den Zustand eines 
Programms zu einem bestimmten Zeitpunkt zu überprüfen, Variablenwerte zu inspizieren und den Programmfluss zu 
kontrollieren. 

Debugger haben alle ähnliche Funktionen:

1. **Haltepunkte setzen**: 
   - Erlaubt es dem Entwickler, die Ausführung des Programms an bestimmten Punkten anzuhalten.

2. **Schrittweise Ausführung**: 
   - Führt das Programm Zeile für Zeile aus, um die Auswirkungen jeder Anweisung zu beobachten.

3. **Variablen inspizieren**: 
   - Zeigt die aktuellen Werte von Variablen im Programm an.

4. **Programmfluss steuern**: 
   - Erlaubt es, den Ablauf des Programms zu steuern, beispielsweise durch Fortsetzen der Ausführung oder Rückkehr 
   zu einem früheren Punkt.

#### Verwendung von `pdb`

Für eine umfassendere Fehlersuche bietet Python jedoch eingebaute Tools wie das `pdb`-Modul, einen interaktiven 
Debugger. 

Das `pdb`-Modul (Python Debugger) ermöglicht es, den Code interaktiv zu durchlaufen, Haltepunkte zu setzen und den 
Zustand des Programms zu inspizieren. Hier sind einige grundlegende Befehle:

- `import pdb`: Importiert das pdb-Modul.
- `pdb.set_trace()`: Setzt einen Haltepunkt im Code.
- `c`: Fährt mit der Ausführung fort, bis zum nächsten Haltepunkt.
- `n`: Führt die nächste Zeile aus.
- `s`: Tritt in eine Funktion oder Methode ein.
- `p`: Druckt den Wert eines Ausdrucks.
- `q`: Beendet den Debugger und das Programm.

#### Beispiel zur Nutzung von `pdb`

```python
import pdb

def berechne_summe(a, b):
    pdb.set_trace()
    summe = a + b
    return summe

ergebnis = berechne_summe(3, 4)
print(ergebnis)
```

In diesem Beispiel wird pdb.set_trace() verwendet, um einen Haltepunkt zu setzen. Wenn das Programm diesen Punkt 
erreicht, wird die Ausführung pausiert und der Benutzer kann mit den pdb-Befehlen den Zustand des Programms 
inspizieren und steuern.

### Übungsaufgaben

1. **Haltepunkt setzen**: Füge in der folgenden Funktion einen Haltepunkt hinzu und führe das Programm aus. 
Untersuche die Werte von `a` und `b`, bevor die Summe berechnet wird.
```python
def addiere(a, b):
    # Füge hier einen Haltepunkt ein
    return a + b

ergebnis = addiere(5, 7)
print(ergebnis)
```

2. Nächste Zeile ausführen: Betrachte das folgende Python-Skript. Führe es mit pdb aus und benutze den Befehl n (next),
um die Ausführung bis zur print-Anweisung Zeile für Zeile zu durchlaufen.
```python 
import pdb

def quadriere(zahl):
    pdb.set_trace()
    ergebnis = zahl * zahl
    return ergebnis

print(quadriere(4))
```

3. In eine Funktion eintreten: In dem folgenden Code, tritt mit dem s (step) Befehl in die Funktion berechne_differenz 
ein. Prüfe die Variablen innerhalb der Funktion.
```python
import pdb

def berechne_differenz(x, y):
    return x - y

pdb.set_trace()
ergebnis = berechne_differenz(10, 5)
print(ergebnis)
```

4. Werte ausdrucken: Verwende p (print), um den Wert von ergebnis in dem folgenden Programm auszugeben, bevor es mit 
dem c (continue) Befehl fortgesetzt wird.
```python
import pdb

def multipliziere(a, b):
    return a * b

pdb.set_trace()
ergebnis = multipliziere(6, 7)
print(ergebnis)
```

5. Haltepunkte dynamisch setzen: Anstatt pdb.set_trace() direkt im Code zu verwenden, starte das folgende Programm mit 
dem Python-Interpreter im Debug-Modus (python -m pdb script.py). Setze dann einen Haltepunkt bei der Zeile, die die 
Multiplikation ausführt. Führe das Programm bis zu diesem Haltepunkt aus und überprüfe die Werte von x und y.
```python
def multipliziere(x, y):
    ergebnis = x * y
    return ergebnis

ergebnis = multipliziere(3, 3)
print(ergebnis)
```

## Neue Begriffe

| Begriff | Kurzerklärung                                        | Link zur Referenz                                                                           |
|---------|------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `pdb`   | Python Debugger                                      | [Referenz](https://docs.python.org/3/library/pdb.html?highlight=pdb)                        |
| Logging | Ausgaben zur Nachvollziehbarkeit des Programmablaufs | [Referenz](https://docs.python.org/3/library/logging.html?highlight=logging#module-logging) |

-----

# Verzweigungen

Verzweigungen sind ein wesentlicher Bestandteil der Programmierung. Sie ermöglichen es, Entscheidungen auf Basis 
bestimmter Bedingungen zu treffen. Python verwendet `if`, `elif` (else if) und `else` zur Steuerung des Programmflusses.

## Einfache if-else-Abfragen

### Grundstruktur

Die grundlegende Struktur einer `if-else`-Verzweigung in Python sieht folgendermaßen aus:

```python
if bedingung:
    # Anweisungen, wenn Bedingung wahr ist
else:
    # Anweisungen, wenn Bedingung falsch ist
```

Die `bedingung` ist ein Ausdruck, der entweder wahr (`True`) oder falsch (`False`) ergibt.

#### Bedingungen


In Python werden Bedingungen in `if`-Abfragen verwendet, um zu bestimmen, ob bestimmte Anweisungen ausgeführt werden 
sollen oder nicht. Diese Bedingungen können auf unterschiedliche Weise formuliert werden, um die Logik des Programms 
zu steuern. 

Eine grundlegende Bedingung in einer `if`-Abfrage könnte so einfach sein wie der Vergleich zweier Werte. Zum Beispiel 
überprüft `if alter >= 18:` ob das Alter einer Person 18 Jahre oder älter ist. Hierbei wird ein Gleichheits- oder 
Ungleichheitsoperator verwendet, um zu entscheiden, ob der Code innerhalb des `if`-Blocks ausgeführt wird.

Komplexere Bedingungen können durch die Verwendung logischer Operatoren wie `and`, `or` und `not` erstellt werden. 
Eine solche Bedingung könnte lauten `if alter >= 18 and student == True:`, was bedeutet, dass der Code nur ausgeführt 
wird, wenn die Person 18 Jahre oder älter ist und gleichzeitig ein Student ist.

Python ermöglicht auch die Überprüfung von Mitgliedschaften mit dem `in`-Operator in Bedingungen. Ein Beispiel wäre 
`if frucht in ['Apfel', 'Banane', 'Kirsche']:`. Diese Bedingung prüft, ob der Wert der Variablen `frucht` in der 
angegebenen Liste enthalten ist.

Bedingungen können auch komplexere Ausdrücke beinhalten, wie z.B. Funktionsaufrufe oder kombinierte Vergleiche. Zum 
Beispiel kann `if ist_regnerisch() and temperatur < 20:` eine Bedingung sein, die wahr ist, wenn die Funktion 
`ist_regnerisch()` `True` zurückgibt und die Temperatur unter 20 Grad liegt.

Insgesamt erlauben Bedingungen in `if`-Abfragen in Python, sehr flexible und leistungsfähige Kontrollstrukturen in 
Programmen zu erstellen, von einfachen Vergleichen bis hin zu komplexen logischen Ausdrücken.

Die Bausteine dafür sehen wir hier:

- Vergleichsoperatoren: ==, !=, >, <, >=, <=
- Logische Operatoren: and, or, not
- Überprüfung auf Null/None: is None, is not None

**Beispiel**:
```python
alter = 18
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")
```

##  if-elif-else-Abfragen

`elif` erlaubt es, mehrere Bedingungen nacheinander zu überprüfen.

**Grundstruktur**
```python
if bedingung1:
    # Anweisungen, wenn bedingung1 wahr ist
elif bedingung2:
    # Anweisungen, wenn bedingung2 wahr ist
else:
    # Anweisungen, wenn keine Bedingung wahr ist
```

Es können beliebig viele Zweige entstehen. Hat der Code sehr viele Zweige, sollte man sich jedoch fragen, ob man das 
nicht anders lösen kann. Je mehr Einrückungsebenen es gibt, desto schwieriger wird es für andere den Code zu lesen.

**Beispiel**
```python
zahl = 15
if zahl > 10:
    print("Die Zahl ist größer als 10.")
elif zahl == 10:
    print("Die Zahl ist genau 10.")
else:
    print("Die Zahl ist kleiner als 10.")
```

Die Verwendung von if, elif und else in Python ermöglicht es, auf Basis von Bedingungen unterschiedliche Wege im 
Programm einzuschlagen. Es ist wichtig, die Struktur dieser Anweisungen zu verstehen und korrekt zu verwenden, um 
logische Entscheidungen in einem Programm zu implementieren.

## Aufgaben
1. **Einfache if-Abfrage**: Schreibe ein Programm, das überprüft, ob eine Variable `x` größer als 10 ist. Gib eine 
entsprechende Nachricht aus.
2. **if-else**: Überprüfe, ob eine Variable `zahl` gerade ist. Verwende dazu den Modulo-Operator `%`.
3. **Negativ oder Positiv**: Schreibe ein Programm, das überprüft, ob eine Zahl positiv, negativ oder 0 ist.
4. **Größer oder kleiner**: Überprüfe, ob eine Variable `a` größer, kleiner oder gleich einer anderen Variable `b` ist.
5. **Alter überprüfen**: Schreibe ein Programm, das überprüft, ob eine Person anhand ihres Alters volljährig ist.
6. **Passwortüberprüfung**: Erstelle ein Programm, das überprüft, ob ein eingegebenes Passwort mit einem gespeicherten 
Passwort übereinstimmt.
7. **Maximalwert**: Schreibe ein Programm, das den größeren Wert von zwei Zahlen ausgibt.
8. **Bewertung**: Überprüfe anhand einer Variable `note`, ob die Note "sehr gut", "gut", "befriedigend", "ausreichend" 
oder "nicht ausreichend" ist.
9. **Temperaturen**: Schreibe ein Programm, das unterschiedliche Meldungen für verschiedene Temperaturbereiche ausgibt 
(z.B. kalt, warm, heiß).
10. **Einfache Rechnung**: Schreibe ein Programm, das eine einfache mathematische Operation (Addition, Subtraktion, 
Multiplikation, Division) basierend auf Benutzereingaben ausführt.

11. **Jahreszeiten**: Schreibe ein Programm, das den Namen einer Jahreszeit ausgibt, basierend auf einer Monatsnummer (1 bis 12).
12. **Teilbarkeit**: Überprüfe, ob eine Zahl durch eine andere Zahl ohne Rest teilbar ist.
13. **Einkaufsliste**: Schreibe ein Programm, das überprüft, ob ein Artikel in einer Einkaufsliste vorhanden ist.
14. **Größte von drei Zahlen**: Bestimme die größte Zahl aus drei gegebenen Zahlen.
15. **Rabattaktion**: Schreibe ein Programm, das basierend auf dem Einkaufswert unterschiedliche Rabatte berechnet.
16. **Lichtschalter**: Simuliere einen Lichtschalter, der das Licht ein- und ausschaltet basierend auf der aktuellen 
Zustandsvariable.
17. **Fahrzeugklasse**: Schreibe ein Programm, das basierend auf dem Gewicht eines Fahrzeugs eine Kategorie
(Leicht, Mittel, Schwer) zuweist.
18. **Kinotag**: Erstelle ein Programm, das unterschiedliche Eintrittspreise basierend auf dem Wochentag berechnet.
19. **Lebensmittelqualität**: Schreibe ein Programm, das basierend auf einem Haltbarkeitsdatum die Qualität eines 
Lebensmittels beurteilt (frisch, abgelaufen, etc.).
20. **Schaltjahr**: Schreibe ein Programm, das überprüft, ob ein gegebenes Jahr ein Schaltjahr ist oder nicht.

## Komplex-Aufgaben
**Benutzereingaben filtern und sortieren**

Aufgabenstellung:

- Fordere den Benutzer auf, mehrere Einträge mit Kundeninformationen einzugeben (Format: "Name, Alter, Email"). Beende 
die Eingabe bei Eingabe von "fertig".
- Filtere die Daten, um nur Kunden über 30 Jahre in die Ausgabe einzuschließen.
- Gib die gefilterten Daten auf der Konsole aus, sortiert nach dem Alter in absteigender Reihenfolge.

## Neue Begriffe

| Begriff     | Kurzerklärung                          | Link zur Referenz                                                                              |
|-------------|----------------------------------------|------------------------------------------------------------------------------------------------|
| `if`, `else` | Verzweigungen aufgrund von Bedingungen | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=else#if-statements)   |

