# Grundbegriffe von Docker

TODO: Das hier bitte in die drei-spaltige Tabellenform bringen mit Referenzen.

1. **Docker:**  
   Eine Plattform für die Entwicklung, Bereitstellung und Ausführung von Anwendungen in isolierten Umgebungen namens
   Containern.

2. **Container:**  
   Eine leichte, eigenständige, ausführbare Softwarepaketeinheit, die alles enthält, was benötigt wird, um Code
   auszuführen, einschließlich Systemtools, Bibliotheken und Einstellungen.

3. **Image:**  
   Eine schreibgeschützte Vorlage mit Anweisungen zum Erstellen eines Docker-Containers. Oft basiert ein Image auf einem
   anderen Image, mit einigen zusätzlichen Anpassungen.

4. **Dockerfile:**  
   Eine Textdatei, die die Schritte enthält, um ein Docker-Image zu erstellen. Sie definiert, was in der Umgebung des
   Containers vorhanden sein wird.

5. **Docker Compose:**  
   Ein Tool zur Definition und Ausführung von Multi-Container Docker-Anwendungen. Mit einer YAML-Datei können Dienste,
   Netzwerke und Volumes konfiguriert werden.

6. **Volume:**  
   Ein Mechanismus zum Persistieren von Daten, die in Docker-Containern erzeugt werden, und zum gemeinsamen Nutzen von
   Daten zwischen Containern.

7. **Docker Hub:**  
   Eine Cloud-basierte Registry, in der Docker-Images gespeichert und geteilt werden können. Es ermöglicht Benutzern,
   Images hochzuladen und herunterzuladen.

8. **Registry:**  
   Ein Speicher- und Verteilungssystem für Docker-Images. Docker Hub ist ein Beispiel für eine öffentliche Registry.

9. **Swarm:**  
   Ein Orchestrierungstool von Docker, das es ermöglicht, eine Gruppe von Docker-Hosts in einen einzigen virtuellen Host
   zu verwalten.

10. **Kubernetes:**  
    Ein Open-Source-Orchestrierungssystem für Docker-Container, das ursprünglich von Google entwickelt wurde.

11. **Layer:**  
    Eine Schicht in einem Docker-Image, die Änderungen oder Ergänzungen zum Image repräsentiert. Jeder Layer wird nur
    einmal gespeichert, was Speicherplatz spart.

12. **Docker Engine:**  
    Die Laufzeit- und Verwaltungsumgebung für Docker-Container. Sie ermöglicht das Erstellen und Ausführen von
    Containern auf dem Host-System.

13. **Docker Daemon:**  
    Der Hintergrundprozess, der die Erstellung, Ausführung und Überwachung der Docker-Container verwaltet.

14. **Docker Client:**  
    Das Kommandozeilen-Tool, das es Benutzern ermöglicht, mit dem Docker Daemon zu interagieren.

15. **Port Binding:**  
    Die Methode, mit der Docker externe Ports auf die internen Ports des Containers abbildet, um Netzwerkkommunikation
    zu ermöglichen.

16. **Wichtige Docker-Kommandozeilenbefehle:**

| Befehl                   | Beschreibung                                                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run`             | Erstellt und startet einen Container aus einem Image.                                                                                                                     |
| `docker build`           | Baut ein Image aus einem Dockerfile.                                                                                                                                      |
| `docker pull`            | Lädt ein Image oder ein Repository aus einer Registry herunter.                                                                                                           |
| `docker push`            | Lädt ein Image oder ein Repository in eine Registry hoch.                                                                                                                 |
| `docker images`          | Listet alle lokal gespeicherten Docker-Images auf.                                                                                                                        |
| `docker rmi`             | Entfernt ein oder mehrere Docker-Images.                                                                                                                                  |
| `docker ps`              | Zeigt laufende Container an. Mit `-a` werden alle Container angezeigt.                                                                                                    |
| `docker stop`            | Stoppt einen oder mehrere laufende Container.                                                                                                                             |
| `docker start`           | Startet einen oder mehrere gestoppte Container.                                                                                                                           |
| `docker restart`         | Startet einen oder mehrere Container neu.                                                                                                                                 |
| `docker rm`              | Entfernt einen oder mehrere Container.                                                                                                                                    |
| `docker exec`            | Führt einen Befehl in einem laufenden Container aus.                                                                                                                      |
| `docker logs`            | Holt die Logs eines Containers.                                                                                                                                           |
| `docker inspect`         | Gibt detaillierte Informationen über Container oder Images aus.                                                                                                           |
| `docker network`         | Verwaltet Docker-Netzwerke.                                                                                                                                               |
| `docker volume`          | Verwaltet Docker-Volumes für die Datenspeicherung.                                                                                                                        |
| `docker compose`         | Verwendet Docker Compose zum Verwalten von Multi-Container-Anwendungen.                                                                                                   |
| `docker stats`           | Zeigt eine Live-Stream-Statistik laufender Container an.                                                                                                                  |
| `docker attach`          | Verbindet die lokale Eingabe, Ausgabe und Fehlerausgabe mit einem laufenden Container.                                                                                    |
| `docker cp`              | Kopiert Dateien oder Verzeichnisse zwischen einem Container und dem lokalen Dateisystem.                                                                                  |
| `docker diff`            | Zeigt Änderungen an Dateien oder Verzeichnissen in einem Container-Dateisystem an.                                                                                        |
| `docker port`            | Zeigt die öffentlichen Port-Bindungen eines Containers an.                                                                                                                |
| `docker search`          | Sucht nach Images in einer Docker-Registry.                                                                                                                               |
| `docker save`            | Speichert ein Image in einer TAR-Datei.                                                                                                                                   |
| `docker load`            | Lädt ein Image aus einer TAR-Datei.                                                                                                                                       |
| `docker info`            | Zeigt Systemweite Informationen über Docker, einschließlich der Anzahl der Container und Images, Speicher- und Netzwerkkonfiguration, Kernel-Version usw.                 |
| `docker version`         | Zeigt Informationen über die Docker-Version, einschließlich der Client- und Server-Version (Docker-Daemon).                                                               |
| `docker system df`       | Zeigt die belegte Speichermenge durch Docker-Images, Container, Volumes und Build Cache.                                                                                  |
| `docker system prune`    | Entfernt ungenutzte Daten, um Speicherplatz freizugeben. Dies umfasst ungenutzte Container, Netzwerke, Images (sowohl hängende als auch ungenutzte) und optional Volumes. |
| `docker network ls`      | Listet alle Netzwerke auf, die von Docker verwaltet werden.                                                                                                               |
| `docker network create`  | Erstellt ein neues Netzwerk.                                                                                                                                              |
| `docker network inspect` | Zeigt detaillierte Informationen zu einem oder mehreren Netzwerken an.                                                                                                    |
| `docker network rm`      | Entfernt ein oder mehrere Netzwerke.                                                                                                                                      |
| `docker volume ls`       | Listet alle Volumes auf, die von Docker verwaltet werden.                                                                                                                 |
| `docker volume create`   | Erstellt ein neues Volume.                                                                                                                                                |
| `docker volume inspect`  | Zeigt detaillierte Informationen zu einem oder mehreren Volumes an.                                                                                                       |
| `docker volume rm`       | Entfernt ein oder mehrere Volumes.                                                                                                                                        |
| `docker login`           | Meldet sich bei einer Docker-Registry an.                                                                                                                                 |
| `docker logout`          | Meldet sich von einer Docker-Registry ab.                                                                                                                                 |
| `docker context ls`      | Listet alle Docker-Kontexte auf. Ein Kontext definiert, wie Befehle mit einem bestimmten Docker-Host und einer Docker-Registry interagieren.                              |
| `docker context create`  | Erstellt einen neuen Docker-Kontext.                                                                                                                                      |
| `docker context use`     | Wechselt zu einem anderen Docker-Kontext.                                                                                                                                 |
| `docker context rm`      | Entfernt einen Docker-Kontext.                                                                                                                                            |
| `docker-compose up`      | Startet die Container, die in der `docker-compose.yml`-Datei definiert sind. Mit der Option `-d` werden die Container im Hintergrund gestartet.                           |
| `docker-compose down`    | Stoppt und entfernt alle Container, Netzwerke, Volumes und Images, die durch `docker-compose up` erstellt wurden.                                                         |
| `docker-compose build`   | Baut alle Dienste, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                                                   |
| `docker-compose pull`    | Lädt alle Images herunter, die in der `docker-compose.yml`-Datei definiert sind, aber nicht lokal gebaut werden.                                                          |
| `docker-compose push`    | Lädt alle Images zu einem Registry-Server hoch, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                      |
| `docker-compose restart` | Startet alle Container neu, die in der `docker-compose.yml`-Datei definiert sind.                                                                                         |
| `docker-compose stop`    | Stoppt alle laufenden Container, die durch `docker-compose up` gestartet wurden, ohne sie zu entfernen.                                                                   |
| `docker-compose start`   | Startet alle gestoppten Container, die durch `docker-compose up` erstellt wurden.                                                                                         |
| `docker-compose logs`    | Zeigt die Log-Ausgaben aller Container an. Mit der Option `-f` können die Logs live verfolgt werden.                                                                      |
| `docker-compose exec`    | Führt einen Befehl in einem laufenden Container aus. Nützlich für das Debugging oder die Interaktion mit Diensten.                                                        |
| `docker-compose run`     | Führt einen einmaligen Befehl in einem Dienst aus. Ideal für administrative Aufgaben oder Tests.                                                                          |

Diese Tabelle deckt die grundlegenden und am häufigsten verwendeten Docker-Befehle ab. Für spezifischere
Anforderungen oder erweiterte Optionen ist es ratsam, die Docker-Dokumentation oder die Hilfeoption im
Terminal (`docker command --help`) zu konsultieren.

