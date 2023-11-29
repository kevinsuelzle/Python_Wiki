# Bessere Praktiken in Python

## Ergänzungen und Beispiele zu [PEP 8](https://peps.python.org/pep-0008/) und [Zen of Python](https://gist.github.com/corysimmons/8b94c08421dec18bbaa4)

## Feinziele

- **Erkennen und Vermeiden von schlechtem Code** 
- **Praktische Anwendung von Namenskonventionen** 
- **Implementierung des DRY-Prinzips** 
- **Verständnis für Testbarkeit** 
- **Anwendung von Kommentaren und Dokumentation** 
- **Einhalten eines konsistenten Codierungsstils** 
- **Refactoring-Kompetenz**
- **Verständnis für die Struktur von Funktionen und Klassen**

In diesem Abschnitt werden wir die wesentlichen Prinzipien des Clean Code detailliert betrachten. Dazu gehören Aspekte
wie Lesbarkeit, Einfachheit und Wartbarkeit des Codes. Die Feinziele geben einen detaillierten Einblick in die
spezifischen Fähigkeiten und Kenntnisse, die die Lernenden erwerben werden, um Clean Code effektiv in der Praxis
anzuwenden. Dies bildet die Grundlage für die folgenden Abschnitte, in denen diese Prinzipien weiter vertieft und durch
praktische Beispiele illustriert werden.

Um ein Gefühl dafür zu bekommen, worum es geht, hier ein Passus entnommen aus Clean Code von Robert C. Martin und von Java nach Python übersetzt.

## Aufgabe: Versuche innerhalb von 3 Minuten eine grobe Vorstellung von der Funktion des folgenden Codes zu bekommen.

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

Der Autor antwortet auf die Aufgabe, Zitat (übersetzt): "Mit nur ein paar einfachen Methodenextraktionen, etwas Umbenennung und einer kleinen Umstrukturierung
konnte ich jedoch die Absicht der Funktion in den neun Zeilen [des folgenden von Java nach Python übersetzten Codes]
erfassen."

**Aufgabe**: Sehen Sie, ob Sie das in den nächsten 3 Minuten verstehen können.

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

**Diskussion**: Wie sind ihre Eindrücke von dem gezeigten Code?

## Einfaches Beispiel mit Analyse

### Ungünstiger Code

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

### Verbesserter Code: Beispiel

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

### Diskussion: Vergleich der Beispiele

**Frage**: Welche Verbesserungen wurden gemacht?

**Frage**: Welche weiteren Verbesserungen könnten an dem verbesserten Code vorgenommen werden?

**Aktivität**: Versuchen Sie, den verbesserten Code weiter zu optimieren und diskutieren Sie Ihre Änderungen.

## Methoden des Clean Code

### [Verwendung von Funktionsparametern statt globaler Variablen](../Globale_Parameter)

### [Fehlerbehandlung](../Fehlerbehandlung)

### [List Comprehensions](../ListComprehension)

### [Benennungskonventionen](../Benennungskonventionen)

### [Hinzufügen von Kommentaren und docstrings](../Kommentare)

### [DRY Don't repeat yourself](../DRY)

### [Gestaltung und Testen von Funktionen](../Funktionsgestaltung)

### [Funktionsparameter](../Funktionsparameter)

### [Abstraktionsebene](../Abstraktionsebene)

### [Refactoring](../Refactoring)

### [Aufgaben](../Aufgaben)

