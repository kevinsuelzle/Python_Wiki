# Grundbegriffe von Docker:

| Begriff        | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Referenz                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Docker         | Eine Plattform für die Entwicklung, Bereitstellung und Ausführung von Anwendungen in isolierten Umgebungen namens Containern.                                                                                                                                                                                                                                                                                                                                                       | [Docker](https://www.docker.com/)                                                          |
| Container      | Eine leichte, eigenständige, ausführbare Softwarepaketeinheit, die alles enthält, was benötigt wird, um Code auszuführen, einschließlich Systemtools, Bibliotheken und Einstellungen.                                                                                                                                                                                                                                                                                               | [Docker Docs: Container](https://docs.docker.com/get-started/overview/#container)          |
| Image          | Eine schreibgeschützte Vorlage mit Anweisungen zum Erstellen eines Docker-Containers. Oft basiert ein Image auf einem anderen Image, mit einigen zusätzlichen Anpassungen.                                                                                                                                                                                                                                                                                                          | [Docker Docs: Images](https://docs.docker.com/get-started/overview/#images)                |
| Dockerfile     | Eine Textdatei, die die Schritte enthält, um ein Docker-Image zu erstellen. Sie definiert, was in der Umgebung des Containers vorhanden sein wird.                                                                                                                                                                                                                                                                                                                                  | [Docker Docs: Dockerfile](https://docs.docker.com/engine/reference/builder/)               |
| Docker Compose | Ein Tool zur Definition und Ausführung von Multi-Container Docker-Anwendungen. Mit einer YAML-Datei können Dienste, Netzwerke und Volumes konfiguriert werden.                                                                                                                                                                                                                                                                                                                      | [Docker Docs: Compose](https://docs.docker.com/compose/)                                   |
| Volume         | Ein Mechanismus zum Persistieren von Daten, die in Docker-Containern erzeugt werden, und zum gemeinsamen Nutzen von Daten zwischen Containern.                                                                                                                                                                                                                                                                                                                                      | [Docker Docs: Volumes](https://docs.docker.com/storage/volumes/)                           |
| Docker Hub     | Eine Cloud-basierte Registry, in der Docker-Images gespeichert und geteilt werden können. Es ermöglicht Benutzern, Images hochzuladen und herunterzuladen.                                                                                                                                                                                                                                                                                                                          | [Docker Hub](https://hub.docker.com/)                                                      |
| Registry       | Ein Speicher- und Verteilungssystem für Docker-Images. Docker Hub ist ein Beispiel für eine öffentliche Registry.                                                                                                                                                                                                                                                                                                                                                                   | [Docker Docs: Registry](https://docs.docker.com/registry/)                                 |
| Swarm          | Ein Orchestrierungstool von Docker, das es ermöglicht, eine Gruppe von Docker-Hosts in einen einzigen virtuellen Host zu verwalten.                                                                                                                                                                                                                                                                                                                                                 | [Docker Docs: Swarm](https://docs.docker.com/engine/swarm/)                                |
| Kubernetes     | Ein Open-Source-Orchestrierungssystem für Docker-Container, das ursprünglich von Google entwickelt wurde.                                                                                                                                                                                                                                                                                                                                                                           | [Kubernetes](https://kubernetes.io/)                                                       |
| Layer          | Eine Schicht in einem Docker-Image, die Änderungen oder Ergänzungen zum Image repräsentiert. Jeder Layer wird nur einmal gespeichert, was Speicherplatz spart.                                                                                                                                                                                                                                                                                                                      | [Docker Docs: Layers](https://docs.docker.com/storage/storagedriver/)                      |
| Docker Engine  | Die Laufzeit- und Verwaltungsumgebung für Docker-Container. Sie ermöglicht das Erstellen und Ausführen von Containern auf dem Host-System.                                                                                                                                                                                                                                                                                                                                          | [Docker Docs: Engine](https://docs.docker.com/engine/)                                     |
| Docker Daemon  | Der Hintergrundprozess, der die Erstellung, Ausführung und Überwachung der Docker-Container verwaltet.                                                                                                                                                                                                                                                                                                                                                                              | [Docker Docs: Daemon](https://docs.docker.com/config/daemon/)                              |
| Docker Client  | Das Kommandozeilen-Tool, das es Benutzern ermöglicht, mit dem Docker Daemon zu interagieren.                                                                                                                                                                                                                                                                                                                                                                                        | [Docker Docs: Client](https://docs.docker.com/engine/reference/commandline/cli/)           |
| Port Binding   | Die Methode, mit der Docker externe Ports auf die internen Ports des Containers abbildet, um Netzwerkkommunikation zu ermöglichen.                                                                                                                                                                                                                                                                                                                                                  | [Docker Docs: Networking](https://docs.docker.com/config/containers/container-networking/) |
| Bind Mounts    | Ein Bind Mount ist ein Mapping eines Host-Dateisystempfads zum Pfad eines Containers. Im Gegensatz zu Volumes, die von Docker verwaltet werden, sind Bind Mounts spezifische Pfade auf dem Host-System. Sie ermöglichen den direkten Zugriff auf das Dateisystem des Hosts und werden oft für die Entwicklung und für Daten, die nicht von Docker verwaltet werden müssen, verwendet. Änderungen an den Bind Mounts sind sofort sowohl im Container als auch auf dem Host sichtbar. | [Docker Docs: Bind Mounts](https://docs.docker.com/storage/bind-mounts/)                   |

# Wichtige Docker-Kommandozeilenbefehle:
| Befehl                   | Beschreibung                                                                                                                                                              | Referenz                                                                                      |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `docker run`             | Erstellt und startet einen Container aus einem Image.                                                                                                                     | [Referenz](https://docs.docker.com/engine/reference/run/)                                     |
| `docker build`           | Baut ein Image aus einem Dockerfile.                                                                                                                                      | [Referenz](https://docs.docker.com/engine/reference/commandline/build/)                       |
| `docker pull`            | Lädt ein Image oder ein Repository aus einer Registry herunter.                                                                                                           | [Referenz](https://docs.docker.com/engine/reference/commandline/pull/)                        |
| `docker push`            | Lädt ein Image oder ein Repository in eine Registry hoch.                                                                                                                 | [Referenz](https://docs.docker.com/engine/reference/commandline/push/)                        |
| `docker images`          | Listet alle lokal gespeicherten Docker-Images auf.                                                                                                                        | [Referenz](https://docs.docker.com/engine/reference/commandline/images/)                      |
| `docker rmi`             | Entfernt ein oder mehrere Docker-Images.                                                                                                                                  | [Referenz](https://docs.docker.com/engine/reference/commandline/rmi/)                         |
| `docker ps`              | Zeigt laufende Container an. Mit `-a` werden alle Container angezeigt.                                                                                                    | [Referenz](https://docs.docker.com/engine/reference/commandline/ps/)                          |
| `docker stop`            | Stoppt einen oder mehrere laufende Container.                                                                                                                             | [Referenz](https://docs.docker.com/engine/reference/commandline/stop/)                        |
| `docker start`           | Startet einen oder mehrere gestoppte Container.                                                                                                                           | [Referenz](https://docs.docker.com/engine/reference/commandline/start/)                       |
| `docker restart`         | Startet einen oder mehrere Container neu.                                                                                                                                 | [Referenz](https://docs.docker.com/engine/reference/commandline/restart/)                     |
| `docker rm`              | Entfernt einen oder mehrere Container.                                                                                                                                    | [Referenz](https://docs.docker.com/engine/reference/commandline/rm/)                          |
| `docker exec`            | Führt einen Befehl in einem laufenden Container aus.                                                                                                                      | [Referenz](https://docs.docker.com/engine/reference/commandline/exec/)                        |
| `docker logs`            | Holt die Logs eines Containers.                                                                                                                                           | [Referenz](https://docs.docker.com/engine/reference/commandline/logs/)                        |
| `docker inspect`         | Gibt detaillierte Informationen über Container oder Images aus.                                                                                                           | [Referenz](https://docs.docker.com/engine/reference/commandline/inspect/)                     |
| `docker network`         | Verwaltet Docker-Netzwerke.                                                                                                                                               | [Referenz](https://docs.docker.com/engine/reference/commandline/network/)                     |
| `docker volume`          | Verwaltet Docker-Volumes für die Datenspeicherung.                                                                                                                        | [Referenz](https://docs.docker.com/engine/reference/commandline/volume/)                      |
| `docker compose`         | Verwendet Docker Compose zum Verwalten von Multi-Container-Anwendungen.                                                                                                   | [Referenz](https://docs.docker.com/compose/reference/)                                        |
| `docker stats`           | Zeigt eine Live-Stream-Statistik laufender Container an.                                                                                                                  | [Referenz](https://docs.docker.com/engine/reference/commandline/stats/)                       |
| `docker attach`          | Verbindet die lokale Eingabe, Ausgabe und Fehlerausgabe mit einem laufenden Container.                                                                                    | [Referenz](https://docs.docker.com/engine/reference/commandline/attach/)                      |
| `docker cp`              | Kopiert Dateien oder Verzeichnisse zwischen einem Container und dem lokalen Dateisystem.                                                                                  | [Referenz](https://docs.docker.com/engine/reference/commandline/cp/)                          |
| `docker port`            | Zeigt die öffentlichen Port-Bindungen eines Containers an.                                                                                                                | [Referenz](https://docs.docker.com/engine/reference/commandline/port/)                        |
| `docker search`          | Sucht nach Images in einer Docker-Registry.                                                                                                                               | [Referenz](https://docs.docker.com/engine/reference/commandline/search/)                      |
| `docker save`            | Speichert ein Image in einer TAR-Datei.                                                                                                                                   | [Referenz](https://docs.docker.com/engine/reference/commandline/save/)                        |
| `docker load`            | Lädt ein Image aus einer TAR-Datei.                                                                                                                                       | [Referenz](https://docs.docker.com/engine/reference/commandline/load/)                        |
| `docker info`            | Zeigt Systemweite Informationen über Docker, einschließlich der Anzahl der Container und Images, Speicher- und Netzwerkkonfiguration, Kernel-Version usw.                 | [Referenz](https://docs.docker.com/engine/reference/commandline/info/)                        |
| `docker version`         | Zeigt Informationen über die Docker-Version, einschließlich der Client- und Server-Version (Docker-Daemon).                                                               | [Referenz](https://docs.docker.com/engine/reference/commandline/version/)                     |
| `docker system df`       | Zeigt die belegte Speichermenge durch Docker-Images, Container, Volumes und Build Cache.                                                                                  | [Referenz](https://docs.docker.com/engine/reference/commandline/system_df/)                   |
| `docker system prune`    | Entfernt ungenutzte Daten, um Speicherplatz freizugeben. Dies umfasst ungenutzte Container, Netzwerke, Images (sowohl hängende als auch ungenutzte) und optional Volumes. | [Referenz](https://docs.docker.com/engine/reference/commandline/system_prune/)                |
| `docker network ls`      | Listet alle Netzwerke auf, die von Docker verwaltet werden.                                                                                                               | [Referenz](https://docs.docker.com/engine/reference/commandline/network_ls/)                  |
| `docker network create`  | Erstellt ein neues Netzwerk.                                                                                                                                              | [Referenz](https://docs.docker.com/engine/reference/commandline/network_create/)              |
| `docker network inspect` | Zeigt detaillierte Informationen zu einem oder mehreren Netzwerken an.                                                                                                    | [Referenz](https://docs.docker.com/engine/reference/commandline/network_inspect/)             |
| `docker network rm`      | Entfernt ein oder mehrere Netzwerke.                                                                                                                                      | [Referenz](https://docs.docker.com/engine/reference/commandline/network_rm/)                  |
| `docker volume ls`       | Listet alle Volumes auf, die von Docker verwaltet werden.                                                                                                                 | [Referenz](https://docs.docker.com/engine/reference/commandline/volume_ls/)                   |
| `docker volume create`   | Erstellt ein neues Volume.                                                                                                                                                | [Referenz](https://docs.docker.com/engine/reference/commandline/volume_create/)               |
| `docker volume inspect`  | Zeigt detaillierte Informationen zu einem oder mehreren Volumes an.                                                                                                       | [Referenz](https://docs.docker.com/engine/reference/commandline/volume_inspect/)              |
| `docker volume rm`       | Entfernt ein oder mehrere Volumes.                                                                                                                                        | [Referenz](https://docs.docker.com/engine/reference/commandline/volume_rm/)                   |
| `docker login`           | Meldet sich bei einer Docker-Registry an.                                                                                                                                 | [Referenz](https://docs.docker.com/engine/reference/commandline/login/)                       |
| `docker logout`          | Meldet sich von einer Docker-Registry ab.                                                                                                                                 | [Referenz](https://docs.docker.com/engine/reference/commandline/logout/)                      |
| `docker-compose up`      | Startet die Container, die in der `docker-compose.yml`-Datei definiert sind. Mit der Option `-d` werden die Container im Hintergrund gestartet.                           | [Referenz](https://docs.docker.com/compose/reference/up/)                                     |
| `docker-compose down`    | Stoppt und entfernt alle Container, Netzwerke, Volumes und Images, die durch `docker-compose up` erstellt wurden.                                                         | [Referenz](https://docs.docker.com/compose/reference/down/)                                   |
| `docker-compose build`   | Baut alle Dienste, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                                                   | [Referenz](https://docs.docker.com/compose/reference/build/)                                  |
| `docker-compose pull`    | Lädt alle Images herunter, die in der `docker-compose.yml`-Datei definiert sind, aber nicht lokal gebaut werden.                                                          | [Referenz](https://docs.docker.com/compose/reference/pull/)                                   |
| `docker-compose push`    | Lädt alle Images zu einem Registry-Server hoch, die in der `docker-compose.yml`-Datei definiert sind und ein `build`-Attribut haben.                                      | [Referenz](https://docs.docker.com/compose/reference/push/)                                   |
| `docker-compose restart` | Startet alle Container neu, die in der `docker-compose.yml`-Datei definiert sind.                                                                                         | [Referenz](https://docs.docker.com/compose/reference/restart/)                                |
| `docker-compose stop`    | Stoppt alle laufenden Container, die durch `docker-compose up` gestartet wurden, ohne sie zu entfernen.                                                                   | [Referenz](https://docs.docker.com/compose/reference/stop/)                                   |
| `docker-compose start`   | Startet alle gestoppten Container, die durch `docker-compose up` erstellt wurden.                                                                                         | [Referenz](https://docs.docker.com/compose/reference/start/)                                  |
| `docker-compose logs`    | Zeigt die Log-Ausgaben aller Container an. Mit der Option `-f` können die Logs live verfolgt werden.                                                                      | [Referenz](https://docs.docker.com/compose/reference/logs/)                                   |
| `docker-compose exec`    | Führt einen Befehl in einem laufenden Container aus. Nützlich für das Debugging oder die Interaktion mit Diensten.                                                        | [Referenz](https://docs.docker.com/compose/reference/exec/)                                   |
| `docker-compose run`     | Führt einen einmaligen Befehl in einem Dienst aus. Ideal für administrative Aufgaben oder Tests.                                                                          | [Referenz](https://docs.docker.com/compose/reference/run/)                                    |

Diese Tabelle deckt die grundlegenden und am häufigsten verwendeten Docker-Befehle ab. Für spezifischere
Anforderungen oder erweiterte Optionen ist es ratsam, die Docker-Dokumentation oder die Hilfeoption im
Terminal (`docker command --help`) zu konsultieren.