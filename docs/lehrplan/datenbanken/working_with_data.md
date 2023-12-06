# Arbeiten mit Daten

Nachdem wir im letzten Kapitel gelernt haben, wie man Tabellen in SQLite erstellt, werden wir uns nun darauf
konzentrieren, wie man Daten in diese Tabellen einfügt. Wir werden das `INSERT`-Kommando sowohl über die Konsole als
auch über das SQLite Command Line Interface (CLI) verwenden. Dies wird uns helfen zu verstehen, wie manuell das Einfügen
von Daten erfolgt und wie mühsam es sein kann, größere Datenmengen händisch einzufügen. Zur Vereinfachung dieses
Prozesses werden wir auch die Funktionen von SQLite zur Importierung von Daten aus CSV-Dateien nutzen. Die Überprüfung
der korrekten Dateneinfügung erfolgt durch einfache `SELECT`-Kommandos.

## Einfügen von Daten mit dem INSERT-Kommando

**Manuelles Einfügen über die Konsole/CLI**:
Um Daten manuell in eine Tabelle einzufügen, verwenden wir das `INSERT INTO`-Statement. Angenommen, wir haben eine
Tabelle `personen` mit den Spalten `id`, `name` und `alter`. Ein Beispiel für das Einfügen eines Datensatzes wäre:

```sql
INSERT INTO personen (id, name, alter)
VALUES (1, 'Max Mustermann', 30);
```

**Aufgabe:**

Wiederholen Sie diesen Vorgang für einige Datensätze, um den Schülern zu zeigen, wie Daten manuell eingefügt werden.

**Einfügen mehrerer Datensätze**:

Um den Prozess zu beschleunigen, können Sie mehrere Datensätze gleichzeitig einfügen:

```sql
INSERT INTO personen (id, name, alter)
VALUES (2, 'Maria Musterfrau', 28),
       (3, 'John Doe', 25);
```

**Aufgabe:**

Wiederholen sie den Vorgang und fügen sie weitere Datensätze in das Kommando ein.

**Überprüfung der Einfügung**:

Um zu überprüfen, ob die Daten korrekt eingefügt wurden, verwenden Sie das `SELECT`-Statement:

```sql
SELECT *
FROM personen;
```

## Importieren von Daten aus einer CSV-Datei (bulk insert)

**Vorbereitung der CSV-Datei**:

Erstellen Sie eine CSV-Datei mit den entsprechenden Daten. Zum Beispiel könnte eine Datei `personen.csv` folgendermaßen
aussehen:

```
id,name,alter
4,Jane Smith,32
5,Alex Johnson,45
```

**Importieren der Daten**:
Verwenden Sie das SQLite-Tool, um die Daten aus der CSV-Datei zu importieren. Öffnen Sie das SQLite CLI und führen
Sie folgende Befehle aus:

```sql
.mode csv
.import pfad/zur/personen.csv personen
```

Stellen Sie sicher, dass der Pfad zur CSV-Datei und der Tabellenname korrekt sind.

**Überprüfung des Imports**:
Verwenden Sie erneut das `SELECT`-Statement, um zu überprüfen, ob die Daten aus der CSV-Datei korrekt importiert
wurden:

```sql
SELECT *
FROM personen;
```

**Aufgabe:**

1. Suchen sie im Internet nach Datentabellen, die im CSV Format geladen werden können. Hier bieten sich fake Datenbanken
   oder Ortsverzeichnisse mit PLZ an.
2. Erstellen sie die passende Tabelle dazu.
3. Fügen sie die Daten in die Tabelle ein und prüfen sie das Ergebnis.

### INSERT Zusammenfassung

Durch das manuelle Einfügen von Daten und den Import aus einer CSV-Datei lernen die Schüler zwei grundlegende Methoden,
um mit Daten in SQLite zu arbeiten. Während das manuelle Einfügen gut für das Verständnis des `INSERT`-Kommandos und für
kleinere Datenmengen geeignet ist, zeigt der Import aus einer CSV-Datei, wie man effizienter mit größeren Datenmengen
umgehen kann. Beide Methoden sind wichtig, um ein umfassendes Verständnis für das Arbeiten mit Datenbanken zu
entwickeln.

## Abschnitt: Komplexere Abfragen in SQLite

Nachdem wir Daten in unsere Datenbank eingefügt haben, ist es an der Zeit, komplexere Abfragen zu üben. Wir werden
verschiedene Sprachelemente von SQL nutzen, darunter `SELECT`-Abfragen
mit `WHERE`, `HAVING`, `ORDER BY`, `GROUP BY`, `LIKE`, `IS (NOT) NULL`, sowie die logischen Operatoren `AND` und `OR`
und den Operatoren `ASC` und `DESC`.
Zunächst erstellen wir eine geeignete Tabelle, und dann üben wir anhand von 15 Beispielen.

### Erstellung einer Beispieltabelle

Lassen Sie uns eine Tabelle `mitarbeiter` erstellen, die wir für unsere Übungen verwenden können:

```sql
CREATE TABLE mitarbeiter
(
    id                INT PRIMARY KEY,
    name              TEXT,
    alter             INT,
    abteilung         TEXT,
    gehalt            REAL,
    eintrittsdatum    DATE,
    hat_fuehrerschein BOOLEAN
);
```
**Aufgabe:** Fülle die Tabelle mit Testdaten.

**Aufgabe:** Erweitere die Tabelle mit dem ALTER Befehl und fülle mit Daten.  

### Liste von Abfragebeispielen

**Einfache Auswahl**:

```sql
SELECT *
FROM mitarbeiter;
```

**Auswahl mit Bedingung**:

```sql
SELECT *
FROM mitarbeiter
WHERE abteilung = 'Vertrieb';
```

**Sortierung der Ergebnisse**:

```sql
SELECT *
FROM mitarbeiter
ORDER BY gehalt DESC;
```

**Auswahl mit mehreren Bedingungen**:

```sql
SELECT *
FROM mitarbeiter
WHERE alter > 30 AND gehalt > 3000;
```

**Verwendung von OR**:

```sql
SELECT *
FROM mitarbeiter
WHERE abteilung = 'Vertrieb'
   OR abteilung = 'Marketing';
```

**Suche mit LIKE**:
```sql
SELECT *
FROM mitarbeiter
WHERE name LIKE '%Schmidt%';
```

**Überprüfung auf NULL-Werte**:
```sql
SELECT *
FROM mitarbeiter
WHERE eintrittsdatum IS NULL;
```

**Gruppierung von Daten**:
```sql
SELECT abteilung, COUNT(*)
FROM mitarbeiter
GROUP BY abteilung;
```

**Gruppierung mit HAVING**:
```sql
SELECT abteilung, COUNT(*)
FROM mitarbeiter
GROUP BY abteilung
HAVING COUNT(*) > 3;
```

**Auswahl spezifischer Spalten**:
```sql
SELECT name, gehalt
FROM mitarbeiter;
```

**Einschränkung der Ergebnismenge**:
```sql
SELECT *
FROM mitarbeiter
WHERE gehalt > 5000 LIMIT 10;
```

**Kombination von AND und OR**:
```sql
SELECT *
FROM mitarbeiter
WHERE (alter < 35 OR alter > 50) 
AND abteilung = 'IT';
```

**Überprüfung auf Nicht-NULL-Werte**:
```sql
SELECT *
FROM mitarbeiter
WHERE eintrittsdatum IS NOT NULL;
```

**Sortierung nach mehreren Kriterien**:
```sql
SELECT *
FROM mitarbeiter
ORDER BY abteilung, gehalt DESC; -- alternativ ASC
```

### Zusammenfassung

Diese Abfragen decken eine breite Palette von SQL-Funktionen ab und bieten eine solide Grundlage für das Verständnis und
die Anwendung komplexerer SQL-Abfragen. Durch das Üben dieser Beispiele werden die Schüler in der Lage sein, effektiv
mit Daten in SQLite zu arbeiten und die vielfältigen Möglichkeiten von SQL-Abfragen zu erkunden.

[zurück](datenbanken.md)
