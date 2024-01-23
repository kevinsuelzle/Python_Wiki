# Lösungen

### Aufgabe: Von diesen sieben Tricks sollt ihr nichts wissen🌶

**Gründe für Fehler:**

* Eigener Code
* Fremder Code im eigenen Projekt
* Fehler in der genutzten Bibliothek
* Compiler hat einen Fehler
* Hardware hat einen Fehler

**7 Tips:**

* (Fremd-)Code und Fehlermeldungen lesen
* Nach Fehlermeldung in Internet suchen
* Logger nutzen
* Debugger nutzen
* Fehler repruduzieren
* Tests schreiben
* Statsiche Codechecker verwenden


Die Lösungen beziehen sich auf die Aktionen, die ausgeführt werden sollen, um mit dem Debugger zu interagieren:


### 1. **Grundlagen des Python-Interpreters**: 
Füge `pdb.set_trace()` vor `return a + b` ein. Starte das Programm und verwende den Befehl `p a` und `p b`, 
um die Werte zu überprüfen.
### 2. **Bytecode in Python verstehen**: 
Starte das Programm und verwende `n`, um jede Zeile auszuführen. Beobachte, wie die Variable `ergebnis` berechnet 
wird.
### 3. **Python und Plattformunabhängigkeit**: 
Starte das Programm und benutze `s`, um in die Funktion `berechne_differenz` einzutreten. Verwende `p x` und `p y`, 
um die Werte zu überprüfen.
### 4. **Einführung in Python Virtual Machine (PVM)**: 
Starte das Programm und verwende `p ergebnis`, um den Wert der Variable `ergebnis` auszugeben, dann `c`, um das 
Programm zu beenden.
### 5. **Python-Interpreter: CPython vs. PyPy**: 
Starte das Programm im Debug-Modus mit `python -m pdb script.py`. Setze einen Haltepunkt mit `b multipliziere` und 
überprüfe `x` und `y` mit `p x` und `p y`, bevor du `c` ausführst.
