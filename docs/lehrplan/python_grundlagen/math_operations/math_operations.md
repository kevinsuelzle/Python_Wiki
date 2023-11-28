
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

Üben wir das Ganze:


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



## Lösungen
1. `print(5 + 3)  # 8`
2. `print(10 - 2)  # 8`
3. `print(4 * 2)  # 8`
4. `print(16 / 2)  # 8.0`
5. `print(17 // 2)  # 8`
6. `print(18 % 10)  # 8`
7. `print(2 ** 3)  # 8`
8. `import math; print(math.sqrt(64))  # 8.0`
9. `import math; print(math.exp(3))  # etwa 20.085`
10. `import math; print(math.log(8, math.e))  # etwa 2.079`

11. `print((3 + 4) * 5)  # 35`
12. `print(2 * 3 == 6)  # True`
13. `print(round(2.7))  # 3`
14. `print(-3 * 3)  # -9`
15. `x = 5; print(x * x)  # 25`
16. `print(2 + 3 * 5)  # 17, da die Multiplikation zuerst ausgeführt wird`
17. `print((2 + 3) * 5)  # 25, da die Klammer zuerst ausgewertet wird`
18. `print(4 ** 2 / 8)  # 2.0, da zuerst potenziert und dann dividiert wird`
19. `print(3 + 4 * 2 - 1)  # 10, da Multiplikation vor Addition und Subtraktion ausgeführt wird`
20. `print((3 + 4) * (5 - 2) ** 2)  # 49, da zuerst die Klammern, dann die Potenzierung und zuletzt die Multiplikation ausgeführt wird`

### **Zinsrechner**
```python
# Benutzereingaben
anfangskapital = float(input("Gib das Anfangskapital ein: "))
zinssatz = float(input("Gib den Zinssatz in Prozent ein: "))
jahre = float(input("Gib die Anlagedauer in Jahren ein: "))

# Berechnung der Endsumme
endsumme = anfangskapital * (1 + zinssatz/100 * jahre)

# Ausgabe
print(f"Die Endsumme nach {jahre} Jahren beträgt: {endsumme:.2f} Euro")

```

### **Umrechner für Temperaturen**

```python
# Benutzereingaben
temperatur = float(input("Gib die Temperatur ein: "))
einheit = input("Ist die Temperatur in Celsius (C) oder Fahrenheit (F)? ")

# Umrechnung
if einheit.lower() == 'c':
    umgerechnet = temperatur * 9/5 + 32
    zieleinheit = "Fahrenheit"
elif einheit.lower() == 'f':
    umgerechnet = (temperatur - 32) * 5/9
    zieleinheit = "Celsius"

# Ausgabe
print(f"Die Temperatur in {zieleinheit} beträgt: {umgerechnet:.2f}°")

```