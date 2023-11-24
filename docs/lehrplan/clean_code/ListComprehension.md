# List Comprehension

![List Comprehension](../clean_code/pictures/ListComprehension.jpg)

Man kann sehr komplexe und verklausulierte Code-Sequenzen schreiben.

```python
words = ["apple", "banana", "cherry", "date", "fig", "grape", "apple", "kiwi", "jamberry"]

print ([(word.upper(), len(word)) for word in set(words) if len(word) > 3])
```

**Frage**: Was wird hier ausgegeben?


```python
my_list = [x ** 2 for x in range(20) if x % 2 == 0 if x % 3 == 0]
```

**Aufgabe:** Schreiben sie den Code in einfachen imperativen Code um.

**Frage**: Welche Argumente für die komplexe Schreibweise könnte es geben?

**Antwort**:

- **Kompakter Code:** 

    List Comprehensions ermöglichen es, komplexe Operationen in einer einzigen, kompakten Zeile zu schreiben, was den Code kürzer und oft leichter lesbar macht.

- **Verbesserte Lesbarkeit:** 

    Für Personen, die mit der Syntax vertraut sind, können List Comprehensions die Absicht des Codes klarer machen als eine entsprechende Schleife.

- **Höhere Ausführungsgeschwindigkeit:** 

    List Comprehensions können in einigen Fällen schneller ausgeführt werden als äquivalente Schleifen, da die Iteration intern optimiert ist.

- **Direkte Nutzung von Funktionen und Bedingungen:** 

    In List Comprehensions können Funktionen und bedingte Logik direkt verwendet werden, was die Notwendigkeit separater Schleifen oder bedingter Anweisungen reduziert.

- **Reduzierung des Bedarfs an temporären Variablen:** 

    List Comprehensions erlauben es, ohne zusätzliche temporäre Listen oder Variablen auszukommen, was den Speicherverbrauch reduzieren kann.

- **Förderung eines funktionalen Programmierstils:** 

    List Comprehensions unterstützen einen funktionalen Ansatz, bei dem Datenverarbeitungsvorgänge oft klarer und konziser ausgedrückt werden können.

- **Einfache Integration mehrerer Iteratoren:** 

    Komplexe List Comprehensions können mehrere Iteratoren und verschachtelte Schleifen in einer einzigen Zeile integrieren, was in traditionellen Schleifenstrukturen oft umständlicher ist.

- **Gute Unterstützung in der Python-Community:** 

    List Comprehensions sind ein beliebtes Feature in Python und werden von der Community gut unterstützt, was bedeutet, dass viele Ressourcen und Beispiele zur Verfügung stehen.

**Diskussion**: Wie soll man sich nun entscheiden?

[zurück](../TheGoodPractices)