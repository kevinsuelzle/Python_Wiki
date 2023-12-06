# Dictionaries (Schlüssel-Wert-Paare):

Dictionaries sind ein Datentyp in Python, mit dem wir Schlüssel-Wert-Paar beschreiben können. 
Sie ermöglichen uns, Werte mithilfe von Schlüsseln zu speichern und abzurufen, ähnlich wie ein echtes Wörterbuch es 
erlaubt, die Bedeutung eines Wortes zu finden. Wir erinnern uns an Listen oder Tupels, bei denen wir auf die Elemente
durch ihre Position in der Sammlung, also deren Index, auf die Elemente zugreifen können. 

## Eigenschaften von Dictionaries

- **Schlüssel und Werte**: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

- **Einzigartige Schlüssel**: Jeder Schlüssel in einem Dictionary muss einzigartig sein. Sollen mehrere Elemente in 
    in einem Schlüssel gespeichert werden, kann man natürlich auch eine Liste in diesem Schlüssel speichern

- **Veränderbar**: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert
   werden können.

- **Ungeordnet**: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert. Man greift 
    auf die Elemente über deren Schlüssel zu.

- **Dynamisch**: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.

## Erstellen und Initialisieren eines Dictionaries

Wir erstellen Dictionaries mit geschweiften Klammern. Die Schlüssel-Wert-Paar werden dann jeweils mit 
`schlüssel: wert` angegeben:

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)
```

## Zugriff auf Werte

Der Zugriff auf die Werte erfolgt über den entsprechenden Schlüssel in eckigen Klammern. Das sieht ähnlich aus wie bei
Listen, nur dass wir keinen Index verwenden, sondern den entsprechenden Schlüssel.

```python
# Zugriff auf den Wert mit dem Schlüssel "Name"
name = mein_dict["Name"]
print(name)  # Gibt "Max" aus
```

## Hinzufügen und Ändern von Einträgen

Werte können hinzugefügt werden, in dem wir einem Element, einen Schlüssel hinzufügen und diesem einen Wert zuweisen.
Existiert der Schlüssel bereits wird der vorhandene Wert einfach überschrieben.

```python
# Hinzufügen eines neuen Eintrags
mein_dict["Beruf"] = "Ingenieur"

# Ändern eines vorhandenen Eintrags
mein_dict["Alter"] = 26
```

## Entfernen von Einträgen

Das Entfernen von Einträgen sieht leider nicht wie typischer Python-Code aus. Man greift auf das Element, welches man 
löschen will wie gewohnt zu und löscht das Element mit einem vorangestellten `del`.

```python
# Entfernen eines Eintrags
del mein_dict["Stadt"]
```

## Durchlaufen eines Dictionaries

```python
# Durchlaufen aller Schlüssel-Wert-Paare
for key, value in mein_dict.items():
    print(key, value)
```

## Häufige Funktionen und Methoden für Dictionaries in Python

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

## Anwendungsbeispiele

Dictionaries sind nützlich für die Speicherung und Manipulation von Schlüssel-Wert-Paaren und bieten schnellen
Zugriff sowie flexible Datenstrukturen.

- **Datenorganisation**: Dictionaries sind ideal für die Speicherung und Organisation komplexer Daten, wie z.B.
  Benutzerinformationen oder Konfigurationseinstellungen.
- **Schneller Zugriff**: Aufgrund ihrer internen Struktur bieten Dictionaries einen schnellen Zugriff auf ihre Elemente.

# Aufgaben

### 1. **Grundlegendes Dictionary**: 
Erstelle ein Dictionary mit drei Schlüssel-Wert-Paaren und gib es aus.
### 2. **Zugriff auf Werte**:
Greife auf einen Wert in einem Dictionary zu und gib ihn aus.
### 3. **Hinzufügen eines Eintrags**: 
Füge einem bestehenden Dictionary einen neuen Schlüssel-Wert-Eintrag hinzu.
### 4. **Ändern eines Wertes**: 
Ändere den Wert eines bestehenden Eintrags in einem Dictionary.
### 5. **Entfernen eines Eintrags**: 
Entferne einen Eintrag aus einem Dictionary.
### 6. **Durchlaufen mit Schleifen**:
Durchlaufe ein Dictionary und gib alle Schlüssel und deren zugehörige Werte aus.
### 7. **Nur Schlüssel durchlaufen**: 
Durchlaufe ein Dictionary und gib nur die Schlüssel aus.
### 8. **Nur Werte durchlaufen**: 
Durchlaufe ein Dictionary und gib nur die Werte aus.
### 9. **Schlüssel-Existenz prüfen**: 
Überprüfe, ob ein bestimmter Schlüssel in einem Dictionary existiert.
### 10. **Nested Dictionary**:
Erstelle ein verschachteltes Dictionary (ein Dictionary innerhalb eines anderen Dictionaries)
    und greife auf ein Element des inneren Dictionaries zu.

[Lösungen](solution.md#lösungen)

# Komplex-Aufgaben

### Aufgabe 1: Wortzähler

Schreibe ein Programm, das einen Text (String) entgegennimmt und ein Dictionary zurückgibt, das die Häufigkeit jedes
Wortes im Text zählt. Wörter sollen unabhängig von Groß- und Kleinschreibung gezählt werden. Verwende `input()` zur
Eingabe des Textes.

### Aufgabe 2: Telefonbuch

Erstelle ein einfaches Telefonbuch-Programm, das es dem Benutzer ermöglicht, Namen und Telefonnummern hinzuzufügen, zu
suchen, zu ändern und zu löschen. Verwende ein Dictionary zur Speicherung der Daten. Das Programm soll fortlaufend
laufen, bis der Benutzer sich entscheidet, es zu beenden.

### Aufgabe 3: Lagerbestandsverwaltung

Implementiere ein Lagerbestandsverwaltungssystem. Erstelle ein Dictionary, das Produkte und ihre Mengen enthält. Das
Programm soll es dem Benutzer ermöglichen, neue Produkte hinzuzufügen, vorhandene zu aktualisieren und Produkte zu
löschen. Zusätzlich soll das Programm eine Übersicht über alle Produkte und Mengen anzeigen können.

### Aufgabe 4: Verschachteltes Dictionary analysieren

Gegeben sei ein verschachteltes Dictionary, das Daten von Studenten und ihren Noten in verschiedenen Fächern enthält (
z.B. `studenten = {"Anna": {"Mathe": 1, "Englisch": 2}, "Max": {"Mathe": 3, "Englisch": 2}}`). Schreibe ein Programm,
das für jeden Studenten den Durchschnitt seiner Noten berechnet und diesen ausgibt. Nutze Schleifen, um durch das
Dictionary zu iterieren.

Diese Aufgaben kombinieren die Nutzung von Dictionaries mit anderen grundlegenden Python-Konzepten wie Schleifen und
Bedingungsanweisungen. Sie sind darauf ausgelegt, das Verständnis und die Fähigkeiten im Umgang mit Dictionaries und
Datenstrukturen im Allgemeinen zu verbessern.

[Lösungen](solution.md#komplex-aufgaben)