# Verwendung von Aliasen

Aliasse sind ein nützliches Werkzeug in SQL, um Tabellen oder Spalten in einer Abfrage temporär umzubenennen. Dies kann
die Lesbarkeit der Abfrage erhöhen, insbesondere bei komplexeren Abfragen oder wenn Tabellen- oder Spaltennamen sehr
lang sind. In diesem Abschnitt lernen wir, wie man Aliasse in SQLite verwendet.

## Grundlagen der Aliasverwendung

Ein Alias wird mit dem Schlüsselwort `AS` definiert, obwohl das `AS` in SQLite optional ist. Aliasse können sowohl für
Tabellennamen als auch für Spaltennamen verwendet werden.

### Beispiele für die Verwendung von Aliassen

**Alias für eine Spalte**:

```sql
SELECT name AS Mitarbeitername
FROM mitarbeiter;
```

Hier wird die Spalte `name` in der Ausgabe als `Mitarbeitername` angezeigt.

**Mehrere Aliasse für Spalten**:

```sql
SELECT name AS Name, gehalt AS Gehalt
FROM mitarbeiter;
```

In dieser Abfrage werden die Spalten `name` und `gehalt` als `Name` und `Gehalt` ausgegeben.

**Alias für eine Tabelle**:

```sql
SELECT m.name
FROM mitarbeiter AS m;
```

Hier wird der Tabelle `mitarbeiter` der Alias `m` zugewiesen, was die Abfrage verkürzt.

**Kombination von Tabellen- und Spaltenalias**:

```sql
SELECT m.name AS Mitarbeitername
FROM mitarbeiter m;
```

Diese Abfrage kombiniert einen Tabellenalias (`m` für `mitarbeiter`) und einen Spaltenalias (`Mitarbeitername`
für `name`).

**Aliasse in WHERE-Klauseln**:

```sql
SELECT name AS Mitarbeitername
FROM mitarbeiter
WHERE gehalt > 3000;
```

Beachten Sie, dass Aliasse nicht in der `WHERE`-Klausel selbst verwendet werden können.

**Aliasse in ORDER BY**:

```sql
SELECT name AS Mitarbeitername
FROM mitarbeiter
ORDER BY Mitarbeitername;
```

Hier wird der Alias `Mitarbeitername` in der `ORDER BY`-Klausel verwendet.

**Aliasse in GROUP BY**:

```sql
SELECT abteilung AS Abteilung, COUNT(*) AS Anzahl
FROM mitarbeiter
GROUP BY Abteilung;
```

In dieser Abfrage wird der Alias `Abteilung` für die Spalte `abteilung` sowohl in der Auswahl als auch in
der `GROUP BY`-Klausel verwendet.

### Zusammenfassung

Aliasse sind ein einfaches, aber mächtiges Werkzeug in SQL, um Abfragen lesbarer und manchmal auch kürzer zu gestalten.
Sie sind besonders nützlich in komplexen Abfragen mit langen oder mehrfach verwendeten Tabellen- und Spaltennamen.

**Aufgabe:**

- Führen sie die verschiedenen Kommandos aus.
- Entwickeln sie eigene Aliasse aufgrund von eigenen Erweiterungen in ihren Daten.

Weiter zu [Eingebaute Funktionen](../unterrichte/build_in_functions.md) &emsp; | &emsp; [zurück](../datenbanken.md)
