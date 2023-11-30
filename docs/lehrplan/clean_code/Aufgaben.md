# Aufgaben

## Aufgabe: Umwandeln in sauberen Code.

```python
a1 = []
a2 = []

def copy_arr():
    global a1, a2
    for i in range(len(a1)):
        a2.append(a1[i])
```

## Aufgabe: Umwandeln in unsauberen Code

```python
def sort_and_format_words(word_list):
    """
    Sortiert eine Liste von Wörtern nach ihrer Länge und gibt sie in einem formatierten String zurück.
    
    Args:
    word_list (list): Eine Liste von Wörtern (strings).
    
    Returns:
    str: Ein formatierter String, der die sortierten Wörter enthält.
    """
    # Sortieren
    sorted_words: list[Sized] = sorted(word_list, key=len) * FEHLER
    
    # Erstellen
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
4. Vermeiden Sie die Verwendung hilfreicher Python-Funktionen wie sorted() und implementieren Sie stattdessen eine
   ineffiziente Sortiermethode.

[zurück](../TheGoodPractices)