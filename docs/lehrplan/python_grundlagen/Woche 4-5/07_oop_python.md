# Objektorientierte Programmierung (OOP) mit Python
[120min]

Die objektorientierte Programmierung (OOP) ist in Python weit verbreitet und basiert auf den grundlegenden Konzepten von Klassen und Objekten. Hier werfen wir einen Blick auf die Prinzipien der OOP in Python.

## Klassen und Objekte in Python

In Python werden Klassen erstellt, um Objekte zu definieren. Eine Klasse ist eine Bauplan für Objekte, die Attribute (Variablen) und Methoden (Funktionen) enthalten kann. Ein Objekt ist eine Instanz einer Klasse.

```python
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def zeige_info(self):
        print(f"Marke: {self.marke}, Farbe: {self.farbe}")
```

In diesem Beispiel erstellen wir eine Klasse namens `Auto`. Die Methode `__init__` wird beim Erstellen eines neuen Objekts aufgerufen und initialisiert die Attribute `marke` und `farbe`. Die Methode `zeige_info` gibt Informationen zum Auto aus.

Ein Objekt ist eine Instanz einer Klasse. Wenn wir die Klasse Auto instanziieren, erhalten wir ein konkretes Auto-Objekt.

Um eine Instanz, ein Objekt von der Klasse `Auto` zu erstellen schreiben wir:

```python
# Erstellen einer Instanz und speichern in Variable
tiguan = Auto("Volkswagen", "rot")

# Zugriff auf die Methode
tiguan.zeige_info()
```

Wir können demnach auch mehrere Objekte erstellen und diese beispielsweise in einer Liste speichern:

```python
# Erstellen einer Instanz und speichern in Variable
tiguan = Auto("Volkswagen", "rot")
golf = Auto("Volkswagen", "blau")
id4 = Auto("Volkswagen", "schwarz")

autos = [tiguan, golf, id4]

# Iteriere über alle Autos in der Liste
for a in autos:
    a.zeige_info()
```

## Attribute

Attribute sind Daten, die zu einem Objekt gehören und seinen Zustand repräsentieren. Im obigen Beispiel sind `marke` und `farbe` Attribute unseres `Auto`-Objekts.

## Methoden

Methoden sind Funktionen, die zu einer Klasse gehören und Operationen auf den Daten der Klasse ausführen. Sie können auf Attribute zugreifen und diese verarbeiten.

Hier haben wir die Methode `zeige_infos` hinzugefügt, die Informationen über das Auto ausgibt.

In Python wird `self` als Parameter in den Methoden verwendet, um auf das aktuelle Objekt zuzugreifen. Es ist eine Konvention, `self` zu verwenden, kann aber auch anders benannt werden.

## Das `self` Schlüsselwort

In Python steht das `self` Schlüsselwort für die Instanz der Klasse selbst und wird als erster Parameter an alle Methoden übergeben. Es ermöglicht den Zugriff auf die Attribute und Methoden der Instanz innerhalb der Klasse.

```python
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def zeige_info(self):
        print(f"Marke: {self.marke}, Farbe: {self.farbe}")
```

# Neue Schlüsselwörter:

- **`class`:** Das Schlüsselwort in Python, um eine Klasse zu definieren. [Python Docs - class](https://docs.python.org/3/tutorial/classes.html)

- **`self`:** Ein Konventionsschlüsselwort in Python, das als erstes Argument in den Methoden einer Klasse verwendet wird und auf die Instanz der Klasse verweist. [Python Docs - instance](https://docs.python.org/3/tutorial/classes.html#instance-objects)

- **Instanzmethode:** Eine Methode, die auf Instanzen einer Klasse angewendet wird und automatisch das `self`-Argument enthält. [Python Docs - instance methods](https://docs.python.org/3/tutorial/classes.html#instance-methods)


# Neue Begriffe:

- **Klasse:** Ein Bauplan für Objekte, der Attribute (Variablen) und Methoden (Funktionen) definiert. In Python wird eine Klasse mit dem Schlüsselwort `class` erstellt.

- **Objekt:** Eine Instanz einer Klasse. Mit dem Befehl `objekt = Klasse()` wird eine Instanz der Klasse erstellt.

- **Instanz:** Ein konkretes Vorkommen eines Objekts. Wenn du ein Objekt von einer Klasse erstellst, erstellst du eine Instanz dieser Klasse.

- **Attribut:** Eine Variable, die zur Darstellung von Eigenschaften oder Merkmalen eines Objekts verwendet wird. In Python können Attribute in der `__init__`-Methode der Klasse initialisiert werden.

- **Methode:** Eine Funktion, die zu einer Klasse gehört und auf Objekten dieser Klasse aufgerufen wird. Methoden werden innerhalb der Klasse definiert und können auf Objekten dieser Klasse aufgerufen werden.

# Aufgaben zu Klassen
[360min]

## 1. **Bibliotheksverwaltungssystem 🌶️🌶️🌶️**
Entwickle ein einfaches System zur Verwaltung von Büchern in einer Bibliothek. Erstelle Klassen für Bücher und Bibliotheken. Die Bücherklasse sollte Attribute wie Titel, Autor und Verfügbarkeit haben. Die Bibliotheksklasse sollte Methoden zum Ausleihen und Zurückgeben von Büchern enthalten.

## 2. **Fahrzeugvermietungssystem 🌶️🌶️**
Implementiere ein System zur Vermietung von Fahrzeugen. Erstelle Klassen für Fahrzeuge (Auto, Motorrad usw.) und Vermietungsagenturen. Die Fahrzeugklasse sollte Informationen wie Modell, Baujahr und Verfügbarkeit enthalten. Die Vermietungsagenturklasse sollte Methoden zum Vermieten und Zurückgeben von Fahrzeugen haben.

## 3. **Online-Shop mit Warenkorb 🌶️🌶️🌶️**
Entwickle ein einfaches System für einen Online-Shop. Erstelle Klassen für Produkte und einen Warenkorb. Die Produkteklasse sollte Attribute wie Name, Preis und Lagerbestand haben. Die Warenkorbklasse sollte Methoden zum Hinzufügen von Produkten, Berechnen des Gesamtpreises und zum Abschließen des Kaufs haben.

## 4. **Schüler- und Kursverwaltung 🌶️🌶️**
Baue ein System zur Verwaltung von Schülern und Kursen. Erstelle Klassen für Schüler, Kurse und Lehrer. Die Schülerklasse sollte Informationen wie Name, Alter und Kurse haben. Die Kursklasse sollte Methoden zum Hinzufügen von Schülern und Lehrern enthalten.

## 5. **Zeitverwaltung mit Aufgabenliste 🌶️🌶️🌶️🌶️**
Entwickle eine Anwendung zur Zeitverwaltung. Erstelle Klassen für Aufgaben und eine Aufgabenliste. Die Aufgabenklasse sollte Attribute wie Titel, Beschreibung und Fälligkeitsdatum haben. Die Aufgabenlistenklasse sollte Methoden zum Hinzufügen, Löschen und Anzeigen von Aufgaben enthalten.

## 6. **Bankkonto-Transaktionen 🌶️🌶️**
Implementiere ein einfaches System für Bankkonto-Transaktionen. Erstelle Klassen für Konten und Transaktionen. Die Kontenklasse sollte Informationen wie Kontostand und Kontoinhaber haben. Die Transaktionsklasse sollte Methoden zum Einzahlen, Abheben und Anzeigen von Transaktionen enthalten.

## 7. **Flugbuchungssystem 🌶️🌶️🌶️**
Entwickle ein System zur Buchung von Flügen. Erstelle Klassen für Flüge, Passagiere und Buchungen. Die Flugklasse sollte Informationen wie Abflugort, Zielort und verfügbare Plätze haben. Die Passagierklasse sollte Attribute wie Name und Alter enthalten. Die Buchungsklasse sollte Methoden zum Buchen und Stornieren von Flügen haben.

## 8. **Fitness-Tracker 🌶️🌶️🌶️**
Baue eine Anwendung zur Verfolgung von Fitnessaktivitäten. Erstelle Klassen für Benutzer, Übungen und Trainingseinheiten. Die Benutzerklasse sollte Informationen wie Name, Alter und Trainingshistorie haben. Die Übungsklasse sollte Attribute wie Name, Kalorienverbrauch und Muskelgruppen enthalten. Implementiere Methoden zum Hinzufügen von Trainingseinheiten und Berechnen des Kalorienverbrauchs.

## 9. **Musikbibliothek 🌶️🌶️🌶️**
Entwickle ein System für die Verwaltung einer Musikbibliothek. Erstelle Klassen für Songs, Künstler und Alben. Die Songklasse sollte Attribute wie Titel, Dauer und Genre haben. Die Künstlerklasse sollte Informationen wie Name und Genre enthalten. Die Albumklasse sollte Methoden zum Hinzufügen von Songs und Anzeigen der Songliste haben.

## 10. **Restaurantreservierungssystem 🌶️🌶️🌶️🌶️**
Baue ein System zur Reservierung von Restauranttischen. Erstelle Klassen für Restaurants, Tische und Reservierungen. Die Restaurantklasse sollte Informationen wie Name und verfügbare Tische haben. Die Tischklasse sollte Attribute wie Kapazität und Verfügbarkeit enthalten. Die Reservierungsklasse sollte Methoden zum Reservieren und Stornieren von Tischen haben.
