# Generatoren und Iteratoren

TODO: Vllt noch mal einen Einleitungssatz?

Iterables sind:

- Lists 
- tuples
- dictionaries
- strings
- files
- generators
- etc...

Jetzt kommen zwei ziemlich einfache Definitionen! :D

#### Definition von iterable:
Objekt besitzt method __iter__()

#### Definition Iterator: 
Objekt besitzt die method __next__()


```python 
nums = [3,2,8]

print(dir(nums))
```

Was macht die For Loop im background?
Die for loop ruft __iter__() auf und gibt einen Iterator aus.

Was macht etwas zu einem Iterator?
Ein Objekt mit einem "Status", sodass es sich merkt, wo es ist, während man darüber iteriert.
Iteratoren wissen auch, wie sie den nächsten Wert bekommen: __next__()

Unsere Liste ist also kein iterator.

```python 
i_nums = nums.__iter__() # auch iter(nums)

print(dir(i_nums))
```

```python 
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
```

Was da eigentlich geschieht, und wieso es zum Abbruch kommt:

```python 
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

```

TODO: Die Texte errinnern mehr an Stichpunkte und müssen ausformuliert werden.

Iteratoren können nur vorwärts gehen!

Wir können auch eigene Iteratoren in unsere Klassen bauen.

Generator (Beispiel) my_range() und yield.

Iteratoren müssen nicht abbrechen. Sie können unendlich lange gehen.


TODO: Das Beispiel ist sehr groß und sollte in Einzelschritten erklärt werden.

```python 
from pympler import summary, muppy
import psutil
import resource
import os
import sys


def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem


import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print 'Took {} Seconds'.format(t2-t1)



# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

my_nums = (x*x for x in [1,2,3,4,5])

print list(my_nums) # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print num
```

TODO: Vllt lieber erstmal dieses einfache Beispiel durchgehen?

```python 
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)

for num in nums:
    print(num)
```

TODO: Bitte diese formatierung für die Aufgaben nutzen.
TODO: Dokument mit Lösungen erstellen und darauf verlinken.

### Aufgabe 1: Quradratzahlgenerator 🌶

Erstelle einen Generator, der die Quadratzahlen von Zahlen bis zu einer Zahl N erstellt.

```python
def genquadrate(N):
    pass
```


```python
for x in genquadrate(10):
    print(x)
```

#### Beispielaufgabe 2

Erstelle einen Generator, der die Primzahlen von Zahlen bis zu einer Zahl N erstellt.


```python
def genprimes(N):
    pass
```


```python
for x in genprimes(10):
    print(x)
```

TODO: Auch hier Lösungen erstellen und verlinken

## Verständnisfragen:
Handelt es sich bei den folgenden Objekten (der Klasse) jeweils um Iteratoren oder Iterables oder beides?

- string
- list
- range(x)
- integer
    

Was ist ein Iterable in Python?

- Eine Funktion, die Werte generiert
- Ein Objekt, das durch eine Schleife durchlaufen werden kann
- Eine Variable, die in einer Schleife verwendet wird
- Eine spezielle Datenstruktur in Python

Welche Funktion wird aufgerufen, um ein Iterator-Objekt aus einem Iterable zu erstellen?

- create_iterator()
- iter()
- make_iterator()
- iterator()

Was ist die Funktion des __iter__-Methode in einem Iterable-Objekt?

- Sie gibt den nächsten Wert im Iterable zurück.
- Sie initialisiert das Iterable-Objekt.
- Sie gibt einen Iterator für das Iterable zurück.
- Sie überprüft, ob das Objekt ein Iterable ist.

Was tut die __next__-Methode in einem Iterator?

- Sie gibt den nächsten Wert im Iterator zurück.
- Sie initialisiert den Iterator.
- Sie überprüft, ob der Iterator beendet ist.
- Sie gibt eine Liste der verbleibenden Elemente im Iterator zurück.

Wie wird eine Schleife in Python implementiert, um durch ein Iterable zu iterieren?

- for i in range(iterable):
- for item in iterable:
- while iterable.hasNext():
- foreach item in iterable:

Was ist der Zweck der iter()-Funktion in Python?

- Sie erstellt ein Iterable-Objekt.
- Sie erstellt ein Iterator-Objekt.
- Sie gibt den aktuellen Zustand des Iterators zurück.
- Sie gibt den nächsten Wert im Iterable zurück.

Welche der folgenden Aussagen ist korrekt für Iteratoren in Python?

- Ein Iterator kann nur einmal durchlaufen werden.
- Ein Iterator kann in beide Richtungen durchlaufen werden.
- Ein Iterator kann mehrmals durchlaufen werden.
- Ein Iterator kann nicht durchlaufen werden.

Welche Methode wird aufgerufen, wenn ein Iterator das Ende der Iteration erreicht hat?

- __stop__
- __finalize__
- __complete__
- StopIteration

Was passiert, wenn in der __next__-Methode eines Iterators der Befehl raise StopIteration ausgeführt wird?

- Der Iterator wird neu gestartet.
- Es wird ein Fehler angezeigt, der die Schleife unterbricht.
- Es wird das Ende der Iteration signalisiert.
- Der Iterator wird pausiert.

Welches der folgenden Python-Objekte ist ein Iterable?

- Integer (z.B., 5)
- Liste
- String
- Alle oben genannten





## Übungsaufgaben

#### Aufgabe 1
Erstelle einen Generator der N zufällige Nummern zwischen einer unteren und oberen Grenze (das sind die Inputs des Nutzers) ausgibt. Nutzt beispielsweise die random Bibliothek. Zum Beispiel:


```python
import random

random.randint(1,10)
```

```python
def zuf_zahl(unten,oben,N):
    pass
```

```python
for num in zuf_zahl(1,10,12):
    print(num)
```

#### Aufgabe 2

Verwende die `iter()` Funktion, um den String zu konvertieren.

```python
s = "Hallo"

# Code hier
```

#### Aufgabe 3

Erklärt einen Anwendungsfall für einen Generator durch die Verwendung der `yield` Anweisung, wo du nicht eine normale Funktion mit einer return Anweisung verwenden willst.

TODO: Achte bitte darauf, dass Codeschnippsel im Fliestext mit den schiefen Hochkomma eingeklammert sind. Also nicht kursiv mit <i></i>

Kannst du erklären, was <i>gencomp</i> im Code unten ist? (Hinweis: wir haben das nie in unseren Lektionen gelernt. Ihr könnt Google/Stack Overflow verwenden!)


```python
meine_liste = [1,2,3,4,5]

gencomp = (item for item in meine_liste if item > 3)

for item in gencomp:
    print(item)
```

Hinweis: "generator comprehension" suchen...


