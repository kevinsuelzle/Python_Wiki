# Getter, Setter und @property in Python
[80min]

In Python gibt es verschiedene Ansätze, um den Zugriff auf Attribute zu steuern. Der Unterstrich `_` vor einem Attribut kennzeichnet es als "privat" und signalisiert, dass es nicht direkt von außerhalb der Klasse geändert werden sollte. Hier betrachten wir die Verwendung von nativen Getter- und Setter-Methoden sowie die Verwendung von `@property`.

## Sichtbarkeit und Unterstrich `_`:

In Python gibt es keine strikte Privatsphäre wie in einigen anderen Programmiersprachen, aber ein vorangestellter Unterstrich `_` signalisiert, dass ein Attribut als privat betrachtet wird. Das bedeutet, dass es von außerhalb der Klasse nicht direkt zugegriffen oder geändert werden sollte. Es ist eher eine Konvention als eine Durchsetzung.

```python
class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
```

## Native Getter und Setter:

Eine Möglichkeit, den Zugriff auf Attribute zu steuern, besteht darin, Getter- und Setter-Methoden zu verwenden.

```python
class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    def get_titel(self):
        return self._titel

    def set_titel(self, neuer_titel):
        self._titel = neuer_titel

    def get_autor(self):
        return self._autor

    def set_autor(self, neuer_autor):
        self._autor = neuer_autor

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
```

Hier werden Getter- und Setter-Methoden verwendet, um auf die privaten Attribute `titel` und `autor` zuzugreifen.

## @property für Getter und Setter:

Mit `@property` kann man Getter- und Setter-Funktionalität auf eine elegante Weise implementieren. Der Dekorator `@property` wird vor die Methode gesetzt, die als Getter fungiert, und `@<property_name>.setter` wird vor die Methode gesetzt, die als Setter fungiert.

```python
class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    @property
    def titel(self):
        return self._titel

    @titel.setter
    def titel(self, neuer_titel):
        self._titel = neuer_titel

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, neuer_autor):
        self._autor = neuer_autor

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
```

# Neue Schlüsselwörter:

- **Getter und Setter:**  
Getter und Setter sind Methoden, die den Lese- und Schreibzugriff auf Attribute ermöglichen. Der Getter liest den Wert eines Attributs, während der Setter den Wert setzt. [Python Docs - property](https://docs.python.org/3/library/functions.html#property)

- **@property:**  
`@property` ist ein Dekorator in Python, der es ermöglicht, eine Methode wie ein Attribut zu behandeln. Es wird verwendet, um den Zugriff auf Attribute zu steuern. [Python Docs - property](https://docs.python.org/3/library/functions.html#property)

- **@setter:**  
`@setter` ist ein spezifischer Dekorator, der mit `@property` verwendet wird, um die Setzung eines Attributs zu steuern. Es wird verwendet, um die Zuweisung eines Werts über den Setter zu ermöglichen. [Python Docs - property](https://docs.python.org/3/library/functions.html#property)

- **_ (Einzelnes Unterstrich):**  
Ein einzelnes Unterstrichzeichen vor einem Attribut (z. B. `_attribut`) signalisiert, dass es als schwach "internen" oder "privaten" Verweis betrachtet werden sollte. Es ist jedoch nur eine Konvention und hat keine eigentliche Auswirkung auf die Sichtbarkeit. [Python Docs - Benennungskonventionen](https://www.python.org/dev/peps/pep-0008/#single-leading-underscore)

# Neue Begriffe:

- **Getter:**  
Ein Getter ist eine Methode, die den Wert eines privaten Attributs zurückgibt. Es ermöglicht den Lesezugriff auf das Attribut von außerhalb der Klasse. Der Getter wird normalerweise mit `@property` implementiert.

- **Setter:**  
Ein Setter ist eine Methode, die den Wert eines privaten Attributs setzt. Es ermöglicht den Schreibzugriff auf das Attribut von außerhalb der Klasse. Der Setter wird normalerweise mit `@setter` implementiert.

- **Sichtbarkeit (Visibility):**  
Sichtbarkeit bezieht sich auf die Zugriffsberechtigungen von Attributen und Methoden. In Python gibt es keine strikte Privatsphäre, sondern nur Konventionen, die durch Namenskonventionen und Name Mangling erreicht werden.

# Aufgaben:
[240min]

## 1. **Buchverwaltung mit Getter, Setter und @property 🌶️🌶️**:
   Erkläre, wie Sichtbarkeit und Getter/Setter zusammenarbeiten, um den Zugriff auf Attribute zu steuern. Erweitere die Klasse `Buch` um @property-Dekoratoren für die Attribute `titel` und `autor`. Zeige, wie @property Getter- und Setter-Funktionalität bereitstellt.

## 2. **Kreisberechnungen mit @property 🌶️🌶️🌶️**:
   Erstelle eine Klasse `Kreis` mit einem privaten Attribut `radius`. Implementiere Getter- und Setter-Funktionen für das Attribut und zeige dann, wie @property verwendet werden kann, um den Zugriff auf das Attribut zu steuern.

## 3. **Temperaturumrechner mit Eigenschaften 🌶️🌶️**:
   Entwickle eine Klasse `Temperaturumrechner`, die private Attribute für Celsius und Fahrenheit hat. Implementiere @property-Dekoratoren, um den Zugriff auf diese Attribute zu ermöglichen. Füge außerdem Methoden hinzu, um von Celsius nach Fahrenheit und umgekehrt umzurechnen.

## 4. **Benutzerkonto mit Guthaben und Transaktionen 🌶️🌶️🌶️**:
   Erstelle eine Klasse `Benutzerkonto`, die ein privates Attribut `guthaben` hat. Implementiere @property-Dekoratoren, um den Zugriff auf das Guthaben zu ermöglichen. Füge Methoden hinzu, um Einzahlungen und Abhebungen vorzunehmen, und zeige dies anhand von Transaktionen.

## 5. **Autoverwaltung mit Kilometerstand 🌶️🌶️**:
   Entwickle eine Klasse `Auto`, die private Attribute für Marke, Modell und Kilometerstand hat. Implementiere @property-Dekoratoren, um den Zugriff auf diese Attribute zu steuern. Füge Methoden hinzu, um den Kilometerstand zu erhöhen und anzuzeigen.

## 6. **Warenkorb mit Produkten und Preisen 🌶️🌶️🌶️**:
   Erstelle eine Klasse `Warenkorb`, die private Attribute für Produkte und Preise enthält. Implementiere @property-Dekoratoren, um den Zugriff auf diese Attribute zu steuern. Füge Methoden hinzu, um Produkte hinzuzufügen, den Gesamtpreis zu berechnen und den Inhalt des Warenkorbs anzuzeigen.

## 7. **Schülerverwaltung mit Noten 🌶️🌶️🌶️🌶️**:
   Implementiere eine Klasse `Schüler`, die private Attribute für den Namen und die Noten eines Schülers enthält. Verwende @property-Dekoratoren, um den Zugriff auf diese Attribute zu steuern. Füge Methoden hinzu, um den Durchschnitt der Noten zu berechnen und die Noten anzuzeigen.