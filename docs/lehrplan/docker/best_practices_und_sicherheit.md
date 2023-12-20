# Best Practices und Sicherheit in Docker

In diesem Kapitel konzentrieren wir uns auf Best Practices und Sicherheitsaspekte beim Umgang mit Docker. Diese
Richtlinien sind entscheidend, um die Integrität und Sicherheit Ihrer Docker-Container und -Images zu gewährleisten und
gleichzeitig eine effiziente und wartbare Umgebung zu schaffen.

## Best Practices in Docker

1. **Verwendung Offizieller Images:**
    - Bevorzugen Sie offizielle Docker-Images oder solche von vertrauenswürdigen Quellen, um Sicherheitsrisiken zu
      minimieren.

2. **Minimale Images:**
    - Verwenden Sie minimale Basis-Images wie Alpine **TODO: alpine?**, um die Angriffsfläche zu reduzieren. Je weniger
      im Image enthalten
      ist, desto geringer ist das Risiko.

3. **Image-Größe Reduzieren:**
    - Entfernen Sie unnötige Dateien und Abhängigkeiten, um die Image-Größe zu reduzieren. Dies verbessert die Startzeit
      und Effizienz.

4. **Effizientes Layering:**
    - Organisieren Sie Anweisungen im Dockerfile effizient, um die Anzahl der Schichten zu reduzieren und Caching zu
      optimieren.

5. **Dockerfile Sicherheit:**
    - Vermeiden Sie das Einbetten sensibler Daten wie Passwörter im Dockerfile. Nutzen Sie stattdessen
      Umgebungsvariablen oder Secrets.

## Sicherheitsaspekte in Docker

1. **Container Isolation:**
    - Stellen Sie sicher, dass Container voneinander isoliert sind und nur auf benötigte Ressourcen Zugriff haben.

2. **Netzwerksicherheit:**
    - Konfigurieren Sie Netzwerke sorgfältig, um unerwünschten Datenverkehr zu verhindern. Verwenden Sie Firewall-Regeln
      und Netzwerksegmentierung.

3. **Volume- und Datenmanagement:**
    - Verwenden Sie Volumes für persistente Daten und achten Sie darauf, dass sensible Daten sicher gespeichert werden.

4. **Regelmäßige Updates:**
    - Halten Sie Ihre Docker-Engine und Container-Images aktuell, um von Sicherheitspatches und Updates zu profitieren.

5. **Nicht als Root laufen:**
    - Vermeiden Sie es, Anwendungen innerhalb von Containern als Root-Benutzer auszuführen, um das Risiko von
      Privilegieneskalation zu minimieren.

## Praktisches Beispiel

Um die Sicherheit zu erhöhen, ist es gängige Praxis, Benutzer anzulegen.
Das folgende Dockerfile Beispiel nutzt Linux Befehle, um im Container einen Benutzer anzulegen. Dies sichert den
Container
ab, da der normale und standardmäßig aktive root-Zugang damit geschlossen ist.

`alpine` ist dabei ein einfaches Linux image ohne weiter Funktionalität.

Der `adduser` Befehl ist ein für alpine Linux gültiger Befehl, um Benutzer anzulegen. Das kann von Distribution zu
Distribution anders sein. Hier gilt die Dokumentation des betreffenden Systems.

Der `user` Befehl legt den akzeptierten Benutzer für das System fest.

- **Dockerfile für ein minimales Image:**
  ```Dockerfile
  FROM alpine:3.12
  RUN adduser -S meinapp
  USER meinapp
  COPY . /app
  WORKDIR /app
  CMD ["./meineapp"]
  ```

[//]: # (  TODO: bitte ausführlicher erklären. Erledigt.) 

- **Netzwerksicherheit konfigurieren:**

Ein weiterer Schritt, um die Sicherheit einer Anwendung zu verbessern, ist die Verwendung eines eigenen internen
Netzwerkes. Ein Zugriff von außen ist damit nicht mehr möglich, es sei denn, man veröffentlicht den Port eines
Containers in die Außenwelt mit der `port` Anweisung wie in docker-compose.yml gezeigt. Das funktioniert auch mit einem
eigenen Befehl im dockerfile.

Zunächst ist es so, dass das Ganze nur Sinn macht, wenn mehrere Container in einer Multi-Container Umgebung zusammen
arbeiten sollen. Meist gibt es einen Zugangspunkt zur App (bezeichnet die Gesamtheit aller Container in einer
docker-compose.yml Datei). Oft macht das nginx, ein reverse proxy. Er nimmt die Anfragen an die App entgegen und
verteilt sie auf die Container.

Standardmäßig baut docker compose ein eigenes Netzwerk auf, ohne weitere Konfiguration. Man kann aber auch Netzwerke
explizit erstellen und so die Zusammenarbeit klarer definieren.

  ```bash
  docker network create --driver bridge isoliertes_netzwerk
  docker run --network=isoliertes_netzwerk meineapp
  ```

Auf diese Weise läuft der Container in einem ganz bestimmten Netzwerk und ist nur darüber erreichbar.

[//]: # (TODO: verstehe ich nicht. Erledigt.) 

## Zusammenfassung

Die Einhaltung von Best Practices und die Berücksichtigung von Sicherheitsaspekten sind unerlässlich, um Docker effektiv
und sicher zu nutzen. Durch die Implementierung dieser Richtlinien können Sie die Sicherheit Ihrer Container-Umgebungen
erhöhen und gleichzeitig eine effiziente und wartbare Plattform für Ihre Anwendungen schaffen.