# Anhang

## Globale Parameter

- **Aufgabe**: Beispiele für nyladische Funktionen

    - **`random.random()`:** Gibt eine Zufallszahl zwischen 0.0 und 1.0 zurück. Erfordert `import random`.
    - **`uuid.uuid4()`:** Erzeugt eine zufällige UUID. Erfordert `import uuid`.
    - **`os.urandom()`:** Gibt eine Zeichenfolge von n zufälligen Bytes zurück. Erfordert `import os`.
    - **`time.time()`:** Gibt die aktuelle Zeit in Sekunden seit der Epoche (1. Januar 1970) zurück.
      Erfordert `import time`.
    - **`datetime.datetime.now()`:** Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
      Erfordert `import datetime`.
    - **`itertools.count()`:** Erzeugt einen unendlichen Zähler. Erfordert `import itertools`.
    - **`sys.getsizeof()`:** Gibt die Größe eines Objekts in Bytes zurück. Erfordert `import sys`.
    - **`gc.collect()`:** Führt eine sofortige Garbage Collection aus. Erfordert `import gc`.

- **Aufgabe**: Beispiel für eine nyladische selbst verfasste Funktion:

```python
import random


def generate_random_numbers():
    """
    Die Funktion generiert eine Liste von 20 zufällige Zahlen zwischen 1 und 100 und gibt sie zurück.
    
    Args: keine
    """
    numbers = [random.randint(1, 100) for _ in range(20)]
    return numbers


# Beispielaufruf der Funktion
random_numbers = generate_random_numbers()
print(random_numbers)
```

## ListComprehension

**Aufgabe:** Code umschreiben

```python
my_list = []
for x in range(20):
    if x % 2 == 0 and x % 3 == 0:
        my_list.append(x ** 2)
```

## DRY

**Aufgabe**: Komplexeres Beispiel

```python
def verarbeite_personendaten(personen, zusatzlogik=None):
    verarbeitete_daten = []
    for person in personen:
        verarbeitete_person = {
            "name": person["name"],
            "email": person["email"]
        }
        if zusatzlogik:
            zusatzlogik(verarbeitete_person, person)
        verarbeitete_daten.append(verarbeitete_person)
    return verarbeitete_daten


def kundenlogik(verarbeitete_person, person):
    # Spezifische Logik für Kunden
    pass


def mitarbeiterlogik(verarbeitete_person, person):
    # Spezifische Logik für Mitarbeiter
    pass


# Beispielaufrufe
kunden = [{"name": "Kunde1", "email": "kunde1@example.com"}, ...]
mitarbeiter = [{"name": "Mitarbeiter1", "email": "mitarbeiter1@example.com"}, ...]

verarbeitete_kunden = verarbeite_personendaten(kunden, kundenlogik)
verarbeitete_mitarbeiter = verarbeite_personendaten(mitarbeiter, mitarbeiterlogik)
```

**Aufgabe**: Ausnahmen zur Regel

1. Über-Abstraktion

   Obwohl das DRY-Prinzip (Don't Repeat Yourself) generell als gute Praxis im Software-Engineering gilt, gibt es
   Situationen, in denen eine strikte Anwendung nicht ideal oder sogar kontraproduktiv sein kann. Hier sind einige
   Argumente, die gegen eine strikte Anwendung von DRY sprechen:
    - **Beschreibung:** Versuche, Wiederholungen zu vermeiden, können zu übermäßiger Abstraktion führen.
    - **Folge:** Der Code wird komplizierter und schwerer verständlich, besonders wenn die Abstraktionen nicht intuitiv
      oder schlecht dokumentiert sind.

2. Vorzeitige Optimierung

    - **Beschreibung:** Das vorzeitige Zusammenführen von Code in Funktionen oder Module kann problematisch sein.
    - **Folge:** Es entstehen starre Strukturen, die spätere Anpassungen erschweren.

3. Leichte Veränderungen in der Logik

    - **Beschreibung:** Ähnlicher, aber nicht identischer Code kann die Zusammenfassung komplex machen.
    - **Folge:** Es kann sinnvoller sein, ähnlichen Code separat zu halten, um Lesbarkeit und Wartbarkeit zu bewahren.

4. Leistungseinbußen

    - **Beschreibung:** In einigen Fällen kann die Vermeidung von Code-Duplikation zu Leistungseinbußen führen.
    - **Folge:** Ersetzen von Inline-Code durch Funktionsaufrufe kann Overhead verursachen, was in performance
      kritischen
      Anwendungen problematisch ist.

5. Erhöhte Kopplung

    - **Beschreibung:** Übermäßige Vermeidung von Duplikation kann zu einer erhöhten Kopplung zwischen Programmteilen
      führen.
    - **Folge:** Die Modularität kann beeinträchtigt werden, was den Code anfälliger für Fehler bei Änderungen macht.

6. Schwierigkeiten bei der Fehlerbehebung

    - **Beschreibung:** Wenn eine DRY-umsetzende Funktion einen Fehler aufweist, kann sich dieser auf mehrere
      Systemteile auswirken.
    - **Folge:** In manchen Fällen kann es sicherer sein, bestimmte Funktionalitäten zu duplizieren, besonders wenn sie
      kritisch sind und isoliert bleiben sollten.

### Zusammenfassung und Fazit

DRY ist ein Leitprinzip und sollte nicht als unumstößliches Gesetz angesehen werden. Die Entscheidung, wann und wie DRY
angewendet wird, sollte auf einem Gleichgewicht zwischen Code-Effizienz, Lesbarkeit und Wartbarkeit basieren. Eine
Dokumentation der Gründe erscheint angebracht.

## Funktionsparameter

**Aufgabe:** Reduktion von Parametern


1. **Verwendung von Objekten:**
    - Anstatt mehrere Parameter zu übergeben, können diese in einem Objekt zusammengefasst werden. Dies ist besonders
      nützlich, wenn mehrere Funktionen ähnliche Parameter benötigen.
    - Beispiel: Statt `function(a, b, c, d)` zu verwenden, erstellen Sie ein Objekt `params = {a, b, c, d}` und rufen
      Sie `function(params)` auf.

2. **Parameter-Objekte:**
    - Ähnlich wie oben, aber spezifischer, können Sie spezielle Klassen oder Strukturen definieren, die als
      Datencontainer dienen. Dies ist besonders nützlich in objektorientierten Sprachen.
    - Beispiel: Erstellen Sie eine Klasse `FunctionParams` mit den erforderlichen Attributen und übergeben Sie eine
      Instanz dieser Klasse an die Funktion.

3. **Standardwerte für Parameter:**
    - Definieren Sie Standardwerte für Parameter, um die Notwendigkeit zu verringern, Werte für alle Parameter bei jedem
      Aufruf anzugeben.
    - Beispiel: In Python können Sie `def function(a, b=5)` verwenden, wobei `b` optional ist und standardmäßig den Wert
      5 hat.

4. **Builder-Muster:**
    - Das Builder-Muster ist nützlich, wenn ein Objekt mit vielen optionalen Parametern erstellt werden muss. Es
      ermöglicht eine schrittweise Konstruktion von Objekten.
    - Beispiel: Anstatt einen Konstruktor mit vielen Parametern zu verwenden, ermöglicht der Builder schrittweise das
      Hinzufügen von Parametern.

5. **Methoden-Ketten (Fluent Interface):**
    - Ähnlich wie das Builder-Muster, aber für Methodenaufrufe. Methoden geben das eigene Objekt zurück, sodass weitere
      Aufrufe gekettet werden können.
    - Beispiel: `objekt.setA(a).setB(b).setC(c)`

6. **Argumente gruppieren:**
    - Gruppieren Sie verwandte Argumente in Unterobjekte oder Strukturen.
    - Beispiel: Statt `drawRectangle(x1, y1, x2, y2, color)` könnten Sie `drawRectangle(point1, point2, color)`
      verwenden, wobei `point1` und `point2` Objekte sind.

7. **Verwendung von Konfigurationsobjekten:**
    - Für komplexere Funktionen, insbesondere solche, die in Konfigurationen oder Umgebungen verwendet werden, können
      Konfigurationsobjekte übergeben werden, die alle erforderlichen Einstellungen enthalten.

8. **Currying und partielle Anwendung:**
    - In funktionalen Programmiersprachen können Sie Currying oder partielle Anwendung verwenden, um Funktionen zu
      erstellen, die einige Parameter vorab festlegen.

## Refactoring

### Lernziele: Refactoring

- **Grobziel**: Verstehen des Refactoring-Prozesses.
- **Richtziel**: Fähigkeit, Refactoring in bestehendem Code durchzuführen.
- **Feinziele**:
    - Identifizieren von "Code Smells".
    - Erlernen von Techniken zum Refactoring von Code.

### Inhalt

Dieser Abschnitt behandelt das Thema Refactoring, einschließlich der Identifizierung von Code Smells und der Schritte,
die erforderlich sind, um Code zu verbessern und zu optimieren.

---

## Beispiele und Übungen

### Lernziele: Beispiele und Übungen

- **Grobziel**: Anwendung des Gelernten in praktischen Beispielen.
- **Richtziel**: Selbstständige Verbesserung und Bewertung von Code.
- **Feinziele**:
    - Analyse und Verbesserung von Beispielcode.
    - Durchführung von Übungen zur Festigung des Gelernten.

### Inhalt

In diesem Kapitel werden praktische Übungen und Beispiele bereitgestellt, um das Verständnis von Clean Code zu
vertiefen. Die Schüler werden ermutigt, Code zu analysieren und zu verbessern.

---

## Zusätzliche Ressourcen

### Inhalt

Eine Liste von Büchern, Websites und Tools, die für weiterführende Studien zum Thema Clean Code nützlich sind.

---
