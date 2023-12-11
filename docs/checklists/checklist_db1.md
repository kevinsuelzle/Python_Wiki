# Lernziele SQL Datenbanken

1. **Grundverständnis relationaler Datenbanken**: Die Schüler sollten die grundlegenden Konzepte relationaler
   Datenbanken verstehen, einschließlich Tabellen, Spalten, Zeilen, Primärschlüssel und Fremdschlüssel.

2. **Einführung in SQL**: Die Schüler sollten die Grundlagen von SQL lernen, einschließlich der Fähigkeit, einfache
   Abfragen mit `SELECT`, `INSERT`, `UPDATE` und `DELETE` zu formulieren.

3. **Erstellung und Design von Datenbanktabellen**: Die Schüler sollten lernen, wie man Tabellen in SQLite erstellt und
   wie man geeignete Datentypen für die verschiedenen Spalten auswählt.

4. **Datenmanipulation und -abfrage**: Die Schüler sollten in der Lage sein, Daten in eine Datenbank einzufügen, zu
   aktualisieren, abzufragen und zu löschen. Sie sollten auch einfache Abfragen mit Bedingungen (`WHERE`-Klausel) und
   Sortierungen (`ORDER BY`) durchführen können.

5. **Verständnis und Anwendung von JOINs**: Die Schüler sollten die verschiedenen Arten von JOINs (wie INNER JOIN, LEFT
   JOIN) verstehen und anwenden können, um Daten aus mehreren Tabellen abzufragen.

6. **Einsatz von Aggregatfunktionen**: Die Schüler sollten lernen, wie man Aggregatfunktionen
   wie `COUNT`, `SUM`, `AVG`, `MAX` und `MIN` verwendet, um zusammengefasste Daten abzufragen.

7. **Einführung in Datenbanktransaktionen**: Die Schüler sollten ein grundlegendes Verständnis von Transaktionen und
   deren Bedeutung für die Datenintegrität erlangen.

8. **Erstellung und Nutzung von Views**: Die Schüler sollten lernen, wie man Views erstellt und nutzt, um komplexe
   Abfragen zu vereinfachen und zu strukturieren.

9. **Praktische Anwendung durch Projekte**: Die Schüler sollten die Möglichkeit haben, ihr Wissen in praktischen
   Projekten anzuwenden, um ein tieferes Verständnis der realen Anwendung von Datenbanken zu entwickeln.

# Aliase

- Ich weiß, was Aliase sind und wie man sie einsetzt
- Ich kann in einem Skript Aliase erkennen

# Eingebaute Funktionen

- Ich kenne übliche eingebaute Funktionen und kann sie in Abfragen einsetzen
- Ich kenne den Unterschied zu Aggregatefunktionen
- Ich kann Aggregatefunktionen sinnvoll in Abfragen verwenden

# Erstellen von Tabellen

- Ich kann Tabellen erstellen
    - mit typisiereten Spalten
    - Indices
    - Constraints
    - Defaults
    - Keys (einfache und fremde)
- Ich kann Tabellen ändern
    - mit dem ALTER Kommando
    - mit dem 4-Schritt
        - neue Tabelle erstellen
        - Daten kopieren
        - alte Tabelle löschen
        - neue Tabelle umbenennen
- Ich kann Tabellen löschen

# Datentypen

- Ich kenne die in SQLite verwendeten Datentypen

# Arbeitsumgebung

- Ich kann eine Arbeitsumgebung herstellen
    - indem ich die Kommandozeile aufrufe und mich mit der Datenbank verbinde
    - indem ich die IDE PyCharm Community öffne und einrichte
        - Plugin installiere
        - Plugin verwende
            - um mich mit der Datenbank zu verbinden und
            - um über eine Konsole Befehle an die Datenbank zu senden und Ergebnisse zurück zu bekommen

# Indizes und referentielle Integrität

- Ich weiß was ein Index ist
- Ich weiß ungefähr, wie er intern funktioniert und kann anhand eines einfachen B-Baumes seine Funktion erklären

# Joins und Views

- Ich kenne die verschiedenen Arten von JOINs
- Ich kann erklären, was ein INNER Join macht und was ich als Ergebnis erwarten kann
- Ich kann ein Beispiel schreiben, das einen INNER JOIN nutzt.

# Normalisierung von Daten

- Ich weiß, warum Daten für die Verwendung in relationalen Datenbanken normalisiert werden müssen
- Ich kenne Ausnahmen zu dieser Regel
- Ich kann Daten in Tabellen ordnen, sodass diese der 1.NF, 2.NF oder 3.NF entsprechen
- Ich weiß, dass die inneren Zusammenhänge dieser Daten durch referentielle Integrität abgesichert wird

# Reservierte Worte

- Ich weiß, dass es reservierte Worte gibt, die nicht für die Namensgebung verwendet werden sollten.

# Batch, Script, Deploy

- Ich kann SQLite Kommandos in einer Datei zusammenfassen.
- Ich weiß, dass das Ausführen aufeinander folgender Kommandos batch genannt wird, die Datei script
- Ich kann erklären, was Transaktionen sind
- Ich kann ein batch oder ein script mit Transaktionen gegen Fehler absichern
- Ich weiß, dass komplexe Fälle mit anderen Sprachen (z.B. python) verarbeitet werden müssen.
- Ich weiß, wie ich, im Falle von SQLite, eine Datenbank verteilen kann.

# SQL Sprachtypisierung

- Ich kenne die Bezeichner DDL und DML

# Unterabfragen und Common Table Expressions

- Ich kann eine Abfrage als Unterabfrage in SELECT, INSERT oder UPDATE Kommandos erstellen.
- Ich verstehe die allgemeine Form der Common Table Expression und deren Bedeutung
- Ich kann einfache Unterabfragen in CTE umschreiben

# UML-Diagramme

- Ich verstehe, was UML-Diagramme sind,
- was sie in Bezug auf Datenbanken ausdrücken und
- welche Bedeutung die Zeichen in diesen Diagrammen haben (Bezug Mermaid / Markdown)
- Ich kann die normalsprachlichen Formulierungen eines Datenbankproblems in UML-Diagramme umsetzen
- Ich kann die UML_Diagramme in die Tabellenstruktur einer Datenbank überführen

# Arbeiten mit Daten

- Ich kenne die CRUD Operationen, die auf Datenbanken angewendet werden können
- Ich kann entsprechende Befehle verfassen
- Ich kann in diesen Befehlen eingebaute Funktionen oder Aggregatefunktionen einsetzen
- Ich kann Daten durch den Einsatz von
    - WHERE filtern,
    - mittels ORDER BY und ASC/DESC aufsteigend oder absteigend sortieren,
    - mittels GROUP BY gruppieren,
    - mittels HAVING nochmals auf anderer Ebene filtern

# Projekte

- Ich kann das Wissen über Datenbanken bei konkreten Projekten anwenden.


# SQLite in Python: 

- Ich habe ein grundlegendes Verständnis dafür, wie SQLite in Python verwendet wird.
- Ich weiß, wie man SQLite-Verbindungen als Context Manager in einem "`with`"-Statement einsetzt.
- Ich kann eine Verbindung zur SQLite-Datenbank in Python herstellen.
- Ich weiß, wie ich die Verbindung zur SQLite-Datenbank ordnungsgemäß schließe.
- Ich kann einen Cursor in SQLite erstellen und verwenden, um SQL-Anweisungen auszuführen.
- Ich kann Tabellen in SQLite erstellen und Daten mithilfe von SQL-Anweisungen einfügen.
- Ich kann Transaktionen in SQLite steuern, einschließlich Starten, Bestätigen (COMMIT) und Rückgängigmachen (ROLLBACK).
- Ich kann benutzerdefinierte Aggregatfunktionen in SQLite erstellen und verwenden.
- Ich kann SQL-Abfragen in SQLite ausführen.
- Ich kann Ergebnisse von SQL-Abfragen mithilfe von `fetchall` und `fetchone` in SQLite abrufen.
- Ich weiß, wie man die `ROLLBACK`-Anweisung in SQLite-Transaktionen verwendet, um Änderungen rückgängig zu machen.
- Ich kann Fehler in Datenbankoperationen ordnungsgemäß handhaben.


# Schlusswort

- Ich verstehe, wie Datenbanken verwendet werden können und das sie noch mehr Potential haben, als wir in diesem Kurs
  angesprochen haben.