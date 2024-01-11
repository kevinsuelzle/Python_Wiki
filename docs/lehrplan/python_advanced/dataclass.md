
# Dataclass

Seit Python 3.7 ginbt es einen dataclass-Decorator, dazu entwickelt Klassen zu erstellen, die primär für die Speicherung von Daten genutzt werden.
Special-Methods wie __init__, __repr__ werden automatisch erzeugt.
Dies schauen wir uns genauer an:

#### Die Syntax

Die grundlegende Syntax sieht so aus:

```python 
from dataclasses import dataclass

@dataclass
class MyClass:
    attribute1: type
    attribute2: type
    # ... additional attributes
```

Einfach die Attribute durch passende Namen ersetzen udn fertig.

#### Klassenvariablen
Man kann Klassenvariablen innerhalb einer dataclass genauso definieren wie in einer regulären Klasse. Diese Klassenvariablen werden über alle Instanzen der Klasse gemeinsam genutzt.

```python 
@dataclass
class MyClass:
    attribute1: int
    attribute2: str
    class_variable: int = 10
```


#### Standardwerte
Sie können auch Standardwerte für Attribute festlegen. Wenn ein Attribut während der Instanzerstellung nicht angegeben wird, nimmt es den Standardwert an.

```python 
@dataclass
class MyClass:
    attribute1: int = 0
    attribute2: str = "default_value"
```

#### Special Methods in der dataclass
Folgende Special-Methods werden vom Decorator automatisch erstellt

TODO: Das hier in eine Liste packen

__init__: Initialisiert Instanzattribute.
__repr__: Bietet eine Zeichenkettenrepräsentation der Instanz.
__eq__: Vergleicht Instanzen auf Gleichheit.
__ne__: Vergleicht Instanzen auf Ungleichheit.
__lt__: Vergleicht Instanzen auf kleiner als.
__le__: Vergleicht Instanzen auf kleiner oder gleich.
__gt__: Vergleicht Instanzen auf größer als.
__ge__: Vergleicht Instanzen auf größer oder gleich.


#### Instanzen miteinander vergleichen 
Dank der Special-Methods lassen sich instanzen direkt vergleichen.

```python 
point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)  # Output: True
print(point1 != point2)  # Output: False
```


#### Mutable und Immutable Dataclass

Standardmäßig sind Instanzen von dataclass veränderbar, was bedeutet, dass Sie ihre Attribute nach der Erstellung ändern können. Möchte man Instanzen unveränderlich machen, können Sie den Parameter frozen des dataclass-Dekorators verwenden.

```python 
@dataclass(frozen=True)
class ImmutableClass:
    attribute1: int
    attribute2: str
```

Instanzen der ImmutableClass können ihre Attribute nach der Erstellung nicht mehr ändern, da sie als unveränderlich (immutable) festgelegt sind.


#### Type Annotations
dataclass unterstützt Type Annotations, die es Ihnen ermöglichen, die erwarteten Datentypen für Ihre Attribute anzugeben. Dies kann die Lesbarkeit des Codes verbessern.

```python 
@dataclass
class TypedClass:
    attribute1: int
    attribute2: str
```

#### Einfache Beispiele
Ein Paar Beispiele um die Konzeopte zu verdeutlichen:

```python 
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```
Jetzt Punkte erstellen_

```python 
point1 = Point(2.5, 3.7)
point2 = Point(2.5, 3.7)
point3 = Point(0.0, 0.0)
```

Und vergleichen:

```python 
print(point1 == point2)  # Output: True
print(point1 == point3)  # Output: False
```

Weiter gehts mit einem neuen Beispiel:

```python 
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    category: str = "Uncategorized"

# Creating instances of Product class
product1 = Product("Widget", 19.99, "Electronics")
product2 = Product("Gadget", 9.99)

# Printing the instances
print(product1)  # Output: Product(name='Widget', price=19.99, category='Electronics')
print(product2)  # Output: Product(name='Gadget', price=9.99, category='Uncategorized')
```


#### Zusammenfassung
Der dataclass-Dekorator ist in der Tat eine fantastische Ergänzung zu Python, die den Prozess der Erstellung von Klassen, die hauptsächlich zur Datenverwaltung dienen, vereinfacht. Er generiert automatisch spezielle Methoden, die Aufgaben wie Instanzerstellung, Vergleich und Repräsentation vereinfachen. Es ist ein wertvolles Werkzeug in Ihrem Python-Werkzeugkasten, insbesondere wenn es um datenzentrierte Klassen geht.

In diesem Tutorial haben wir die Grundlagen der Verwendung von dataclass behandelt, einschließlich Syntax, Klassenvariablen, Standardwerten, speziellen Methoden, Typannotationen und mehr. Wir haben auch zwei praktische Beispiele erkundet, um seine Verwendung in realen Szenarien zu verdeutlichen. Beachten Sie, dass dataclass zwar unglaublich nützlich ist, aber möglicherweise nicht für jede von Ihnen erstellte Klasse geeignet ist. Berücksichtigen Sie die Komplexität des Verhaltens Ihrer Klasse, bevor Sie sich für die Verwendung von dataclass entscheiden.

Viel Spaß beim Coden!


## Aufgaben Dataclass:

#### Aufgabe 1: Einführung in dataclass
Erstellen Sie eine dataclass namens Person mit den Feldern name (String), alter (int) und stadt (String).

#### Aufgabe 2: Vererbung von dataclass
Erstellen Sie eine dataclass namens Student, die von der Person-dataclass erbt. Fügen Sie der Student-dataclass ein zusätzliches Feld namens matrikelnummer (int) hinzu.

#### Aufgabe 3: Standardwerte in dataclass
Fügen Sie den Person- und Student-dataclasses Standardwerte für die Felder alter und stadt hinzu. Der Standardwert für alter sollte 0 sein, und der Standardwert für stadt sollte "Unbekannt" sein.

#### Aufgabe 4: Methoden in dataclass
Erstellen Sie eine Methode namens geburtstag_feiern in der Person-dataclass, die das Alter um 1 erhöht. Fügen Sie außerdem eine Methode studieren in der Student-dataclass hinzu, die eine Nachricht ausgibt, dass der Student studiert.

#### Aufgabe 5: dataclass-Instanzen vergleichen
Überladen Sie die Vergleichsoperatoren (== und !=) für die Person-dataclass, sodass zwei Person-Instanzen als gleich betrachtet werden, wenn ihre Namen und Alter übereinstimmen.

#### Aufgabe 6: dataclass als unveränderlich markieren
Markieren Sie die Person-dataclass als unveränderlich, sodass die Instanzen nach der Erstellung nicht mehr geändert werden können.

#### Aufgabe 7: Anwendung von dataclass
Erstellen Sie eine Liste von Person- und Student-Instanzen und führen Sie verschiedene Operationen wie Hinzufügen, Entfernen und Sortieren durch.

