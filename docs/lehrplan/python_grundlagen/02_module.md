# Module und Pakete
[60min]

In Python ermöglichen Module und Pakete die Organisation von Code in wiederverwendbare Einheiten, um die Lesbarkeit zu verbessern und die Codeverwaltung zu optimieren. Hier schauen wir uns Module genauer an und werfen einen Blick auf Pakete sowie einige fortgeschrittene Konzepte.
Module

## Module

Ein Modul in Python ist im Grunde genommen eine Datei mit Python-Code. In dieser Datei können Funktionen, Variablen und Klassen definiert werden, die in anderen Python-Dateien wiederverwendet werden können.
Beispiel

Angenommen, du erstellst ein Modul namens `greetings.py`:

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("John"))
```
Du kannst dieses Modul in einem anderen Skript verwenden:

```python
# main.py

import greetings

print(greetings.greet("Alice"))
```
Hier verwenden wir den import-Befehl, um das Modul greetings einzubinden und die darin definierte greet-Funktion aufzurufen.
Alias für Module

Du kannst auch Alias für Module verwenden, um den Code kompakter zu gestalten:

```python
# main.py

import greetings as gr

print(gr.greet("Bob"))
```

In diesem Beispiel wird das Modul greetings als `gr` abgekürzt, und wir können den Alias verwenden, um auf die Funktion greet zuzugreifen.
```if __name__ == "__main__":```

Die Bedingung ```if __name__ == "__main__":``` ermöglicht es, Code in einem Modul auszuführen, wenn es direkt ausgeführt wird, aber nicht, wenn es in einem anderen Skript importiert wird. Das ist nützlich, um Code für Testzwecke oder Beispiele bereitzustellen.

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("John"))
```
Hier wird die Grußnachricht nur ausgegeben, wenn das Modul direkt ausgeführt wird, nicht wenn es importiert wird.

## Pakete

Pakete sind Verzeichnisse, die Module und möglicherweise Unterpakete enthalten. Ein Paket kann auch eine `__init__.py`-Datei enthalten, die Code für die Initialisierung des Pakets bereitstellt.

```
my_package/
|-- __init__.py
|-- module1.py
|-- module2.py
|-- subpackage/
|   |-- __init__.py
|   |-- module3.py
```

### Nutzung der init Datei

Angenommen, wir haben ein Paket mit dem Namen "mypackage" und folgender Struktur:

```
mypackage/
|-- __init__.py
|-- module1.py
|-- module2.py
```

Der `__init__.py`-Code kann dazu verwendet werden, Initialisierungscodes für das Paket bereitzustellen, die beim Importieren des Pakets ausgeführt werden. Hier ist ein Beispiel:

`__init__.py`:
```python
# Dieser Code wird ausgeführt, wenn das Paket importiert wird.
print("Das Paket mypackage wurde importiert!")
```

## Weitere Möglichkeiten für import

Du kannst auch spezifische Funktionen oder Klassen aus einem Modul importieren:

```python
# main.py
from greetings import greet

print(greet("Eve"))
```
Oder du kannst alle Funktionen/Klassen importieren:

```python
# main.py

from greetings import *

print(greet("Charlie"))
```

Es ist jedoch ratsam, selektiv zu importieren, um potenzielle Namenskonflikte zu vermeiden.
Zusammenfassung

Module und Pakete sind wichtig, um Code zu organisieren und wiederzuverwenden. Du kannst Module importieren, Alias verwenden, Bedingungen für den direkten Aufruf festlegen und mit Paketen eine noch höhere Organisationsebene erreichen. Dies ermöglicht eine flexible und saubere Strukturierung deines Codes.

# Aufgaben
[120min]

## 1. Einfache Modulnutzung 🌶️
   - Erstelle ein einfaches Python-Modul mit einer Funktion, die eine Begrüßung ausgibt. Importiere und verwende dieses Modul in einem anderen Python-Skript.

## 2. Modul mit Alias importieren 🌶️
   - Erstelle ein weiteres Modul und importiere es in einem neuen Skript mit einem Alias. Verwende dann das Alias, um auf Funktionen oder Variablen aus dem Modul zuzugreifen.

## 3. Selektiven Import durchführen 🌶️
   - Erstelle ein Modul mit mehreren Funktionen und Variablen. Importiere nur eine ausgewählte Funktion in einem neuen Skript und verwende sie.

## 4. Verwendung von `__init__.py` 🌶️🌶️
   - Erstelle ein Paket mit mehreren Modulen. Nutze die Datei `__init__.py`, um das Paket zu initialisieren und den Zugriff auf Module zu erleichtern. Importiere dann Module aus dem Paket in einem Skript.
