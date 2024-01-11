# Einführung in List Comprehensions in Python
[15min]
List Comprehensions in Python sind eine elegante und effiziente Möglichkeit, Listen zu erstellen und Operationen auf 
ihren Elementen auszuführen. Sie bieten eine klare und prägnante Alternative zu traditionellen Schleifen
und Funktionsaufrufen. List Comprehensions sind eine typische Struktur, die man in Python-Code häufig findet.

**Beispiel**

```python
quadrate = [i * i for i in range(1, 6)]

print(quadrate)  # Ausgabe: [1, 4, 9, 16, 25]
```

## Motivation für List Comprehensions
[35min]

1. **Kompakter Code**: List Comprehensions ermöglichen es, Schleifen und bedingte Anweisungen in einer Zeile zu
   schreiben, wodurch der Code kürzer und wenn man es nicht übertreibt auch leichter lesbar wird.

2. **Performance**: Sie sind oft schneller als traditionelle Schleifen, besonders bei der Erstellung großer Listen.

3. **Klarheit und Präzision**: Sie machen den Code ausdrucksstärker und klarer, indem sie genau beschreiben, was jede
   Liste enthält.

4. **Reduzierung von Boilerplate-Code**: Weniger Codezeilen bedeuten weniger Platz für Fehler und vereinfachen die
   Wartung des Codes.


## Problemstellungen
[35min]
Stellen wir unsh vor, wir möchten aus einer vorhandenen Liste eine neue Liste erstellen, in der jedes Element aufgrund
einer Bedingung oder einer Operation verändert wurde. Traditionell würden wir dazu eine for-Schleife verwenden, die
über die alte Liste iteriert, die Operation durchführt und das Ergebnis in einer neuen Liste speichert. Dies führt zu
mehrzeiligen Konstruktionen, die nicht nur umständlich, sondern auch fehleranfällig sein können.

List Comprehensions lösen dieses Problem, indem sie die gesamte Logik in eine einzige, lesbare Zeile komprimieren. Sie
können Bedingungen anwenden, Funktionen aufrufen und die resultierende Liste direkt erzeugen, was den Code wesentlich
sauberer und eleganter macht.

List Comprehensions bieten eine elegante Möglichkeit, for-Schleifen zu ersetzen, insbesondere wenn es darum geht, Listen
zu erstellen oder zu modifizieren. 

## Beispiel: Erstellen einer Liste mit Quadratzahlen

### Traditionelle Methode mit einer for-Schleife
[25min]
Angenommen, wir möchten eine Liste der Quadrate der Zahlen von 1 bis 5 erstellen. Mit einer for-Schleife könnte das so
aussehen:

```python
quadrate = []
for i in range(1, 6):
    quadrate.append(i * i)

print(quadrate)  # Ausgabe: [1, 4, 9, 16, 25]
```

In diesem Code erstellen wir zunächst eine leere Liste `quadrate`. Dann iterieren wir mit einer for-Schleife über die
Zahlen von 1 bis 5, berechnen das Quadrat jeder Zahl und fügen es der Liste `quadrate` hinzu.

### Ersetzen durch eine List Comprehension
[75min]
Die gleiche Aufgabe lässt sich mit einer List Comprehension viel kompakter lösen:

```python
quadrate = [i * i for i in range(1, 6)]

print(quadrate)  # Ausgabe: [1, 4, 9, 16, 25]
```

### Wie geht man vor?

1. **Ausdruck bestimmen**: Zuerst überlegen wir, welchen Wert jedes Element der neuen Liste haben soll. In unserem Fall
   ist es das Quadrat jeder Zahl `i * i`.

2. **Iteration definieren**: Dann bestimmen wir, über welchen Bereich oder welche Werte wir iterieren wollen. Hier
   verwenden wir `for i in range(1, 6)`, um über die Zahlen 1 bis 5 zu iterieren.

3. **List Comprehension formulieren**: Diese beiden Teile setzen wir in der Syntax der List Comprehension
   zusammen: `[ausdruck for item in iterable]`. In unserem Fall ist das `[i * i for i in range(1, 6)]`.

### Vorteile der List Comprehension
[15min]

- **Kürzer und klarer**: Der Code ist kürzer und oft leichter zu verstehen.
- **Direkte Erstellung der Liste**: Es ist keine separate Initialisierung einer leeren Liste und kein anschließendes
  Hinzufügen von Elementen notwendig.
- **Performance**: In vielen Fällen sind List Comprehensions schneller als eine entsprechende for-Schleife.

List Comprehensions sind ein hervorragendes Beispiel für *pythonic* Code, also Code der typisch für Python-Programme
ist und die jeder kennen und verstehen sollte.

# Aufgaben
[75min]

### 1. **Quadrate erstellen**: 🌶️
Erstelle eine Liste der Quadrate der Zahlen von 1 bis 10.
### 2. **Gerade Zahlen**: 🌶️
Erzeuge eine Liste aller geraden Zahlen zwischen 1 und 20.
### 3. **Ungerade Zahlen umwandeln**: 🌶️
Verwandle jede ungerade Zahl in einer Liste von 1 bis 10 in ihr Quadrat.
### 4. **Zeichenkettenlängen**: 🌶️
Erstelle eine Liste mit den Längen jedes Wortes in einer vorgegebenen Liste von Wörtern.
### 5. **Absolute Werte**: 🌶️
Wandele eine Liste von Zahlen in eine Liste ihrer absoluten Werte um.
### 6. **Filtern nach Bedingung**: 🌶️
Erzeuge eine Liste aller Zahlen von 1 bis 20, die durch 3 teilbar sind.
### 7. **String in Großbuchstaben**: 🌶️🌶️
Konvertiere jede Zeichenkette in einer Liste in Großbuchstaben.
### 8. **Tupel erstellen**: 🌶️
Erstelle eine Liste von Tupeln `(x, x*x)` für jede Zahl x von 1 bis 10.
### 9. **Nicht-leere Strings**: 🌶️
Filtere eine Liste von Strings und behalte nur die nicht-leeren bei.
### 10. **Negative Zahlen umkehren**: 🌶️
Erstelle eine Liste, in der alle negativen Zahlen einer vorgegebenen Liste positiv
    sind.
### 11. **Fizz Buzz**: 🌶️🌶️
Erstelle eine Liste von Strings "Fizz", "Buzz" oder "FizzBuzz" für Zahlen von 1 bis 15, abhängig
    davon, ob die Zahl durch 3, 5 oder beide teilbar ist.
### 12. **Wurzeln ziehen**: 🌶️
Berechne die Quadratwurzel jeder Zahl in einer Liste von Zahlen.
### 13. **Filtern und Umwandeln**: 🌶️
Filtere eine Liste von Zahlen und behalte nur die geraden Zahlen bei, die dann verdoppelt
    werden.
### 14. **Teile von Strings**: 🌶️🌶️
Erstelle eine Liste der ersten Zeichen jedes Wortes in einer Liste von Wörtern.
### 15. **Vokale entfernen**: 🌶️🌶️
Entferne alle Vokale aus jeder Zeichenkette in einer Liste von Strings.
### 16. **Einzigartige Werte**: 🌶️🌶️🌶️
Erstelle eine Liste einzigartiger Zahlen aus einer Liste mit Duplikaten.
### 17. **Index und Wert**: 🌶️🌶️
Erstelle eine Liste von Tupeln, die den Index und den Wert jedes Elements in einer vorgegebenen
    Liste enthalten.
### 18. **Summe von Paaren**: 🌶️🌶️
Erstelle eine Liste aller Paare von Zahlen in einer Liste, deren Summe 10 ergibt.
### 19. **Durchschnittswerte**: 🌶️🌶️
Berechne den Durchschnitt von jedem Paar aufeinanderfolgender Zahlen in einer Liste.
### 20. **Liste von Listen abflachen**: 🌶️🌶️🌶️
Flache eine Liste von Listen zu einer einzigen Liste ab.

[Lösungen](solutions.md)
