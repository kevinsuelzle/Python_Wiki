# Dockerfile und Docker Compose

In diesem Kapitel werden wir uns mit Dockerfile und Docker Compose befassen, zwei zentralen Werkzeugen in der
Docker-Technologie, die für die Automatisierung des Docker-Image-Build-Prozesses und das Management von
Multi-Container-Anwendungen unerlässlich sind.

## Dockerfile: Erstellen von Docker-Images

### 1. **Grundlagen eines Dockerfiles:**

- Ein Dockerfile ist eine Textdatei mit einer Reihe von Anweisungen, die beschreiben, wie ein Docker-Image aufgebaut
  wird.
- Jede Anweisung im Dockerfile fügt eine neue Schicht zum Docker-Image hinzu.

### 2. **Beispiel eines Dockerfiles**

```Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### 3. **Erklärungen der Dockerfile-Anweisungen**

1. **`FROM python:3.8-slim`**:
    - Dies ist die erste Anweisung im Dockerfile und legt das Basis-Image fest.
    - Hier wird das offizielle Python-Image in der Version 3.8 verwendet, das auf einer schlanken Version von Debian
      basiert (`slim`).
    - Dieses Basis-Image enthält bereits Python und alle notwendigen Abhängigkeiten, um Python-Anwendungen auszuführen.

2. **`WORKDIR /app`**:
    - Diese Anweisung setzt das Arbeitsverzeichnis im Container.
    - Wenn dieses Verzeichnis im Basis-Image nicht existiert, wird es erstellt.
    - Nachfolgende Anweisungen wie `COPY` und `RUN` werden relativ zu diesem Verzeichnis ausgeführt.

3. **`COPY . /app`**:
    - Kopiert Dateien und Verzeichnisse aus dem Kontextverzeichnis (in diesem Fall das Verzeichnis, in dem das
      Dockerfile liegt) in das Image.
    - Hier werden alle Dateien und Verzeichnisse aus dem aktuellen Verzeichnis des Hosts in das `/app` Verzeichnis im
      Container kopiert.

4. **`RUN pip install -r requirements.txt`**:
    - Führt Befehle aus, um das Image zu bauen.
    - In diesem Fall wird `pip`, der Paketmanager für Python, verwendet, um alle Abhängigkeiten zu installieren, die in
      der `requirements.txt`-Datei aufgelistet sind.

5. **`CMD ["python", "app.py"]`**:
    - Definiert den Standardbefehl, der ausgeführt wird, wenn ein Container aus dem Image gestartet wird.
    - Hier wird die Python-Anwendung gestartet, indem `app.py` mit dem Python-Interpreter ausgeführt wird.
    - Dieser Befehl kann beim Starten des Containers überschrieben werden.

Der einfache Punkt (`.`) in Dockerfiles und Docker-Befehlen hat eine spezifische Bedeutung:

1. **Im `COPY` Befehl**:
    - Im Dockerfile, speziell im `COPY` Befehl, bezieht sich der Punkt auf das Kontextverzeichnis.
    - Der Befehl `COPY . /app` bedeutet, dass alle Dateien und Verzeichnisse aus dem Kontextverzeichnis (in der Regel
      das Verzeichnis, in dem das Dockerfile liegt) in das Verzeichnis `/app` im Docker-Image kopiert werden.

2. **Im `docker build` Befehl**:
    - Wenn Sie ein Docker-Image bauen, verwenden Sie den Befehl `docker build`. Der Punkt am Ende dieses Befehls gibt
      das Kontextverzeichnis für den Build-Prozess an.
    - Zum Beispiel, `docker build -t mein_python_app:latest .` bedeutet, dass Docker das aktuelle Verzeichnis (angezeigt
      durch `.`) als Kontext für den Build-Prozess verwenden soll.
    - Der Kontext ist wichtig, da er alle Dateien und Verzeichnisse enthält, die für den Build-Prozess zugänglich sein
      müssen, einschließlich des Dockerfiles und aller Dateien, die durch `COPY` oder `ADD` Befehle ins Image übertragen
      werden.

In beiden Fällen ist der Punkt eine Kurzform, um das aktuelle Verzeichnis zu bezeichnen. Es ist eine gängige Praxis in
Unix- und Linux-basierten Systemen, den aktuellen Ordner mit einem Punkt zu referenzieren.

### 4. **Erstellung des Images**

Das Image, das durch dieses Dockerfile erstellt wird, hat standardmäßig **keinen** spezifischen Namen. Um dem Image
einen Namen zu geben, müssen Sie den `docker build` Befehl mit dem `-t` Flag verwenden, gefolgt von dem gewünschten
Namen und Tag. Zum Beispiel:

```bash
docker build -t meine_python_app:latest .
```

Durch diese Anweisungen wird ein Docker-Image erstellt, das eine lauffähige Umgebung für Ihre Python-Anwendung
bereitstellt.

Hierbei ist `meine_python_app` der Name des Images und `latest` ist der Tag, der die Version des Images angibt. Ohne
das `-t` Flag würde das Image nur eine generierte ID erhalten und keinen benutzerfreundlichen Namen.

## Docker Compose: Management von Multi-Container-Anwendungen

### 1. **Einführung in Docker Compose:**

- Docker Compose ist ein Tool zur Definition und Ausführung von Multi-Container Docker-Anwendungen.
- Mit einer YAML-Datei können Sie Dienste, Netzwerke und Volumes definieren.

### 2. **Docker-Compose-Datei:**

- Die `docker-compose.yml`-Datei ist das Herzstück von Docker Compose und beschreibt, wie Ihre Anwendung in Docker
  ausgeführt wird.

### 3. **Beispiel einer `docker-compose.yml`-Datei:**

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

  meine_python_app:
    build:
      context: .
      dockerfile: Dockerfile
    network_mode: service:nginx
    depends_on:
      - sql-server
```

Dieses `docker-compose` Beispiel ist ein gutes Szenario, um die Funktionsweise von Docker Compose
zu demonstrieren. Docker Compose wird verwendet, um mehrere Docker-Container zu definieren und zu betreiben, die
zusammenarbeiten. Hier ist eine detaillierte Erläuterung Ihres Beispiels:

### 4. **Struktur des `docker-compose.yml`-Files**

1. **Version**:
    - `version: '3'` gibt die Version der Docker Compose-Datei an. Version 3 ist eine der neuesten Versionen und bietet
      Unterstützung für Docker Swarm.

2. **Services**:
    - Unter `services` werden die verschiedenen Container definiert, die Teil Ihrer Anwendung sind.

### 5. **Definition der einzelnen Services**

1. **nginx**:
    - `nginx` ist der Name des Services.
    - `image: nginx:latest` gibt an, dass der Service das neueste offizielle nginx-Image von Docker Hub verwendet.
    - `volumes: - ./nginx.conf:/etc/nginx/nginx.conf:ro` bindet die lokale `nginx.conf`-Datei in den Container ein.
      Das `:ro` bedeutet, dass das Volume im "read-only"-Modus gemountet wird.
    - `ports: - "80:80"` leitet den Port 80 des Hosts auf den Port 80 des nginx-Containers um, was bedeutet, dass nginx
      auf dem Standard-HTTP-Port erreichbar ist.

2. **sql-server**:
    - `sql-server` ist der Name dieses Services.
    - `image: mcr.microsoft.com/mssql/server:2019-latest` verwendet das neueste SQL Server 2019-Image von Microsoft.
    - `environment:` definiert Umgebungsvariablen im Container:
        - `ACCEPT_EULA=Y` akzeptiert die Endbenutzer-Lizenzvereinbarung.
        - `SA_PASSWORD=Sql12345` setzt das Passwort für den SQL Server.
    - `ports: - "1433:1433"` leitet den SQL Server-Port 1433 des Hosts auf den Port 1433 des Containers um.
    - `volumes: - ./mydatabase:/var/opt/mssql` bindet das lokale Verzeichnis `mydatabase` in den Container ein, um Daten
      dauerhaft zu speichern.

3. **meine_python_app**:
    - `meine_python_app` ist der Name dieses Services.
    - `build:` gibt an, dass das Image aus einem Dockerfile gebaut werden soll. Das startet den o.a. build Prozess.
        - `context: .` setzt den Kontext für den Build auf das aktuelle Verzeichnis.
        - `dockerfile: Dockerfile` gibt an, welches Dockerfile für den Build verwendet werden soll.
    - `network_mode: service:nginx` bedeutet, dass der `node-app`-Service das gleiche Netzwerk wie der `nginx`-Service
      verwendet.
    - `depends_on: - sql-server` stellt sicher, dass der `sql-server`-Service gestartet wird, bevor der `node-app`
      -Service gestartet wird.

Dieses `docker-compose.yml`-File definiert eine Multi-Container-Anwendung mit drei Services: einem nginx-Webserver,
einem SQL Server und einer eigenen Anwendung. Die Konfiguration sorgt dafür, dass die Services miteinander kommunizieren
können, wobei nginx als Webserver, SQL Server als Datenbank und die Anwendung als Backend fungieren. Durch die
Verwendung von Docker Compose können diese Services einfach und konsistent gestartet, gestoppt und verwaltet werden.

**Hinweis:** Die Kommunikation zwischen den Containern läuft über Netzwerke. Dafür werden von den einzelnen Conatinern
Ports festgelegt, über die sie erreichbar sind. Die `port` Anweisung ist dafür nicht zuständig! Sie definiert den Port,
über den der Container von außen zugänglich ist. Kurz gesagt: der Container ist ohne `port` Anweisung für die Außenwelt
nicht erreichbar. Innerhalb der Containerumgebung allerdings schon.

### 5. **Verwendung von compose Befehlen**

Im Unterschied zu docker-compose.yml ist `docker compose` als Aufruf in der Kommandozeile ein Programm, dass mit
verschiedenen Parametern die Ausführung der Multi-Container Umgebung steuern kann. Hier einige Befehle dazu:

| Befehl                   | Beschreibung                                                                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker compose up`      | Startet die Container, die in der `docker-compose.yml`-Datei definiert sind. Mit der Option `-d` werden die Container im Hintergrund gestartet. |
| `docker compose down`    | Stoppt und entfernt alle Container, Netzwerke, Volumes und Images, die durch `docker-compose up` erstellt wurden.                               |
| `docker compose build`   | Baut alle Dienste, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                         |
| `docker compose pull`    | Lädt alle Images herunter, die in der `docker-compose.yml`-Datei definiert sind, aber nicht lokal gebaut werden.                                |
| `docker compose restart` | Startet alle Container neu, die in der `docker-compose.yml`-Datei definiert sind.                                                               |
| `docker compose stop`    | Stoppt alle laufenden Container, die durch `docker-compose up` gestartet wurden, ohne sie zu entfernen.                                         |
| `docker compose start`   | Startet alle gestoppten Container, die durch `docker-compose up` erstellt wurden.                                                               |

In unserem Beispiel würde es genügen,

```bash
   docker compose up -d 
```

in der Kommandozeile aufzurufen, um die vollständige Anwendung zu starten. Je nachdem, was im Arbeitsverzeichnis
vorhanden ist oder nicht, würden Container geladen oder gebaut und als Hintergrundprozess gestartet.

Die hier gezeigt App würde den Webserver `nginx`, die `SQL Server` Datenbank und die `meine_python_app`starten. DAmit
Könnten Netzwerkanfragen an den Port 80 angenommen und an die App weitergeleitet werden. Die App hat dann die
Möglichkeit, ihre Daten in der Datenbank zu speichern.

## Zusammenfassung

Dockerfile und Docker Compose sind mächtige Werkzeuge im Docker-Ökosystem. Während Dockerfiles die Grundlage für das
Erstellen von Docker-Images bilden, ermöglicht Docker Compose das einfache Management komplexer Anwendungen, die aus
mehreren Containern bestehen. Durch die Kombination dieser Werkzeuge können Sie effiziente, reproduzierbare und
skalierbare Anwendungsumgebungen erstellen.
