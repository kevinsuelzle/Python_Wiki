# Dockerfile und Docker Compose

In diesem Kapitel werden wir uns mit Dockerfile und Docker Compose befassen, zwei zentralen Werkzeugen in der
Docker-Technologie, die für die Automatisierung des Docker-Image-Build-Prozesses und das Management von
Multi-Container-Anwendungen unerlässlich sind.

## Dockerfile: Erstellen von Docker-Images

### 1. **Grundlagen eines Dockerfiles:**

- Ein Dockerfile ist eine Textdatei mit einer Reihe von Anweisungen, die beschreiben, wie ein Docker-Image aufgebaut
  wird.
- Jede Anweisung im Dockerfile fügt eine neue Schicht zum Docker-Image hinzu.

### 2. **Wichtige Anweisungen:**

- `FROM`: Definiert das Basis-Image.
- `RUN`: Führt Befehle aus.
- `COPY`/`ADD`: Kopiert Dateien und Verzeichnisse in das Image.
- `CMD`: Gibt den Standardbefehl an, der beim Starten des Containers ausgeführt wird.
- `EXPOSE`: Gibt an, welche Ports freigegeben werden.
- `ENV`: Setzt Umgebungsvariablen.

### 3. **Beispiel eines Dockerfiles:**

```Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Dieses Dockerfile erstellt ein Image für eine einfache Python-Anwendung.

## Docker Compose: Management von Multi-Container-Anwendungen

### 1. **Einführung in Docker Compose:**

- Docker Compose ist ein Tool zur Definition und Ausführung von Multi-Container Docker-Anwendungen.
- Mit einer YAML-Datei können Sie Dienste, Netzwerke und Volumes definieren.

### 2. **Docker-Compose-Datei:**

- Die `docker-compose.yml`-Datei ist das Herzstück von Docker Compose und beschreibt, wie Ihre Anwendung in Docker
  ausgeführt wird.

### 3. **Wichtige Konzepte:**

- `services`: Definiert die Container, die Teil Ihrer Anwendung sind.
- `networks`: Definiert Netzwerke für die Kommunikation zwischen den Containern.
- `volumes`: Definiert persistente Datenspeicherung für die Container.

### 4. **Beispiel einer `docker-compose.yml`-Datei:**

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

TODO: Könntest du hier bitte alles kurz erklären? Was ist Redis?

Dieses Beispiel definiert eine einfache Anwendung mit einem Webdienst und einem Redis-Cache.

Hier ist eine Tabelle mit den wichtigsten Docker Compose-Befehle und ihren Erklärungen:

TODO: Wo ist der Unterschied zwischen starten und bauen?
TODO: Die Befehle hier gehen weit über das hinaus, was man sich mit Hilfe des Beispiels vorstellen kann.

| Befehl                   | Beschreibung                                                                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker-compose up`      | Startet die Container, die in der `docker-compose.yml`-Datei definiert sind. Mit der Option `-d` werden die Container im Hintergrund gestartet. |
| `docker-compose down`    | Stoppt und entfernt alle Container, Netzwerke, Volumes und Images, die durch `docker-compose up` erstellt wurden.                               |
| `docker-compose build`   | Baut alle Dienste, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                         |
| `docker-compose pull`    | Lädt alle Images herunter, die in der `docker-compose.yml`-Datei definiert sind, aber nicht lokal gebaut werden.                                |
| `docker-compose push`    | Lädt alle Images zu einem Registry-Server hoch, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.            |
| `docker-compose restart` | Startet alle Container neu, die in der `docker-compose.yml`-Datei definiert sind.                                                               |
| `docker-compose stop`    | Stoppt alle laufenden Container, die durch `docker-compose up` gestartet wurden, ohne sie zu entfernen.                                         |
| `docker-compose start`   | Startet alle gestoppten Container, die durch `docker-compose up` erstellt wurden.                                                               |
| `docker-compose logs`    | Zeigt die Log-Ausgaben aller Container an. Mit der Option `-f` können die Logs live verfolgt werden.                                            |
| `docker-compose exec`    | Führt einen Befehl in einem laufenden Container aus. Nützlich für das Debugging oder die Interaktion mit Diensten.                              |
| `docker-compose run`     | Führt einen einmaligen Befehl in einem Dienst aus. Ideal für administrative Aufgaben oder Tests.                                                |

Diese Befehle bilden die Grundlage für die Interaktion mit Docker Compose und ermöglichen es Ihnen, komplexe
Anwendungen, die aus mehreren Containern bestehen, effizient zu verwalten.

## Zusammenfassung

Dockerfile und Docker Compose sind mächtige Werkzeuge in der Docker-Ökosystem. Während Dockerfiles die Grundlage für das
Erstellen von Docker-Images bilden, ermöglicht Docker Compose das einfache Management komplexer Anwendungen, die aus
mehreren Containern bestehen. Durch die Kombination dieser Werkzeuge können Sie effiziente, reproduzierbare und
skalierbare Anwendungsumgebungen erstellen.

TODO: mir fehlt ein größeres Beispiel um zu verstehen, was hier abgehen soll.