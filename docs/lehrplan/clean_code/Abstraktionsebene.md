# Abstraktionsebenen

![Abstraktionsebenen](../clean_code/pictures/LevelOfAbstraction.jpg)

## Code von oben nach unten lesen: die Stepdown-Regel

Wir wollen, dass der Code wie eine Top-Down-Erzählung gelesen wird. Wir möchten, dass jede Funktion von denen auf der
nächsten Abstraktionsebene gefolgt wird, damit wir das Programm lesen können, wobei wir jeweils eine Abstraktionsebene
absteigen, während wir die Liste der Funktionen lesen. Man nennt das die Step-down-Regel. Um dies anders auszudrücken,
möchten wir in der Lage sein, das Programm so zu lesen, als wäre es eine Reihe von "Um zu"-Absätzen, von denen jeder die
aktuelle Abstraktionsebene beschreibt und auf nachfolgende "Um zu"-Absätze auf der nächsten Ebene nach unten verweist.

- **Um die Setups und Teardowns einzubeziehen**, schließen wir Setups ein, dann schließen wir den Testseiten-Content
  und dann die Teardowns ein.
- **Um die Setups einzubeziehen**, schließen wir das Suite-Setup ein, wenn es sich um eine Suite handelt, dann
  schließen
  wir das reguläre Setup ein.
- **Um das Suite-Setup einzubeziehen**, durchsuchen wir die übergeordnete Hierarchie nach der Seite "Suite-Setup" und
  fügen eine include-Anweisung mit dem Pfad dieser Seite hinzu.
- **Um den Elternteil zu suchen** ...

Für Programmierer ist es oft sehr schwierig ist, dieser Regel zu folgen und Funktionen
zu schreiben, die auf einer einzigen Abstraktionsebene bleiben. Aber das Erlernen dieses Tricks ist sehr
wichtig.
Es ist der Schlüssel, um Funktionen kurzzuhalten und sicherzustellen, dass sie "eine Sache" tun. Den Code wie einen
Top-Down-Satz von "Um zu"-Absätzen lesen zu lassen, ist eine effektive Technik, um die Abstraktionsebene konsistent zu
halten.

**Aufgabe**: Suchen sie Beispiele für Abstraktionsebenen in der Funktion testable_html.

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

Bei der Analyse des gegebenen Python-Codes hinsichtlich der Abstraktionsebenen können wir verschiedene Aspekte
betrachten:

1. **Funktionslevel-Abstraktion:**
    - Die Funktion `testable_html` ist auf einer höheren Abstraktionsebene angesiedelt. Sie orchestriert den Prozess der
      Erstellung einer HTML-Seite basierend auf `page_data` und `include_suite_setup`.
    - Innerhalb dieser Funktion werden jedoch mehrere niedrigere Abstraktionsebenen angesprochen, wie das Abrufen von
      Seiten, das Generieren von Pfaden und das Zusammenbauen des HTML-Inhalts.

2. **Verwendung von API-Aufrufen und Hilfsklassen:**
    - Die Funktion nutzt verschiedene Hilfsklassen wie `PageCrawlerImpl` und `PathParser`, die spezifischere Aufgaben
      erfüllen. Diese Klassen operieren auf einer niedrigeren Abstraktionsebene, da sie sich mit den Details der
      Datenmanipulation und -verarbeitung befassen.

3. **Detailgrad innerhalb der Funktion:**
    - Innerhalb der `testable_html`-Funktion gibt es eine Mischung aus Abstraktionsebenen. Zum Beispiel:
        - Der Aufruf von `page_data.get_wiki_page()` und ähnlichen Methoden ist auf einer höheren Ebene, da er abstrakte
          Konzepte wie "Wiki-Seite abrufen" repräsentiert.
        - Die Logik, die überprüft, ob bestimmte Seitenattribute vorhanden sind (`page_data.has_attribute("Test")`), und
          die darauf folgenden bedingten Anweisungen sind spezifischer und detaillierter.

4. **Wiederholung und Potenzial für Refactoring:**
    - Es gibt wiederholte Muster im Code, wie das Abrufen von Seiten (`get_inherited_page`), das Generieren von Pfaden
      und das Hinzufügen von Inhalten zum `buffer`. Diese Muster könnten in separate Funktionen abstrahiert werden, um
      die Klarheit zu erhöhen und Redundanzen zu reduzieren.

5. **Konsistenz in der Abstraktion:**
    - Der Code könnte von einer gleichmäßigeren Abstraktionsebene profitieren. Zum Beispiel könnten die Operationen zum
      Abrufen und Verarbeiten von Seiten in separate Funktionen ausgelagert werden, um die Hauptfunktion `testable_html`
      auf einer konsistenten, höheren Abstraktionsebene zu halten.

Zusammenfassend lässt sich sagen, dass der Code eine Mischung aus verschiedenen Abstraktionsebenen aufweist und durch
Refactoring und das Auslagern von spezifischeren Aufgaben in separate Funktionen oder Klassen verbessert werden könnte,
um die Lesbarkeit und Wartbarkeit zu erhöhen.

**Aufgabe**: Wie steht es damit in der Funktion render_page_with_setups_and_teardowns?

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

Bei der Analyse des Python-Codes `render_page_with_setups_and_teardowns` hinsichtlich der Abstraktionsebenen können wir
folgende Punkte feststellen:

1. **Funktionslevel-Abstraktion:**
    - Die Funktion `render_page_with_setups_and_teardowns` ist auf einer höheren Abstraktionsebene angesiedelt. Sie
      steuert den Prozess der Erstellung einer HTML-Seite, indem sie Setup- und Teardown-Seiten einbezieht, falls
      erforderlich.
    - Die Funktion abstrahiert den Prozess der Seitenerstellung, indem sie die Details der Einbeziehung von Setup- und
      Teardown-Seiten in separate Funktionen auslagert (`include_setup_pages` und `include_teardown_pages`).

2. **Klarheit und Fokussierung:**
    - Die Funktion ist klar fokussiert auf das, was sie tun soll – das Rendern einer Seite mit möglichen Setups und
      Teardowns. Dies macht sie lesbar und verständlich.
    - Die Verwendung von Hilfsfunktionen wie `include_setup_pages` und `include_teardown_pages` trägt zur Klarheit bei,
      indem sie spezifische Aufgaben in eigenen Abstraktionsebenen kapselt.

3. **Konsistenz in der Abstraktion:**
    - Die Funktion bleibt auf ihrer Abstraktionsebene konsistent. Sie behandelt nicht die Details der Implementierung
      von Setup- oder Teardown-Seiten, sondern delegiert diese Aufgaben an andere Funktionen.
    - Die Hauptfunktion kümmert sich hauptsächlich um die Entscheidungslogik (ob Setups und Teardowns einbezogen werden
      sollen) und das Zusammenstellen des endgültigen Seiteninhalts.

4. **Separation von Bedenken:**
    - Die Funktion `render_page_with_setups_and_teardowns` trennt klar die Bedenken des Renderns der Seite von den
      Bedenken des Einbeziehens von Setup- und Teardown-Seiten. Dies folgt dem Prinzip der Separation von Bedenken und
      trägt zur Wartbarkeit und Erweiterbarkeit des Codes bei.

5. **Potenzial für weitere Abstraktion:**
    - Obwohl der Code bereits gut strukturiert ist, könnte es Bereiche geben, in denen weitere Abstraktion sinnvoll sein
      könnte. Zum Beispiel könnte die Logik zur Bestimmung, ob eine Seite eine Testseite ist, in eine separate Funktion
      ausgelagert werden, um die Hauptfunktion noch weiter zu vereinfachen.

Zusammenfassend lässt sich sagen, dass dieser Code gut strukturiert ist und eine klare Trennung der Abstraktionsebenen
aufweist. Die Hauptfunktion bleibt auf einer höheren Ebene und delegiert spezifischere Aufgaben an andere Funktionen,
was zu einer guten Lesbarkeit und Wartbarkeit beiträgt.

[zurück](../TheGoodPractices)