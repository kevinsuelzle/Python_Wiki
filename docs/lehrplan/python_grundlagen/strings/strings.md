# Strings in Python

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/EA_PBdovZBU?si=SCrNKqnhiAQVueYG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Um Zeichenketten in Python darzustellen, benötigt man sogenannte Strings. Strings werden in
Python in einfachen oder doppelten Anführungszeichen eingeschlossen (`''` oder `""`). Mehrzeilige Strings können mit
drei Anführungszeichen erstellt werden. (`''' ''' ` oder `""" """`). 

```python
a = "Hallo"
b = 'du'
c = """Wie geht es dir?
Mir geht es gut.

Danke der Nachfrage
"""

d = '''mir geht es super!
Und bei dir so?
'''
e = "alles klar\nbis bald" # Absätze durch \n bei normalen Strings anzeigen

f = '' # Leeres Wort
```

## Eigenschaften von Strings

[//]: # ([60min])
<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/GPSkj72ziQI?si=B6ZZOH84q4qNLxcP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

**Sequenz von Zeichen:** Ein String ist eine geordnete Sequenz von Zeichen. Jedes Zeichen in einem String hat eine
Position, die durch einen Index dargestellt wird.

```python
my_string = "Aloah"
print(my_string[0]) # A
```

**Unveränderbarkeit (Immutable):** Strings sind in Python unveränderlich, d.h. sie können nach ihrer Erstellung nicht
geändert werden.

```python
my_string = "Aloah"
my_string[0] = "B" # EXCEPTION!
```

**Indizierbarkeit:** Jedes Zeichen in einem String hat einen eindeutigen Index, beginnend mit `0` für das erste
Zeichen, `1` für das zweite Zeichen und so weiter.
```python
my_string = "Aloah"
print(my_string[0]) # A
print(my_string[1]) # l
print(my_string[-1]) # h
```

**Slicing (Ausschneiden):** Strings unterstützen das Slicing, d.h. es können Teilzeichenketten aus einem String
extrahiert werden, indem man einen Bereich von Indizes angibt.

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

# Angabe der Step-Size
teil_text6 = text[::2] # Ergebnis: "Pto s rßri."
```

**Teilstrings leicht finden:** Mit dem Keyword `in` lässt sich leicht überprüfen, ob ein String in einem anderen
enthalten ist:

```python
print("lo" in "Hallo") # True
print("lo" in "Moin") # False

print("lo" not in "Moin") # True
print("lo" not in "Aloa") # False
```

**Länge (Length):** Die Länge eines Strings, d.h. die Anzahl der Zeichen in einem String, kann mit der Funktion `len()`
ermittelt werden.

```python
print(len("High Five")) # 9
```

**Concatenation (Verkettung):** Strings können mithilfe des `+`-Operators zu einem einzigen String verkettet werden, um
längere Zeichenketten zu erstellen.

```python
print("Ma" + "ma")
```

**Escape-Zeichen:** Strings können Escape-Zeichen wie `\n` (für Zeilenumbruch) und `\t` (für Tabulator) enthalten, um
spezielle Zeichen darzustellen. [Hier ist die Liste aller Excapezeichen](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences).

```python
print("Hallo,\nWie geht es Ihnen?\n\tViele Grüße")
# Hallo,
# Wie geht es Ihnen?
#   Viele Grüße
```
**Unicode-Unterstützung:** Strings in Python sind Unicode-zeichenketten, d.h. sie können Zeichen aus verschiedenen
Sprachen und Schriften darstellen. Auf [symbl.cc](https://symbl.cc/de/) findest du alle Unicodes. Viel Spaß🏄‍♂️

```python
# Unicode-Zeichen in einem Python-String
unicode_string = "Python unterstützt Unicode \u2192 \U0001F609"
print(unicode_string)  # 'Python unterstützt Unicode → 😉'

# Länge des Strings mit Unicode-Zeichen
laenge = len(unicode_string)
print(f"Länge des Strings: {laenge} Zeichen")
```
**String-Methoden:** Python bietet eine Vielzahl von eingebauten String-Methoden, die helfen, Zeichenketten zu
manipulieren, zu durchsuchen, zu überprüfen und zu formatieren. Im Folgenden ist eine Auswahl einiger
wichtigen String Methoden gegeben. [Hier finden sie eine Auflistung aller String-Methoden](https://docs.python.org/3/library/stdtypes.html#string-methods).

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


### Aufgabe: Benutzernamen🌶🌶

[//]: # ([20min])

Beschreiben Sie, was der folgende Code tut:

```python
benutzername = input("Bitte geben Sie Ihren Benutzernamen ein: ")

if len(benutzername) > 10:
    print("Der Benutzername ist zu lang.")
elif len(benutzername) < 3:
    print("Der Benutzername ist zu kurz.")
else:
    print(f"Willkommen, {benutzername}!")

if benutzername.isupper():
    print("Ihr Benutzername ist vollständig in Großbuchstaben geschrieben.")
elif benutzername.islower():
    print("Ihr Benutzername ist vollständig in Kleinbuchstaben geschrieben.")
else:
    print("Ihr Benutzername enthält sowohl Groß- als auch Kleinbuchstaben.")

if "!" in benutzername:
    print("Ihr Benutzername enthält ein Ausrufezeichen!")

kleinbuchstaben_benutzername = benutzername.lower()
print(f"Ihr Benutzername in Kleinbuchstaben: {kleinbuchstaben_benutzername}")
```

[Lösung](solutions.md#aufgabe-benutzernamen)

## f-Strings

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vQaCY_HT8mQ?si=4Nw7sjRehy9sd4PZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Um den Inhalt von Variablen einfach in Strings einzubetten, gibt es in Python sog. f-Strings
(siehe [PEP 498](https://peps.python.org/pep-0498/).

Dies sieht dann wie folgt aus:

```python
my_int = 30
my_float = 0.123456789

print(f"My Integer is {my_int} and my float is {my_float}")
print(f"I can also round my float to five places: {my_float:.5}")
```

[Hier](https://note.nkmk.me/en/python-f-strings/) findest du noch viele weitere Beispiele für den Einsatz von f-Strings.

# Aufgaben

[//]: # ([40min])

### 1. Länge eines Strings ermitteln: 🌶️️🌶️️
Schreibe ein Programm, um die Länge eines Strings zu ermitteln.

### 2. String rückwärts ausgeben: 🌶️️🌶️️
Erstelle einen String und gib ihn rückwärts aus.

### 3. String in Großbuchstaben konvertieren: 🌶️️🌶️️
Erstelle einen String und konvertiere ihn in Großbuchstaben.

### 4. Anzahl der Vokale zählen: 🌶️️🌶️️🌶️️
Erstelle einen String und zähle die Anzahl der Vokale in ihm.

### 5. Erster und letzter Buchstabe eines Strings: 🌶️️
Schreibe einen Python-Code, um den ersten und den letzten Buchstaben eines Strings auszugeben.

### 6. Zeichen ersetzen:  🌶️️
Erstelle einen String und ersetze ein bestimmtes Zeichen darin durch ein anderes.

### 7. Leerzeichen entfernen: 🌶️️
Erstelle einen String und entferne alle Leerzeichen daraus.

### 8. String in Wörter aufteilen: 🌶️️
Erstelle einen String und teile ihn in Wörter auf.

### 9. Überprüfung, ob ein String nur aus Zahlen besteht: 🌶️️🌶️️
Erstelle einen String und überprüfe, ob er nur aus Zahlen besteht.

### 10. Funktion zur Überprüfung von Anagrammen: 🌶️️🌶️️
Schreibe eine Funktion, die zwei Strings nimmt und überprüft, ob sie Anagramme sind (dh dieselben Buchstaben in
unterschiedlicher Reihenfolge).

### 11. Anzahl der Wörter in einem String zählen: 🌶️️🌶️️
Erstelle einen String und zähle die Anzahl der Wörter darin.

### 12. String in Titel-Case umwandeln: 🌶️️
Schreibe Code, die einen gegebenen String in einen Titel-Case-String umwandelt (jedes Wort beginnt mit
einem Großbuchstaben).

### 13. Funktion für Palindrom-Überprüfung: 🌶️️🌶️️
Schreibe Code, die überprüft, ob ein String ein Palindrom ist (d.h. rückwärts gelesen dasselbe wie
vorwärts).

### 14. Funktion für Palindrom-Überprüfung: 🌶️️🌶️️🌶️️
Schreibe Code, der alle Vokale in einem Satz durch das Symbol `*` ersetzt.

[Lösung](solutions.md#1-länge-eines-strings-ermitteln)
