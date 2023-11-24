## Dictionaries (Schlüssel-Wert-Paare):

Dictionaries speichern Daten in Schlüssel-Wert-Paaren und sind eine zentrale Datenstruktur in Python. Sehr viele
tolle Sachen in Python lassen sich auf die Verwendung von Dictionaries zurückführen.

Sie sind ungeordnet, veränderbar und werden in geschweiften Klammern {} mit Schlüsseln und Werten definiert.

Jeder Eintrag in einem Dictionary, besteht aus einem Schlüssel (engl. Key) und einem dazugehörigem Wert (engl. Value).

**Beispiel**:

```python
person = {"name": "Anna", "alter": 30}
farben = {"rot": "#FF0000", "grün": "#00FF00", "blau": "#0000FF"}
```

| Funktion        | Beschreibung                                                                                                                     | Beispiel                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `[key]`         | Greif auf den Wert mit dem Key `key` zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler | `dict["Key"] = Value`               |
| `get(key)`      | Gibt den Wert für den angegebenen Schlüssel zurück. Gibt `None` zurück, wenn der Schlüssel nicht existiert.                      | `wert = dict.get('schluessel')`     |
| `keys()`        | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel des Dictionaries enthält.                                               | `schluessel = dict.keys()`          |
| `values()`      | Gibt ein neues Ansichtsobjekt zurück, das alle Werte des Dictionaries enthält.                                                   | `werte = dict.values()`             |
| `items()`       | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel-Wert-Paare des Dictionaries als Tupel enthält.                          | `paare = dict.items()`              |
| `update(dict2)` | Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus einem anderen Dictionary oder iterierbaren Schlüssel-Wert-Paaren.      | `dict.update(dict2)`                |
| `pop(key)`      | Entfernt den Eintrag mit dem angegebenen Schlüssel und gibt dessen Wert zurück.                                                  | `wert = dict.pop('schluessel')`     |
| `popitem()`     | Entfernt und gibt ein zufälliges Schlüssel-Wert-Paar als Tupel zurück.                                                           | `schluessel, wert = dict.popitem()` |
| `clear()`       | Entfernt alle Elemente aus dem Dictionary.                                                                                       | `dict.clear()`                      |
| `copy()`        | Erstellt eine flache Kopie des Dictionaries.                                                                                     | `neues_dict = dict.copy()`          |

Diese Tabelle bietet einen Überblick über gängige Methoden, die bei der Arbeit mit Dictionaries in Python verwendet
werden.

Dictionaries sind nützlich für die Speicherung und Manipulation von Schlüssel-Wert-Paaren und bieten schnellen
Zugriff sowie flexible Datenstrukturen.