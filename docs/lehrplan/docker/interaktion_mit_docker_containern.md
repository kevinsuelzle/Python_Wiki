# Interaktion mit Docker-Containern: Übersicht und praktische Beispiele

## 1. Starten und Stoppen von Containern

- **Starten eines Containers:**
  ```bash
  docker run -d --name mein-container hello-world-python
  ```

  Das Image haben wir [hier](docker_images_erstellen.md) erstellt.

  Dieser Befehl startet einen Container namens `mein-container` im Hintergrund (`-d`) basierend auf
  dem `hello-world-python` Image.

  Der Begriff "im Hintergrund" (englisch "detached") im Zusammenhang mit dem Befehl `docker run -d ...` bezieht sich auf
  den
  Modus, in dem der
  Docker-Container ausgeführt wird. Wenn Sie einen Container im detached Modus starten, bedeutet das, dass der Container
  im Hintergrund des Docker-Hosts ausgeführt wird also, dass der Container startet und weiterläuft, ohne die
  aktuelle Terminal- oder Kommandozeilensitzung zu blockieren.

Hier sind einige wichtige Punkte zum detached Modus:

1. **Hintergrundausführung:** Der Container läuft im Hintergrund, und Sie erhalten sofort die Kontrolle über die
   Kommandozeile zurück, nachdem der Container gestartet wurde.

2. **Keine Ausgabe im Terminal:** Im detached Modus sehen Sie keine Ausgabe des Containers in Ihrem Terminal. Der
   Container läuft still im Hintergrund, es sei denn, Sie greifen explizit auf seine Logs zu.

3. **Zugriff auf Logs:** Obwohl der Container im Hintergrund läuft und keine Ausgabe direkt im Terminal anzeigt, können
   Sie die Logs des Containers jederzeit mit dem Befehl `docker logs [CONTAINER_ID oder NAME]` oder über Docker
   Desktop einsehen, wie [hier](fehlersuche_mit__container_logs.md) beschrieben.

4. **Verwendung:** Der detached Modus wird häufig verwendet, wenn Sie einen Container als langlaufenden Dienst oder
   Prozess ausführen möchten, ohne dass dieser Ihre Terminal-Sitzung blockiert. Dies ist besonders nützlich in
   Produktionsumgebungen oder beim Ausführen von Anwendungen, die als Hintergrunddienste fungieren sollen.

- **Stoppen eines Containers:**
  ```bash
  docker stop mein-container
  ```
  Dieser Befehl stoppt den Container `mein-container`.

## 2. Zugriff auf laufende Container

- **Interaktiver Modus:**

  ```bash
  docker exec -it mein-container bash
  ```

  Mit diesem Befehl starten Sie eine interaktive Bash-Shell im Container `mein-container`.
  Der Befehl `docker exec -it ...` wird verwendet, um in einem bereits laufenden Docker-Container interaktive Befehle
  auszuführen. Dieser Befehl ist besonders nützlich, wenn Sie eine interaktive Shell innerhalb des Containers starten
  möchten, um verschiedene Aufgaben auszuführen, wie z.B. das Überprüfen von Konfigurationen, das Ändern von Dateien
  oder das Ausführen von Diensten innerhalb des Containers. Hier ist, was die einzelnen Optionen und Argumente bedeuten:

- `docker exec`: Dieser Befehl führt einen neuen Befehl in einem laufenden Container aus.

- `-i` (oder `--interactive`): Hält den STDIN offen, auch wenn er nicht an das Terminal angeschlossen ist. Dies
  ermöglicht die interaktive Eingabe in den Container.

- `-t` (oder `--tty`): Weist Docker an, ein Pseudo-TTY zuzuweisen, das heißt, es simuliert ein Terminal, ähnlich wie
  wenn Sie eine Shell-Sitzung in einem normalen Terminal verwenden. Dies ermöglicht eine formatierte Ausgabe und die
  Möglichkeit, interaktive Anwendungen zu nutzen.

Zusammen ermöglichen `-it` die Interaktivität mit dem Container, was bedeutet, dass Sie Befehle eingeben und die
Ausgaben so sehen können, als ob Sie direkt in einer Terminal-Sitzung auf dem Container arbeiten würden.

In diesem Befehl:

- `mein-container` ist der Name oder die ID Ihres laufenden Containers.
- `bash` ist der Befehl, den Sie im Container ausführen möchten, in diesem Fall das Starten einer Bash-Shell.

Sobald Sie diesen Befehl ausführen, werden Sie in die Bash-Shell des Containers versetzt, wo Sie Befehle ausführen und
mit dem Container interagieren können, als ob Sie direkt in ihm arbeiten würden. Wenn Sie fertig sind, können Sie `exit`
eingeben, um die Shell zu verlassen und zum Host-Terminal zurückzukehren.

### Zusammenfassung

Der Befehl `docker exec -it` ist ein mächtiges Werkzeug in der Docker-Toolbox, das es Ihnen ermöglicht, interaktiv mit
Ihren laufenden Containern zu arbeiten. Es ist besonders nützlich für die Fehlerbehebung, schnelle Änderungen oder
einfach nur, um den Zustand und die Konfiguration von Diensten innerhalb des Containers zu überprüfen.

## 3. Datenmanagement und -austausch

Die folgenden Kommandos beziehen sich auf die Arbeit mit einem Container.

- **Kopieren von Dateien:**
  ```bash
  docker cp host_datei.txt mein-container:/container_datei.txt
  ```
  Kopiert `host_datei.txt` vom Host-System in den Container `mein-container`.

- **Persistente Daten mit Volumes:**
  ```bash
  docker run -d --name mein-container -v mein-volume:/app hello-world-python
  ```

  In diesem Befehl:

    - `-d` ist der Schalter für den oben beschriebenen detached mode.
    - `--name mein-container` gibt dem container seinen Namen.
    - `-v mein-volume:/app` sagt Docker, dass es das Volume `mein-volume` an den Pfad `/app` im Container binden soll.
    - `hello-world-python` ist das Image, aus dem der Container erstellt wird.

  Näheres dazu findet sich [hier](wo_und_wie_docker_container_daten_speichern.md).

## 4. Netzwerkkommunikation

- **Port-Weiterleitung:**
  ```bash
  docker run -d --name mein-webserver -p 8080:80 nginx
  ```
  Startet einen nginx-Webserver-Container und leitet den Port 8080 des Hosts auf den Port 80 des Containers um.

  Funktionsweise des nginx-Webservers:
  ```mermaid
  graph LR
      client[Client] -- HTTP Request :8080 --> host[Host Machine]
      host -- Port 8080 to 80 Mapping --> nginx[Nginx Container]
      nginx -- Static Content --> host
      host -- Static Content :8080 --> client
      nginx -- HTTP Request --> app[Application Server]
      app -- Response --> nginx
      nginx -- HTTP Response --> host
      host -- HTTP Response :8080 --> client
  ```

  Nginx agiert als Vermittler zwischen dem Client und den Ressourcen, die der Client anfordert, sei es statischer Inhalt
  oder dynamische Inhalte, die von einem Anwendungsserver generiert werden. Nginx ist bekannt für seine
  Leistungsfähigkeit, Effizienz und seine Fähigkeit, eine große Anzahl von gleichzeitigen Verbindungen zu verwalten, was
  es zu einer beliebten Wahl für moderne Webanwendungen macht.

  Diese Grafik zeigt, wie der Docker-Befehl docker run -d --name mein-webserver -p 8080:80 nginx den Datenfluss zwischen
  dem Client, dem Host und dem Nginx-Container in einem Docker-Ökosystem beeinflusst. Durch die Portweiterleitung können
  Clients auf den Nginx-Webserver zugreifen, als ob er direkt auf dem Host auf Port 8080 laufen würde, während er
  tatsächlich sicher und isoliert innerhalb eines Containers auf Port 80 läuft.


- **Container in einem Netzwerk:**
  ```bash
  docker network create mein-netzwerk
  docker run -d --name mein-container --network mein-netzwerk hello-world-python
  ```
  Erstellt ein Netzwerk `mein-netzwerk` und startet einen Container darin.

  ```mermaid
  graph LR
      subgraph Docker Host
          subgraph Netzwerk A [mein-netzwerk]
              A[Container A] 
              B[Container B]
          end
          subgraph Netzwerk B [anderes-netzwerk]
              C[Container C]
              D[Container D]
          end
      end
  
      A -- Kommunikation --> B
      C -- Kommunikation --> D
      A <-. Keine direkte Kommunikation .-> C
      B <-. Keine direkte Kommunikation .-> D
  ```

  Diese Grafik veranschaulicht, wie Docker-Netzwerke zur Isolation und Kommunikation zwischen Containern beitragen.
  Durch
  die Verwendung von benutzerdefinierten Netzwerken können Sie sicherstellen, dass nur die gewünschten Container
  miteinander kommunizieren können, während andere Container oder Netzwerke isoliert bleiben. Dies ist besonders wichtig
  für die Sicherheit, das Netzwerkmanagement und die Architektur von Microservices.

## 5. Überwachung und Management

- **Container-Status überprüfen:**
  ```bash
  docker ps
  ```
  Zeigt alle laufenden Container an.

- **Ressourcennutzung überwachen:**
  ```bash
  docker stats
  ```
  Zeigt Echtzeitinformationen zur Ressourcennutzung aller Container.

## 6. Container-Updates und -Änderungen

- **Container aktualisieren:**
  ```bash
  # Stoppen des alten Containers
  docker stop mein-container
  # Entfernen des alten Containers
  docker rm mein-container
  # Starten eines neuen Containers mit dem aktualisierten Image
  docker run -d --name mein-container hello-world-python:neue-version
  ```
  Wenn ein Image erstellt wird, sollte ein Tag (hier 'neue-version') als Versionsbezeichnung hintere einem Doppelpunkt
  angegeben werden. So können Tags wie :latest dafür sorgen, dass immer das aktuellste Image verwendet wird.

## Aufgaben

### **Aufgabe: Information 🌶🌶️**

1. Nutzen Sie die Kommandozeile, um sich die laufenden Container aufzulisten.
2. Suchen Sie den Kommandozeilenbefehl über docker --help, um sich die vorhandenen Images aufzulisten.
3. Lassen Sie sich die vorhandenen Netzwerke anzeigen.

### **Aufgabe: Interaktion mit Docker-Containern 🌶🌶**

In dieser Übung werden Sie praktische Erfahrungen im Umgang mit Docker-Containern sammeln. Sie werden lernen, wie man
Container startet, stoppt, löscht und mit ihnen interagiert. Folgen Sie den untenstehenden Anweisungen, um die Aufgaben
zu erfüllen.

#### 1. Starten, Stoppen und Löschen von Containern

- **Starten Sie einen Container:**
  ```bash
  docker run -d --name mein-container nginx  // es kann auch ein anderes Image sein
  ```
  Dieser Befehl startet einen neuen Container im Hintergrund mit dem Namen `mein-container` basierend auf dem `nginx`
  Image.

- **Stoppen Sie den Container:**
  ```bash
  docker stop mein-container
  ```
  Dieser Befehl stoppt den laufenden Container `mein-container`.

- **Löschen Sie den Container:**
  ```bash
  docker rm mein-container
  ```
  Dieser Befehl entfernt den gestoppten Container `mein-container` aus Ihrem System.

#### 2. Interaktion mit einem laufenden Container

Öffnen Sie eine Konsole im Container:

```bash
    docker exec -it mein-container /bin/bash
```
  Dieser Befehl öffnet eine interaktive Bash-Shell im Container mein-container. Sie können nun Befehle wie ls, cd und cd .. verwenden, um die Dateistruktur zu erkunden.
  
  Erkunden Sie das Dateisystem:
      Verwenden Sie ls um die Dateien im aktuellen Verzeichnis aufzulisten.
      Navigieren Sie mit cd [Verzeichnisname] in ein Verzeichnis oder mit cd .. zurück zum übergeordneten Verzeichnis.
  
  Verlassen Sie die Konsole:
      Nachdem Sie das Dateisystem erkundet haben, geben Sie `exit` ein, um die Bash-Shell zu verlassen und zum Host-System zurückzukehren.
  
  Nun können Sie mit dem nächsten Schritt fortfahren, um eine Textdatei zu erstellen und diese in den Container zu
  kopieren.

#### 3. Erstellen und Kopieren einer Textdatei

- **Erstellen Sie eine Textdatei `mein-script.sh` auf Ihrem Host-System:**
  ```bash
  echo 'echo Hallo aus meinem Container!' > mein-script.sh
  ```
  Dieser Befehl erstellt eine einfache Shell-Skriptdatei mit dem Namen `mein-script.sh`.

- **Kopieren Sie die Textdatei in den Container:**
  ```bash
  docker cp mein-script.sh mein-container:/usr/mein-script.sh
  ```
  Dieser Befehl kopiert die Datei `mein-script.sh` in das Verzeichnis `/usr/` des Containers `mein-container`.

#### 4. Ausführen der Datei im Container

- **Führen Sie die Datei im Container aus:**
  ```bash
  docker exec mein-container bash -c "chmod +x /usr/mein-script.sh && /usr/mein-script.sh"
  ```
  Dieser Befehl macht das Skript ausführbar und führt es dann im Container aus. Sie sollten die Ausgabe "Hallo aus
  meinem Container!" sehen.

  Vertiefende Übung: Wiederholen Sie Aufgabe 2 und suchen Sie die kopierte und ausgeführte Datei im Container.

#### 5. Verlassen der Konsole

- **Verlassen Sie die Konsole:**
  Wenn Sie in der interaktiven Shell des Containers sind, können Sie `exit` eingeben, um die Shell zu verlassen und zur
  Kommandozeile Ihres Host-Systems zurückzukehren.

### **Zusammenfassung**

Durch das Ausführen dieser Aufgaben haben Sie gelernt, wie man mit Docker-Containern interagiert, indem Sie sie starten,
stoppen, löschen, auf sie zugreifen und in ihnen Befehle ausführen. Diese Fähigkeiten sind grundlegend für die Arbeit
mit Docker und bieten Ihnen eine solide Basis für komplexere Docker-Anwendungen und -Dienste.
