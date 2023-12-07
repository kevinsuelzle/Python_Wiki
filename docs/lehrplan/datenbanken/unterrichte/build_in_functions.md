## Eingebaute Funktionen

SQLite bietet eine Vielzahl von eingebauten Funktionen, die für verschiedene Operationen verwendet werden können, von
mathematischen Berechnungen bis hin zur Textmanipulation. Diese Funktionen sind direkt in SQLite integriert und können
in Ihren SQL-Abfragen verwendet werden.

### Beispiele für eingebaute Funktionen

**Mathematische Funktionen**:

- `ABS(x)`: Gibt den absoluten Wert von `x` zurück.

```sql
SELECT ABS(-15);
```

- `ROUND(x, y)`: Rundet `x` auf `y` Dezimalstellen.

```sql
SELECT ROUND(gehalt, 2)
FROM mitarbeiter;
```

**Textfunktionen**:

- `LENGTH(x)`: Gibt die Länge des Strings `x` zurück.

```sql
SELECT name, LENGTH(name) AS Namenslänge
FROM mitarbeiter;
```

- `UPPER(x)`, `LOWER(x)`: Konvertiert den String `x` in Groß- bzw. Kleinbuchstaben.

```sql
SELECT UPPER(name)
FROM mitarbeiter;
```

**Datum- und Zeitfunktionen**:

- `DATE()`, `TIME()`, `DATETIME()`: Gibt das aktuelle Datum, die aktuelle Uhrzeit bzw. beides zurück.

```sql
SELECT DATE('now');
```

**Sonstige Funktionen**:

- `RANDOM()`: Gibt eine Zufallszahl zurück.

```sql
SELECT RANDOM();
```

## Aggregatefunktionen in SQLite

Aggregatefunktionen in SQLite werden verwendet, um eine Berechnung auf einer Gruppe von Werten durchzuführen und ein
einzelnes Ergebnis zurückzugeben. Sie sind besonders nützlich in Kombination mit der `GROUP BY`-Klausel.

#### Beispiele für Aggregatefunktionen

**COUNT()**:

- Zählt die Anzahl der Zeilen in einer Tabelle.

```sql
SELECT COUNT(*)
FROM mitarbeiter;
```

**SUM()**:

- Summiert die Werte einer bestimmten Spalte.

```sql
SELECT SUM(gehalt)
FROM mitarbeiter;
```

**AVG()**:

- Berechnet den Durchschnittswert einer Spalte.

```sql
SELECT AVG(gehalt)
FROM mitarbeiter;
```

**MAX() und MIN()**:

- Findet den höchsten bzw. niedrigsten Wert in einer Spalte.

```sql
SELECT MAX(gehalt), MIN(gehalt)
FROM mitarbeiter;
```

**GROUP_CONCAT()**:

- Kombiniert Werte aus einer Spalte zu einem durch Kommas getrennten String.

```sql
SELECT GROUP_CONCAT(name)
FROM mitarbeiter
WHERE abteilung = 'IT';
```

## Zusammenfassung

Die Verwendung von eingebauten Funktionen und Aggregatefunktionen in SQLite ermöglicht es, komplexe Berechnungen und
Datenmanipulationen effizient durchzuführen. Diese Funktionen erweitern die Möglichkeiten der Datenabfrage und -analyse
erheblich und sind ein wesentlicher Bestandteil der SQL-Kenntnisse. Durch das Üben mit diesen Funktionen können die
Schüler lernen, wie man Daten in einer Datenbank effektiv verarbeitet und analysiert.

## Liste der Eingebauten Funktionen in SQLite

Hier ist eine Liste der wichtigsten eingebauten Funktionen in SQLite, gruppiert nach ihrer Funktionalität:

### Mathematische Funktionen

- `ABS(x)`: Gibt den absoluten Wert von `x` zurück.
- `ROUND(x, y)`: Rundet `x` auf `y` Dezimalstellen.
- `RANDOM()`: Gibt eine Zufallszahl zurück.
- `MOD(x, y)`: Gibt den Rest der Division von `x` durch `y` zurück.
- `CEIL(x)`: Gibt die kleinste ganze Zahl, die größer oder gleich `x` ist.
- `FLOOR(x)`: Gibt die größte ganze Zahl, die kleiner oder gleich `x` ist.
- `POWER(x, y)`: Gibt `x` hoch `y` zurück.

### Textfunktionen

- `LENGTH(x)`: Gibt die Länge des Strings `x` zurück.
- `UPPER(x)`: Konvertiert den String `x` in Großbuchstaben.
- `LOWER(x)`: Konvertiert den String `x` in Kleinbuchstaben.
- `SUBSTR(x, y, z)`: Gibt einen Teilstring von `x` zurück, beginnend bei `y` mit der Länge `z`.
- `TRIM(x)`: Entfernt Leerzeichen am Anfang und Ende des Strings `x`.
- `REPLACE(x, y, z)`: Ersetzt alle Vorkommen von `y` in `x` durch `z`.

### Datum- und Zeitfunktionen

- `DATE()`: Gibt das aktuelle Datum zurück.
- `TIME()`: Gibt die aktuelle Uhrzeit zurück.
- `DATETIME()`: Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
- `JULIANDAY()`: Gibt den Julianischen Tag zurück.
- `STRFTIME()`: Formatiert Datum und Zeit gemäß dem angegebenen Format.

### Sonstige Funktionen

- `COALESCE(x, y, ...)`: Gibt den ersten nicht-NULL-Wert in der Liste zurück.
- `NULLIF(x, y)`: Gibt NULL zurück, wenn `x` gleich `y` ist, sonst `x`.
- `LAST_INSERT_ROWID()`: Gibt die ROWID des zuletzt eingefügten Datensatzes zurück.

## Liste der Aggregatefunktionen in SQLite

Aggregatefunktionen in SQLite werden verwendet, um Berechnungen auf einer Gruppe von Werten durchzuführen:

- `COUNT(x)`: Zählt die Anzahl der Zeilen, die den Ausdruck `x` enthalten.
- `SUM(x)`: Summiert die Werte von `x`.
- `AVG(x)`: Berechnet den Durchschnittswert von `x`.
- `MAX(x)`: Findet den höchsten Wert von `x`.
- `MIN(x)`: Findet den niedrigsten Wert von `x`.
- `GROUP_CONCAT(x)`: Kombiniert Werte aus `x` zu einem durch Kommas getrennten String.
- `TOTAL(x)`: Berechnet die Gesamtsumme von `x` (ähnlich wie `SUM`, aber immer gibt einen Wert zurück, auch bei
  NULL-Werten).

Diese Listen bieten eine Übersicht über die gängigsten Funktionen in SQLite. Es ist wichtig zu beachten, dass einige
Funktionen je nach SQLite-Version variieren können.

## Ausblick

In SQLite können auch eigene Funktionen programmiert werden. Dieses Kapitel ist Bestandteil eines weiterführenden
Kurses.

[zurück](../datenbanken.md)
