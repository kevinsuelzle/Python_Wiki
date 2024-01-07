# Projekt Arbeitszeiterfassung

Das Projekt besteht aus einem Pyton Programm, einem nginx Webserver und einer MS SQL Server Datenbank.

Die Absicht ist es, über Postman geeignete REST Anfragen an das Projekt zu senden.

Im Anschluss daran können die übertragenen Daten per REST Anfrage abgerufen werden.

### **Aufgabe: Projekt 🌶️🌶️🌶️**

Projektbeschreibung:

Das Projekt

- soll ein JSON Objekt über einen HTTP Request entgegennehmen
- die Daten in einer SQL Server Datenbank ablegen
- die vollständige Liste der vorhandenen Datensätze in Form von JSON Objekten zurückgeben

Wir benötigen dazu:

- einen Empfänger, der die Anfragen annimmt. Dazu verwenden wir nginx.
- eine Software, die die Daten verarbeitet und an die Datenbank sendet. Dazu gibt es ein node.js Backend Programm.
- eine Software, die die Datenbank abfragt und die Daten zurückschickt. Das gleiche Programm.
- die Datenbank selbst. Wir verwenden SQL Server von Microsoft.

Dargestellt wird das mit Containern, die auf folgenden Images basieren:

- nginx:latest (der Webserver)
- node:current-alpine (ein oft verwendetes stabiles linux) darauf basiert unser Python Programm
- mcr.microsoft.com/mssql/server:2019-latest (die Datenbank)

Konfiguration:

- nginx.conf

    ```nginx
    events {}
    
    http {
        server {
          listen 80;
    
          location / {
             proxy_pass http://localhost:3000;
             proxy_http_version 1.1;
             proxy_set_header Upgrade $http_upgrade;
             proxy_set_header Host $host;
             proxy_set_header content-type "application/json";
             proxy_cache_bypass $http_upgrade;
             proxy_set_header Connection 'upgrade';
         }
        }
    }
    ```

  **Anmerkung:**

  Wir gehen hier nicht auf alle Punkte der nginx.conf ein. Wichtig zu sehen ist, dass dieser Webserver Anfragen an den
  internen Port 3000 weiterleitet (proxy_pass ...) und Anfragen am internen Port 80 (listen 80) entgegennimmt.

- dockerfile

    ```dockerfile
    FROM node:current-alpine
    LABEL authors="joachimwalther"
    
    WORKDIR /app
    
    COPY package*.json ./
    RUN npm ci
    COPY . .
    
    EXPOSE 3000
    CMD ["node", "app.js"]
    ```

  **Anmerkung:**

  Das Dockerfile sagt aus,
    - dass das Basisimage `node` ist in der Version `:current-alpine`.
    - dass das Arbeitsverzeichnis /app ist.
    - dass die Dateien `package*.json` in das `./` Verzeichnis kopiert werden.
    - dass zur Initialisierung der **N**ode **P**ackage **M**anager (npm) mit create and install (ci) Option aufgerufen
      werden soll.
    - dass alle Dateien des Projekts (erster . ) in das Image Basisverzeichnis (zweiter . ) kopiert werden.
    - dass das Programm auf Port 3000 hören soll
    - dass das Programm mit der Anweisung `node` und der Option `app.js` gestartet wird.

- docker-compose.yaml

```yaml
version: '3'
services:
  nginx:
    image: nginx:latest
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    ports:
      - "80:80"

  sql-server:
    image: mcr.microsoft.com/mssql/server:2019-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=Sql12345
    ports:
      - "1433:1433"
    volumes:
      - ./mydatabase:/var/opt/mssql

  node-app:
    build:
      context: .
      dockerfile: Dockerfile
    network_mode: service:nginx
    depends_on:
      - sql-server
```

**Anmerkung:**

Diese YAML-Datei definiert drei Services:

- nginx: der Webserver mit dem Volume nginx.conf und dem Port Mapping 80:80.
  So kann die Konfiguration gelesen werden und Anfragen an den Port 80 werden registriert und weiter verarbeitet wie in
  der Konfigurationsdatei beschrieben.
- sql-server: der SQL Server von Microsoft wird in der aktuellen Version 2019 geladen, seine Lizenzbestimmungen werden
  akzeptiert und das Passwort für den allgemeinen Nutzer `sa`wird festgelegt. Der Port 1433 wird intern verwendet und
  nach außen hin freigegeben. So können wir von anderen Anwendungen auf dem lokalen Rechner auf die Datenbank zugreifen.
- node-app: ein Container, der nach Vorschriften des Dockerfile zu bauen ist und der auf den Webserver hören soll. Zudem
  ist er abhängig von der Datenbank.

