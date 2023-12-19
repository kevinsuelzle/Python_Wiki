# Interaktion mit Docker-Containern: Übersicht und praktische Beispiele

## 1. Starten und Stoppen von Containern

- **Starten eines Containers:**
  ```bash
  docker run -d --name mein-container hello-world-python
  ```
  TODO: einen link hinzufügen, wo wir das image definieren?
  Dieser Befehl startet einen Container namens `mein-container` im Hintergrund (`-d`) basierend auf
  dem `hello-world-python` Image.
TODO: was bedeutet 'im Hintergurnd'?

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
TODO: was macht -it? ICh verstehe das mit den interaktiven modus nicht wirklich.

- **Logs anzeigen:**
  ```bash
  docker logs mein-container
  ```
  Zeigt die Ausgabe des Containers `mein-container` an.

## 3. Datenmanagement und -austausch

TODO: ist das was du hier zeigst, in einem/wei laufenden docker Containern? Die Änderungen gehen
verloren, wenn die Container beendet und removed werden, oder?

- **Kopieren von Dateien:**
  ```bash
  docker cp host_datei.txt mein-container:/container_datei.txt
  ```
  Kopiert `host_datei.txt` vom Host-System in den Container `mein-container`.

- **Persistente Daten mit Volumes:**
  ```bash
  docker run -d --name mein-container -v mein-volume:/app hello-world-python
  ```
  Startet einen Container mit einem Volume `mein-volume`, das an `/app` im Container gemountet ist.
TODO: Ich verstehe nicht, was "Volume" ist. Sind das die Anzahl der Bytes, die der Container als Speicherplatz hat?
## 4. Netzwerkkommunikation

- **Port-Weiterleitung:**
  ```bash
  docker run -d --name mein-webserver -p 8080:80 nginx
  ```
  Startet einen Nginx-Webserver-Container und leitet den Port 8080 des Hosts auf den Port 80 des Containers um.
TODO: was ist Nginx?
- **Container in einem Netzwerk:**
  ```bash
  docker network create mein-netzwerk
  docker run -d --name mein-container --network mein-netzwerk hello-world-python
  ```
  Erstellt ein Netzwerk `mein-netzwerk` und startet einen Container darin.
TODO: was bedeutet hier "Netzwerk"?
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

- **Änderungen commiten:**
  ```bash
  docker commit mein-container mein-neues-image
  ```
  Erstellt ein neues Image `mein-neues-image` basierend auf dem aktuellen Zustand des Containers `mein-container`.

TODO: ich finde die Aufgabe sehr dünn formuliert ohne Images zur Verfügung zu stellen.
### **Aufgabe: Arbeiten sie die Beispiele nach 🌶️**