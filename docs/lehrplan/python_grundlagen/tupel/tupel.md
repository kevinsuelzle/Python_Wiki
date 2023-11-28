# Tupel in Python

In Python ist ein Tupel eine grundlegende Datenstruktur, die einer Liste ähnlich ist, aber einen entscheidenden
Unterschied aufweist: Sie ist unveränderlich. 

Das bedeutet, dass der Inhalt eines Tupels, sobald es erstellt wurde,
nicht mehr geändert werden kann. Dies ist nützlich, um die Integrität der Daten im gesamten Programm zu gewährleisten.

Tupel werden definiert, indem Elemente in Klammern `( )` eingeschlossen werden, wobei die Elemente durch Kommas getrennt
sind.

## Grundlegende Verwendung

Ein einfaches Beispiel für ein Tupel zum Beispiel die Defintion von Koordianten als ein Paar von zwei Fließkommazahlen:

```python
koordinaten = (50.8215, -0.1372)
```

Dieses Tupel, `koordinaten`, enthält zwei Fließkommazahlen und stellt einen festen Punkt auf einer Fläche dar.

## Eigenschaften von Tupeln

1. **Immutability:**
   Einmal erstellt, können wir keine Elemente zu einem Tupel hinzufügen, entfernen oder ändern. 

2. **Indizierung und Slicing:**
   Ähnlich wie Listen unterstützen Tupel die Indizierung und das Slicing. `koordinaten[0]` würde in unserem
   Beispiel `50.8215` zurückgeben.

3. **Iterierbarkeit:**
   Tupel können in Schleifen zur Iteration verwendet werden, genau wie Listen.

4. **Gemischte Datentypen:**
   Tupel können eine Mischung aus verschiedenen Datentypen enthalten: `('Hallo', 42, 3.14)` ist ein gültiges Tupel.

## Vorteile der Verwendung von Tupeln

- **Effizienz:** Tupel können hinsichtlich Speicherplatz und Leistung effizienter sein als Listen, besonders bei großen
  Datensätzen.
- **Sicherheit:** Da sie unveränderlich sind, können Tupel verwendet werden, um sicherzustellen, dass Daten im gesamten
  Programm unverändert bleiben.
- **Funktionalität:** Tupel können als Schlüssel in Wörterbüchern verwendet werden, Listen hingegen nicht.

Hier sehen wir einige Code-Beispiele, die verschiedene Aspekte von Tupeln in Python veranschaulichen:

## Arbeiten mit Tupels

### Erstellung und Zugriff auf Elemente:

```python
# Ein Tupel erstellen
fruechte = ("Apfel", "Banane", "Kirsche")

# Auf Elemente zugreifen
print(fruechte[0])  # Gibt 'Apfel' aus
print(fruechte[-1])  # Gibt 'Kirsche' aus (letztes Element)
```

### Unveränderlichkeit von Tupeln

Versuch, ein Element zu ändern (führt zu einem Fehler):

```python
fruechte[0] = "Erdbeere"  # Dies verursacht einen TypeError
```

### Tupel mit Gemischten Datentypen

```python
gemischtes_tupel = ("Max", 28, 1.75, True)
print(gemischtes_tupel)
```

### Tupel-Operationen

Verkettung und Wiederholung:

```python
# Tupel Verkettung
tupel1 = (1, 2, 3)
tupel2 = (4, 5, 6)
verkettetes_tupel = tupel1 + tupel2
print(verkettetes_tupel)  # Gibt (1, 2, 3, 4, 5, 6) aus

# Tupel wiederholen
wiederholtes_tupel = tupel1 * 2
print(wiederholtes_tupel)  # Gibt (1, 2, 3, 1, 2, 3) aus
```

### Tupel-Packen und -Entpacken

```python
# Tupel entpacken
name, alter, groesse = "Lisa", 30, 1.68

# Tupel packen
person_info = (name, alter, groesse)
print(person_info)

# Alternativ direkt beim Entpacken
(name, alter, groesse) = "Tom", 25, 1.80
print(name, alter, groesse)
```

### Verwendung von Tupeln als Schlüssel in einem Wörterbuch

```python
# Koordinaten als Schlüssel für Orte
orte = {(52.5200, 13.4050): "Berlin", (48.8566, 2.3522): "Paris"}
print(orte[(52.5200, 13.4050)])  # Gibt 'Berlin' aus
```

## Häufige Funktionen und Methoden für Tupel in Python

Hier ist eine übersichtliche Tabelle, die einige der häufigsten Funktionen und Methoden für Tupel in Python
zusammenfasst. Für jede Funktion/Methode gibt es eine kurze Beschreibung und ein kleines Beispiel.

| Funktionsname   | Kurzbeschreibung                                       | Beispiel                              |
|-----------------|--------------------------------------------------------|---------------------------------------|
| `len()`         | Gibt die Anzahl der Elemente im Tupel zurück.          | `len((1, 2, 3)) # Ergebnis: 3`        |
| `max()`         | Gibt das größte Element im Tupel zurück.               | `max((1, 4, 2)) # Ergebnis: 4`        |
| `min()`         | Gibt das kleinste Element im Tupel zurück.             | `min((1, 4, 2)) # Ergebnis: 1`        |
| `sum()`         | Berechnet die Summe der Elemente im Tupel.             | `sum((1, 2, 3)) # Ergebnis: 6`        |
| `tupel.index()` | Sucht nach einem Element und gibt dessen Index zurück. | `(1, 2, 3).index(2) # Ergebnis: 1`    |
| `tupel.count()` | Zählt, wie oft ein Element im Tupel vorkommt.          | `(1, 2, 2, 3).count(2) # Ergebnis: 2` |

### Anmerkungen:

- `len()`, `max()`, `min()`, und `sum()` sind eingebaute Python-Funktionen, die auf Tupel anwendbar sind.
- `tupel.index()` und `tupel.count()` sind Methoden, die spezifisch für Tupel-Objekte sind. Hierbei ist `tupel` ein
  Platzhalter für das jeweilige Tupel-Objekt.

Diese Funktionen und Methoden sind grundlegend für die Arbeit mit Tupeln und ermöglichen es Ihnen, grundlegende Abfragen
und Operationen auf Tupel-Datenstrukturen durchzuführen.

## Aufgaben

1. Erstelle ein Tupel mit den Namen von fünf verschiedenen Früchten.
2. Zugriff auf das zweite Element im Tupel von Aufgabe 1.
3. Ändere das zweite Element im Tupel von Aufgabe 1 auf "Erdbeere" (Trickfrage).
4. Überprüfe, ob "Apfel" in dem Tupel von Aufgabe 1 enthalten ist.
5. Zähle, wie oft die Frucht "Banane" im Tupel von Aufgabe 1 vorkommt.
6. Erstelle ein neues Tupel, das die Elemente des Originaltupels in umgekehrter Reihenfolge enthält.
7. Erstelle ein Tupel aus den ersten drei Elementen des Tupels von Aufgabe 1.
8. Kombiniere das Tupel von Aufgabe 1 mit einem neuen Tupel, das drei Gemüsesorten enthält.
9. Multipliziere das Tupel von Aufgabe 1, um ein Tupel zu erstellen, das jedes Element dreimal enthält.
10. Erstelle ein verschachteltes Tupel, das das Originaltupel von Aufgabe 1 und das Gemüsetupel von Aufgabe 8 enthält.
11. Finde den Index des Elements "Kirsche" im Tupel von Aufgabe 1.
12. Erstelle ein Tupel mit Zahlen von 1 bis 5 und berechne die Summe der Zahlen.
13. Sortiere das Tupel von Aufgabe 12 in absteigender Reihenfolge (Hinweis: Tupel können nicht sortiert werden, aber es
    gibt einen Workaround).
14. Überprüfe, ob das Tupel von Aufgabe 1 ein Subtupel von dem in Aufgabe 10 erstellten verschachtelten Tupel ist.
15. Schreibe eine Funktion, die ein beliebiges Tupel nimmt und jedes Element davon in Großbuchstaben ausgibt (Hinweis:
    Funktioniert nur mit Strings).

## Komplex-Aufgaben

### Komplexe Aufgaben

#### Aufgabe 1: Einkaufsliste Manager

**Aufgabenstellung:**
Schreibe ein Programm, das eine Einkaufsliste verwaltet. Der Benutzer kann folgende Aktionen durchführen:

1. Ein neues Produkt zur Liste hinzufügen (mit Name und Menge als Tupel).
2. Ein Produkt von der Liste entfernen.
3. Die gesamte Liste anzeigen.
4. Beenden des Programms.

Die Einkaufsliste sollte eine Liste von Tupeln sein, wobei jedes Tupel aus einem Produktname und der dazugehörigen Menge
besteht.


## Zusammenfassung

Zusammenfassend sind Tupel eine einfache, aber mächtige Datenstruktur in Python. Ihre Unveränderlichkeit macht sie ideal
für die Speicherung von Daten, die sich nicht ändern sollen, wie feste Konfigurationen oder Einstellungen. Das
Verständnis, wann und wie man Tupel verwendet, ist eine grundlegende Fähigkeit in der Python-Programmierung und trägt zu
robusterem und fehlerresistenterem Code bei.

## Lösungen

1. `fruechte = ("Apfel", "Banane", "Kirsche", "Orange", "Mango")`
2. `print(fruechte[1]) # Gibt 'Banane' aus`
3. Dies ist nicht möglich, da Tupel unveränderlich sind.
4. `print("Apfel" in fruechte) # Gibt True aus, falls Apfel enthalten ist`
5. `print(fruechte.count("Banane")) # Gibt die Anzahl der 'Banane' aus`
6. `umgekehrtes_tupel = fruechte[::-1]`
7. `erste_drei = fruechte[:3]`
8. `gemuese = ("Karotte", "Brokkoli", "Zwiebel")`
   `kombiniert = fruechte + gemuese`
9. `dreifach = fruechte * 3`
10. `verschachtelt = (fruechte, gemuese)`
11. `print(fruechte.index("Kirsche")) # Gibt den Index von 'Kirsche' aus`
12. `zahlen = (1, 2, 3, 4, 5)`
    `print(sum(zahlen)) # Gibt die Summe aus, also 15`
13. `sortierte_zahlen = tuple(sorted(zahlen, reverse=True))`
14. `print(fruechte in verschachtelt) # Gibt True aus, falls fruechte ein Subtupel ist`
15.

```python
def drucke_gross(tupel):
    for element in tupel:
        if isinstance(element, str):
            print(element.upper())


drucke_gross(fruechte)
```

Dies druckt jedes String-Element im Tupel in Großbuchstaben aus.

### Einkaufslistenmanager

**Lösung:**

```python
einkaufsliste = []

while True:
    aktion = input("Wähle eine Aktion: Hinzufügen (h), Entfernen (e), Anzeigen (a), Beenden (b): ")

    if aktion == "h":
        produkt = input("Gib den Produktnamen ein: ")
        menge = input("Gib die Menge ein: ")
        einkaufsliste.append((produkt, menge))
    elif aktion == "e":
        produkt = input("Gib den Namen des zu entfernenden Produkts ein: ")
        einkaufsliste = [item for item in einkaufsliste if item[0] != produkt]
    elif aktion == "a":
        for produkt, menge in einkaufsliste:
            print(f"{produkt}: {menge}")
    elif aktion == "b":
        break
    else:
        print("Ungültige Eingabe.")
```


