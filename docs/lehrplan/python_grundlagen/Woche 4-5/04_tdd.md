# Tests schreiben
[180min]

## Fehlerarten

Es gibt unterschiedliche Fehlerarten. Während der Programmentwicklung gibt es immer wieder "kleine Fehler", häufig sind es Tippfehler. Irgendwo fehlt immer mal ein Doppelpunkt, so zum Beispiel hinter einem "else", oder man hat vielleicht "true" statt "True" geschrieben.

All dies sind sogenannte syntaktische Fehler oder Syntaxfehler. Dabei handelt es
sich um die Verletzung von Schreibweisen von einzelnen Wörtern, also zum Beispiel Schlüsselwörtern oder von Strukturregeln. In der Linguistik würde man
das als Satzbauregeln bezeichnen, also zum Beispiel der vergessene Doppelpunkt hinter dem "else" oder eckiger statt runder Klammer bei einem Funktionsaufruf.

Neben den syntaktischen Fehlern, die sich häufig relativ leicht finden und beheben lassen, gibt es auch die semantischen Fehler. Betrachten wir folgenden
Programmausschnitt:

```python
x = int(input("x? "))
y = int(input("y? "))

if x > 10:
    if y == x:
        print("Fine")
else:
    print("So what?")
```

Es gibt zwei if-Anweisungen, aber nur eine else-Anweisung. Das Codefragment ist syntaktisch korrekt. Es könnte aber sein, dass der Schreiber des Programmes den
Text "So what?" nur ausgeben wollte, wenn x größer als 10 ist und der Wert von y nicht dem von x entspricht. Das bedeutet, dass er folgenden Code hätte
schreiben müssen:

```python
x = int(input("x? "))
y = int(input("y? "))

if x > 10:
    if y == x:
        print("Fine")
    else:
        print("So what?")
```

Beide Programme bzw. Programmfragmente sind syntaktisch korrekt. Aber einer von beiden verstößt gegen die intendierte Semantik, dass der Text "So what?" nur
ausgegeben werden sollte, wenn x größer als 10 ist und der Wert von y nicht dem von x entspricht. Der Programmierer hatte wahrscheinlich die Semantik der if-Anweisung korrekt verstanden, aber sein Problem nicht richtig umgesetzt. Es
ist aber auch denkbar, dass ein Programmierer die Semantik eines Python-Konstruktes nicht richtig verstanden und deshalb einen Fehler produziert hat. Betrachten wir hierzu das folgende Beispiel:

```bash
>>> for i in range(7):
...     print(i)
... 
0
1
2
3
4
5
6
>>> 
```

Aus der Tatsache, dass es keinen Fehler bei der Ausführung gab, ersehen wir, dass diese Anweisungen syntaktisch korrekt sind. Ob sie jedoch semantisch korrekt sind, können wir nicht entscheiden, da wir ja nicht die Problemstellung kennen. Nehmen wir an, dass der Programmierer die Zahlen von 1 bis 7 hatte
ausgeben wollen. In diesem Fall hat er einen semantischen Fehler begangen, der wohl daraus resultiert, dass er die range-Funktion nicht richtig verstanden hat.
Er ging irrtümlich davon aus, dass range(7) die Zahlen von 1 bis 7 produziere, d.h. 1, 2, 3, 4, 5, 6 und 7. Wir können also die Semantikfehler in zwei Gruppen
unterteilen:

* Fehler, die aus dem mangelnden Verständnis eines Sprachkonstrukts herrühren.
* Fehler, die aus der fehlerhaften Umsetzung des Problems resultieren.

Modultests
==

Für den Begriff Modultest oder Komponententest wird häufig im Deutschen der englische Begriff "Unittest" ("unit test") verwendet.  Modultests verwendet man
in der Software-Entwicklung, um Module, - also funktionale Einzelteile eines Programmes, - zu testen, d.h. man prüft, ob sie die geforderte Funktionalität bringen. Es empfiehlt sich, Tests auf Modulebene durchzuführen, da die dortigen
Funktionalitäten noch eine begrenzte bzw. überschaubare Komplexität zeigen und die Schnittstellen noch klar definiert sind. Häufig kann man so ein Modul
vollständig auf Korrektheit prüfen. Dies ist auf einem umfassenden Software-Paket in der Regel nicht mehr möglich. Niemand kann beispielsweise ein
Betriebssystem vollständig auf Korrektheit prüfen.

Modultests unter Benutzung von `__name__`
==

Jedes Python-Modul hat einen im built-in-Attribut `__name__` definierten Namen.

Nehmen wir an, wir haben ein Modul mit dem Namen `abc` unter `abc.py` gespeichert. Wird dieses Modul mit `import abc` importiert, dann hat das built-in-Attribut `__name__` den Wert `abc`. Wird die Datei `abc.py` als
eigenständiges Programm aufgerufen, also mittels

```bash
$ python3 abc.py
```

dann hat diese Variable den Wert `__main__`.

Anhand des folgenden Modul, - das sowohl eine einzelne Fibonacci-Zahl für eine bestimmte Generation n als auch die Liste der Fibonacci-Zahlen bis zu einer
Generation n berechnen kann, - wollen wir veranschaulichen, wie man mit dem built-in-Attribut `__name__` einen einfachen, aber sehr wirkungsvollen Modultest durchführen kann.

Das fibonacci-Modul sieht wie folgt aus und ist unter dem Namen `fibonacci.py` in unserem Beispielverzeichnis zu finden:

```python
""" Modul mit wichtigen Funktionen zur Fibonacci-Folge """

def fib(n):
    """ Die Fibonacci-Zahl für die n-te 
        Generation wird iterativ berechnet """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ produziert die Liste der Fibbo-Zahlen 
        bis zur n-ten Generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib
```

Natürlich kann man dieses Modul auch "manuell" in der interaktiven Python-Shell testen:

```bash
>>> from fibonacci import fib, fiblist
>>> fib(0)
0
>>> fib(1)
1
>>> fib(10)
55
>>> fiblist(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> fiblist(-8)
[0, 1]
>>> fib(-1)
0
>>> fib(0.5)
Traceback (most recent call last):
  File "", line 1, in 
  File "fibonacci.py", line 6, in fib
    for i in range(n):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
```

Wir sehen, dass die Funktionen auf Integer-Zahlen definiert sind. Für negative ganze Zahlen liefert die Funktion fib nur Nullen zurück, während fiblist nur die Liste [0,1] zurückliefert. Ruft man die Funktionen mit Float-Zahlen auf, gibt es einen TypeError, weil range nicht für Float-Werte definiert ist.  Wir könnten
unser nun Modul testen, ob die Aufrufe für `fib()` und `fiblist()` für bestimmte Werte definierte Ergebniswerte zurückliefern. Man könnte also unser Modul
direkt um eine oder mehrere if-Anweisungen erweitern:

```python
if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
    print("Test für fib-Funktion erfolgreich")
else:
    print("fib-Funktion liefert fehlerhafte Werte")
```

Ruft man das Programm dann direkt auf, erhält man folgende Ausgabe:

```bash
$ python3 fibonacci.py 
Test für fib-Funktion erfolgreich
```

Nun wollen wir bewusst einen Fehler in unsere fib-Funktion einbauen. Dazu ändern wir die Zeile

```python
a, b = 0, 1  
```

in

```python
a, b = 1, 1
```

um.

Im Prinzip liefert fib zwar noch die Fibonacci-Werte, aber um eins versetzt. Wollen wir den n-ten Wert (für n größer als 0 berechnen), so müssen wir fib(n-1) aufrufen. Ein Aufruf des veränderten Moduls liefert nun eine Fehlermeldung:

```python
$ python3 fibonacci.py 
fib-Funktion liefert fehlerhafte Werte
```

Dieses Vorgehen hat jedoch einen entscheidenden Nachteil. Wenn man das Modul importiert, wird auch das Ergebnis dieses oder ähnlicher Tests angezeigt:

```bash
>>> import fibonacci
Test für fib-Funktion erfolgreich
```

Es ist aber störend und auch nicht üblich, wenn Module solche Meldungen beim import ausgeben. Module sollen sich "schweigend" laden lassen.

Die Lösung für dieses Problem stellt das eingangs erwähnte built-in-Attribut `__name__` dar. Wird unser Modul direkt gestartet, also nicht importiert, hat `__name__` den Wert `"__main__"`.  Wir können unser Modul nun so umschreiben, dass die Tests nur gestartet werden, wenn das Modul direkt gestartet wird:

```python
""" Modul mit wichtigen Funktionen zur Fibonacci-Folge """

def fib(n):
    """ Iterative Fibonacci-Funktion """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ produziert Liste der Fibbo-Zahlen """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("Test für fib-Funktion erfolgreich")
    else:
        print("fib-Funktion liefert fehlerhafte Werte")
```

Nun gibt es keine Ausgaben, wenn das Modul importiert wird, und zwar weder im Fehlerfall noch im Erfolgsfall.  Diese Methode ist die einfachste und am
weitesten verbreitetste Methode für Modultests.

doctest-Modul
==

Das doctest-Modul stellt eine weitere einfache Methode dar, Modultests durchzuführen. Der eigentliche Test befindet sich bei dieser Methode, wie der
Name vermuten lässt, im Docstring.

### Vorgehensweise:

Man muss das Modul "doctest" importieren. Dann kopiert man einen Auszug aus einer interaktiven Sitzung in den Docstring einer Funktion.

Im Folgenden zeigen wir das Vorgehen an einem simplen Beispiel. Dazu haben wir das vorige fibonacci-Modul bis auf die Funktion fib abgespeckt:

```python
import doctest

def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
```

Dieses Modul rufen wir nun in einer interaktiven Python-Shell auf und lassen ein
paar Werte berechnen:

```bash
>>> from fibonacci import fib
>>> fib(0)
0
>>> fib(1)
1
>>> fib(10)
55
>>> fib(15)
610
>>> 
```

Diese Aufrufe mit den Ergebnissen kopieren wir aus der interaktiven Shell in den
Docstring unserer Funktion. Damit das Modul doctest aktiv wird, müssen wir die
Methode `testmod()` starten, falls das Modul direkt aufgerufen wird. Dies können
wir wie üblich mit einem Test des Attributs `__name__` auf den Wert `"__main__"`
machen. Das vollständige Modul sieht nun wie folgt aus:

```python
import doctest

def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet 

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 

    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__": 
    doctest.testmod()
```

Starten wir obiges Modul direkt mit dem Aufruf

```bash
$ python3 fibonacci_doctest.py
```

erhalten wir keine Ausgabe, weil alles okay ist.

Deshalb bauen wir wieder einen kleinen Fehler ein. Dazu ändern wir erneut die Zeile

```python
a, b = 0, 1
```

in

```python
a, b = 1, 1
```

um.

Nun erhalten wir folgende Ausgabe beim direkten Start des Moduls:

```bash
$ python3 fibonacci_doctest.py 
**********************************************************************
File "fibonacci_doctest.py", line 8, in __main__.fib
Failed example:
    fib(0)
Expected:
    0
Got:
    1
**********************************************************************
File "fibonacci_doctest.py", line 12, in __main__.fib
Failed example:
    fib(10) 
Expected:
    55
Got:
    89
**********************************************************************
File "fibonacci_doctest.py", line 14, in __main__.fib
Failed example:
    fib(15)
Expected:
    610
Got:
    987
**********************************************************************
1 items had failures:
   3 of   4 in __main__.fib
***Test Failed*** 3 failures.
```

Es werden alle Aufrufe angezeigt, die ein fehlerhaftes Ergebnis geliefert haben.
Wir sehen jeweils den Beispielaufruf hinter der Zeile "Failed example:". Hinter
"Expected:" folgt der erwartete Wert, also der korrekte Wert, und hinter "Got:"
folgt der von der Funktion produzierte Ausdruck, also der Wert, den doctest beim
Aufruf von fib erhalten hat.

unittest
==

Eine weitere Möglichkeit Unittests zu schreiben ist mittels des Pakets `unittest`. Der offensichtlichste Unterschied zum Modul `doctest` besteht darin, dass die
Testfälle bei dem Modul "unittest" außerhalb des eigentlichen Programmcodes definiert werden, d.h. in einer eigenen Datei. Der Vorteil besteht unter anderem
darin, dass die Programmdokumentation und die Testbeschreibungen voneinander getrennt sind. Der Preis dafür besteht besteht jedoch in einem erhöhten Aufwand
für die Erstellung der Tests.

### Vorgehen

Wir wollen nun für unser Modul `fibonacci.py` einen Test mit unittest erstellen. In einer Datei, z.B. `fibonacci_unittest.py`, müssen wir das Modul unittest und
das zu testende Modul, also in unserem Fall `fibonacci`, importieren.

__Hinweis:__ Es empfiehlt sich eine einheitliche Konventions innerhalb des Projekts für die Dateinamen die Tests enthalten zu wählen. Wird _Visual Studio Code_ verwendet so sollte für die Ausführungserkennung das Wort `test` im Dateinamen vorkommen. Entweder `fibonacci_test.py` oder `test_fibonacci.py` abhängig davon, ob bevorzugt wird alle Testdateien im Dateibaum nebeneinandern zu haben, oder alternativ die Testdatei neben der Codedatei die sie testet liegen zu haben.

Außerdem müssen wir eine Klasse mit beliebigem Namen - wir wählen in unserem Beispiel `FibonacciTest` - erstellen, die von `unittest.TestCase` erbt. In dieser Klasse werden die nötigen Testfälle in Methoden definiert. __Der Name dieser Methoden ist beliebig, er muss jedoch mit test beginnen.__ In unserer Methode `testCalculation` benutzen wir die Methode `assertEqual` der Klasse
`TestCase`. `assertEqual(first, second, msg = None)` prüft, ob der Ausdruck `first` gleich dem Ausdruck `second` ist. Falls die beiden Ausdrücke ungleich
sind, wird `msg` ausgegeben, wenn `msg` ungleich `None` ist.

```python
import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

if __name__ == "__main__": 
    unittest.main()
```

Rufen wir obigen Testfall auf, erhalten wir folgende Ausgabe:

```bash
$ python3 fibonacci_unittest.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Bei der normalen Programmentwicklung ist dies das von uns gewünschte Ergebnis.

Hier sind wir allerdings interessiert, was im Fehlerfall passiert. Wir produzieren deshalb wieder unseren Fehler. Dazu ändern wir von neuem die Zeile

```python
a, b = 0, 1
```

in

```python
a, b = 1, 1
```

um.

Jetzt sieht der Test wie folgt aus:

```bash
$ python3 fibonacci_unittest.py 
F
======================================================================
FAIL: testCalculation (__main__.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "fibonacci_unittest.py", line 7, in testCalculation
    self.assertEqual(fib(0), 0)
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

Bereits die erste Anweisung in testCalculation hat eine Ausnahme erzeugt. In diesem Fall wurden die weiteren assertEqual-Aufrufe nicht mehr ausgeführt. Wir verändern fib nun dahingehend, dass wir nur einen falschen Wert erhalten, wenn n auf 20 gesetzt ist:

```python
def fib(n):
    """ Iterative Fibonacci-Funktion """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    if n == 20:
        a = 42    
    return a
```

Die Ausgabe eines Testlaufs sieht nun wie folgt aus:

```bash
$ python3 fibonacci_unittest.py 
F
======================================================================
FAIL: testCalculation (__main__.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "fibonacci_unittest.py", line 12, in testCalculation
    self.assertEqual(fib(20), 6765)
AssertionError: 42 != 6765

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

Jetzt wurden aber auch die folgenden Anweisungen durchgeführt, allerdings
generierten sie keine Ausnahme, da ihre Ergebnisse ja korrekt sind:

```python
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
```



### Methoden der Klasse TestCase

Wir wollen nun näher auf die Klasse TestCase eingehen. Wir stellen dazu einige
wichtige Methoden dieser Klasse vor. Zunächst stellen wir die beiden
Hook-Methoden `setUp()` und `tearDown()` vor.

| Methode  | Bedeutung |
| --- | --- |
| setUp()  | Bei der Methode setUp handelt es sich um eine sogenannte Hook-Methode. Sie wird vor jedem Aufruf der implementierten Testmethoden aufgerufen. Wird in der Methode setUp eine Ausnahme generiert, so wird diese auch als Error in der Testausgabe ausgegeben. Selbstverständlich wird auch bei einer Ausnahme im setUp-Code der Test abgebrochen. |
| tearDown()  | Die Methode tearDown wird nach dem Aufruf einer Testmethode gestartet. Ebenso wie bei setUp gilt, dass im Code von tearDown generierte Ausnahmen auch in der Testausgabe ausgegeben werden. |
| assertEqual(self, first, second, msg=None)  | Der Test schlägt fehl, wenn die Parameter "first" und "second" nicht gleich sind. Dabei ist Gleichheit im Sinne von "==" gemeint, also Wertegleichheit und nicht nur reine Objektgleichheit. |
| assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)  | Diese Methode schlägt fehl, wenn die Differenz der beiden Parameter "first" und "second" gleich 0 ist, nachdem man sie vor dem Vergleich auf "places" Nachkommastellen gerundet hatte. Der Default-Wert für "places" ist 7. |
| assertCountEqual(self, first, second, msg=None)  | Die Parameter "first" und "second" müssen hierbei sequentielle Datentypen sein. Es muss folgendes gelten:<br>Alle Elemente müssen genauso oft in "first" wie in "second" vorkommen.<br><br>Beispiel:<br><br>[0, 1, 1] und [1, 0, 1] gelten in obigem Sinne als gleich, weil die 0 und die 1 jeweils gleich oft vorkommen.<br><br>[0, 0, 1] und [0, 1] sind verschieden, weil die 0 in der ersten Liste zweimal vorkommt und in der zweiten Liste nur einmal. |
| assertDictEqual(self, d1, d2, msg=None)  | Betrachtet die beiden Argumente als Dictionaries und prüft auf Gleichheit. |
| assertTrue(self, expr, msg=None)  | Prüft, ob der Ausdruck "expr" True ist. |
| assertGreater(self, a, b, msg=None)  | Prüft, ob a > b gilt. |
| assertGreaterEqual(self, a, b, msg=None)  | Prüft, ob a ≥ b gilt. |
| assertFalse(self, expr, msg=None)  | Prüft, ob der Ausdruck "expr" False ist. |
| assertLess(self, a, b, msg=None)  | Prüft, ob a < b gilt. |
| assertLessEqual(self, a, b, msg=None)  | Prüft, ob a ≤ b gilt. |
| assertIn(self, member, container, msg=None)  | Prüft, ob a in b gilt. |
| assertIs(self, expr1, expr2, msg=None)  | Prüft, ob "a is b" gilt. |
| assertIsInstance(self, obj, cls, msg=None)  | Prüft, ob isinstance(obj, cls) gilt. |
| assertIsNone(self, obj, msg=None)  | Prüft, ob "obj is None" gilt. |
| assertIsNot(self, expr1, expr2, msg=None)  | Prüft, ob "a is not b" gilt. |
| assertIsNotNone(self, obj, msg=None)  | Prüft, ob obj nicht None ist. |
| assertListEqual(self, list1, list2, msg=None)  | Listen werden auf Gleichheit geprüft. |
| assertMultiLineEqual(self, first, second, msg=None)  | Mehrzeilige Strings werden auf Gleichheit geprüft. |
| assertNotRegexpMatches(self, text, unexpected_regexp, msg=None)  | Schlägt fehl, wenn der Text "text" den regulären Ausdruck unexpected_regexp matched. |
| assertTupleEqual(self, tuple1, tuple2, msg=None)  | Analog zu assertListEqual |

> https://docs.python.org/3/library/unittest.html

Wir erweitern unser voriges Beispiel um eine setUp- und eine tearDown-Methode:

```python
import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.fib_elems = ( (0,0), (1,1), (2,1), (3,2), (4,3), (5,5) )
        print ("setUp executed!")

    def testCalculation(self):
        for (i,val) in self.fib_elems:
            self.assertEqual(fib(i), val)

    def tearDown(self):
        # Objekte können gelöscht oder geändert werden
        # in diesem Fall macht es jedoch wenig Sinn:
        self.fib_elems = None
        print ("tearDown executed!")

if __name__ == "__main__": 
    unittest.main()
```

Ein Aufruf führt zu folgendem Ergebnis:

```bash
$ python3 fibonacci_unittest2.py 
setUp executed!
tearDown executed!
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Die meisten der TestCase-Methoden verfügen über einen optionalen Parameter
`msg`. Mit `msg` kann man eine zusätzliche Beschreibung für einen Fehler
ausgeben.

## TDD: Testgetriebene Entwicklung
### oder "Am Anfang war der Test"

Im vorigen Abschnitt hatten wir bereits eine fertig geschriebene Fibonacci-Funktion. Man kann auch so vorgehen, dass man bereits am Anfang Ergebnisse in den Docstring schreibt und die Funktion dann erst entwickelt. Das ist die Grund-Idee von "Testgetriebener Entwicklung". Diese wird auf Englisch auch als **Test Driven Development** kurz **_TDD_** bezeichnet. Der Entwickler definiert ein Testszenario, welches die gewünschte Funktion abbildet. Zu Beginn wird der
Test fehlschlagen, denn der Code muss noch geschrieben werden.

Die Kunst dabei ist, passende Testszenarien zu schreiben. Es ist natürlich erstrebenswert, dass der Test alle möglichen Argumente und alle möglichen
Rückgabewerte prüft. Das ist aber in der Regel nicht machbar.

Im Folgenden haben wir den Rückgabewert der Funktion fib fest auf 0 gesetzt:

```python
import doctest

def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet 

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 

    """

    return 0

if __name__ == "__main__": 
    doctest.testmod()
```

Es versteht sich von selbst, dass ein Test dieses Moduls außer für fib(0) nur
Fehler liefert:

```bash
$ python3 fibonacci_TDD.py 
**********************************************************************
File "fibonacci_TDD.py", line 10, in __main__.fib
Failed example:
    fib(1)
Expected:
    1
Got:
    0
**********************************************************************
File "fibonacci_TDD.py", line 12, in __main__.fib
Failed example:
    fib(10) 
Expected:
    55
Got:
    0
**********************************************************************
File "fibonacci_TDD.py", line 14, in __main__.fib
Failed example:
    fib(15)
Expected:
    610
Got:
    0
**********************************************************************
1 items had failures:
   3 of   4 in __main__.fib
***Test Failed*** 3 failures.
```

Man ändert bzw. schreibt nun den eigentlichen Code der Funktion fib solange, bis die Tests im Doctest "bestanden" werden.

Dieses Vorgehen ist eine Methode der Software-Entwicklung, die man als "Testgetriebene Entwicklung" oder auch "Testgesteuerte Entwicklung" bezeichnet.

Aber wie so häufig in der Softwareentwicklungsbranche werden auch in diesem Fall die englischen
Fachbegriffe benutzt, d.h. "test first development" oder noch geläufiger "test-driven development" (TDD).

# Aufgabe
[150min]

1. Schreibe für das Codebeispiel `primzahlen.py` einen
    1. Modultest
    2. Unittest
    3. Doctest
2. Erstelle eine Klasse _Geo_ für geometrische Objekte (z.B. Rechteck, Quadrat, Kreis)
mit Berechnungsfunktionen für Umfang und Fläche. 
3. Teste die Korrektheit der _Geo_-Klasse mit Hilfe von doctests.
4. Nutze TDD um ein Klasse zu entwickeln, die mathematische Grundoperationen
ermöglicht, also z.B. `add()`, `sub()`, `mul()` und `div()`. Erstelle dazu das
Klassengerüst mit "leeren" Funktionen und entwickle zuerst die (Unit-)Testmethoden nach
dem Muster "Was muss das Ergebnis einer Addition, Subtraktion, etc sein".
Ziel ist es eine möglichst hohe Testabdeckung zu erreichen!
5. Welches Verhalten sollte bei der `div()` Methode umbedingt getestet werden? 

# Neue Schlüsselwörter



- **Unittest**: Das `unittest`-Modul ist ein integriertes Testframework in Python, das Testfälle und Testsuiten bereitstellt. Es ermöglicht die Strukturierung von Tests und das Vergleichen von erwarteten und tatsächlichen Ergebnissen. Unittests können dazu verwendet werden, die Korrektheit von Funktionen, Klassen und Modulen sicherzustellen.

[Python-Dokumentation zu unittest](https://docs.python.org/3/library/unittest.html)

- **assert**: In Python dient das `assert`-Statement dazu, eine Bedingung zu überprüfen und sicherzustellen, dass sie während der Ausführung wahr ist. Wenn die Bedingung falsch ist, wird eine `AssertionError`-Ausnahme ausgelöst. Die Verwendung von `assert` ist besonders nützlich für das Schreiben von Tests und die Gewährleistung von Invarianten im Code.
[Python-Dokumentation zu assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement).

- **TDD (Test-Driven Development)**: TDD, oder "Test Driven Development", ist eine Entwicklungspraxis, bei der Tests vor dem eigentlichen Code geschrieben werden. Der Zyklus besteht typischerweise aus den Schritten: 

Schreibe erst einen Test, führe den Test aus (er sollte fehlschlagen), schreibe den Code, um den Test zu bestehen, und führe den Test erneut aus. Dieser Ansatz fördert schrittweise Entwicklung von Funktionen und stellt sicher, dass jede Funktion getestet wird.

- **Doctest**: Das `doctest`-Modul ermöglicht das Schreiben von Tests innerhalb der Docstrings von Python-Modulen und -Funktionen. Es führt die in den Docstrings geschriebenen Beispiele aus und überprüft, ob die Ausgabe mit den erwarteten Ergebnissen übereinstimmt. Doctests sind eine praktische Möglichkeit, Tests direkt in der Dokumentation zu integrieren.
[Python-Dokumentation zu doctest](https://docs.python.org/3/library/doctest.html)

# Aufgaben

## 1. Primzzahlenfunktion testen 🌶️
   - Modultest: Schreibe Tests für das Modul `primzahlen.py`, um sicherzustellen, dass die Primzahlberechnung korrekt funktioniert.
   - Unittest: Erstelle Unittests für die Funktionen in `primzahlen.py` mit dem `unittest`-Framework.
   - Doctest: Integriere Beispiele und Tests direkt in die Docstrings des Moduls.

primzahlen.py: 

```python
def ist_primzahl(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

## 2. Geo-Funktionssammlung: 🌶️🌶️
   - Implementiere eine Funktionssammlung namens `Geo`, die geometrische Objekte berechnen kann (z.B., Rechteck, Quadrat, Kreis).
   - Füge Berechnungsmethoden für Umfang und Fläche hinzu.
   - Schreibe doctest-Tests, um die Korrektheit der Implementierung sicherzustellen.

## 3. Mathe-Funktionssammlung (TDD): 🌶️🌶️
   - Nutze TDD, um eine Funktionssammlung für mathematische Grundoperationen (`add()`, `sub()`, `mul()`, `div()`) zu entwickeln.
   - Schreibe zuerst die Unit-Tests und dann die Implementierung.
   - Achte auf eine hohe Testabdeckung.
   - Beachte insbesondere die Testfälle für die `div()` Methode, um sicherzustellen, dass unerwartete Fehler oder Divisionen durch Null behandelt werden.
   