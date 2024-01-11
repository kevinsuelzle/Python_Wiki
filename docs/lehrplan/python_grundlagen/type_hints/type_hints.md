# Einführung in Type Hints in Python

Type Hints sind in Python seit der Version 3.5 offiziell verfügbar und stellen eine bedeutende Erweiterung für die
Sprache dar. Sie ermöglichen es Entwicklern, den erwarteten Datentyp von Parametern und Rückgabewerten in Funktionen
anzugeben. 

Leider ist dies lediglich ein Hinweis für andere Programmierer und wird durch Python nicht überprüft. Dafür
gibt es allerdings frei verfügbare Tools, um dies zu tun.

## Wichtigkeit von Type Hints
[40min]

1. **Verbesserte Lesbarkeit und Wartbarkeit**: Type Hints machen den Code für andere Entwickler (oder auch für den Autor
   selbst zu einem späteren Zeitpunkt) leichter verständlich.

2. **Fehlervermeidung**: Sie helfen dabei, Fehler zu identifizieren, indem sie sicherstellen, dass Funktionen mit den
   erwarteten Datentypen verwendet werden.

3. **Unterstützung durch Entwicklungswerkzeuge**: Moderne Entwicklungsumgebungen und Linter nutzen Type Hints, um
   potenzielle Laufzeitfehler zu erkennen.

4. **Verbesserte Refactoring-Unterstützung**: Type Hints erleichtern das Refactoring von Code, da Tools präziser
   erkennen können, wie bestimmte Variablen und Funktionen verwendet werden.

5. **Dokumentation**: Sie dienen als eine Form der Dokumentation, die es neuen Nutzern des Codes erleichtert, die
   Funktionsweise und den Zweck von Funktionen zu verstehen.

## Definition von Type Hints

Type Hints werden in Python durch die Verwendung von Anmerkungen (Annotations) definiert:

- **Parameter**: Der Typ eines Parameters wird nach dem Parameter und einem Doppelpunkt angegeben.
- **Rückgabewerte**: Der Typ des Rückgabewerts wird nach einem `->` und vor dem Doppelpunkt am Ende der
  Funktionsdefinition angegeben.

## Beispiele
[25min]

- **Einfache Funktion mit Type Hints**
```python
def addiere(a: int, b: int) -> int:
    return a + b
```

- **Funktion mit gemischten Datentypen**
```python
def begruesse(name: str, alter: int) -> str:
    return f"Hallo {name}, du bist {alter} Jahre alt."
```

- **Funktion mit komplexeren Datentypen**
```python
from typing import List, Dict

def verarbeite_daten(daten: List[int]) -> Dict[str, int]:
    return {"max": max(daten), "min": min(daten)}
```

## Type Hints Testen
[50min]
Obwohl Type Hints in Python eine wertvolle Ergänzung für die Typisierung des Codes bieten, werden sie zur Laufzeit
standardmäßig nicht erzwungen. Stattdessen können sie mit zusätzlichen Tools überprüft werden, um die Sicherheit und
Korrektheit des Programms zu erhöhen.

### Statische Typüberprüfung

Eine der Hauptmethoden zum Testen von Type Hints ist die statische Typüberprüfung. Hier sind einige Tools, die dabei
helfen können:

1. **mypy**: `mypy` ist ein beliebtes Open-Source-Tool, das die statische Typüberprüfung in Python unterstützt. Es kann
   als Teil des Entwicklungsprozesses verwendet werden, um sicherzustellen, dass Type Hints konsistent angewendet werden
   und der Code den angegebenen Typen entspricht.

    - Installation: `pip install mypy`
    - Verwendung: `mypy script.py`

2. **pyright**: `pyright` ist ein statischer Typüberprüfer für Python, entwickelt von Microsoft. Er ist schneller
   als `mypy` und kann ebenfalls als Teil des Entwicklungsworkflows integriert werden.

    - Installation: `npm install -g pyright`
    - Verwendung: `pyright script.py`

3. **PyCharm**: Die integrierte Entwicklungsumgebung (IDE) PyCharm von JetBrains bietet eingebaute Unterstützung für
   Type Hints und die statische Typüberprüfung. PyCharm hebt Typkonflikte hervor und bietet Korrekturvorschläge während
   der Entwicklung.

4. **Pylance**: Pylance ist eine Erweiterung für Visual Studio Code, die auf Pyright basiert. Sie verbessert die
   Python-Unterstützung in VS Code durch Features wie schnelle und umfassende statische Typüberprüfung.

### Typüberprüfung bei Unit-Tests

Neben statischen Typüberprüfern können Type Hints auch beim Schreiben von Unit-Tests hilfreich sein. Tools
wie `unittest` oder `pytest` ermöglichen es, zu überprüfen, ob Funktionen mit den erwarteten Datentypen arbeiten.
Während des Testlaufs können Sie überprüfen, ob die Funktionen korrekt auf Typfehler reagieren.

### Continuous Integration (CI)
[30min]
Die Einbindung von statischen Typüberprüfungstools in den CI/CD-Workflow stellt sicher, dass die Typsicherheit eines
Programms bei jedem Build überprüft wird. Dies kann erreicht werden, indem man Tools wie `mypy` oder `pyright` in die
CI-Pipeline integriert, sodass Pull Requests und Commits vor der Integration in den Hauptbranch automatisch auf
Typkonflikte überprüft werden.

### Zusammenfassung

Type Hints in Python sind ein mächtiges Werkzeug, das zur Verbesserung der Code-Qualität, der Lesbarkeit und der
Wartbarkeit beiträgt. Sie sind besonders nützlich in großen Projekten oder Projekten, die von mehreren Entwicklern
bearbeitet werden. Obwohl Python eine dynamisch typisierte Sprache ist und Type Hints nicht zwingend erforderlich sind,
wird ihre Verwendung zunehmend als Best Practice angesehen, um klaren und fehlerfreien Code zu fördern.

Die Verwendung von Type Hints allein bietet keine Garantie für die Typsicherheit zur Laufzeit. Durch den Einsatz von
statischen Typüberprüfungstools wie `mypy`, die Integration in Entwicklungsumgebungen und die Verwendung von Unit-Tests
können jedoch Typfehler vor der Ausführung erkannt und korrigiert werden. Dies trägt erheblich zur Stabilität und
Sicherheit von Python-Programmen bei und fördert die Entwicklung von robustem und wartbarem Code.

# Aufgaben
[25min]

### 1. **Typisierte Variable** 🌶️️: 
Definiere eine Variable `alter` vom Typ `int`.

### 2. **Typisierte Funktion** 🌶️️: 
Schreibe eine Funktion `quadrat`, die einen `int` als Parameter nimmt und einen `int`
   zurückgibt.

### 3. **Mehrere Parameter** 🌶️️: 
Schreibe eine Funktion `addiere`, die zwei `float`-Parameter annimmt und ihr Ergebnis
   als `float` zurückgibt.

### 4. **Optionale Parameter** 🌶️️🌶️️: 
Schreibe eine Funktion `begruessen`, die einen `str`-Parameter und einen optionalen
   Parameter `alter` vom Typ `Optional[int]` hat.

### 5. **Rückgabewert None** 🌶️️: 
Schreibe eine Funktion `drucke_hallo`, die einen `str` entgegennimmt und `None` zurückgibt.

### 6. **Listen als Parameter** 🌶️️🌶️️: 
Schreibe eine Funktion `durchschnitt`, die eine Liste von `int` annimmt und einen `float`
   zurückgibt.

### 7. **Dictionary als Rückgabewert** 🌶️️🌶️️: 
Schreibe eine Funktion `erstelle_dict`, die zwei `str`-Parameter annimmt und
   ein `Dict[str, str]` zurückgibt.

### 8. **Komplexe Typen** 🌶️️🌶️️: 
Schreibe eine Funktion `verarbeite_daten`, die eine `List[Dict[str, int]]` annimmt und
   eine `List[int]` zurückgibt.

### 9. **Typisierte Tuples** 🌶️️🌶️️: 
Schreibe eine Funktion `min_max`, die eine `List[int]` annimmt und ein `Tuple[int, int]`
   zurückgibt (das Minimum und Maximum der Liste).

### 10. **Union Type Hints** 🌶️️🌶️️: 
Schreibe eine Funktion `id_oder_name`, die einen Parameter annimmt, der entweder `int`
    oder `str` sein kann, und denselben Typ zurückgibt.



