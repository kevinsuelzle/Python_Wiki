# Bessere Praktiken in Python

## Ergänzungen und Beispiele zu [PEP 8](https://peps.python.org/pep-0008/) und [Zen of Python](https://gist.github.com/corysimmons/8b94c08421dec18bbaa4)

<div style="display: flex; justify-content: space-between;">
    <img src="../pictures/HurraSuccess.jpg" alt="Hurra! Clean Code" style="width: 35%; height: auto;">
    <img src="../pictures/ThrowAwayBadCode.jpg" alt="Throw away bad code" style="width: 35%; height: auto;">
</div>

### Verwendung von Funktionsparametern statt globalen Variablen

```python
x = 10


def increment():
    global x
    x += 1
```

Anstatt eine globale Variable zu verwenden, sollte die Funktion einen Wert als Argument annehmen und den modifizierten
Wert zurückgeben. Dies erhöht die Wiederverwendbarkeit und Klarheit der Funktion.

```python
def increment(x):
    return x + 1
```

**Frage**: Warum ist das ein schlechter Stil und kann es unter diesem Aspekt Funktionen ohne Argumente überhaupt geben?

### Fehlerbehandlung

```python
def divide(a, b):
    return a / b
```

Es ist wichtig, Ausnahmen zu behandeln, um unerwartete Abstürze zu vermeiden. Im Fall einer Division sollten wir
insbesondere eine Division durch Null abfangen.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        return None
```

**Frage**: Gibt es noch weitere Verbesserungen an dieser Funktion? 

### Vereinfachung von List Comprehensions

```python
my_list = [x ** 2 for x in range(20) if x % 2 == 0 if x % 3 == 0]
```

Komplexe List Comprehensions sollten vermieden werden, da sie schwer zu lesen und zu verstehen sind. Eine Schleife mit
klaren Bedingungen ist oft besser.

```python
my_list = []
for x in range(20):
    if x % 2 == 0 and x % 3 == 0:
        my_list.append(x ** 2)
```

### Benennung von Variablen

```python
a = 50
b = 100
c = a + b
```

[Bezeichner](Conventions.md) sollten klar und eindeutig sein und [Regeln](CamelsAndSnakes.md) folgen. 

```python
basispreis = 50
steuer = 100
gesamtpreis = basispreis + steuer
```

### Hinzufügen von Kommentaren und docstrings

```python
def calc(x):
    return x * 2 + 5
```

Kommentare sind wichtig, um die Absicht hinter dem Code zu erklären, insbesondere in Fällen, in denen die Logik nicht
sofort offensichtlich ist.

```python
"""
Sammlung von Funktionen um ....    
"""


def calculate_adjusted_value(x):
    """
    Berechnet den angepassten Wert durch Verdopplung und Addition von 5 oder
    
    oder
    
    Die binäre Verschiebung um ein Bit nach links wird hier durch die Multiplikation mit 2 erreicht. 
    Der Offset von 5 Bytes ist technisch erforderlich. Quelle ...
    """
    return x * 2 + 5
```

### DRY Don't repeat yourself

```python
# Berechnung des Quadrats von Zahlen
num1 = 4
quadrat_num1 = num1 * num1

num2 = 5
quadrat_num2 = num2 * num2

num3 = 6
quadrat_num3 = num3 * num3

print(quadrat_num1, quadrat_num2, quadrat_num3)
```

Funktionen reduzieren die Code-Menge und erhöhen die Wartbarkeit.

```python
def quadrat(zahl):
    return zahl * zahl


num1 = 4
num2 = 5
num3 = 6

quadrat_num1 = quadrat(num1)
quadrat_num2 = quadrat(num2)
quadrat_num3 = quadrat(num3)

print(quadrat_num1, quadrat_num2, quadrat_num3)
```

**Frage**: Das obige Beispiel ist sehr trivial. Man könnte sagen: "Ist doch klar, was soll das?". Also warum wird dieser
Punkt hier aufgelistet?

**Aufgabe**: Finde komplexere Beispiele.

**Frage**: Gibt es [Ausnahmen](DRY.md) zu dieser Regel?


### Beispiel mit Analyse

#### Ungünstiger Code

```python
def f(a, b):
    if a > 10 and b > 10:
        return a + b
    else:
        if a <= 10: return a * 2
        if b <= 10: return b * 2
```

Probleme in diesem Code:

1. Funktion und Variablennamen: Die Funktion f und die Variablen a und b sind nicht aussagekräftig.
2. Einzeilige if-Anweisung: Die Verwendung einer einzeiligen if-Anweisung reduziert die Lesbarkeit.
3. Keine Konsistenz: Inkonsistente Verwendung von Einrückungen und Leerzeichen.
4. Logik: Die Logik könnte klarer und effizienter gestaltet werden.

#### Verbesserter Code: Beispiel

Jetzt sehen wir uns eine verbesserte Version des obigen Codes an:

```python
def sum_or_double(a, b):
    if a > 10 and b > 10:
        return a + b
    elif a <= 10:
        return a * 2
    else:
        return b * 2
```

#### Diskussion: Vergleich der Beispiele

**Frage**: Welche Verbesserungen wurden gemacht?
**Frage**: Welche weiteren Verbesserungen könnten an dem verbesserten Code vorgenommen werden?
**Aktivität**: Versuchen Sie, den verbesserten Code weiter zu optimieren und diskutieren Sie Ihre Änderungen.

### Aufgabe: Umwandeln in sauberen Code.

```python
a1 = []
a2 = []


def copyarr():
    global a1, a2
    for i in range(len(a1)):
        a2.append(a1[i])
```

### Aufgabe: Umwandeln in unsauberen Code

```python
def sort_and_format_words(word_list):
    """
    Sortiert eine Liste von Wörtern nach ihrer Länge und gibt sie in einem formatierten String zurück.

    Args:
    word_list (list): Eine Liste von Wörtern (strings).

    Returns:
    str: Ein formatierter String, der die sortierten Wörter enthält.
    """
    # Sortieren der Wörter nach Länge
    sorted_words = sorted(word_list, key=len)

    # Erstellen eines formatierten Strings
    formatted_output = "Sortierte Wörter: " + ", ".join(sorted_words)

    return formatted_output


# Beispielverwendung
words = ["Python", "ist", "eine", "tolle", "Programmiersprache"]
print(sort_and_format_words(words))
```

Sie können diesen Code als Übung in schlechten Code umwandeln, indem Sie folgende Änderungen vornehmen:

1. Entfernen Sie alle Kommentare und Docstrings.
2. Verwenden Sie unklare oder irreführende Variablennamen.
3. Integrieren Sie unnötige oder komplexe Logik.
4. Vermeiden Sie die Verwendung hilfreicher Python-Funktionen wie sorted() und implementieren Sie stattdessen eine
   ineffiziente Sortiermethode.

### Aufgabe: Versuche innerhalb von 3 Minuten eine grobe Vorstellung von der Funktion des folgenden Codes zu bekommen.

Entnommen aus Clean Code von Robert C. Martin und von Java nach Python übersetzt.

```python
def testable_html(page_data, include_suite_setup):
    wiki_page = page_data.get_wiki_page()
    buffer = []

    if page_data.has_attribute("Test"):
        if include_suite_setup:
            suite_setup = PageCrawlerImpl.get_inherited_page(SuiteResponder.SUITE_SETUP_NAME, wiki_page)
            if suite_setup is not None:
                page_path = suite_setup.get_page_crawler().get_full_path(suite_setup)
                page_path_name = PathParser.render(page_path)
                buffer.append(f"!include -setup .{page_path_name}\n")

    setup = PageCrawlerImpl.get_inherited_page("SetUp", wiki_page)
    if setup is not None:
        setup_path = wiki_page.get_page_crawler().get_full_path(setup)
        setup_path_name = PathParser.render(setup_path)
        buffer.append(f"!include -setup.{setup_path_name}\n")

    buffer.append(page_data.get_content())

    if page_data.has_attribute("Test"):
        teardown = PageCrawlerImpl.get_inherited_page("TearDown", wiki_page)
        if teardown is not None:
            tear_down_path = wiki_page.get_page_crawler().get_full_path(teardown)
            tear_down_path_name = PathParser.render(tear_down_path)
            buffer.append(f"\n !include -teardown .{tear_down_path_name}\n")

        if include_suite_setup:
            suite_teardown = PageCrawlerImpl.get_inherited_page(SuiteResponder.SUITE_TEARDOWN_NAME, wiki_page)
            if suite_teardown is not None:
                page_path = suite_teardown.get_page_crawler().get_full_path(suite_teardown)
                page_path_name = PathParser.render(page_path)
                buffer.append(f" !include -teardown .{page_path_name}\n")

    page_data.set_content(''.join(buffer))
    return page_data.get_html()
```

Zitat (übersetzt): Mit nur ein paar einfachen Methodenextraktionen, etwas Umbenennung und einer kleinen Umstrukturierung
konnte ich jedoch die Absicht der Funktion in den neun Zeilen [des folgenden von Java nach Python übersetzten Codes]
erfassen.
Sehen Sie, ob Sie das in den nächsten 3 Minuten verstehen können.

```python
def render_page_with_setups_and_teardowns(page_data, is_suite):
    is_test_page = page_data.has_attribute("Test")
    if is_test_page:
        test_page = page_data.get_wiki_page()
        new_page_content = []

        include_setup_pages(test_page, new_page_content, is_suite)
        new_page_content.append(page_data.get_content())
        include_teardown_pages(test_page, new_page_content, is_suite)

        page_data.set_content(''.join(new_page_content))

    return page_data.get_html()
```

Auch wenn dieses Beispiel keinen tieferen Sinn ergibt, so ist doch klar ersichtlich, wie viel eine gute Benennung und
Gliederung von Funktionalität ausmacht.

### Erkenntnisse bezüglich der Gestaltung von Funktionen:

Funktionen sollten

1. kurz sein
2. sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. im Namen das "One Thing" klar beschreiben und in den Parametern ebenfalls sprechende Namen verwenden.
4. keine Nebeneffekte haben. 
5. sich nur um eine Abstraktionsebene kümmern. 
6. wenig Argumente haben.
7. echte Fehler verarbeiten und keine Fehlerwerte an die aufrufende Funktion "hoch" geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.
8. wenn sie eine Ausnahmebehandlung vorsehen, nichts vor dem "try" stehen haben und nach dem "except" Block sollte auch
   kein weiterer Code mehr folgen. Ausnahme: der "finally" Block. Es kann ja sein, dass man was aufräumen muss.

#### Funktionsparameter

Man unterscheidet aufgrund der Anzahl der Parameter:

1. **niladic**: Funktionen ohne Argumente sind am einfachsten zu testen.
2. **monadic**: Funktionen mit einem Argument sind noch recht einfach zu testen, da der Wertebereich nur für
   einen Parameter zu erfassen ist und es keine Kombinatorik gibt.
3. **dyadic**: Funktionen mit zwei Argumenten sind schon schwerer in ihrer Totalität zu testen. Je nach Datentyp der
   Parameter ufert der Test aus.
4. **triadic**: gar nicht erst dran denken.
5. **polyadic**: das muss anders gemacht werden.
   Aufgabe: Wie kann man eine Reduktion von Parametern erreichen? Wie kann eine Funktion ohne Parameter auskommen?

#### Erklärung: Abstraktionsebene

Code von oben nach unten lesen: Die Stepdown-Regel

Wir wollen, dass der Code wie eine Top-Down-Erzählung gelesen wird. Wir möchten, dass jede Funktion von denen auf der
nächsten Abstraktionsebene gefolgt wird, damit wir das Programm lesen können, wobei wir jeweils eine
Abstraktionsebene
absteigen, während wir die Liste der Funktionen lesen. Ich nenne das die Step-down-Regel.
Um dies anders auszudrücken, möchten wir in der Lage sein, das Programm so zu lesen, als wäre es eine Reihe von Um
zu-Absätzen, von denen jeder die aktuelle Abstraktionsebene beschreibt und auf nachfolgende Um zu-Absätze auf der
nächsten Ebene nach unten verweist.

- **Um die Setups und Teardowns einzubeziehen**, schließen wir Setups ein, dann schließen wir den Testseiten-Content
  und dann die Teardowns ein.
- **Um die Setups einzubeziehen**, schließen wir das Suite-Setup ein, wenn es sich um eine Suite handelt, dann
  schließen
  wir das reguläre Setup ein.
- **Um das Suite-Setup einzubeziehen**, durchsuchen wir die übergeordnete Hierarchie nach der Seite "SuiteSetUp" und
  fügen eine include-Anweisung mit dem Pfad dieser Seite hinzu.
- **Um den Elternteil zu suchen**...

Es stellt sich heraus, dass es für Programmierer sehr schwierig ist, zu lernen, dieser Regel zu folgen und Funktionen
zu schreiben, die auf einer einzigen Abstraktionsebene bleiben. Aber das Erlernen dieses Tricks ist sehr
wichtig.
Es ist der Schlüssel, um Funktionen kurzzuhalten und sicherzustellen, dass sie "eine Sache" tun. Den Code wie einen
Top-Down-Satz von Um zu-Absätzen lesen zu lassen, ist eine effektive Technik, um die Abstraktionsebene konsistent zu
halten.

**Aufgabe**: Suchen sie Beispiele für Abstraktinsebenen in der Funktion testable_html weiter oben.
**Frage**: Wie steht es damit in der Funktion render_page_with_setups_and_teardowns?