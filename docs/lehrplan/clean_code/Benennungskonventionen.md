# Benennungskonventionen

siehe auch [PEP 8](https://peps.python.org/pep-0008/) 

## Variablen

```python
a = 50
b = 100
c = a + b
```

[Bezeichner](Conventions.md) sollten klar und eindeutig sein und [PEP 8](https://peps.python.org/pep-0008/#prescriptive-naming-conventions) folgen.

```python
basispreis = 50
steuer = 100
gesamtpreis = basispreis + steuer
```
# Aussagekräftige Namen

Variablennamen und Funktionsnamen sollten

- aussagekräftig und
- beschreibend sein, um die Lesbarkeit und Wartbarkeit des Codes zu verbessern.
- gut auszusprechen sein und nicht in die Irre führen.
- durchsuchbar sein.
- nichts kodiertes enthalten. $$$ Task 17: was heißt das genau?
- einfach zu verstehen sein.
- nicht schwafelig sein, keine Mundart wiedergeben oder sonstiges kulturelles Gut enthalten.
- nicht doppelt verwendet werden oder mit einem Prefix versehen sein.
- us dem Fachgebiet übernommen werden, um das es gerade geht.

Nutzt man Begriffe aus der fachlichen Domain des Anwenders, so entsteht eine problemspezifische Sprache, die eventuell
sogar genügt, um mit Nicht-Programmierern zu diskutieren.
Hier kommen wir in den Bereich des Domain-Designs.

## Funktionen

```python
def calc(x):
    return x * 2 + 5
```

Eine sehr allgemein formulierte Namensgebung trägt nichts zum Verständnis der Aufgabe der Funktion bei. Da sie nur eine
Sache tun soll, kann man sich gut auf dieses Tun beziehen.

$$$ Task 7 hier ein anderes Beispiel verwenden. Und Satz nachvollziehbarer formulieren.

```python
def calculate_adjusted_value(x):
    return x * 2 + 5
```

Immer noch nicht verständlich, was hier passiert, oder?
Stellen wir uns also vor, dass wir in einer Applikation sind, die mit direkten Speicheradressen operiert.
Dabei bekommt auch die Variable eine Bedeutung zugewiesen.

```python
def get_next_memory_address(old_address):
    return old_address * 2 + 5
```

Dadurch erspart man sich möglicherweise die [Kommentare](../Kommentare).

[zurück](../TheGoodPractices) 

