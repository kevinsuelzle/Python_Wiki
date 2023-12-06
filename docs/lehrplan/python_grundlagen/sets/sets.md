# Sets

Ein Set ist eine Datenstruktur, die für die Speicherung einer ungeordneten Sammlung von einzigartigen Elementen
verwendet wird. Das heißt, dass sich die Elemente in einem Set nicht wiederholen. 

Sets bieten folgende Eigenschaften:

## Eigenschaften von Sets

1. **Ungeordnet**:
    - Sets haben keine feste Reihenfolge der Elemente.
    - Sie bieten dadurch auch keinen Indexzugriff wie Listen oder Tupel.

2. **Einzigartige Elemente**:
    - Jedes Element in einem Set ist einzigartig.
    - Duplikate werden ignoriert und tauchen im Set nur einmal auf..

3. **Unveränderliche Elemente**:
    - Sets können nur unveränderliche (immutable) Datentypen als Elemente enthalten, wie Zahlen, Strings und Tupel.
    - Das heißt, Listen und Dictionaries können zum Beispiel nicht in Sets gespeichert werden.

4. **Veränderlich**:
    - Sets selbst sind veränderlich, das heißt man kann Elemente hinzufügen und entfernen.

5. **Kein Indexzugriff**:
    - Aufgrund der Ungeordnetheit der Elemente gibt es keinen direkten Indexzugriff.
    - Die Mitgliedschaft eines Elements wird mit Methoden wie `in` überprüft.

## Erstellung und Nutzung von Sets

Sets werden mit geschweiften Klammern `{}` oder der `set()`-Funktion erstellt.

**Beispiel**:

```python
einzigartige_zahlen = {1, 2, 3, 4, 5}
buchstaben = {'a', 'b', 'c', 'd'}
abc = set(['a', 'b', 'c'])

for element in buchstaben:
    print(element)
```

Man kann Elemente zu einem Set hinzufügen (mit `add()`) und entfernen (mit `remove()` oder `discard()`).

Sets sind nützlich für mathematische Operationen wie Union, Schnitt und Differenz.

Hier eine Übersicht über häufig verwendete Funktionen im Zusammenhang mit Sets:

| Funktion                          | Beschreibung                                                                                           | Beispiel                                 |
|-----------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------|
| `set1.add(x)`                     | Fügt das Element `x` zum Set hinzu.                                                                    | `set1.add(5)`                            |
| `set1.remove(x)`                  | Entfernt das Element `x` aus dem Set. Wirft einen Fehler, falls `x` nicht vorhanden ist.               | `set1.remove(5)`                         |
| `set1.discard(x)`                 | Entfernt das Element `x` aus dem Set. Kein Fehler, wenn `x` nicht vorhanden ist.                       | `set1.discard(5)`                        |
| `set.1pop()`                      | Entfernt und gibt ein zufälliges Element aus dem Set zurück.                                           | `element = set1.pop()`                   |
| `set1.clear()`                    | Entfernt alle Elemente aus dem Set.                                                                    | `set1.clear()`                           |
| `set1.union(set2)`                | Gibt ein Set zurück, dass die Summe der Elemente von `set1` und `set2` enthält                         |                                          |                                                                                                     | Gibt ein neues Set zurück, das die Vereinigung von `set1` und `set2` ist.                              | `set3 = set1.union(set2)`                |
| `set1.intersection(set2)`         | Gibt ein neues Set zurück, das die Schnittmenge von `set1` und `set2` ist.                             | `set3 = set1.intersection(set2)`         |
| `set1.difference(set2)`           | Gibt ein neues Set zurück, das die Elemente von `set1` enthält, die nicht in `set2` sind.              | `set3 = set1.difference(set2)`           |
| `set1.symmetric_difference(set2)` | Gibt ein neues Set zurück, das Elemente enthält, die in `set1` oder `set2`, aber nicht in beiden sind. | `set3 = set1.symmetric_difference(set2)` |

Für einige Funktionen gibt es seit neustem auch Kurzformen:

- `set1.union(set2)`: `set1 | set2` gibt ein neues Set mit allen Elementen aus beiden Sets zurück.
- `set1.intersect(set2)`: `set1 & set2` gibt ein Set mit Elementen zurück, die in beiden Sets vorhanden sind.
- `set1.difference(set2)`: `set1 - set2` gibt ein Set mit Elementen zurück, die in set1, aber nicht in set2 sind.
- `set1.symmetric_difference(set2)`: `set1 ^ set2` gibt ein Set mit Elementen zurück, die nur in einem der beiden Sets sind.

Sets sind nützlich, um Mengen zu speichern, in denen nur das Vorhandensein eines Elements relevant ist, jedoch
nicht wie oft dieses Element vorhanden ist.

## Anwendungsbeispiele

- Entfernen von Duplikaten: Sets können verwendet werden, um Duplikate aus einer Liste zu entfernen.
- Mitgliedschaftstests: Aufgrund ihrer internen Struktur sind Sets effizienter um zu Testen ob Elemente in dieser 
Struktur vorhanden sind als Listen.

# Aufgaben

[40min]

### 1. **Set Erstellung**:
Erstelle ein Set aus den Zahlen 1 bis 5 und gib es aus.
### 2. **Duplikatentfernung**:
Konvertiere die Liste `[1, 2, 2, 3, 4, 5, 5, 6]` in ein Set, um Duplikate zu entfernen.
### 3. **Elemente Hinzufügen**: 
Füge die Zahlen 6, 7 und 8 zu dem Set aus Aufgabe 1 hinzu.
### 4. **Element Entfernen**: 
Entferne die Zahl 5 aus dem Set, das du in Aufgabe 3 erstellt hast.
### 5. **Set Durchlaufen**:
Durchlaufe ein Set und drucke jedes Element aus.
### 6. **Set Union**:
Erstelle zwei Sets, `set1 = {1, 2, 3}` und `set2 = {3, 4, 5}`, und finde ihre Union.
### 7. **Set Schnittmenge**:
Finde die Schnittmenge von `set1` und `set2` aus der vorherigen Aufgabe.
### 8. **Set Differenz**:
Ermittle die Differenz zwischen `set1` und `set2`.
### 9. **Symmetrische Differenz**:
Finde die symmetrische Differenz zwischen `set1` und `set2`.
### 10. **Set Länge**: 
Ermittle die Anzahl der Elemente in einem Set deiner Wahl.
### 11. **Set Mitgliedschaftstest**:
Überprüfe, ob ein bestimmtes Element in einem Set vorhanden ist.
### 12. **Set Leeren**: 
Entferne alle Elemente aus einem Set.
### 13. **Subsets**:
Überprüfe, ob ein Set ein Subset eines anderen Sets ist.
### 14. **Supersets**: 
Überprüfe, ob ein Set ein Superset eines anderen Sets ist.
### 15. **Frozen Set**: 
Erstelle ein `frozenset` aus der Liste `[1, 2, 3, 4, 5]` und erkläre den Unterschied zwischen
    einem `set` und einem `frozenset`.

[Lösungen](solutions.md)