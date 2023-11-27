# Bessere Praktiken in Python

![HurraSuccess](pictures/HurraSuccess.jpg "Hurra! Clean Code")

## Verwendung von Funktionsparametern statt globalen Variablen
Anstatt eine globale Variable zu verwenden, sollte die Funktion einen Wert als Argument annehmen und den modifizierten Wert zurückgeben. Dies erhöht die Wiederverwendbarkeit und Klarheit der Funktion.

```python
def increment(x):
    return x + 1
```

### Fehlerbehandlung
Es ist wichtig, Ausnahmen zu behandeln, um unerwartete Abstürze zu vermeiden. Im Fall einer Division sollten wir insbesondere eine Division durch Null abfangen.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        return None
```

### Vereinfachung von List Comprehensions
Komplexe List Comprehensions sollten vermieden werden, da sie schwer zu lesen und zu verstehen sind. Eine Schleife mit klaren Bedingungen ist oft besser.

```python
my_list = []
for x in range(20):
    if x % 2 == 0 and x % 3 == 0:
        my_list.append(x**2)
```

### Benennung von Variablen
Bezeichner sollten klar und eindeutig sein. 

```python
basispreis = 50
steuer = 100
gesamtpreis = basispreis + steuer
```

### Hinzufügen von Kommentaren
Kommentare sind wichtig, um die Absicht hinter dem Code zu erklären, insbesondere in Fällen, in denen die Logik nicht sofort offensichtlich ist.

```python
def calculate_adjusted_value(x):
    # Berechnet den angepassten Wert durch Verdopplung und Addition von 5 oder
    # Die binäre Verschiebung um ein Bit nach links wird hier durch die Multiplikation mit 2 erreicht. 
    # Der Offset von 5 Bytes ist technisch erforderlich. Quelle ...
    return x * 2 + 5
```

### DRY Don't repeat yourself
Funktionen reduzieren die Code Menge und erhöhen die Wartbarkeit.

```python
def quadrat(zahl):
    return zahl * zahl

num1 = 4
num2 = 5
num3 = 6

quadrat_num1 = quadrat(num1)
quadrat_num2 = quadrat(num2)
quadrat_num3 = quadrat(num3)

print(quadrat_num1, quadrat_num2, quadrat_num3)
```

### Aufgabe: Umwandeln in unsauberen Code

```python
def sort_and_format_words(word_list):
    """
    Sortiert eine Liste von Wörtern nach ihrer Länge und gibt sie in einem formatierten String zurück.

    Args:
    word_list (list): Eine Liste von Wörtern (strings).

    Returns:
    str: Ein formatierter String, der die sortierten Wörter enthält.
    """
    # Sortieren der Wörter nach Länge
    sorted_words = sorted(word_list, key=len)

    # Erstellen eines formatierten Strings
    formatted_output = "Sortierte Wörter: " + ", ".join(sorted_words)

    return formatted_output

# Beispielverwendung
words = ["Python", "ist", "eine", "tolle", "Programmiersprache"]
print(sort_and_format_words(words))
```

Sie können diesen Code als Übung in schlechten Code umwandeln, indem Sie folgende Änderungen vornehmen:

1. Entfernen Sie alle Kommentare und Docstrings.
2. Verwenden Sie unklare oder irreführende Variablennamen.
3. Integrieren Sie unnötige oder komplexe Logik.
4. Vermeiden Sie die Verwendung hilfreicher Python-Funktionen wie sorted() und implementieren Sie stattdessen eine ineffiziente Sortiermethode.

