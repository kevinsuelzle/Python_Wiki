# PEP 8, PEP 20 und PEP 257
## Python-Style-Guide, Zen of Python und Docstrings
[240min]

In der Python-Community gibt es Richtlinien und Prinzipien, um den Code einheitlich und lesbar zu gestalten. Diese werden in sogenannten PEPs (Python Enhancement Proposals) festgehalten. Hier sind drei wichtige PEPs, die eine Rolle in Bezug auf den Code-Stil und die Dokumentation spielen: PEP 8, PEP 20 und PEP 257.

## PEP 8: Style Guide for Python Code 🌶️

PEP 8 ist der Style Guide für Python-Code. Er legt Konventionen für die Formatierung von Code, einschließlich Einrückungen, Zeilenlängen, Importen und Namenskonventionen, fest. Einige wichtige Punkte sind:

```python
# Verwende 4 Leerzeichen pro Einrückungsebene
def example_function():
    # Begrenze Zeilen auf 79 Zeichen für Code und 72 Zeichen für Docstrings
    long_variable_name = "This is a long string that exceeds the recommended line length"

    # Verwende sprechende Namen für Variablen, Funktionen und Module
    meaningful_variable_name = 42
```

Weitere Details findest du [hier](https://www.python.org/dev/peps/pep-0008/).

## PEP 20: The Zen of Python 🌶️

PEP 20 enthält 19 Grundsätze, die als "The Zen of Python" bekannt sind. Diese Grundsätze bieten Richtlinien für das Schreiben von Python-Code und betonen Lesbarkeit und Einfachheit. Einige davon sind:

```python
# Schönheit zählt
beautiful_code = readable + simple

# Explizit ist besser als implizit
explicit_code = explicit_function()

# Flach ist besser als verschachtelt
flat_code = not_nested()
```

Du kannst sie dir in der Python-Shell anzeigen lassen, indem du `import this` ausführst.

## PEP 257: Docstring Conventions 🌶️

PEP 257 legt Konventionen für Docstrings fest. Docstrings sind mehrzeilige Zeichenketten, die an den Anfang von Modulen, Funktionen, Klassen und Methoden platziert werden, um deren Verwendung zu dokumentieren. Wichtige Punkte sind:

```python
def example_function(param1, param2):
    """Kurze Zusammenfassung.

    Eine detaillierte Beschreibung dieses Beispiels und seiner Parameter.

    Args:
        param1: Erklärung des ersten Parameters.
        param2: Erklärung des zweiten Parameters.

    Returns:
        Der Rückgabewert dieser Funktion.
    """
    return result
```

Weitere Details findest du [hier](https://www.python.org/dev/peps/pep-0257/).

# Neue Schlüsselwörter:

- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [PEP 20](https://www.python.org/dev/peps/pep-0020/)
- [PEP 257](https://www.python.org/dev/peps/pep-0257/)
- Style Guide
- Zen of Python
- Docstrings

# Neue Begriffe:

- **Docstring:** Ein Docstring ist eine Zeichenkette (String) in einem Python-Script, Modul, einer Funktion oder Klasse, die dazu dient, die Funktionalität und Verwendung des Codes zu dokumentieren. Docstrings werden häufig verwendet, um automatisch generierte Dokumentation zu erstellen.

- **PEPs (Python Enhancement Proposals):** PEPs sind Vorschläge für Verbesserungen des Python-Programmiersprachekerns. Diese Vorschläge können neue Funktionen, Erweiterungen bestehender Funktionen oder Änderungen an der Python-Infrastruktur umfassen. PEPs dienen als Diskussionsgrundlage für die Python-Community und werden durch die Zustimmung der Beteiligten implementiert.

- **Konventionen:** In der Programmierung bezieht sich der Begriff "Konventionen" auf bestimmte Vereinbarungen und Standards, die von Entwicklern befolgt werden, um den Code einheitlich und leicht verständlich zu gestalten. Dies kann beispielsweise die Benennung von Variablen, die Einrückung oder die Verwendung von Leerzeichen betreffen. PEP 8 ist ein Beispiel für einen Leitfaden, der Konventionen für den Python-Code festlegt.

# Aufgaben:
[120min]

## 1. **PEP 8-Konformität 🌶️🌶️**
   
Überprüfe das folgende Python-Skript auf PEP 8-Konformität. Finde und behebe Verstöße gegen die Richtlinien. Achte besonders auf Einrückungen, Zeilenlängen, Importe und Namenskonventionen.

```python
# Beispiel-Skript

def benutzerEingabe():
    benutzerEingabe = input("Gib eine Zahl ein: ")
    return int(benutzerEingabe)

def quadratBerechnung(zahl):
    return zahl**2

ergebnis = quadratBerechnung(benutzerEingabe())
print("Ergebnis:", ergebnis)
```

## 2. **Umsetzung des "Zen of Python" 🌶️**
   
Wähle einen Grundsatz aus dem "Zen of Python" und integriere ihn in das obige Python-Skript. Erläutere im Code-Kommentar, wie diese Umsetzung sich auf den Code auswirkt.

## 3. **Docstrings für Funktionen und Klassen 🌶️**

Füge Docstrings zu den Funktionen `benutzerEingabe` und `quadratBerechnung` im obigen Python-Skript hinzu. Stelle sicher, dass die Docstrings die Funktionalität klar und prägnant erklären.


# Checkliste:

- [ ] Ich kenne die Bedeutung von PEP (_Python Enhancement Proposal_) in der Python-Entwicklung.
- [ ] Ich verstehe, wie PEPs zur Verbesserung und Erweiterung der Python-Sprache beitragen.
- [ ] Ich bin mit einigen wichtigen PEPs vertraut und deren Auswirkungen auf die Sprache.
- [ ] Ich kann selbst Docstrings schreiben.