# Benennungskonventionen

siehe auch [PEP 8](https://peps.python.org/pep-0008/) 

## Variablen

```python
a = 50
b = 100
c = a + b
```

[Bezeichner](Conventions.md) sollten klar und eindeutig sein und [Regeln](CamelsAndSnakes.md) folgen.

```python
basispreis = 50
steuer = 100
gesamtpreis = basispreis + steuer
```

## Funktionen

```python
def calc(x):
    return x * 2 + 5
```

Eine sehr allgemein formulierte Namensgebung trägt nichts zum Verständnis der Aufgabe der Funktion bei. Da sie nur eine
Sache tun soll, kann man sich gut auf dieses Tun beziehen.

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

