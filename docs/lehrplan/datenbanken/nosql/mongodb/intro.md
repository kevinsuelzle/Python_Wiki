**MongoDB: Eine Einführung**

MongoDB ist eine dokumentenorientierte NoSQL-Datenbank, die auf hohe Flexibilität und Skalierbarkeit ausgelegt ist. Im Gegensatz zu relationalen Datenbanken speichert MongoDB Daten in einem flexiblen, JSON-ähnlichen Format, das als BSON (Binary JSON) bekannt ist. Wie auch andere Dokumentenbasierte Datenbanken ist MongoDB frei von Schemaanforderungen. Insgesamt gelten for MongoDB die 

MongoDB eignet sich besonders gut für Anwendungsfälle mit unstrukturierten oder stark variierenden Daten, darunter Content-Management-Systeme, Echtzeitanwendungen und Big-Data-Anwendungen.


## BSON
BSON (Binary JSON) ist ein Binärformat, das zur Serialisierung von JSON-ähnlichen Dokumenten verwendet wird. Es wurde speziell für die Verwendung mit MongoDB entwickelt und ermöglicht die effiziente Speicherung und Übertragung von Daten in MongoDB-Dokumenten. BSON unterstützt im Gegensatz zu JSON nicht nur Text, sondern auch andere Datentypen wie Datum/Uhrzeit, Binärdaten und reguläre Ausdrücke. Die binäre Repräsentation macht BSON effizienter für die Speicherung und Übertragung von Daten. BSON-Dokumente können auch komprimiert werden, um die Effizienz weiter zu verbessern. Die Verarbeitung der Binärdateien ist sowohl auf Server- als auch auf Clientseite möglich.


## Installation und Hosting

MongoDB kann auf verschiedene Arten bereitgestellt und verwendet werden. Hier sind einige Möglichkeiten, MongoDB-Server zu verwenden:

1. **Lokale Installation:**
   - MongoDB kann direkt auf einem lokalen Rechner installiert und ausgeführt werden. Diese Option ist besonders nützlich, wenn lokal entwickelt wird oder wenn es sich um kleinere Projekte handelt.

2. **Cloud-Dienste:**
   - Mehrere Cloud-Anbieter bieten MongoDB als verwalteten Dienst an. Einige bekannte Optionen sind:
     - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas): Ein Cloud-Dienst von MongoDB, der eine vollständig verwaltete Datenbank in der Cloud bereitstellt.
     - [Amazon DocumentDB](https://aws.amazon.com/documentdb/): Ein von Amazon Web Services (AWS) verwalteter Dienst, der MongoDB-kompatibel ist.
     - [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/): Ein von Microsoft Azure bereitgestellter Dienst, der mehrere Datenbankmodelle unterstützt.

3. **Docker:**
   - MongoDB kann in einem Docker-Container ausgeführt werden. Dies ermöglicht eine flexible Bereitstellung und Skalierung, besonders wenn Docker bereits in der Infrastruktur verwendet wird.

   ```bash
   # Beispiel Docker-Befehl für MongoDB
   docker run --name mein-mongodb -p 27017:27017 -d mongo
   ```

4. **Lokale Entwicklungsumgebungen:**
   - Einige Entwicklungsumgebungen bieten GUIs für die Verbindung zu lokalen oder entfernten MongoDB-Servern. Beispiele sind [MongoDB Compass](https://www.mongodb.com/products/compass) oder [Robo 3T](https://robomongo.org/).

5. **Plattformübergreifende Installationsmanager:**
   - Installationsmanager wie [Homebrew](https://brew.sh/) für macOS oder [Chocolatey](https://chocolatey.org/) für Windows ermöglichen eine einfache Installation von MongoDB.


Wir werden MongoDB zunächst über einen Docker Container ausführen.

### Aufgabe:
Erstelle ein Docker-Compose File, das einen MongoDB Container startet. Achte darauf, dass die Datenbank auch nach einem Neustart des Containers erhalten bleibt.

***Lösung***:
Um MongoDB mit einer eigenen Datenbank über `docker-compose` bereitzustellen, kannst du eine `docker-compose.yml`-Datei erstellen. Hier ist ein einfaches Beispiel:

1. Erstelle eine Datei mit dem Namen `docker-compose.yml` und füge den folgenden Inhalt ein:

   ```yaml
   version: '3'
   services:
     mongodb:
       image: mongo
       container_name: my-mongodb
       ports:
         - "27017:27017"
       environment:
         MONGO_INITDB_ROOT_USERNAME: root
         MONGO_INITDB_ROOT_PASSWORD: example
       volumes:
         - ./data:/data/db
   ```

   Dieses Beispiel verwendet das offizielle MongoDB-Image aus dem Docker Hub (`mongo`). Es definiert einen MongoDB-Container mit dem Namen `my-mongodb`, der auf Port `27017` lauscht. Die Umgebungsvariablen `MONGO_INITDB_ROOT_USERNAME` und `MONGO_INITDB_ROOT_PASSWORD` werden verwendet, um einen Benutzer mit Root-Rechten zu erstellen. Der Container bindet außerdem ein Volumen (`./data:/data/db`), um die Datenbankdaten dauerhaft zu speichern.

2. Erstelle einen Ordner namens `data` im gleichen Verzeichnis wie deine `docker-compose.yml`-Datei. Dieser Ordner wird das Volumen für die MongoDB-Datenbank sein.

3. Öffne ein Terminal im Verzeichnis, das die `docker-compose.yml`-Datei enthält, und führe den folgenden Befehl aus:

   ```bash
   docker-compose up -d
   ```

   Dieser Befehl startet die Docker-Container im Hintergrund (`-d`).

Nachdem dieser Befehl erfolgreich ausgeführt wurde, sollte MongoDB mit einer eigenen Datenbank bereitgestellt sein. Du kannst dies überprüfen, indem du dich zum MongoDB-Server verbindest (z. B. mit einem MongoDB-Client wie [MongoDB Compass](https://www.mongodb.com/products/compass)) und die erstellte Datenbank verwendest. In diesem Beispiel wäre die Datenbank standardmäßig "admin" aufgrund der Umgebungsvariablen, die wir in der `docker-compose.yml`-Datei festgelegt haben.

## MongoDB Shell

Die MongoDB Shell ist in dem Docker Container standardmäßg vorhanden. Möchten wir also aus dem Container heraus mit der Datenbank interagieren, können wir die MongoDB Shell verwenden. Dafür müssen wir uns zunächst mit dem Container verbinden. Dies können wir über den Befehl `docker exec` erreichen.

```bash
docker exec -it mongo mongosh
```

Alternativ können wir auch über Homebrew die MongoDB Shell installieren und uns dann mit der Datenbank verbinden. Die Installation erfolgt durch den Befehlt `brew install mongosh`. Anschließend können wir uns mit der Datenbank verbinden, indem wir den Befehl `mongosh` ausführen und uns mit dem ausgewählen Port verbinden.

```bash
mongosh --port 27017
```


Nach dem Ausführen dieses Befehls sollte die MongoDB-Shell geöffnet werden. Nun könnenw wir über die Konsole mit der Datenbank direkt interagieren.

Über den Befehl `show databases` können wir uns alle bestehenden Datenbanken anzeigen lassen. Um eine neue Datenbank zu erstellen, können wir den Befehl `use <database_name>` verwenden. Zunächst ist diese Datenbank leer und wir daher über `show databases` auch nicht angezeit. Sobald wir jedoch eine Collection in dieser Datenbank erstellen, wird diese auch angezeigt. Collections sind in MongoDB das Äquivalent zu Tabellen in relationalen Datenbanken. Collections können über den Befehl `db.createCollection(<collection_name>)` erstellt werden.Wenn wir nun erneut `show databases` ausführen, sollte unsere neue Datenbank angezeigt werden. Um die aktuelle Datenbank zu wechseln, können wir den Befehl `use <database_name>` erneut verwenden. 

**Hinweis**: Wenn wir keine Collection explizit erstellen, sondern lediglich ein Dokument in eine Collection einfügen, wird diese Collection automatisch erstellt.

Über den Befehl `show collections` können wir uns alle Collections anzeigen lassen, die in der aktuellen Datenbank vorhanden sind. Im nächsten Kapitel werden wir uns ausführlicher mit den CRUD Operationen beschäftigen. Das Schließen der MongoDB Shell erfolgt über den Befehl `exit`.

### Aufgabe:
Erstelle eine Collection mit dem Namen `users` und füge ein Dokument mit dem Namen `John Doe` ein. Lass die alle Collections anzeigen.