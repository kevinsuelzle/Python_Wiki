# Migrationsstrategien
[60 min]

Die Migration von Datenbankenversionen beschreibt den Prozess des Aktualisieren der Datenbankstruktur. Sie wird insbesondere beim Refactoring von Datenbanken notwendig, um den Verlust von Daten und unerwartete Fehler zu vermeiden. Dabei sind verschiedene Techniken und Ansätze verfügbar, um einen reibungslosen Übergang von einer Datenbankversion zur nächsten zu gewährleisten.

Die Auswahl der geeigneten Migrationsstrategie hängt von verschiedenen Faktoren ab, darunter die Größe der Datenbank, die Komplexität der Datenstrukturen, die Performance-Anforderungen und die gewünschten Verbesserungen. In diesem Kontext werden wir einige gängige Ansätze für die Migration und das Refactoring von MongoDB-Datenbanken erkunden, um ein tieferes Verständnis für die verschiedenen Techniken zu gewinnen, die in der Datenbankentwicklung eingesetzt werden können.


## Grundätzliches

Bei der Durchführung von Migrations- und Refactoring-Aktivitäten in MongoDB-Datenbanken sind einige grundlegende Prinzipien zu berücksichtigen, um einen reibungslosen Prozess zu gewährleisten. Diese haben noch keine konkrete technische Umsetzung, sondern dienen als Leitfaden für die Planung und Durchführung von Migrationsstrategien.

**Kommunikation:**
Informiere das Entwicklungsteam, das Betriebsteam und andere relevante Stakeholder über den Migrationsplan. Dies schließt die Bekanntgabe möglicher Ausfallzeiten ein. Transparente Kommunikation über den Fortschritt und etwaige Probleme trägt dazu bei, Vertrauen zu schaffen und ermöglicht es den Teams, angemessen zu reagieren.

**Rollback-Plan:**
Es ist ratsam, einen Rollback-Plan zu entwickeln, der im Falle unerwarteter Probleme oder Fehlschläge während des Migrationsprozesses aktiviert werden kann. Dieser Plan sollte sicherstellen, dass keine Datenverluste auftreten und die Datenbank wieder in einen stabilen Zustand versetzt wird, falls ein Rollback erforderlich ist.

**Dokumentation:**
Die Dokumentation des Migrationsprozess hilft den Entwicklern bei dem Verständnis und als Referenz für zukünftige Entwickler und Administratoren. Dokumentiere nicht nur den Migrationsprozess selbst, sondern auch jegliche Änderungen am Datenmodell und die Bewältigung eventueller Herausforderungen. Dies fördert eine nachhaltige Wartbarkeit und Weiterentwicklung der Datenbankstruktur. Dieser Punkt wird leider häufig unterschätzt und vernachlässigt.

## Technische Umsetzung

Die technische Umsetzung von Migrationsstrategien kann auf verschiedene Weise erfolgen. Im Folgenden werden einige gängige Ansätze für die Migration von MongoDB-Datenbanken vorgestellt.

**Schrittweise Migration:**
Die schrittweise Migration beinhaltet die schrittweise Einführung von Änderungen im Datenmodell. Jede Phase wird sorgfältig validiert, bevor die nächste in Angriff genommen wird. Dieser Ansatz minimiert das Risiko von Ausfallzeiten und ermöglicht eine umfassende Überprüfung und Validierung in jedem Entwicklungsstadium.

**Parallelbetrieb:**
Die Implementierung einer neuen Datenbankversion parallel zur bestehenden ermöglicht einen nahtlosen Übergang. Durch die schrittweise Umleitung von Anfragen und Aktualisierungen zur neuen Datenbank wird ein stufenweiser Übergang gewährleistet. Dies minimiert Störungen und sorgt für eine reibungslose Transition zwischen den Datenbankversionen.

**Datenmigrationsskripte:**
Datenmigrationsskripte sind essenziell, um Daten von der alten Struktur in die neue zu überführen. Diese Skripte sollten Aspekte wie Datenbereinigung, Datentyp-Umwandlung und Anpassungen an das neue Datenmodell berücksichtigen. Ein sorgfältig entwickeltes Skript gewährleistet die Integrität der Daten während des Migrationsprozesses.

**Versionierung von Dokumenten:**
Die Hinzufügung von Versionsinformationen zu Dokumenten ermöglicht die Bewältigung unterschiedlicher Datenmodellversionen. Durch die Implementierung von Logik, die basierend auf der Version unterschiedliche Codepfade verwendet, können Anwendungen mit verschiedenen Datenstrukturen interoperabel arbeiten.

**Feature-Schalter:**
Die Integration von Feature-Schaltern erlaubt die Aktivierung oder Deaktivierung von Funktionen basierend auf der Datenbankversion. Dies ermöglicht eine graduelle Einführung neuer Funktionen, während ältere Datenmodelle weiterhin unterstützt werden.

**Testumgebung:**
Die Einrichtung einer dedizierten Testumgebung ist unerlässlich. Hier können Änderungen vor der Implementierung in der Produktionsumgebung ausgiebig getestet werden. Die Verwendung von Mock-Daten oder Duplikaten der Produktionsdaten ermöglicht realistische Tests und trägt dazu bei, potenzielle Probleme im Voraus zu identifizieren.



### Aufgabe:
[60 min]

Erstelle eine MongoDB-Datenbank mit PyMongo und Migration in zwei Umgebungen**

**Teil 1: Datenbankerstellung und Testumgebung**

1. **Datenbankerstellung mit PyMongo:**
   - Schreibe ein Python-Skript, das eine MongoDB-Datenbank mit PyMongo erstellt.
   - Definiere eine Sammlung (Collection) namens "users".
   - Füge einige Testdatensätze in die "users"-Sammlung ein.

2. **Docker-Container für Testumgebung:**
   - Erstelle einen Docker-Container für die MongoDB-Testumgebung.
   - Konfiguriere die Containerumgebung für den Zugriff auf die erstellte Datenbank und Sammlung.
   - Starte den Container und überprüfe, ob die Testdaten korrekt eingefügt wurden.

**Teil 2: Datenbankmigration und Produktionsumgebung**

3. **Datenbankmigrationsskript:**
   - Entwickle ein Python-Skript für die Migration der Datenbank. Beispiel: Ändere den Datentyp eines Feldes oder füge ein neues Feld hinzu.
   - Berücksichtige Fehlererkennung und Protokollierung im Skript.

4. **Docker-Container für Produktionsumgebung:**
   - Erstelle einen separaten Docker-Container für die MongoDB-Produktionsumgebung.
   - Konfiguriere die Containerumgebung, um auf die produktive Datenbank zuzugreifen.
   - Starte den Produktionscontainer und überprüfe, ob das Migrationsskript erfolgreich angewendet wurde.

5. **Rollback-Plan:**
   - Entwickle einen klaren Rollback-Plan für den Fall von Problemen während der Migration.
   - Simuliere einen Rollback in der Testumgebung und überprüfe, ob alle Schritte korrekt durchgeführt werden.

6. **Kommunikation und Dokumentation:**
   - Implementiere eine Funktion, um den Fortschritt und mögliche Fehler während der Migration zu protokollieren.
   - Dokumentiere den gesamten Prozess, einschließlich der Skriptänderungen und der Docker-Konfiguration.



### Lösungsskizze:

**Teil 1: Datenbankerstellung und Testumgebung**

```python
from pymongo import MongoClient

# Datenbankerstellung mit PyMongo
def create_database():
    client = MongoClient('localhost', 27017)
    db = client['example_database']
    collection = db['users']

    test_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22}
    ]

    collection.insert_many(test_data)
    client.close()

create_database()
```

Für den Docker-Container können wir eine `docker-compose.test.yml`-Datei erstellen:


```yaml
version: '3'
services:
mongodb:
   image: mongo
   container_name: mongodb-test
   ports:
      - "27017:27017"
   environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
   volumes:
      - ./data:/data/db
```

Dann führen wir den Container mit dem Befehl `docker-compose -f docker-compose.test.yml up` aus.

**Teil 2: Datenbankmigration und Produktionsumgebung**

```python
from pymongo import MongoClient

# Datenbankmigrationsskript
def perform_migration():
    client = MongoClient('localhost', 27017)
    db = client['example_database']
    collection = db['users']

    # Beispiel-Migration: Ändere den Datentyp des "age"-Feldes von int zu str
    documents_to_update = collection.find({"age": {"$type": "int"}})

    for document in documents_to_update:
        new_age = str(document["age"])
        collection.update_one({"_id": document["_id"]}, {"$set": {"age": new_age}})

    client.close()

perform_migration()
```

Für den Docker-Container können wir eine `docker-compose.prod.yml`-Datei erstellen:


```yaml
version: '3'
services:
mongodb:
   image: mongo
   container_name: mongodb-prod
   ports:
      - "27017:27017"
   environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
   volumes:
      - ./data:/data/db
```

Dann führen wir den Container mit dem Befehl `docker-compose -f docker-compose.prod.yml up` aus.

**Rollback-Plan:**

Wir könnten vor Ausrollen des Migrations-Skripts ein Backup der Datenbank erstellen. Wenn das Skript fehlschlägt, können wir die Datenbank wiederherstellen und den Container neu starten.

```bash
mongodump --db your_database_name --out /path/to/backup/folder
```

Das Wiederherstellen des Backups bei fehlgeschlagener Migration kann mit dem folgenden Befehl erfolgen:

```bash
mongodump --db your_database_name --out /path/to/backup/folder
```

**Kommunikation und Dokumentation:**

Für das Logging können wir beispielweise das Logging von MongoDB verwenden. Mehr dazu finden wir in dem vorherigen Abschnitt zu Sicherheitsmechanismen für MongoDB.

```yaml
# Konfigurationsdatei (mongod.conf)
auditLog:
  destination: file
  path: /var/log/mongodb/audit.log
```

