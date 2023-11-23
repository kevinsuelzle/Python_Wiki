# Week 2

Inhalt:

- Listen, Tupel, Strings
- Schleifen: for, while
- Dictionaries und Sets
- Bytecode & Machinencode

# Datentypen als Container
- Listen
    mutable vs immutable
    Listen mit gleichen typen
    Listen mit unterschiedlichen typen
    Häufig verwendete Funktionen und Link zur Referenz

- Tupel
    Was macht Tupel aus?
    Wann verwende ich Tupel?
    Syntax
    Häufige Funktionen und LInk zur Referenz

- Strings
    Eine Art Spezialfall von Listen
    String-Slicing
    Häufige Operationen

- Schleifen
    for
        Syntax
        iterieren über Zahlenbereiche
        iterieren über Collections
    while
        Syntax

# Dictionaries & Sets
- Anwendung im Vgl zu Listen
- Syntax
- Vor- und Nachteile
- Nutzung von Schleifen mit Dictionaries und Sets

## Sets in Python

Sets in Python sind eine Datenstruktur, die für die Speicherung einer ungeordneten Sammlung von einzigartigen Elementen verwendet wird. Sie bieten folgende Eigenschaften:

### Eigenschaften von Sets

1. **Ungeordnet**: 
   - Sets haben keine feste Reihenfolge der Elemente.
   - Sie bieten keinen Indexzugriff wie Listen oder Tupel.

2. **Einzigartige Elemente**: 
   - Jedes Element in einem Set ist einzigartig.
   - Duplikate sind nicht erlaubt und werden ignoriert.

3. **Unveränderliche Elemente**: 
   - Sets können nur unveränderliche (immutable) Datentypen als Elemente enthalten, wie Zahlen, Strings und Tupel.

4. **Veränderlich**: 
   - Sets selbst sind veränderlich, d.h., man kann Elemente hinzufügen und entfernen.

5. **Kein Indexzugriff**: 
   - Aufgrund der Ungeordnetheit der Elemente gibt es keinen direkten Indexzugriff.
   - Die Mitgliedschaft eines Elements wird mit Methoden wie `in` überprüft.

### Erstellung und Nutzung von Sets

Sets werden mit geschweiften Klammern `{}` oder der `set()`-Funktion erstellt. 


**Beispiel**:

```python
einzigartige_zahlen = {1, 2, 3, 4, 5}
buchstaben = {'a', 'b', 'c', 'd'}
```
Man kann Elemente zu einem Set hinzufügen (mit `add()`) und entfernen (mit `remove()` oder `discard()`). 
Sets sind nützlich für mathematische Operationen wie Union, Schnitt und Differenz.

| Funktion                      | Beschreibung                                                                                              | Beispiel                                 |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `add(x)`                      | Fügt das Element `x` zum Set hinzu.                                                                       | `set1.add(5)`                            |
| `remove(x)`                   | Entfernt das Element `x` aus dem Set. Wirft einen Fehler, falls `x` nicht vorhanden ist.                  | `set1.remove(5)`                         |
| `discard(x)`                  | Entfernt das Element `x` aus dem Set. Kein Fehler, wenn `x` nicht vorhanden ist.                          | `set1.discard(5)`                        |
| `pop()`                       | Entfernt und gibt ein zufälliges Element aus dem Set zurück.                                              | `element = set1.pop()`                   |
| `clear()`                     | Entfernt alle Elemente aus dem Set.                                                                       | `set1.clear()`                           |
| `union(set2)`                 | Gibt ein neues Set zurück, das die Vereinigung von `set1` und `set2` ist.                                 | `set3 = set1.union(set2)`                |
| `intersection(set2)`          | Gibt ein neues Set zurück, das die Schnittmenge von `set1` und `set2` ist.                                | `set3 = set1.intersection(set2)`         |
| `difference(set2)`            | Gibt ein neues Set zurück, das die Elemente von `set1` enthält, die nicht in `set2` sind.                 | `set3 = set1.difference(set2)`           |
| `symmetric_difference(set2)`  | Gibt ein neues Set zurück, das Elemente enthält, die in `set1` oder `set2`, aber nicht in beiden sind.    | `set3 = set1.symmetric_difference(set2)` |

Diese Tabelle bietet einen Überblick über gängige Methoden, die mit Sets in Python verwendet werden. Wir brauchen
viele dieser Methoden nicht jetzt, aber es soll uns als Referenz dienen.

Sets sind nützlich, um einzigartige Elemente zu speichern und schnelle Operationen wie Vereinigungen, Schnittmengen und
Differenzen durchzuführen.

### Dictionaries (Schlüssel-Wert-Paare):
Dictionaries speichern Daten in Schlüssel-Wert-Paaren und sind eine zentrale Datenstruktur in Python. Sehr viele
tolle Sachen in Python lassen sich auf die Verwendung von Dictionaries zurückführen.

Sie sind ungeordnet, veränderbar und werden in geschweiften Klammern {} mit Schlüsseln und Werten definiert.

Jeder Eintrag in einem Dictionary, besteht aus einem Schlüssel (engl. Key) und einem dazugehörigem Wert (engl. Value).

**Beispiel**:

```python
person = {"name": "Anna", "alter": 30}
farben = {"rot": "#FF0000", "grün": "#00FF00", "blau": "#0000FF"}
```

| Funktion                        | Beschreibung                                                                                                                     | Beispiel                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `[key]`                         | Greif auf den Wert mit dem Key `key` zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler | `dict["Key"] = Value`                       |
| `get(key)`                      | Gibt den Wert für den angegebenen Schlüssel zurück. Gibt `None` zurück, wenn der Schlüssel nicht existiert.                      | `wert = dict.get('schluessel')`             |
| `keys()`                        | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel des Dictionaries enthält.                                               | `schluessel = dict.keys()`                  |
| `values()`                      | Gibt ein neues Ansichtsobjekt zurück, das alle Werte des Dictionaries enthält.                                                   | `werte = dict.values()`                     |
| `items()`                       | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel-Wert-Paare des Dictionaries als Tupel enthält.                          | `paare = dict.items()`                      |
| `update(dict2)`                 | Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus einem anderen Dictionary oder iterierbaren Schlüssel-Wert-Paaren.      | `dict.update(dict2)`                        |
| `pop(key)`                      | Entfernt den Eintrag mit dem angegebenen Schlüssel und gibt dessen Wert zurück.                                                  | `wert = dict.pop('schluessel')`             |
| `popitem()`                     | Entfernt und gibt ein zufälliges Schlüssel-Wert-Paar als Tupel zurück.                                                           | `schluessel, wert = dict.popitem()`         |
| `clear()`                       | Entfernt alle Elemente aus dem Dictionary.                                                                                       | `dict.clear()`                              |
| `copy()`                        | Erstellt eine flache Kopie des Dictionaries.                                                                                     | `neues_dict = dict.copy()`                  |

Diese Tabelle bietet einen Überblick über gängige Methoden, die bei der Arbeit mit Dictionaries in Python verwendet 
werden. 

Dictionaries sind nützlich für die Speicherung und Manipulation von Schlüssel-Wert-Paaren und bieten schnellen 
Zugriff sowie flexible Datenstrukturen.


# Bytecode & Maschinencode
- Python Ausführungsmodell im Vergleich zu anderen Sprachen
- Vgl zu Java und C/C++


        
