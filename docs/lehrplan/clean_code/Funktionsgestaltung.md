# Funktionsgestaltung

## Gestaltung von Funktionen

Funktionen sollten

1. kurz sein
2. sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. im Namen das "One Thing" klar beschreiben und in den Parametern ebenfalls sprechende Namen verwenden.
4. sich nur um eine [Abstraktionsebene](../Abstraktionsebene) kümmern.
5. wenig [Argumente](../Funktionsparameter) haben.
6. echte Fehler verarbeiten und keine Fehlerwerte an die aufrufende Funktion "hoch" geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.
7. Keine Seiteneffekte haben. (*Seiteneffekt* ist der Fachbegriff für eine Änderung des Speichers.)

$$$ Task 11: Füge eine Übungsaufgabe ein, bei der Code aufgesplittet werden soll.

# Aufgabe: Versuche innerhalb von 3 Minuten eine grobe Vorstellung von der Funktion des folgenden Codes zu bekommen.
$$$ TASK 1 START: anderes Beispiel finden, dass nachvollziebarer ist.
$$$ Neue Aufgabenstellung: Code in 45 Minuten selbst lesbarer machen z.B. durch einführen neuer funktionen.
$$$ Dabei darauf achten, dass auch einige triviale Fehler gemacht werden, wie kein camelcase, doofe Variablennamen etc.
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

[zurück](../TheGoodPractices)