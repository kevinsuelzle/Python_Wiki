# Variablen und Datentypen

In diesem Abschnitt lernen wir die Grundlagen von Variablen und verschiedenen Datentypen in Python kennen. Variablen
sind wie Behälter, in denen wir Daten speichern können, während Datentypen die Art der Daten bestimmen, die in diesen
Variablen gespeichert werden können.

## Bedeutung von Variablen in der Programmierung

Variablen sind ein unverzichtbarer Bestandteil der meisten Programmiersprachen, einschließlich Python. Sie erfüllen
mehrere wichtige Funktionen:

1. **Daten speichern**:
   Variablen dienen als Speicherorte im Arbeitsspeicher eines Computers, in denen Daten gespeichert werden können.
   Diese Daten können Zahlen, Texte, und andere möglichen anderen Objekte sein.
    ```python
    sum = 10 + 13
    print(sum)
    ```

2. **Lesbarkeit und Wartbarkeit**:
   Variablen helfen, den Code verständlicher zu machen. Durch sinnvolle Namen wird der Zweck des Codes klarer, was die
   Wartung und Fehlerbehebung vereinfacht.

3. **Berechnungen durchführen und Ergebnisse speichern**:
   Variablen ermöglichen die Durchführung von Berechnungen mit gespeicherten Werten. So können beispielsweise
   mathematische Operationen ausgeführt und das Ergebnis in einer anderen Variablen gespeichert werden.
```python
nominator = 3
denominator = 6
result = nominator / denominator
print(result)
```
4. **Daten wiederverwenden**:
   Variablen werden eingesetzt, um Daten in verschiedenen Teilen eines Programms zu nutzen.

5. **Speichern von Zuständen**:
   In komplexeren Anwendungen dienen Variablen dazu, den Zustand einer Anwendung zu speichern und zu verwalten.
   Beispiele hierfür sind der Login-Status eines Nutzers oder die Anzahl der Artikel in einem Warenkorb.

```python
name = "Hans"
print("Hallo " + name)
print("Ich heiße auch " + name)
name = "Klaus"
print("Hallo auch " + name)
```

Variablen sind somit essenziell für die Erstellung flexibler, effizienter und verständlicher Programme und bilden die
Grundlage für fast alle Operationen und Logiken in der Programmierung.

----

# Variablen

Eine Variable in Python kann erstellt werden, indem man ihr einen Namen gibt und
ihr einen Wert zuweist.

**Beispiel:**

```python
meine_variable = 10
alter = 23
Geburtsjahr = 1940
willkommens_text = "Hey du!"
```

## Namenskonventionen:

- Variablennamen sollten klar und beschreibend sein. In Python verwenden wir oft Snake-Case,
  bei dem Wörter durch Unterstriche getrennt werden (z.B. `meine_variable`).
- Variablennamen dürften nicht mit einer Zahl anfangen und keine Sonderzeichen außer dem Unterstrich enhalten

Kurze Variablennamen sind nur in absoluten Ausnahmefällen zu verwenden, z.B. als Laufvariable in einer Schleife. Es
kostet keine Ressourcen und kein Geld aussagekräftige Variablen zu nutzen.

Eine Variable `a` könnte alles sein, während die Variable `zinssatz` recht sicher ein Zinssatz darstellen wird.

----

# Datentypen

In Python gibt es verschiedene Datentypen, aber hier konzentrieren wir uns auf die grundlegendsten.

## Primitive Datentypen

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

### Übungsaufgaben

1. **Integer Addition**: Schreibe ein Programm, das zwei Integers addiert.
2. **Integer Subtraktion**: Subtrahiere einen Integer von einem anderen und gib das Ergebnis aus.
3. **Float Division**: Dividiere zwei Floats und gib das Ergebnis aus.
4. **Multiplikation von Integers**: Multipliziere zwei Integers und gib das Ergebnis aus.
5. **Konvertierung von Float zu Integer**: Konvertiere einen Float in einen Integer und gib das Ergebnis aus.
6. **Vergleich von Integers**: Vergleiche zwei Integers mit einem Vergleichsoperator und gib das Ergebnis (True oder
   False) aus.
7. **Booleansches AND**: Verwende den AND-Operator, um zwei boolesche Werte zu vergleichen.
8. **Booleansches OR**: Verwende den OR-Operator, um zwei boolesche Werte zu vergleichen.
9. **Umwandlung von Integer in Boolean**: Konvertiere einen Integer in einen Boolean und gib das Ergebnis aus.
10. **Modulo-Operator mit Integers**: Verwende den Modulo-Operator, um den Rest zweier Integers zu finden.
11. **Potenzierung von Floats**: Berechne die Potenz eines Floats (z.B. 5.5^3) und gib das Ergebnis aus.
12. **Vergleich von Floats**: Vergleiche zwei Floats miteinander und gib das Ergebnis (True oder False) aus.
13. **Integer in Float konvertieren**: Konvertiere einen Integer in einen Float.
14. **Negation eines Booleans**: Negiere einen booleschen Wert und gib das Ergebnis aus.
15. **Kombination von Booleans und Integers**: Überprüfe, ob ein Integer positiv ist und gib das Ergebnis als Boolean
    zurück.
15. **Diskussion**: Für welche Anwendungen float und integer jeweils besser geeignet sind und wo es keine Rolle spielt!
16. **Diskussion**: Kann man mit Fließkommazahlen jede Dezimalzahl darstellen? Begründet eure Antworten.

## Strings, List, Tupel, Set, Dictionary

### Strings (Zeichenketten):

Strings werden verwendet, um Text zu speichern. In Python gibt es eine Vielzahl von Funktionen und Methoden, die es
erlauben Strings zu verarbeiten. Strings in Python sind Unicode, das heißt so ziemlich jedes Zeichen, was es gibt kann
gespeichert werden, auch Emojis zum Beipiel!

**Beispiel**:

```python
name = "Anna"
begruessung = 'Hallo Welt!'
zahl_als_text = "1234"
```

Strings sind für uns sehr wichtig. Der Datentyp ist sehr universell und typischerweise werden jegliche Eingaben und
Ausgaben eine Art String sein.

### Listen

Listen in Python sind eine der vielseitigsten Datenstrukturen und werden verwendet, um eine geordnete Sammlung von
Elementen zu speichern.

Listen werden mit eckigen Klammern `[]` erstellt, und die Elemente werden durch Kommata getrennt.

**Beispiel:**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
zahlen = [1, 2, 3, 4, 5]
gemischt = [3.14, "Hallo", True]
```

Listen sind sehr häufig verwendete Datenstrukturen. Deswegen ist dies hier nur ein kleiner Einstieg und wir lernen
später noch mehr zu Listen.

### Tupel

Tupel in Python sind ähnlich wie Listen eine Datenstruktur zur Sammlung von Werten. Im Gegensatz zu Listen sind sie
unveränderlich, wenn sie einmal erstell wurden.

Sie werden mit runden Klammern `()` erstellt. Die Elemente werden durch Kommas getrennt.

**Beispiel**:

```python
koordinaten = (50.0, 20.1)
rgb_farbe = (256, 128, 0)
```

Ebenso wie Listen, sind Tupel wichtige Datenstrukturen. Auch hier lernen wir später noch mehr.

### Sets

Sets in Python sind eine Datenstruktur, die für die Speicherung einer ungeordneten Sammlung von einzigartigen Elementen
verwendet wird. Das heißt kein Element kann doppelt vorkommen.

Wir erstellen Sets mit geschweiften Klammern `{}` und den jeweiligen Elementen:

```python
einzigartige_zahlen = {1, 2, 3, 4, 5}
buchstaben = {'a', 'b', 'c', 'd'}
```

### Dictionaries

Mit Dictionaries können wir Schlüssel-Wert-Paare speichern. Dies ist die vielleicht wichtigste Datenstruktur in Python
und wird auch von der Sprache selbst in hohem Maße genutzt. Sehr viele Dinge in Python lassen sich im Grunde auf
Dictionaries zurückführen.

Wir erstellen Dictionaries mit geschweiften Klammern `{}` und `Schlüssel: Wert`- Paaren, die durch Komma getrennt sind:

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)

# Zugriff auf den Wert mit dem Schlüssel "Name"
name = mein_dict["Name"]
print(name)  # Gibt "Max" aus
```

### Aufgaben

### Übungsaufgaben

1. **Liste erstellen**: Erstelle eine Liste mit den Zahlen von 1 bis 10.
2. **Tupel zu Liste**: Konvertiere das Tupel `(1, 2, 3)` in eine Liste.
3. **Elemente zu Set hinzufügen**: Füge die Zahlen 4, 5 und 6 zu einem Set `{1, 2, 3}` hinzu.
4. **Schlüssel-Wert-Paare in Dictionary**: Erstelle ein Dictionary mit den Schlüsseln "a", "b", "c" und den Werten 1, 2,
   3.
5. **Liste invertieren**: Kehre die Reihenfolge der Elemente in der Liste von Aufgabe 1 um.
6. **Tupel aus Listen**: Erstelle ein Tupel aus den ersten drei Elementen der Liste von Aufgabe 1.
7. **Element aus Set entfernen**: Entferne ein beliebiges Element aus dem Set von Aufgabe 3.
8. **Werte aus Dictionary abrufen**: Greife auf den Wert des Schlüssels "b" im Dictionary von Aufgabe 4 zu.
9. **Liste von Tupeln**: Erstelle eine Liste von Tupeln, wobei jedes Tupel aus einer Zahl und ihrem Quadrat besteht (für
   Zahlen von 1 bis 5).
10. **Dictionary Werte ändern**: Ändere im Dictionary von Aufgabe 4 den Wert von "c" zu 4.
11. **Set Operationen**: Erstelle die Vereinigung und Schnittmenge zweier Sets `{1, 2, 3}` und `{3, 4, 5}`.
12. **Listenelemente filtern**: Erstelle eine neue Liste aus der Liste von Aufgabe 1, die nur gerade Zahlen enthält.
13. **Schlüssel aus Dictionary entfernen**: Entferne den Schlüssel "a" aus dem Dictionary von Aufgabe 4.
14. **Element in Tupel überprüfen**: Überprüfe, ob die Zahl 3 im Tupel von Aufgabe 6 enthalten ist.
15. **Duplikate aus Liste entfernen**: Entferne alle Duplikate aus der Liste `[1, 2, 2, 3, 3, 4, 4, 5]`.

# Lösungen

## Floats, Integers, Booleans

Hier sind die Lösungen zu den vorgeschlagenen Übungsaufgaben zu Integers, Floats und Booleans in Python:

1. **Integer Addition**

```python
print(3 + 5)
```

2. **Integer Subtraktion**

```python
print(10 - 4)
```

3. **Float Division**

```python
print(7.5 / 2.5)
```

4. **Multiplikation von Integers**

```python
print(6 * 8)
```

5. **Konvertierung von Float zu Integer**

```python
print(int(7.8))
```

6. **Vergleich von Integers**

```python
print(5 > 3)
```

7. **Booleansches AND**

```python
print(True and False)
```

8. **Booleansches OR**

```python
print(False or True)
```

9. **Umwandlung von Integer in Boolean**

```python
print(bool(0))  # False
print(bool(5))  # True
```

10. **Modulo-Operator mit Integers**

```python
print(10 % 3)
```

11. **Potenzierung von Floats**

```python
print(5.5 ** 3)
```

12. **Vergleich von Floats**

```python
print(5.5 == 5.5)
```

13. **Integer in Float konvertieren**

```python
print(float(7))
```

14. **Negation eines Booleans**

```python
print(not True)
```

15. **Kombination von Booleans und Integers**

```python
num = 5
print(num > 0)
```

16. **Diskussion**:
    Integer: Wenn es nur ganze Zahlen Sinn ergeben, z.B. Alter, Geburtsjahr
    Floats: Wenn auch Bruchteile relevant sind, z.B. Gewicht
17. **Diskussion**:
    Nein, Fließkommazahlen haben keine unendlich hohe Genauigkeit. Für viele Anwendungen reicht dies aus, aber
    inbesondere
    wenn sehr viele Berechnungen durchgeführt werden, können diese Ungenauigkeiten zu signifikanten Abweichungen führen.
    Deswegen verwendet man zum Beispiel für Geldbeträge auch immer Integer und nutzt die kleines WÄhrungseinheit. Erst
    zur
    Ausgabe wird umgerechnet.

Diese Lösungen decken grundlegende Operationen mit Integers, Floats und Booleans in Python ab. Sie bieten praktische
Beispiele, die das Verständnis dieser Datentypen und ihrer Anwendungen in der Programmierung verbessern.

## Lists, Tupels, Sets, Dictionaries

Hier sind die Lösungen zu den gestellten Übungsaufgaben zu Listen, Tupeln, Sets und Dictionaries in Python:

1. **Liste erstellen**
```python
liste = [i for i in range(1, 11)]
```

2. **Tupel zu Liste**
```python
tupel = (1, 2, 3)
liste = list(tupel)
```

3. **Elemente zu Set hinzufügen**
```python
s = {1, 2, 3}
s.update([4, 5, 6])
```

4. **Schlüssel-Wert-Paare in Dictionary**
```python
dictionary = {"a": 1, "b": 2, "c": 3}
```

5. **Liste invertieren**
```python
liste = liste[::-1]
```

6. **Tupel aus Listen**
```python
tupel = tuple(liste[:3])
```

7. **Element aus Set entfernen**
```python
s.remove(4)  # Entfernt die Zahl 4 aus dem Set
```

8. **Werte aus Dictionary abrufen**
```python
wert = dictionary["b"]
```

9. **Liste von Tupeln**
```python
liste_von_tupeln = [(i, i**2) for i in range(1, 6)]
```

10. **Dictionary Werte ändern**
```python
dictionary["c"] = 4
```

11. **Set Operationen**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
vereinigung = set1 | set2
schnittmenge = set1 & set2
```

12. **Listenelemente filtern**
```python
gerade_zahlen = [i for i in liste if i % 2 == 0]
```

13. **Schlüssel aus Dictionary entfernen**
```python
del dictionary["a"]
```

14. **Element in Tupel überprüfen**
```python
enthalten = 3 in tupel
```

15. **Duplikate aus Liste entfernen**
```python
liste_ohne_duplikate = list(set([1, 2, 2, 3, 3, 4, 4, 5]))
```

Diese Lösungen decken eine breite Palette von Operationen und Techniken ab, die mit Listen, Tupeln, Sets und
Dictionaries in Python durchgeführt werden können, und bieten praktische Beispiele für den Umgang mit diesen wichtigen
Datenstrukturen.