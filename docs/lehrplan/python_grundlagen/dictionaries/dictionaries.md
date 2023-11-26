# Dictionaries (Schlüssel-Wert-Paare):

Dictionaries in Python sind Sammlungen von Schlüssel-Wert-Paaren. Sie ermöglichen es, Werte durch Schlüssel zu speichern
und abzurufen, ähnlich wie ein echtes Wörterbuch es erlaubt, die Bedeutung eines Wortes zu finden.

## Eigenschaften von Dictionaries

1. **Schlüssel und Werte**: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

2. **Einzigartige Schlüssel**: Jeder Schlüssel in einem Dictionary muss einzigartig sein.

3. **Veränderbar**: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert
   werden können.

4. **Ungeordnet**: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert.

5. **Dynamisch**: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.

## Erstellen und Initialisieren eines Dictionaries

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)
```

## Zugriff auf Werte

```python
# Zugriff auf den Wert mit dem Schlüssel "Name"
name = mein_dict["Name"]
print(name)  # Gibt "Max" aus
```

## Hinzufügen und Ändern von Einträgen

```python
# Hinzufügen eines neuen Eintrags
mein_dict["Beruf"] = "Ingenieur"

# Ändern eines vorhandenen Eintrags
mein_dict["Alter"] = 26
```

## Entfernen von Einträgen

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

## Aufgaben

1. **Grundlegendes Dictionary**: Erstelle ein Dictionary mit drei Schlüssel-Wert-Paaren und gib es aus.
2. **Zugriff auf Werte**: Greife auf einen Wert in einem Dictionary zu und drucke ihn aus.
3. **Hinzufügen eines Eintrags**: Füge einem bestehenden Dictionary einen neuen Schlüssel-Wert-Eintrag hinzu.
4. **Ändern eines Wertes**: Ändere den Wert eines bestehenden Eintrags in einem Dictionary.
5. **Entfernen eines Eintrags**: Entferne einen Eintrag aus einem Dictionary.
6. **Durchlaufen mit Schleifen**: Durchlaufe ein Dictionary und drucke alle Schlüssel und deren zugehörige Werte aus.
7. **Nur Schlüssel durchlaufen**: Durchlaufe ein Dictionary und drucke nur die Schlüssel aus.
8. **Nur Werte durchlaufen**: Durchlaufe ein Dictionary und drucke nur die Werte aus.
9. **Schlüssel-Existenz prüfen**: Überprüfe, ob ein bestimmter Schlüssel in einem Dictionary existiert.
10. **Nested Dictionary**: Erstelle ein verschachteltes Dictionary (ein Dictionary innerhalb eines anderen Dictionaries)
    und greife auf ein Element des inneren Dictionaries zu.

## Komplex-Aufgaben

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

# Lösungen

1. **Grundlegendes Dictionary**
   ```python
   mein_dict = {"Name": "Anna", "Alter": 30, "Beruf": "Ingenieurin"}
   print(mein_dict)
   ```

2. **Zugriff auf Werte**
   ```python
   print(mein_dict["Name"])  # Gibt "Anna" aus
   ```

3. **Hinzufügen eines Eintrags**
   ```python
   mein_dict["Stadt"] = "Berlin"
   print(mein_dict)
   ```

4. **Ändern eines Wertes**
   ```python
   mein_dict["Alter"] = 31
   print(mein_dict)
   ```

5. **Entfernen eines Eintrags**
   ```python
   del mein_dict["Beruf"]
   print(mein_dict)
   ```

6. **Durchlaufen mit Schleifen**
   ```python
   for key, value in mein_dict.items():
       print(f"{key}: {value}")
   ```

7. **Nur Schlüssel durchlaufen**
   ```python
   for key in mein_dict.keys():
       print(key)
   ```

8. **Nur Werte durchlaufen**
   ```python
   for value in mein_dict.values():
       print(value)
   ```

9. **Schlüssel-Existenz prüfen**
   ```python
   key = "Name"
   if key in mein_dict:
       print(f"{key} ist im Dictionary vorhanden.")
   else:
       print(f"{key} ist nicht im Dictionary vorhanden.")
   ```

10. **Nested Dictionary**
    ```python
    mein_nested_dict = {
        "person1": {"Name": "Max", "Alter": 25},
        "person2": {"Name": "Lisa", "Alter": 28}
    }
    print(mein_nested_dict["person1"]["Name"])  # Gibt "Max" aus
    ```

## Komplex-Aufgaben

Hier sind die Lösungen für die vorgeschlagenen komplexen Aufgaben mit Python Dictionaries:

### Lösung zu Aufgabe 1: Wortzähler

```python
text = input("Gib einen Text ein: ").lower()
wort_haeufigkeit = {}

for wort in text.split():
    if wort in wort_haeufigkeit:
        wort_haeufigkeit[wort] += 1
    else:
        wort_haeufigkeit[wort] = 1

print(wort_haeufigkeit)
```

### Lösung zu Aufgabe 2: Telefonbuch

```python
telefonbuch = {}

while True:
    aktion = input("Wähle eine Aktion: hinzufügen, suchen, ändern, löschen, beenden: ")

    if aktion == "beenden":
        break
    elif aktion == "hinzufügen":
        name = input("Name: ")
        nummer = input("Telefonnummer: ")
        telefonbuch[name] = nummer
    elif aktion == "suchen":
        name = input("Name: ")
        print(telefonbuch.get(name, "Nicht gefunden"))
    elif aktion == "ändern":
        name = input("Name: ")
        if name in telefonbuch:
            nummer = input("Neue Telefonnummer: ")
            telefonbuch[name] = nummer
        else:
            print("Name nicht im Telefonbuch")
    elif aktion == "löschen":
        name = input("Name: ")
        if name in telefonbuch:
            del telefonbuch[name]
        else:
            print("Name nicht im Telefonbuch")

    print("Aktuelles Telefonbuch:", telefonbuch)
```

### Lösung zu Aufgabe 3: Lagerbestandsverwaltung

```python
lager = {}

while True:
    aktion = input("Aktion wählen: hinzufügen, aktualisieren, löschen, anzeigen, beenden: ")

    if aktion == "beenden":
        break
    elif aktion == "hinzufügen":
        produkt = input("Produktname: ")
        menge = int(input("Menge: "))
        lager[produkt] = lager.get(produkt, 0) + menge
    elif aktion == "aktualisieren":
        produkt = input("Produktname: ")
        if produkt in lager:
            menge = int(input("Neue Menge: "))
            lager[produkt] = menge
        else:
            print("Produkt nicht gefunden")
    elif aktion == "löschen":
        produkt = input("Produktname: ")
        if produkt in lager:
            del lager[produkt]
        else:
            print("Produkt nicht gefunden")
    elif aktion == "anzeigen":
        for produkt, menge in lager.items():
            print(f"{produkt}: {menge}")

    print("Aktueller Lagerbestand:", lager)
```

### Lösung zu Aufgabe 4: Verschachteltes Dictionary analysieren

```python
studenten = {"Anna": {"Mathe": 1, "Englisch": 2}, "Max": {"Mathe": 3, "Englisch": 2}}

for name, faecher in studenten.items():
    durchschnitt = sum(faecher.values()) / len(faecher)
    print(f"{name}: Durchschnittsnote = {durchschnitt:.2f}")
```
