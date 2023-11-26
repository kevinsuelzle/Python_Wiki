# Strings in Python

Ein String in Python ist eine Zeichenkette, die aus einer Abfolge von einzelnen Zeichen besteht. Strings werden in
Python in einfachen oder doppelten Anführungszeichen eingeschlossen (`''` oder `""`). Mehrzeilige Strings können mit
drei Anführungszeichen erstellt werden. (`''' '''' ` oder `""" """`).

## Eigenschaften von Strings

Hier sind die Eigenschaften von Strings in Python im Markdown-Format:

1. **Sequenz von Zeichen:** Ein String ist eine geordnete Sequenz von Zeichen. Jedes Zeichen in einem String hat eine
   Position, die durch einen Index dargestellt wird.

2. **Unveränderbarkeit (Immutable):** Strings sind in Python unveränderlich, dh sie können nach ihrer Erstellung nicht
   geändert werden. Sie können jedoch neue Strings durch Manipulation von vorhandenen Strings erstellen.

3. **Indizierbarkeit:** Jedes Zeichen in einem String hat einen eindeutigen Index, beginnend mit 0 für das erste
   Zeichen, 1 für das zweite Zeichen und so weiter.

4. **Slicing (Ausschneiden):** Strings unterstützen das Slicing, dh Sie können Teilzeichenketten aus einem String
   extrahieren, indem Sie einen Bereich von Indizes angeben.

5. **Länge (Length):** Die Länge eines Strings, dh die Anzahl der Zeichen in einem String, kann mit der Funktion `len()`
   ermittelt werden.

6. **Concatenation (Verkettung):** Sie können Strings mithilfe des `+`-Operators zu einem einzigen String verketten, um
   längere Zeichenketten zu erstellen.

7. **Escape-Zeichen:** Strings können Escape-Zeichen wie `\n` (für Zeilenumbruch) und `\t` (für Tabulator) enthalten, um
   spezielle Zeichen darzustellen.

8. **String-Methoden:** Python bietet eine Vielzahl von eingebauten String-Methoden, die Ihnen helfen, Zeichenketten zu
   manipulieren, zu durchsuchen, zu überprüfen und zu formatieren.

9. **Unicode-Unterstützung:** Strings in Python sind Unicode-zeichenketten, dh sie können Zeichen aus verschiedenen
   Sprachen und Schriften darstellen.

10. **Verwendung von Anführungszeichen:** Strings können entweder in einfachen Anführungszeichen (`'`) oder doppelten
    Anführungszeichen (`"`) eingeschlossen werden, solange die Anführungszeichen am Anfang und am Ende des Strings
    übereinstimmen.

## Beispiel

Hier ist ein konkretes Code-Beispiel, das die Verwendung von Strings in Python zeigt:

```python
# Eingabe eines Benutzernamens
benutzername = input("Bitte geben Sie Ihren Benutzernamen ein: ")

# Überprüfung der Länge des Benutzernamens
if len(benutzername) > 10:
    print("Der Benutzername ist zu lang.")
elif len(benutzername) < 3:
    print("Der Benutzername ist zu kurz.")
else:
    print(f"Willkommen, {benutzername}!")

# Überprüfung auf Großschreibung
if benutzername.isupper():
    print("Ihr Benutzername ist vollständig in Großbuchstaben geschrieben.")
elif benutzername.islower():
    print("Ihr Benutzername ist vollständig in Kleinbuchstaben geschrieben.")
else:
    print("Ihr Benutzername enthält sowohl Groß- als auch Kleinbuchstaben.")

# Überprüfung auf das Vorhandensein eines bestimmten Zeichens
if "!" in benutzername:
    print("Ihr Benutzername enthält ein Ausrufezeichen!")

# Konvertierung des Benutzernamens in Kleinbuchstaben
kleinbuchstaben_benutzername = benutzername.lower()
print(f"Ihr Benutzername in Kleinbuchstaben: {kleinbuchstaben_benutzername}")
```

In diesem Beispiel wird der Benutzer aufgefordert, einen Benutzernamen einzugeben. Dann werden if-Abfragen verwendet, um
verschiedene Bedingungen zu überprüfen:

1. Die Länge des Benutzernamens wird überprüft, und je nach Länge werden verschiedene Meldungen ausgegeben.

2. Es wird überprüft, ob der Benutzername ausschließlich aus Groß- oder Kleinbuchstaben besteht, und entsprechende
   Meldungen werden ausgegeben.

3. Es wird überprüft, ob ein Ausrufezeichen im Benutzernamen vorhanden ist, und eine Meldung wird ausgegeben, wenn dies
   der Fall ist.

4. Schließlich wird der Benutzername in Kleinbuchstaben konvertiert und angezeigt.

## Häufig verwendete Funktionen und Methoden im Zusammenhand mit Strings

Hier ist eine Tabelle mit häufig verwendeten Funktionen von Strings in Python im Markdown-Format:

| Funktion                    | Kurzbeschreibung                                                                                                               | Beispiel                                                                           |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `len(string)`               | Gibt die Länge des Strings zurück.                                                                                             | `text = "Python"`<br>`laenge = len(text)`                                          |
| `string.upper()`            | Konvertiert den String in Großbuchstaben.                                                                                      | `text = "python"`<br>`grossbuchstaben = text.upper()`                              |
| `string.lower()`            | Konvertiert den String in Kleinbuchstaben.                                                                                     | `text = "PYTHON"`<br>`kleinbuchstaben = text.lower()`                              |
| `string.strip()`            | Entfernt Leerzeichen am Anfang und Ende des Strings.                                                                           | `text = "  Beispiel "`<br>`bereinigt = text.strip()`                               |
| `string.replace(old, new)`  | Ersetzt Teilzeichenketten im String.                                                                                           | `text = "Hello, World!"`<br>`neuer_text = text.replace("Hello", "Hi")`             |
| `string.split(delimiter)`   | Teilt den String in Teile anhand eines Trennzeichen.                                                                           | `text = "Python ist toll"`<br>`woerter = text.split(" ")`                          |
| `string.find(substring)`    | Sucht nach einer Teilzeichenkette und gibt den Index des ersten Vorkommens zurück. Wenn nicht gefunden, wird -1 zurückgegeben. | `text = "Python ist toll"`<br>`index = text.find("ist")`                           |
| `string.startswith(prefix)` | Überprüft, ob der String mit einem bestimmten Präfix beginnt.                                                                  | `text = "Python"`<br>`ist_start = text.startswith("Py")`                           |
| `string.endswith(suffix)`   | Überprüft, ob der String mit einem bestimmten Suffix endet.                                                                    | `text = "Python"`<br>`ist_ende = text.endswith("on")`                              |
| `string.count(substring)`   | Zählt die Anzahl der Vorkommnisse einer Teilzeichenkette im String.                                                            | `text = "Python ist toll, Python ist mächtig."`<br>`anzahl = text.count("Python")` |

## Slicing

Slicing ist ein nützliches Konzept in Python, mit dem Sie Teilzeichenketten (Teilstrings) aus einem vorhandenen
String extrahieren können, indem Sie einen Bereich von Indizes angeben. Dies ermöglicht es Ihnen, auf Teile eines
Strings zuzugreifen, ohne den ursprünglichen String zu verändern.

Die Syntax für das Slicing lautet:

```python
substring = string[start:stop]
```

- `string`: Der ursprüngliche String, aus dem Sie einen Teil extrahieren möchten.
- `start`: Der Index, ab dem das Slicing beginnt (inklusiv). Der Standardwert ist 0, wenn nicht angegeben.
- `stop`: Der Index, an dem das Slicing endet (exklusiv). Der Standardwert ist die Länge des Strings, wenn nicht
  angegeben.

Hier ist ein Beispiel, das die Verwendung des Slicing in Python zeigt:

```python
text = "Python ist großartig."

# Teilstring von Index 0 bis 6 (exklusiv)
teil_text1 = text[0:6]  # Ergebnis: "Python"

# Teilstring von Index 7 bis 10 (exklusiv)
teil_text2 = text[7:10]  # Ergebnis: "ist"

# Teilstring ab Index 11 bis zum Ende des Strings
teil_text3 = text[11:]  # Ergebnis: "großartig."

# Teilstring von Anfang bis Index 5 (exklusiv)
teil_text4 = text[:5]  # Ergebnis: "Pytho"

# Negative Indizes - Teilstring von den letzten 7 Zeichen
teil_text5 = text[-7:]  # Ergebnis: "großartig."
```

In diesem Beispiel haben wir den String "Python ist großartig." definiert und verschiedene Slices davon erstellt:

- `teil_text1` enthält den Teilstring von Index 0 bis 6 (exklusiv), was "Python" ergibt.
- `teil_text2` enthält den Teilstring von Index 7 bis 10 (exklusiv), was "ist" ergibt.
- `teil_text3` enthält den Teilstring ab Index 11 bis zum Ende des Strings, was "großartig." ergibt.
- `teil_text4` enthält den Teilstring vom Anfang bis Index 5 (exklusiv), was "Pytho" ergibt.
- `teil_text5` verwendet negative Indizes, um den Teilstring von den letzten 7 Zeichen zu erhalten, was wieder "
  großartig." ergibt.

## Unicode in Python-Strings

Unicode ist ein wichtiges Konzept in Python, das die Verwendung von Zeichen aus verschiedenen Sprachen und
Schriftsystemen in Strings ermöglicht. In Python sind Strings Unicode-Zeichenketten, was bedeutet, dass sie Zeichen aus
dem gesamten Unicode-Zeichenvorrat unterstützen. Dies ermöglicht es, Texte in verschiedenen Sprachen zu verarbeiten und
Unicode-Sonderzeichen in Zeichenketten zu repräsentieren.

Die Verwendung von Unicode in Python erleichtert die internationale Textverarbeitung und ermöglicht die korrekte
Darstellung von Zeichen aus unterschiedlichen Schriften und Kulturen. Python bietet viele eingebaute Funktionen und
Bibliotheken, um mit Unicode-Zeichenketten zu arbeiten und Texte in verschiedenen Sprachen effektiv zu verarbeiten.

### Beispiel

Hier sehen wir ein einfaches Beispiel, das die Verwendung von Unicode in Python Strings zeigt:

```python
# Unicode-Zeichen in einem Python-String
unicode_string = "Python unterstützt Unicode \u2192 \U0001F609"
print(unicode_string)  # 'Python unterstützt Unicode → 😉'

# Länge des Strings mit Unicode-Zeichen
laenge = len(unicode_string)
print(f"Länge des Strings: {laenge} Zeichen")
```

In diesem Beispiel verwenden wir Unicode-Zeichen in einem Python-String. Das Zeichen `\u2192` repräsentiert einen
Pfeil (→) und `\U0001F609` repräsentiert das Emoji "😉". Wenn Sie diesen Code ausführen, wird der String korrekt mit den
Unicode-Zeichen angezeigt.

Die Verwendung von Unicode ermöglicht es uns, Zeichen aus verschiedenen Schriften und sogar Emoji in Zeichenketten
darzustellen und zu verarbeiten, was für die Unterstützung von Texten in verschiedenen Sprachen und für die Darstellung
von Symbolen und Emojis in Anwendungen sehr nützlich ist.

## Übungsaufgaben

1. Schreibe ein Programm, um die Länge eines Strings zu ermitteln.
2. Erstelle einen String und geben Sie ihn rückwärts aus.
3. Erstelle einen String und konvertieren Sie ihn in Großbuchstaben.
4. Erstelle einen String und zählen Sie die Anzahl der Vokale in ihm.
5. Schreibe einen Python-Code, um den ersten und den letzten Buchstaben eines Strings auszugeben.
6. Erstelle einen String und ersetzen Sie ein bestimmtes Zeichen darin durch ein anderes.
7. Schreibe eine Funktion, die prüft, ob ein gegebener String ein gültiger E-Mail-Adresse ist.
8. Erstelle einen String und entfernen Sie alle Leerzeichen daraus.
9. Erstelle einen String und teilen Sie ihn in Wörter auf.
10. Schreibe einen Python-Code, um den häufigsten Buchstaben in einem String zu finden.
11. Erstelle einen String und überprüfen Sie, ob er nur aus Zahlen besteht.
12. Schreibe eine Funktion, die zwei Strings nimmt und überprüft, ob sie Anagramme sind (dh dieselben Buchstaben in
    unterschiedlicher Reihenfolge).
13. Erstelle einen String und zählen Sie die Anzahl der Wörter darin.
14. Schreibe einen Python-Code, um alle Zeichen in einem String zu zählen.
15. Erstelle einen String und überprüfen Sie, ob er eine gültige URL ist.
16. Schreibe eine Funktion, die einen gegebenen String in einen Titel-Case-String umwandelt (jedes Wort beginnt mit
    einem Großbuchstaben).
17. Erstelle einen String und zählen Sie die Anzahl der Zeichen, die keine Buchstaben oder Zahlen sind (
    Sonderzeichen und Leerzeichen).
18. Schreibe einen Python-Code, um alle URLs in einem gegebenen Text zu extrahieren.
19. Schreibe eine Funktion, die überprüft, ob ein String ein Palindrom ist (d.h. rückwärts gelesen dasselbe wie
    vorwärts).

## Lösungen

Selbstverständlich, hier sind Lösungen zu den Übungsaufgaben zu Strings in Python:

1. Länge eines Strings ermitteln:
   ```python
   text = "Dies ist ein Beispiel"
   laenge = len(text)
   print(f"Länge des Strings: {laenge}")
   ```

2. String rückwärts ausgeben:
   ```python
   text = "Python"
   rueckwaerts = text[::-1]
   print(rueckwaerts)
   ```


1. String in Großbuchstaben konvertieren:
   ```python
   text = "python"
   grossbuchstaben = text.upper()
   print(grossbuchstaben)
   ```

2. Anzahl der Vokale zählen:
   ```python
   text = "Python ist großartig."
   anzahl_vokale = sum(1 for char in text if char.lower() in "aeiou")
   print(anzahl_vokale)
   ```

3. Erster und letzter Buchstabe eines Strings:
   ```python
   text = "Python"
   erster_buchstabe = text[0]
   letzter_buchstabe = text[-1]
   print(f"Erster Buchstabe: {erster_buchstabe}, Letzter Buchstabe: {letzter_buchstabe}")
   ```

4. Zeichen ersetzen:
   ```python
   text = "Python ist großartig."
   neuer_text = text.replace("groß", "super")
   print(neuer_text)
   ```

5. Funktion zur Überprüfung einer E-Mail-Adresse:
   ```python
   import re

   def ist_gueltige_email(email):
       pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       return re.match(pattern, email) is not None

   print(ist_gueltige_email("beispiel@email.com"))  # True
   print(ist_gueltige_email("keine-email"))  # False
   ```

6. Leerzeichen entfernen:
   ```python
   text = " Text mit Leerzeichen "
   ohne_leerzeichen = text.strip()
   print(ohne_leerzeichen)
   ```

7. String in Wörter aufteilen:
   ```python
   text = "Dies ist ein Satz."
   woerter = text.split()
   print(woerter)
   ```

8. Häufigster Buchstabe in einem String finden:
   ```python
   text = "Mississippi"
   haeufigster_buchstabe = max(set(text), key=text.count)
   print(haeufigster_buchstabe)
   ```

9. Überprüfung, ob ein String nur aus Zahlen besteht:
   ```python
   text = "12345"
   if text.isdigit():
       print("Der String besteht nur aus Zahlen.")
   else:
       print("Der String enthält andere Zeichen als Zahlen.")
   ```

10. Funktion zur Überprüfung von Anagrammen:
    ```python
    def sind_anagramme(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    print(sind_anagramme("listen", "silent"))  # True
    print(sind_anagramme("Python", "Java"))  # False
    ```

11. Anzahl der Wörter in einem String zählen:
    ```python
    text = "Dies ist ein Beispiel Satz."
    woerter = text.split()
    anzahl_woerter = len(woerter)
    print(f"Anzahl der Wörter: {anzahl_woerter}")
    ```

12. Anzahl der Zeichen in einem String zählen:
    ```python
    text = "Python ist großartig."
    anzahl_zeichen = sum(1 for char in text)
    print(f"Anzahl der Zeichen: {anzahl_zeichen}")
    ```

13. Überprüfung, ob ein String eine gültige URL ist (mithilfe einer regulären Ausdrucks):
    ```python
    import re

    def ist_gueltige_url(url):
        pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
        return re.match(pattern, url) is not None

    print(ist_gueltige_url("https://www.example.com"))  # True
    print(ist_gueltige_url("www.invalid-url"))  # False
    ```

14. String in Titel-Case umwandeln:
    ```python
    text = "python ist großartig"
    titel_case = text.title()
    print(titel_case)
    ```

15. Anzahl der Zeichen, die keine Buchstaben oder Zahlen sind, zählen:
    ```python
    text = "Python 123!?"
    anzahl_sonderzeichen = sum(1 for char in text if not char.isalnum())
    print(f"Anzahl der Sonderzeichen: {anzahl_sonderzeichen}")
    ```

16. Extrahieren von URLs aus einem Text (mithilfe einer regulären Ausdrucks):
    ```python
    import re

    text = "Besuchen Sie meine Website unter https://www.example.com. Weitere Informationen finden Sie unter www.invalid-url."
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    print(urls)
    ```

17. Funktion für Palindrom-Überprüfung:
    ```python
    def ist_palindrom(text):
        text = text.lower()  # Um Groß-/Kleinschreibung zu ignorieren
        return text == text[::-1]

    print(ist_palindrom("anna"))  # True
    print(ist_palindrom("Python"))  # False
    ```
