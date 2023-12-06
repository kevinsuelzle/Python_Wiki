# Bytecode und Maschinencode in Relation zu Python

Python ist eine Programmiersprache, die für ihre einfache Syntax und Lesbarkeit bekannt ist. Um zu
verstehen, wie Python-Code auf einem Computer ausgeführt wird, ist es wichtig, die Konzepte von Bytecode und
Maschinencode zu verstehen.

## Bytecode in Python 
[50min]

1. **Was ist Bytecode?**
   Bytecode ist eine niedrigere, abstraktere Darstellung des Quellcodes, die nicht direkt von der Hardware gelesen
   werden kann, aber maschinennäher als der ursprüngliche Python-Quellcode ist.

2. **Wie wird Python in Bytecode umgewandelt?**
   Wenn ein Python-Skript ausgeführt wird, wird es zunächst von einem Interpreter in Bytecode umgewandelt. Dieser
   Bytecode wird dann von einer virtuellen Maschine – in Pythons Fall der Python Virtual Machine (PVM) – ausgeführt.

3. **Vorteile von Bytecode**
    - **Plattformunabhängigkeit**: Da der Bytecode von der PVM und nicht direkt von der Hardware ausgeführt wird, ist
      Python plattformunabhängig. Der gleiche Python-Code kann auf verschiedenen Betriebssystemen laufen, solange eine
      passende PVM vorhanden ist.
    - **Effizienz**: Die Umwandlung in Bytecode ermöglicht einige Optimierungen, die die Ausführungsgeschwindigkeit
      verbessern können.

4. **Kompilierung vs. Interpretation**
   Python ist eine interpretierte Sprache, aber dieser Prozess beinhaltet eine Kompilierungsstufe, in der der Quellcode
   in Bytecode umgewandelt wird. Der Bytecode wird dann interpretiert.

## Maschinencode
[50min]

1. **Was ist Maschinencode?**
   Maschinencode ist die niedrigste Ebene der Code-Darstellung, die direkt von der CPU eines Computers verstanden und
   ausgeführt werden kann.

2. **Von Bytecode zu Maschinencode**
   In der Python Virtual Machine wird der Bytecode interpretiert und in Maschinencode übersetzt, der dann von der CPU
   ausgeführt wird.

3. **Just-In-Time-Kompilierung**
   Einige Python-Implementierungen, wie PyPy, verwenden Just-In-Time (JIT)-Kompilierung, um Bytecode während der
   Laufzeit in Maschinencode zu übersetzen, was die Ausführungsgeschwindigkeit deutlich verbessern kann.

Das Verständnis, wie Python-Code zu Bytecode und dann zu Maschinencode umgewandelt wird, ist grundlegend für das
Verständnis der Funktionsweise von Python. Hier ist ein einfaches Beispiel, um diesen Prozess zu veranschaulichen:

## Beispiel
[90min]
Angenommen, wir haben ein einfaches Python-Skript:

```python
def add_numbers(a, b):
    return a + b


result = add_numbers(3, 4)
print(result)
```

### Schritt 1: Umwandlung in Bytecode

Wenn dieses Skript ausgeführt wird, kompiliert der Python-Interpreter den Quellcode zuerst in Bytecode. Dieser Bytecode
ist eine niedrigstufigere, abstraktere Darstellung des Quellcodes. In Python können Sie den Bytecode eines Programms mit
dem `dis`-Modul anzeigen. Zum Beispiel:

```python
import dis


def add_numbers(a, b):
    return a + b


dis.dis(add_numbers)
```

Dies würde etwas in der Art ausgeben:

```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

Dieser Output zeigt den Bytecode für die Funktion `add_numbers`. Jede Zeile repräsentiert eine Operation, die die Python
Virtual Machine ausführen wird. Beispielsweise `LOAD_FAST` lädt eine lokale Variable, und `BINARY_ADD` führt eine
Addition aus.

### Schritt 2: Ausführung als Maschinencode

Der Bytecode wird dann von der Python Virtual Machine (PVM) ausgeführt. Die PVM ist ein Interpreter, der den Bytecode
liest und interpretiert, um die entsprechenden Operationen auf der Hardwareebene auszuführen.

Die Umwandlung des Bytecodes in Maschinencode – also den Code, den die CPU direkt versteht und ausführt – erfolgt durch
die PVM. Dieser Prozess ist plattformabhängig, da er von der spezifischen Architektur der CPU abhängt.

### Maschinencode-Generierung

Die genaue Umwandlung von Bytecode in Maschinencode und dessen Ausführung ist in Standard-Python-Implementierungen (wie
CPython) für den Benutzer nicht sichtbar und erfolgt intern in der PVM. Bei Just-In-Time-Kompilierern wie PyPy kann
dieser Prozess jedoch zur Laufzeit erfolgen, wobei der Bytecode direkt in optimierten Maschinencode für die spezifische
Maschine übersetzt wird.

## Zusammenfassung

- **Python zu Bytecode**: Der Python-Quellcode wird in Bytecode umgewandelt, der eine abstraktere Darstellung des Codes
  ist.
- **Bytecode zu Maschinencode**: Dieser Bytecode wird von der Python Virtual Machine interpretiert und auf der
  Hardwareebene als Maschinencode ausgeführt.

Das Wissen um diese Prozesse hilft zu verstehen, warum Python als plattformunabhängig gilt und wie es trotz der höheren
Abstraktionsebene effizient ausgeführt werden kann.

# Diskussionsaufgaben
[120min + 30min Auswertung]
### 1. **Grundlagen des Python-Interpreters**: 🌶️
Recherchiere, was ein Python-Interpreter ist und wie er funktioniert. 
Diskutiere, was beim Ausführen eines Python-Skripts im Hintergrund passiert, von der Eingabe des Codes bis zur
Ausführung.

### 2. **Bytecode in Python verstehen**: 🌶️
Informiere dich darüber, was Bytecode in Python ist und warum Python-Code zuerst in
Bytecode umgewandelt wird, bevor er ausgeführt wird. Diskutiere die Rolle des Bytecodes im Python-Ausführungsprozess.

### 3. **Python und Plattformunabhängigkeit**: 🌶️
Recherchiere, was es bedeutet, dass Python plattformunabhängig ist.
Diskutiere, wie Python auf verschiedenen Betriebssystemen wie Windows, MacOS und Linux ausgeführt werden kann, ohne
den Code zu ändern.

### 4. **Einführung in Python Virtual Machine (PVM)**: 🌶️
Finde heraus, was die Python Virtual Machine (PVM) ist und welche Rolle
sie bei der Ausführung von Python-Code spielt. Diskutiere, wie die PVM Bytecode interpretiert und ausführt.

### 5. **Python-Interpreter: CPython vs. PyPy**: 🌶️
Recherchiere die Unterschiede zwischen CPython (dem Standard-Python-Interpreter) und PyPy (einem alternativen 
Interpreter). Diskutiere, wie diese Interpreter Python-Code  verarbeiten und welche Vor- und Nachteile sie haben.

[Lösung](solution.md)
