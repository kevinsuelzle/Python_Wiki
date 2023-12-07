# Fragen an die Datenbank

## Verwendung von JOINs in SQL

JOINs sind ein zentrales Konzept in relationalen Datenbanken und ermöglichen es, Daten aus zwei oder mehr Tabellen
basierend auf einer gemeinsamen Beziehung zusammenzuführen (Umkehrung der Normalisierung). Hier sind einige grundlegende
Typen von JOINs mit
Beispielen:

### INNER JOIN

Der `INNER JOIN` gibt alle Zeilen aus beiden Tabellen zurück, bei denen die angegebene JOIN-Bedingung erfüllt ist.

```sql
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         INNER JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id;
```

### LEFT JOIN (LEFT OUTER JOIN)

Der `LEFT JOIN` gibt alle Zeilen aus der linken Tabelle und die übereinstimmenden Zeilen aus der rechten Tabelle zurück.
Wenn es keine Übereinstimmung gibt, werden die Ergebnisse der rechten Tabelle mit NULL aufgefüllt.

```sql
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         LEFT JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id;
```

### RIGHT JOIN (RIGHT OUTER JOIN)

Der `RIGHT JOIN` funktioniert wie der `LEFT JOIN`, aber in umgekehrter Reihenfolge: Alle Zeilen aus der rechten Tabelle
und die übereinstimmenden Zeilen aus der linken Tabelle werden zurückgegeben.

```sql
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         RIGHT JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id;
```

### FULL OUTER JOIN

Der `FULL OUTER JOIN` gibt alle Zeilen zurück, wenn es eine Übereinstimmung in einer der Tabellen gibt. Dieser JOIN-Typ
wird in SQLite nicht direkt unterstützt, kann aber simuliert werden.

```sql
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         LEFT JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id
UNION
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         RIGHT JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id;
```

## Erstellung von Views in SQL

Ein View in SQL ist eine virtuelle Tabelle, die das Ergebnis einer Abfrage darstellt. Views können verwendet werden, um
komplexe Abfragen zu vereinfachen, die Datenintegrität zu wahren und die Sicherheit zu erhöhen, indem Benutzern der
Zugriff auf spezifische Daten ermöglicht wird.

### Erstellen eines einfachen Views

```sql
CREATE VIEW view_mitarbeiter_abteilung AS
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
         INNER JOIN abteilung ON mitarbeiter.abteilungs_id = abteilung.id;
```

Mit diesem View können Sie dann einfach die Namen der Mitarbeiter und ihre Abteilungsbezeichnungen abfragen:

```sql
SELECT *
FROM view_mitarbeiter_abteilung;
```

### Erstellen eines Views mit JOINs

Views sind besonders nützlich, um komplexe JOINs zu kapseln:

```sql
CREATE VIEW view_projekt_mitarbeiter AS
SELECT projekt.name AS Projektname, mitarbeiter.name AS Mitarbeitername
FROM projekt
         INNER JOIN projektmitarbeiter ON projekt.id = projektmitarbeiter.projekt_id
         INNER JOIN mitarbeiter ON projektmitarbeiter.mitarbeiter_id = mitarbeiter.id;
```

Dieser View kombiniert Informationen aus den Tabellen `projekt`, `projektmitarbeiter` und `mitarbeiter`, um eine
übersichtliche Darstellung der Mitarbeiter in jedem Projekt zu ermöglichen.

### Zusammenfassung

Die Verwendung von JOINs und Views in SQL ist entscheidend für den effektiven Umgang mit relationalen Datenbanken.
Während JOINs es ermöglichen, Daten aus verschiedenen Tabellen dynamisch zu kombinieren, bieten Views eine Möglichkeit,
solche Abfragen zu standardisieren und zu vereinfachen, was besonders bei wiederkehrenden oder komplexen Abfragen
nützlich ist.

**Aufgabe:**

- Führen sie JOINs in ihre Projekte ein. Suchen sie nach Fällen und Fragestellungen, in denen JOINs sinnvolle Aussagen generieren.
- Erstellen sie aus den entwickelten JOINs VIEWS, die diese Abfragen fixieren.

[zurück](../datenbanken.md)
