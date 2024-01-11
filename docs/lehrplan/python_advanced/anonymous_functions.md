# Anonyme Funktionen

#### Ein geschichtlicher Hintergrund
Alonzo Church hat in den 1930er Jahren die Lambda-Kalkül formalisiert, eine Sprache, die auf reiner Abstraktion basiert. Lambda-Funktionen werden auch als Lambda-Abstraktionen bezeichnet, was direkt auf das Abstraktionsmodell von Alonzo Church's Originalkreation verweist.

Der Lambda-Kalkül kann jede Berechnung codieren. Er ist Turing-vollständig, aber im Gegensatz zum Konzept einer Turing-Maschine ist er rein und behält keinen Zustand.

Funktionale Sprachen haben ihren Ursprung in mathematischer Logik und dem Lambda-Kalkül, während imperative Programmiersprachen das zustandsbasierte Berechnungsmodell von Alan Turing übernommen haben. Die beiden Berechnungsmodelle, Lambda-Kalkül und Turing-Maschinen, können ineinander übersetzt werden. Diese Äquivalenz wird als die Church-Turing-Hypothese bezeichnet.

Funktionale Sprachen übernehmen direkt die Philosophie des Lambda-Kalküls und setzen auf einen deklarativen Programmieransatz, der Abstraktion, Datenverarbeitung, Komposition und Reinheit (kein Zustand und keine Seiteneffekte) betont. Beispiele für funktionale Sprachen sind Haskell, Lisp oder Erlang.

Im Gegensatz dazu führte die Turing-Maschine zur imperativen Programmierung, die in Sprachen wie Fortran, C oder Python zu finden ist.

Der imperative Stil besteht darin, mit Anweisungen zu programmieren und den Programmfluss schrittweise mit detaillierten Anweisungen zu steuern. Dieser Ansatz fördert Mutation und erfordert das Management von Zuständen.

Die Trennung in beiden Sprachfamilien hat einige Nuancen, da einige funktionale Sprachen imperative Funktionen integrieren, wie zum Beispiel OCaml, während funktionale Funktionen die imperative Sprachfamilie durch die Einführung von Lambda-Funktionen in Java oder Python durchdrungen haben.

Python ist an sich keine funktionale Sprache, hat aber frühzeitig einige funktionale Konzepte übernommen. Im Januar 1994 wurden map(), filter(), reduce() und der Lambda-Operator der Sprache hinzugefügt.

```python 
def identity(x):
    return x
```

```python 
lambda x: x
```

```python 
lambda x: x + 1
```

Die Funktion oben lässt sich dann so schreiben:
```python 
(lambda x: x + 1)(2)

```

```python 
add_one = lambda x: x + 1
add_one(2)
```

```python 
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
```

```python 
lambda x, y: x + y
```

```python 
high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)

high_ord_func(2, lambda x: x + 3)
```

#### Statements sind verboten!
 in einer Lambda-Funktion können keine Anweisungen verwendet werden. Statements wie return, pass, assert oder raise führen zu einer SyntaxError-Ausnahme. Hier ist ein Beispiel, wenn versucht wird, assert im Körper einer Lambda-Funktion zu verwenden:

```python 
(lambda x: assert x == 2)(2) # SyntaxError: invalid syntax
```

#### Type Annotations
```python 
lambda first: str, last: str: first.title() + " " + last.title() -> str
```

#### Argumente
Wie bei einem normalen Funktionsobjekt, das mit def definiert ist, unterstützen Python Lambda-Ausdrücke alle verschiedenen Arten der Argumentübergabe. Dazu gehören:

Positionale Argumente
Benannte Argumente (manchmal als Schlüsselwortargumente bezeichnet)
Variable Liste von Argumenten (oft als Varargs bezeichnet)
Variable Liste von Schlüsselwortargumenten
Nur-Schlüsselwortargumente
Die folgenden Beispiele veranschaulichen die Möglichkeiten, wie Sie Argumente an Lambda-Ausdrücke übergeben können:

```python 
(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1,2,3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
```

#### Decorators
Sogar ein Dekorator kann auf eine Lambda-Funktion angewendet werden. Obwohl es nicht möglich ist, eine Lambda-Funktion mit der @decorator-Syntax zu dekorieren, ist ein Dekorateur einfach eine Funktion. Daher kann er die Lambda-Funktion aufrufen:

```python 
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
```


Oben add_two(), dekoriert mit @trace. Im Gegensatz dazu wird in Zeile 18 eine Lambda-Funktion sofort aufgerufen und in einen Aufruf von trace(), dem Dekorator, eingebettet. Wenn Sie den obigen Code ausführen, erhalten Sie folgendes:

#### Closures:

Closures gefällig? Kein Problem!

```python 
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
```


#### Evaluation Time

In Schleifen verhält sich eine Python-Lambda-Funktion als Closure manchmal unerwartet. Es erfordert ein Verständnis dafür, wann freie Variablen im Kontext einer Lambda gebunden werden. Die folgenden Beispiele zeigen den Unterschied zwischen der Verwendung einer regulären Funktion und der Verwendung einer Python-Lambda.

Wir testen das Szenario zunächst mit einer regulären Funktion:

```python 
def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
```

Als La,bda Funktion führt das zu folgendem anderen Verhalten.

```python 
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
```
Das unerwartete Ergebnis tritt auf, weil die freie Variable n, wie implementiert, zur Ausführungszeit des Lambda-Ausdrucks gebunden wird.

Auf folgende Art und Weise kann man das Problem lösen:

```python 
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()
```

#### unittest

Auch Unittests sind kein Problem mit lambda-Functions.

```python 
import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

Hier bildet die Klasse LambdaTest ein Testszenario mit drei Test Methods. 

```shell
$ python lambda_unittest.py
test_add_three (__main__.LambdaTest) ... FAIL
test_add_two (__main__.LambdaTest) ... ok
test_add_two_point_two (__main__.LambdaTest) ... ok

======================================================================
FAIL: test_add_three (__main__.LambdaTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "lambda_unittest.py", line 18, in test_add_three
    self.assertEqual(addtwo(3), 6)
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```


#### Doctest

Das doctest-Modul extrahiert interaktiven Python-Code aus Docstrings, um Tests auszuführen. Obwohl die Syntax von Python-Lambda-Funktionen keine typische Docstring unterstützt, ist es möglich, einem benannten Lambda eine Zeichenkette zuzuweisen und sie dem __doc__ Element zuzuordnen:

```python 
addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```

Als nächstes in der Shell ausführen:


```shell
$ python lambda_doctest.py
Trying:
    addtwo(2)
Expecting:
    4
ok
Trying:
    addtwo(2.2)
Expecting:
    4.2
ok
Trying:
    addtwo(3) # Should fail
Expecting:
    6
**********************************************************************
File "lambda_doctest.py", line 16, in __main__.addtwo
Failed example:
    addtwo(3) # Should fail
Expected:
    6
Got:
    5
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   1 of   3 in __main__.addtwo
3 tests in 2 items.
2 passed and 1 failed.
***Test Failed*** 1 failures.
```

#### Lambda Expression No-Go

Mehrere Beispiele in diesem Artikel würden, wenn sie im Kontext professionellen Python-Codes geschrieben wären, als No-Go gelten.

Stellst du fest, dass du versuchst, etwas zu überwinden, was eine Lambda-Funktion nicht unterstützt, ist dies wahrscheinlich ein Zeichen dafür, dass eine normale Funktion besser geeignet wäre. Die Docstring für einen Lambda-Ausdruck im vorherigen Abschnitt ist ein gutes Beispiel. Der Versuch, die Tatsache zu überwinden, dass eine Python-Lambda-Funktion keine Anweisungen unterstützt, ist ein weiteres Warnsignal.

Die nächsten Abschnitte zeigen einige Beispiele für die Verwendung von Lambdas, die vermieden werden sollten. Diese Beispiele könnten Situationen sein, in denen der Code im Kontext von Python-Lambda das folgende Muster aufweist:

Es folgt nicht dem Python-Style-Guide (PEP 8).
Es ist umständlich und schwer zu lesen.
Es ist unnötig clever auf Kosten der Lesbarkeit.


#### Keine Ausnahmen in Lambda-Functions erzeugen

```python 
def throw(ex): raise ex
(lambda: throw(Exception('Something bad happened')))()
```
Merke: Siehst du solchen Code, solltest du den Code sofort umzugestalten, dass eine reguläre Funktion verwendet wird. 

#### Cryptischer Stil
Wie in jeder Programmiersprache finden Sie auch in Python Code, der aufgrund des verwendeten Stils schwer zu lesen sein kann. Lambda-Funktionen können aufgrund ihrer Kürze dazu neigen, schwer lesbaren Code zu schreiben.

```python 
(lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
```
Es ist viel besser den Variablen Namen zu geben als sie nicht explizit zu benennen.

```python 
(lambda some_list: list(map(lambda n: n // 2, some_list)))([1,2,3,4,5,6,7,8,9,10])

```
Zugegebenermaßen ist es immer noch schwierig zu lesen. Indem man weiterhin von einer Lambda Gebrauch macht, könnte eine normale Funktion dazu beitragen, diesen Code lesbarer zu gestalten, indem man die Logik auf mehrere Zeilen und Funktionsaufrufe verteilt:

```python 
def div_items(some_list):
    div_by_two = lambda n: n // 2
    return map(div_by_two, some_list)

list(div_items([1,2,3,4,5,6,7,8,9,10]))
```
Das ist immer noch nicht optimal, zeigt aber einen möglichen Weg, Code und insbesondere Python-Lambda-Funktionen, lesbarer zu gestalten. Man kann map() und lambda durch Listenabstraktionen oder Generatorausdrücke ersetzen. Dies wird die Lesbarkeit des Codes erheblich verbessern.

#### Python Klassen
Class-Methods als Lambda Ausdrücke sind schlecht. Das folgende Beispiel ist gültiger Python-Code, zeigt jedoch unkonventionellen Python-Code, der auf Lambda basiert. Zum Beispiel verwendet es anstelle der Implementierung von __str__ als reguläre Funktion ein Lambda. Ebenso sind brand und year Eigenschaften, die ebenfalls mit Lambda-Funktionen implementiert sind, anstelle von regulären Funktionen oder Decorators:

```python 
class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'  # 1: error E731

    honk = lambda self: print('Honk!')     # 2: error E731
```


Das Guide Enforcement Tool flake8 würde folgende Bemerkung ausspucken:

```shell
E731 do not assign a lambda expression, use a def
```
So kann man es besser machen:

```python 
def __str__(self):
    return f'{self.brand} {self.year}'
```

Brand würde man dann so schreiben:

```python 
@property
def brand(self):
    return self._brand

@brand.setter
def brand(self, value):
    self._brand = value
```
Als allgemeine Regel im Kontext von in Python geschriebenem Code einfach reguläre Funktionen gegenüber Lambda-Ausdrücken bevorzugen. Dennoch gibt es Fälle, in denen die Lambda-Syntax von Vorteil ist, wie Sie im nächsten Abschnitt sehen werden.


#### Angemessene Verwendung von Lambda-Ausdrücken
Lambdas in Python neigen dazu, Gegenstand von Kontroversen zu sein. Einige der Argumente gegen Lambdas in Python sind:

Probleme mit der Lesbarkeit
Die Auferlegung einer funktionalen Denkweise
Schwere Syntax mit dem Schlüsselwort lambda
Trotz der hitzigen Debatten über die bloße Existenz dieses Features in Python haben Lambda-Funktionen Eigenschaften, die manchmal einen Mehrwert für die Python-Sprache und Entwickler bieten.

Die folgenden Beispiele veranschaulichen Szenarien, in denen die Verwendung von Lambda-Funktionen angemessen ist.

#### Classicche functionale Konstrukte
Lambda Ausdrücke verwendet man häufig in Kombination mit map(), filter() und functools.reduce()

```python 
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
```


#### Python Interpreter
Im interaktiven Interpreter sind Python-Lambda-Funktionen oft ein Segen. Es ist einfach, eine schnelle Einzeiler-Funktion zu erstellen, um einige Code-Schnipsel zu erkunden, die außerhalb des Interpreters nie das Licht der Welt erblicken werden. Die in diesem Sinne im Interpreter geschriebenen Lambdas sind wie Schmierpapier, das Sie nach Gebrauch wegwerfen können.

timeit
Insbesondere kann timeit.timeit() direkt aufgerufen werden, indem man Python-Code in einem String übergibt. Hier ist ein Beispiel:

```python 
from timeit import timeit
timeit("factorial(999)", "from math import factorial", number=10)
```
Wenn die Anweisung als Zeichenkette übergeben wird, benötigt timeit() den vollständigen Kontext. Im obigen Beispiel wird dies durch das zweite Argument bereitgestellt, das die Umgebung einrichtet, die von der Hauptfunktion benötigt wird, um gemessen zu werden. Wenn dies nicht getan wird, würde dies eine NameError-Ausnahme auslösen.

Und jetzt der Lambda-Ansatz:

```python 
from math import factorial
timeit(lambda: factorial(999), number=10)
```

Diese Lösung ist sauberer, besser lesbar und schneller einzugeben im Interpreter. Obwohl die Ausführungszeit für die Lambda-Version geringfügig kürzer war, könnte die Ausführung der Funktionen erneut einen leichten Vorteil für die Zeichenketten-Version zeigen. Die Ausführungszeit des Setups wird aus der Gesamtausführungszeit ausgeschlossen und sollte keinen Einfluss auf das Ergebnis haben.

#### Monkey Patching

Für Tests ist es manchmal notwendig, sich auf reproduzierbare Ergebnisse zu verlassen, auch wenn während der normalen Ausführung einer bestimmten Software davon ausgegangen wird, dass die entsprechenden Ergebnisse unterschiedlich oder sogar völlig zufällig sind.

Angenommen, man möchte eine Funktion testen, die zur Laufzeit zufällige Werte verarbeitet. Während der Testausführung muss man jedoch vorhersehbare Werte auf reproduzierbare Weise überprüfen. Das folgende Beispiel zeigt, wie mit einer Lambda-Funktion das Monkey Patching helfen kann:

```python 
from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex
    function during testing.
    """
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_token():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_token()
```
Ein Kontext-Manager hilft dabei, die Operation des Monkey Patching einer Funktion aus der Standardbibliothek (in diesem Beispiel secrets) zu isolieren. Die Lambda-Funktion, die secrets.token_hex() zugewiesen ist, ersetzt das Standardverhalten durch die Rückgabe eines statischen Werts.

Dies ermöglicht das Testen jeder Funktion, die von token_hex() abhängt, auf vorhersehbare Weise. Vor dem Verlassen des Kontext-Managers wird das Standardverhalten von token_hex() wiederhergestellt, um unerwartete Nebenwirkungen zu beseitigen, die andere Bereiche des Tests beeinträchtigen könnten, die vom Standardverhalten von token_hex() abhängig sein können.

Unit-Test-Frameworks wie unittest und pytest heben dieses Konzept auf eine höhere Ebene der Raffinesse.

Mit pytest wird das gleiche Beispiel, unter Verwendung einer Lambda-Funktion, eleganter und kürzer:

```python 
import secrets

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_token(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"
```


Und jetzt den Test ausführen:

```shell 
$ pytest test_token.py -v
============================= test session starts ==============================
platform linux -- Python 3.7.2, pytest-4.3.0, py-1.8.0, pluggy-0.9.0
cachedir: .pytest_cache
rootdir: /home/andre/AB/tools/bpython, inifile:
collected 1 item

test_token.py::test_gen_token PASSED                                     [100%]

=========================== 1 passed in 0.01 seconds ===========================
```


#### Zusammenfassung
Was wir gelernt haben: 

Python-Lambdas schreiben und anonyme Funktionen nutzen
Zwischen Lambdas und normalen Python-Funktionen wählen
Übermäßigen Gebrauch von Lambdas vermeiden
Lambdas mit High-Order-Functions oder Python-Key-Functions verwenden
Lambda für mathematische Formeln

Python-Lambdas sind wie Salz. Eine Prise zuviel wird das Gericht verderben.


## Beispielaufgaben:

#### Beispiel 1: Überprüfen ob eine Zahl gerade ist

```python
even = lambda x: x%2==0
```

```python
even(3)
```

```python
even(4)
```
#### Beispiel 2: Erstes Zeichen eines Strings ausgeben

```python
erstes = lambda s: s[0]
```

```python
erstes('Hallo')
```


## Verständnisfragen:
Was ist eine Lambda-Funktion in Python?

- Eine spezielle Funktion für mathematische Berechnungen
- Eine anonyme Funktion
- Eine Funktion, die nur für Listen verwendet wird
- Eine Funktion, die nur in Klassen definiert werden kann

Wie wird eine Lambda-Funktion in Python erstellt?

- Mit dem Schlüsselwort lambda gefolgt von Argumenten und einem Ausdruck
- Mit dem Schlüsselwort def gefolgt von Funktionennamen und Argumenten
- Mit dem Schlüsselwort function gefolgt von Argumenten und einem Ausdruck
- Mit dem Schlüsselwort anonymous gefolgt von Argumenten und einem Ausdruck

Welche der folgenden Aussagen zur Lambda-Funktion ist korrekt?

- Lambda-Funktionen können mehrere Ausdrücke enthalten
- Lambda-Funktionen können nicht als Argumente an andere Funktionen übergeben werden
- Lambda-Funktionen können keine Variablen referenzieren, die außerhalb der Funktion definiert sind
- Lambda-Funktionen sind für komplexe Berechnungen nicht geeignet

Wofür werden Lambda-Funktionen häufig verwendet?

- Zur Definition von Klassen
- Zur Berechnung von komplexen mathematischen Ausdrücken
- Zur Erstellung von anonymen Funktionen für kurzzeitige Verwendung
- Zur Implementierung von Schleifen in Python

Wie können Lambda-Funktionen in Kombination mit der Funktion map verwendet werden?

- Zur Definition von benutzerdefinierten Sortieralgorithmen
- Zur Anwendung einer Funktion auf jedes Element einer Liste
- Zur Erstellung von Bedingungen in Schleifen
- Zur Umwandlung von Strings in Zahlen


Wie sieht die Syntax einer einfachen Lambda-Funktion aus?

- function: arguments => expression
- lambda {arguments}: {expression}
- lambda arguments: expression
- def lambda(arguments, expression)

Welche der folgenden Funktionen akzeptiert eine Lambda-Funktion als Argument?

- sort()
- sum()
- filter()
- append()

Was passiert, wenn eine Lambda-Funktion mehrere Argumente hat, aber nur eines beim Aufruf übergeben wird?

- Die Lambda-Funktion gibt einen Fehler aus.
- Die Lambda-Funktion akzeptiert nur ein Argument.
- Die Lambda-Funktion gibt den Wert des übergebenen Arguments aus.
- Die Lambda-Funktion ignoriert das übergebene Argument.

Welcher Ausdruck ist äquivalent zur Lambda-Funktion lambda x, y: x + y?

- def add(x, y): return x + y
- def add(x, y): x + y
- def add(x, y) => x + y
- def add(x, y) { return x + y }

Wie wird die Funktion reduce aus dem Modul functools mit einer Lambda-Funktion verwendet?

- reduce(lambda x, y: x + y, sequence)
- functools.reduce(lambda x, y: x + y, sequence)
- sequence.reduce(lambda x, y: x + y)
- sequence(functools.lambda x, y: x + y)



## Beispielaufgaben

#### Beispielaufgabe 1: Einen String umkehren

```python
umk = lambda s: s[::-1]
```

```python
umk('Hallo')
```

### Beispielaufgabe 2: Genau wie bei normalen Funktionen können wir mehr als einen Parameter aufnehmen

```python
add = lambda x,y: x+y
```

```python
add(3,4)
```

## Weiterführende Übungsaufgaben: Chillies

#### Addition mit Lambda:
Schreiben Sie eine Lambda-Funktion, die zwei Zahlen addiert.

#### Quadratzahlen mit Lambda:
Erstellen Sie eine Lambda-Funktion, die das Quadrat einer Zahl berechnet.

#### Filtern von geraden Zahlen:
Verwenden Sie filter und eine Lambda-Funktion, um eine Liste von ganzen Zahlen zu erstellen, die nur gerade Zahlen enthält.

#### Wortlänge sortieren:
Gegeben ist eine Liste von Wörtern. Verwenden Sie sorted und eine Lambda-Funktion, um die Liste nach der Länge der Wörter zu sortieren.

#### Potenzen mit Lambda:
Schreiben Sie eine Lambda-Funktion, die eine Zahl und einen Exponenten akzeptiert und die Potenz berechnet.

#### Umwandlung in Großbuchstaben:
Verwenden Sie map und eine Lambda-Funktion, um eine Liste von Wörtern in Großbuchstaben umzuwandeln.

#### Addition von drei Zahlen:
Schreiben Sie eine Lambda-Funktion, die drei Zahlen addiert.

#### Filtern von negativen Zahlen:
Verwenden Sie filter und eine Lambda-Funktion, um eine Liste von ganzen Zahlen zu erstellen, die nur negative Zahlen enthält.

#### Maximum von zwei Zahlen:
Schreiben Sie eine Lambda-Funktion, die das Maximum von zwei Zahlen zurückgibt.

#### Anonyme Funktionen in einer Liste:
Gegeben ist eine Liste von Lambda-Funktionen. Verwenden Sie map, um eine Liste von Ergebnissen zu erstellen, indem Sie jeder Funktion eine Zahl übergeben.
