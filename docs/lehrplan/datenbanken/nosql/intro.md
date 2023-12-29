# NoSQL Intro und Motivation

NoSQL steht für "Not only SQL" und bezeichnet eine Vielzahl von Datenbankmanagementsystemen, die sich von traditionellen relationalen Datenbanken unterscheiden. Der Begriff "NoSQL" bedeutet nicht zwangsläufig "kein SQL", sondern betont, dass diese Systeme zusätzlich zu SQL-basierten Datenbanken existieren. NoSQL Datenbanken sind in der Regel nicht relational und verzichten auf starre Schemata. Dadurch sind sie flexibler und können besser mit sich ändernden Anforderungen umgehen.

NoSQL Datenbanken können allgemein in folgende Kategorien eingeteilt werden:

- Dokumentenorientierte Datenbanken
- Graphdatenbanken
- Spaltenorientierte Datenbanken
- Schlüssel-Wert-Datenbanken

## Dokumentenorientierte Datenbanken

Dokumentenorientierte Datenbanken speichern Daten in semi-strukturierten Dokumenten, oft im JSON- oder BSON-Format. Dies ermöglicht eine einfache Handhabung von komplexen Datenstrukturen und eine schnelle Anpassung an sich ändernde Anforderungen. Dokumentenorienterite Datenbanken sind besonders gut für Anwendungen geeignet, die mit großen Mengen von Daten arbeiten, wie zum Beispiel Content-Management-Systeme, E-Commerce-Plattformen und Anwendungen des IOT Berechs.

Die Verwendung von Dokumentenbasierten Datenbanken bietet sich inbesondere dann an, wenn die Datenstruktur nicht von vornherein feststeht oder sich in einzelnen Dokumenten unterscheidet. Ein Beispiel hierfür ist die Speicherung von Daten aus Formularen, die von Benutzern ausgefüllt werden. Die Daten können in einem Dokument gespeichert werden, ohne dass ein Schema definiert werden muss. Dies ermöglicht eine einfache Handhabung von komplexen Datenstrukturen und eine schnelle Anpassung an sich ändernde Anforderungen.

Beispiele für bekannte Dokumentenorientierte Datenbanken sind MongoDB, CouchDB und Couchbase.

## Graphdatenbanken

Graphdatenbanken verwenden Graphen, um Beziehungen zwischen Entitäten darzustellen. Diese eignen sich besonders gut für Anwendungen, bei denen die Beziehungen zwischen den Datenpunkten von zentraler Bedeutung sind, wie zum Beispiel in sozialen Netzwerken. Graphdatenbanken sind in der Regel sehr effizient bei der Verarbeitung von komplexen Abfragen, die mehrere Beziehungen zwischen den Datenpunkten umfassen.

Beispiele für bekannte Graphdatenbanken sind Neo4j, OrientDB und ArangoDB.

## Spaltenorientierte Datenbanken

Spaltenspeicherdatenbanken speichern Daten spaltenweise anstelle von zeilenweise. In herkömmlichen Datenbanken werden Daten als zweidimensionale Tabellen aus Zeilen und Spalten dargestellt. Diese müssen jedoch in einer eindimensionalen Form auf der Festplatte und im Arbeitsspeicher des Computers gespeichert werden. Die spaltenorientierte Datenbank löst diese Herausforderung, indem sie die Daten spaltenweise abspeichert. Spaltenorientierte Systeme bieten Vorteile bei Anwendungen wie Data Warehousing, bei denen Aggregate über große Mengen ähnlicher Elemente gebildet werden. Der effiziente Zugriff auf Festplattendaten steht im Fokus von Vergleichen zwischen zeilenorientierten und spaltenorientierten Systemen. Ein Megabyte sequentiell gespeicherter Daten kann genauso lang dauern wie ein einzelner Direktzugriff.

**_Beispiel:_**

| Personalnr | Nachname | Vorname | Gehalt |
| ---------- | -------- | ------- | ------ |
| 10001      | Becker   | Thomas  | 55000  |
| 10002      | Wagner   | Sabine  | 48000  |
| 10003      | Schulz   | Andreas | 60000  |

Bei einer Zeilenorientierten Speicherung werden die Daten wie folgt gespeichert:
1001, Becker, Thomas, 55000, 10002, Wagner, Sabine, 48000, 10003, Schulz, Andreas, 60000

Bei einer Spaltenorientierten Speicherung werden die Daten wie folgt gespeichert:
10001, 10002, 10003, Becker, Wagner, Schulz, Thomas, Sabine, Andreas, 55000, 48000, 60000

In der Praxis eignen sich zeilenorientierte Architekturen gut für typische OLTP-Aufgaben (z.B. Buchhaltungssysteme) mit vielen interaktiven Transaktionen, während spaltenorientierte Systeme für OLAP-Aufgaben (z.B. analytische Informationssysteme) mit komplexen Abfragen über alle Datensätze geeignet sind.

Beispiele für bekannte Spaltenspeicherdatenbanken sind Cassandra, HBase und Vertica.

## Exkurs: OLTP und OLAP

### OLTP (Online Transaction Processing)

OLTP steht für "Online Transaction Processing" und beschreibt Systeme, die darauf ausgerichtet sind, Transaktionen in Echtzeit zu verarbeiten. Diese Transaktionen sind typischerweise alltägliche Geschäftsaktivitäten wie das Hinzufügen von Datensätzen, das Aktualisieren von Informationen oder das Durchführen von Abfragen. OLTP-Systeme sind darauf optimiert, schnelle und effiziente Einzeltransaktionen zu unterstützen und bieten eine hohe Datensicherheit.

### OLAP (Online Analytical Processing)

OLAP steht für "Online Analytical Processing" und bezieht sich auf Systeme, die auf die Analyse großer Mengen von Daten ausgerichtet sind. Diese Systeme ermöglichen komplexe Abfragen und Auswertungen, um geschäftliche Entscheidungen zu unterstützen. OLAP-Systeme organisieren Daten in mehrdimensionalen Modellen, um es Benutzern zu ermöglichen, Daten aus verschiedenen Perspektiven zu betrachten. Im Gegensatz zu OLTP-Systemen liegt der Schwerpunkt bei OLAP auf aggregierten und historischen Daten.

## Unterschiede zwischen OLTP und OLAP

| Merkmal          | OLTP                                            | OLAP                                           |
| ---------------- | ----------------------------------------------- | ---------------------------------------------- |
| Hauptziel        | Verarbeitung von Einzeltransaktionen            | Analyse großer Datenmengen                     |
| Art der Abfragen | Einfache Abfragen auf Einzeldatensätzen         | Komplexe Abfragen und Analyse von Aggregaten   |
| Datenmodell      | Normalisierte Datenmodelle                      | Denormalisierte oder stark strukturierte Daten |
| Antwortzeit      | Niedrige Antwortzeit für einzelne Transaktionen | Akzeptable Antwortzeit für komplexe Abfragen   |
| Datenvolumen     | Geringes bis mittleres Datenvolumen             | Großes Datenvolumen                            |
| Datenaktualität  | Echtzeitaktualität der Daten                    | Aktualität kann etwas verzögert sein           |
| Benutzer         | Alltägliche Benutzer (Clerks, Kunden)           | Entscheidungsträger und Analysten              |
| Beispiele        | Point-of-Sale-System, Buchungssysteme           | Business Intelligence-Systeme, Data Warehouses |

## Schlüssel-Wert-Datenbanken:

Das Schlüssel-Wert-Datenbankmodell gleicht einer Datenbank bestehend aus Dictionaries bzw. Einträgen im JSON format. Jeder Eintrag besteht aus einem eindeutigen Schlüssel, der einem bestimmten Wert zugeordnet ist. Dies eignet sich gut für Anwendungsfälle wie Caching und einfache Datenzugriffe. Schlüssel-Wert-Datenbanken sind in der Regel sehr schnell und skalierbar, aber sie bieten nur begrenzte Abfragemöglichkeiten.

Beispiele für bekannte Schlüssel-Wert-Datenbanken sind Redis, DynamoDB und Riak.

## Unterschiede zu SQL-Datenbanken

Neben dem bereits Angesprochenen Unterschied des fehlenden Schemas und den vielfältigen Strukturen gibt es noch weitere Unterschiede zwischen NoSQL- und SQL-Datenbanken. Diese sind im folgenden aufgeführt und erklärt:

### Skalierbarkeit

NoSQL Datenbanken lassen sich in der Regel leichter horizontal skalieren als SQL Datenbanken. Dies liegt daran, dass NoSQL Datenbanken meistens auf die Primary-Secondary-Architektur setzen. Die Primary-Secondary-Architektur ist eine Datenbankarchitektur, die darauf abzielt, Redundanz und hohe Verfügbarkeit zu gewährleisten. In dieser Architektur gibt es eine primäre (Primary) Datenbankinstanz und mehrere sekundäre (Secondary) Datenbankinstanzen. Die primäre Instanz ist die Hauptdatenbank, die für Lese- und Schreibzugriffe verantwortlich ist. Die sekundären Instanzen replizieren Daten von der primären Instanz, um eine Kopie der Datenbank bereitzustellen. Dadurch kann die Last auf mehrere Server verteilt werden. Wenn die primäre Instanz ausfällt, kann eine der sekundären Instanzen zur primären Instanz werden, um die Verfügbarkeit zu gewährleisten.

Bei SQL Datenbaken ist diese horizontale Skalierung aufgrund der bestehenden Relationen nicht so einfach möglich. Es gibt zwar verschiedene Ansätze, wie SQL Datenbanken horizontal skaliert werden können, jedoch gehen diese häufig mit einer höheren Komplexität und einer geringeren Performance einher. Daher werden SQL Datenbanken in der Regel eher vertikal skaliert. Dies bedeutet, dass die Hardware, auf der die Datenbank läuft, aufgerüstet wird um die Leistungsfähigkeit zu erhöhen. Dies ist in Cloud Umgebungen wie AWS oder Azure einfach möglich, geht jedoch tendenziell mit höheren Kosten, als bei eine horziontalen Skalierung von NoSQL Datenbanken einher.

### ACID Eigenschaften

Im Gegensatz zu SQL Datenbaken müssen NoSQL Datenbanken nicht unbedingt die ACID Eigenschaften (Atomicity, Consistency, Isolation, Durability) erfüllen. Hier noch einmal die ACID Eigenschaften zur Erinnerung:

- Atomicity (Atomarität): Eine Transaktion wird entweder vollständig ausgeführt oder gar nicht. Es gibt keine Zwischenzustände.
- Consistency (Konsistenz): Die Datenbank befindet sich immer in einem konsistenten Zustand. Dies bedeutet, dass die Datenbank nach einer Transaktion in einen gültigen Zustand übergeht.
- Isolation (Isolation): Transaktionen werden unabhängig voneinander ausgeführt. Dies bedeutet, dass eine Transaktion nicht von einer anderen Transaktion beeinflusst werden kann.
- Durability (Dauerhaftigkeit): Nachdem eine Transaktion abgeschlossen wurde, bleiben die Daten dauerhaft in der Datenbank gespeichert.

Es gibt auch NoSQL Datenbanken, die diese Eigenschaften erfüllen. Beispiele hierfür sind MongoDB und Couchbase. Andere NoSQL Datenbanken, wie zum Beispiel Redis, verzichten auf die ACID Eigenschaften, um eine höhere Performance zu erreichen. Letztendlich sollte vor der Verwendung einer NoSQL Datenbank geprüft werden, ob die ACID Eigenschaften für die Anwendung relevant sind oder nicht und ob die Datenbank diese Eigenschaften erfüllt.
