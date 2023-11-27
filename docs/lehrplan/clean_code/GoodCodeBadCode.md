# Beispiele für schlechten Code in Python


```python
x = 10


def increment():
    global x
    x += 1
```

```python
def divide(a, b):
    return a / b
```

```python
my_list = [x ** 2 for x in range(20) if x % 2 == 0 if x % 3 == 0]
```

```python
a = 50
b = 100
c = a + b
```

```python
def calc(x):
    return x * 2 + 5
```

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

Diskussion: Vergleich der Beispiele

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
konnte ich jedoch die Absicht der Funktion in den neun Zeilen [des folgenden von Java nach Python übersetzten Codes] erfassen.
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

Auch wenn dieses Beispiel, ganz bewusst aus einer fremden Programmiersprache gewählt, keinen tieferen Sinn ergibt, so
ist doch klar ersichtlich,
wie viel eine gute Benennung und Gliederung von Funktionalität ausmacht.

### Erkenntnisse bezüglich der Gestaltung von Funktionen:

1. sie sollten kurz sein
2. sie sollten sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. sie sollten keine Nebeneffekte haben.
4. innerhalb einer Funktion sollte es nur eine Abstraktionsebene geben.
5. sie sollten wenig Argumente haben. Das bezieht sich auf das Testen von Funktionen.

    1. **niladic**: Funktionen ohne Argumente sind am einfachsten zu testen.
    2. **monadic**: Funktionen mit einem Argument sind noch recht einfach zu testen, da der Wertebereich nur für die
       eineVariable zu erfassen ist und es keine Kombinatorik gibt.
    3. **dyadic**: Funktionen mit zwei Argumenten sind schon schwer in ihrer Totalität zu testen. Je nach Datentyp der
       Parameter ufert der Test aus.
    4. **triadic**: gar nicht erst dran denken.
    5. **polyadic**: das muss anders gemacht werden.
       Aufgabe: Wie kann man eine Reduktion von Parametern erreichen? Wie kann eine Funktion ohne Parameter auskommen?
   
6. sie sollten eher echte Fehler verarbeiten als Fehlerwerte an die aufrufende Funktion "hoch" zu geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.
7. wenn sie eine Ausnahmebehandlung vorsehen, sollte nichts vor dem "try" stehen und nach dem "except" Block sollte auch
   kein weiterer Code mehr folgen. Ausnahme: der "finally" Block. Es kann ja sein, dass man was aufräumen muss.

### Abstraktionsebene

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
zu schreiben, die auf einer einzigen Abstraktionsebene bleiben. Aber das Erlernen dieses Tricks ist auch sehr
wichtig.
Es ist der Schlüssel, um Funktionen kurzzuhalten und sicherzustellen, dass sie "eine Sache" tun. Den Code wie einen
Top-Down-Satz von Um zu-Absätzen lesen zu lassen, ist eine effektive Technik, um die Abstraktionsebene konsistent zu
halten.

