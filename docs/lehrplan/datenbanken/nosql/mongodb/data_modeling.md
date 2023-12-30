## Data Modeling und Design Patterns


## Schema Design Patterns

In MongoDB bezieht sich der Begriff "Schema Design Patterns" auf bewährte Methoden und Ansätze für das Entwerfen von Dokumentstrukturen in einer MongoDB-Datenbank. Anders als in traditionellen relationalen Datenbanken gibt es in MongoDB kein festes Schema, und die Daten werden in der Regel in BSON-Dokumenten (Binary JSON) gespeichert. Schema Design Patterns bieten Richtlinien und bewährte Praktiken für die Strukturierung von MongoDB-Dokumenten, um die Leistung, Skalierbarkeit und Flexibilität der Datenbank zu optimieren. Im Folgenden sind einige der wichtigsten Schema Design Patterns aufgeführt:



3. **Präkalkulierte Muster (Precomputed Patterns):**
    - **Berechnungen im Voraus:** Speicherung vorberechneter Daten im Dokument zur Vermeidung häufiger Berechnungen.

4. **Baumstrukturen (Tree Structures):**
    - **Materialisierte Pfade:** Anwendung materialisierter Pfade zur Abbildung von Baumstrukturen.
    - **Elternreferenzen:** Jeder Knoten enthält eine Referenz auf seinen Elternknoten.

5. **Polymorphe Muster (Polymorphic Patterns):**
    - **Verwendung von Schlüsseln zur Typisierung:** Einsatz spezieller Schlüssel zur Angabe des Dokumenttyps.

6. **Caching Patterns:**
    - **Caching wiederholter Daten:** Speicherung wiederholter Daten in Dokumenten zur Minimierung von wiederholten Abfragen.

7. **Zeitreihenmuster (Time Series Patterns):**
    - **Rollende Sammlungen:** Erstellung rollender Sammlungen für Zeitreihendaten zur Speicherung über einen bestimmten Zeitraum.

8. **Bucket Patterns:**
    - **Bucketing von Daten:** Gruppierung von Daten in Buckets zur Effizienzsteigerung von Abfragen und Analysen.

9. **Outlier Patterns:**
    - **Auslagerung von Ausreißern:** Auslagerung von Ausreißern in separate Dokumente zur Vermeidung von Leistungseinbußen.

## Data Modeling Patterns

Data Modeling Patterns beziehen sich auf bewährte Methoden für das Modellieren von Daten in MongoDB, das die Strukturierung von Dokumenten und die Beziehungen zwischen Dokumenten umfasst. Hier sind einige wichtige Data Modeling Patterns:

1. **Einbettung von Datenmodellen:**
    - **Mehrfache Einbettung (Nested Documents):** Einbetten von Dokumenten in andere ermöglicht die Zusammenfassung mehrerer Informationen in einem einzigen Dokument.
    - **Arrays:** Die Verwendung von Arrays gestattet die Speicherung mehrerer Werte oder Dokumente für ein bestimmtes Feld.

2. **Verweise (References):**
    - **Manuelle Verweise:** Nutzung von manuellen Verweisen durch Verlinken mit Dokumenten in anderen Sammlungen.
    - **DBRefs (Database References):** MongoDB unterstützt DBRefs als spezielle Struktur für Verweise.

### Aufgabe:
Teilt euch in Gruppen auf und bearbeitet jeweils ein Schema Design Pattern. Erstellt eine Präsentation inklusive Live-coding, in der ihr das Schema Design Pattern vorstellt und anhand eines Beispiels erklärt. Die Präsentation sollte einen Umfang von ca. 5 - 10 Minuten haben.


