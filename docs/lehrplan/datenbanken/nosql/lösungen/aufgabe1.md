# MongoDB mit Docker laden 🌶🌶

Um MongoDB mit einer eigenen Datenbank über `docker-compose` bereitzustellen, kannst du eine `docker-compose.yml`-Datei erstellen. Hier ist ein Beispiel:

- Erstelle eine Datei mit dem Namen `docker-compose.yml` und füge den folgenden Inhalt ein:

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

- Erstelle einen Ordner namens `data` im gleichen Verzeichnis wie deine `docker-compose.yml`-Datei. Dieser Ordner wird das Volumen für die MongoDB-Datenbank sein.

- Öffne ein Terminal im Verzeichnis, das die `docker-compose.yml`-Datei enthält, und führe den folgenden Befehl aus:

```bash
docker-compose up -d
```

Dieser Befehl startet die Docker-Container im Hintergrund (`-d`).

Nachdem dieser Befehl erfolgreich ausgeführt wurde, sollte MongoDB mit einer eigenen Datenbank bereitgestellt sein. Du kannst dies überprüfen, indem du dich zum MongoDB-Server verbindest (z. B. mit einem MongoDB-Client wie [MongoDB Compass](https://www.mongodb.com/products/compass)) und die erstellte Datenbank verwendest. In diesem Beispiel wäre die Datenbank standardmäßig "admin" aufgrund der Umgebungsvariablen, die wir in der `docker-compose.yml`-Datei festgelegt haben.
