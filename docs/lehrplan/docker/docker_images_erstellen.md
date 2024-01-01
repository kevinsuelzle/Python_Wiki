# Erstellung von Docker-Images:

Docker-Images werden üblicherweise mit einem Dockerfile erstellt. Ein Dockerfile ist eine Textdatei, die eine Reihe von
Anweisungen enthält, die beschreiben, wie das Image aufgebaut werden soll. Diese Anweisungen können das Hinzufügen von
Dateien, das Ausführen von Befehlen und das Setzen von Umgebungsvariablen umfassen.

## Grundlagen der Docker-Image-Erstellung

Ein Docker-Image dient
als Vorlage für das Erstellen von Containern und enthält alles, was für das Ausführen einer Anwendung benötigt wird –
von Binärdateien und Bibliotheken bis hin zu Systemeinstellungen.

## Schritte zur Erstellung eines Docker-Images

### **Erstellen eines Dockerfiles:**

- Ein Dockerfile ist eine Textdatei, die eine Reihe von Anweisungen enthält, um ein Docker-Image zu erstellen.
- Jede Anweisung im Dockerfile fügt eine neue Schicht zum Image hinzu.

### **Definieren der Basisumgebung:**

- Die erste Anweisung in einem Dockerfile ist in der Regel `FROM`, die ein Basis-Image angibt, auf dem das neue
  Image aufbaut.

### **Hinzufügen von Anwendungsdateien:**

- Mit Anweisungen wie `COPY` oder `ADD` werden Anwendungsdateien und -verzeichnisse in das Image kopiert.

### **Installieren von Abhängigkeiten:**

- Befehle wie `RUN` werden verwendet, um Softwarepakete zu installieren und Konfigurationen vorzunehmen.

### **Konfigurieren von Startbefehlen:**

- Die `CMD`- oder `ENTRYPOINT`-Anweisungen definieren, welcher Befehl ausgeführt wird, wenn ein Container aus dem
  Image gestartet wird.

## Schritte zur Erstellung des Docker-Images für eine Python-Anwendung

### **Vorbereitung:**

- Stellen Sie sicher, dass Docker auf Ihrem System installiert ist.
- Erstellen Sie ein Verzeichnis für Ihr Projekt und navigieren Sie in dieses Verzeichnis.

### **Erstellen einer Python-Anwendung:**

- Erstellen Sie eine Datei namens `app.py` mit folgendem Inhalt:

```python
print("Hello World from Docker using Python!")
```

### **Erstellen des Dockerfiles:**

- Erstellen Sie eine Datei namens `Dockerfile` im selben Verzeichnis mit folgendem Inhalt:

```Dockerfile
FROM python:3.8-slim
COPY images_und_container /app
WORKDIR /app
CMD ["python", "app.py"]
```

Um ein Python-Programm auszuführen, benötigen Sie einen Python-Interpreter, der die Python-Befehle zur Laufzeit
interpretiert und in Maschinencode übersetzt.
Hier nutzen wir das Image `python` in der Version `3.8-slim`, das aus
dem [Docker Hub Repository](https://hub.docker.com/_/python) heruntergeladen wird. Es
handelt sich um ein offizielles Image, das für seine Zuverlässigkeit und Sicherheit bekannt ist.
Dieses Dockerfile verwendet also das offizielle Python-Image als Basis, kopiert die Anwendungsdateien in das Image und
definiert den Befehl zum Starten der Python-Anwendung.

### **Bauen des Docker-Images:**

- Führen Sie den folgenden Befehl im Terminal aus, um das Image zu erstellen:

```bash
docker build -t hello-world-python .
```

Achten Sie auf den Punkt am Ende der Anweisung.

In dem Befehl `docker build -t hello-world-python .` gibt der Punkt `.` das Kontextverzeichnis für den Build-Prozess
an, typischerweise das Verzeichnis, in dem sich das Dockerfile befindet. Hier sind die Details:

- **Punkt `.`:** Der Punkt repräsentiert das aktuelle Verzeichnis in Unix- und Linux-basierten Systemen. Im Kontext
  des `docker build`-Befehls teilt der Punkt Docker mit, dass das Build-Kontextverzeichnis das aktuelle Verzeichnis ist,
  in dem der Befehl ausgeführt wird. Docker sucht in diesem Verzeichnis nach dem Dockerfile (es sei denn, ein anderes
  wird explizit angegeben) und verwendet alle Dateien und Verzeichnisse innerhalb dieses Kontexts für den Build-Prozess,
  soweit sie nicht durch eine `.dockerignore`-Datei ausgeschlossen sind.

- **`-t hello-world-python`:** Dieser Teil des Befehls legt den Namen (und optional das Tag) des zu erstellenden Images
  fest. In diesem Fall wird das Image `hello-world-python` genannt.

Zusammengefasst bedeutet `docker build -t hello-world-python .`, dass Docker ein Image mit dem
Namen `hello-world-python` erstellen soll, indem es das Dockerfile im aktuellen Verzeichnis verwendet und alle
notwendigen Dateien aus diesem Verzeichnis in den Build-Prozess einbezieht. Dieser Befehl wird typischerweise im
Wurzelverzeichnis des Projekts ausgeführt, wo sich das Dockerfile befindet.

### **Ausführen des Containers:**

- Starten Sie einen Container basierend auf Ihrem Image mit:

```bash
docker run hello-world-python
```

- Sie sollten die Ausgabe "Hello World from Docker using Python!" im Terminal sehen.

Prüfen Sie mithilfe des Docker Dashboards ihre Container. Der Container `hello-world-python` sollte da sein, aber nicht
aktiv laufen.

Hier sind die Schritte, die im Detail passieren:

1. Container Start: Der Container startet und führt das Python-Skript aus.
2. Skriptausführung: Das Python-Skript führt seine Befehle aus, in diesem Fall print('hello world').
3. Prozessende: Nachdem das Skript ausgeführt wurde und keine weiteren Anweisungen vorhanden sind, endet der
   Python-Prozess.
4. Container Stoppt: Da der Hauptprozess (Python-Skript) beendet wurde, hat der Container keine weiteren Aufgaben mehr
   und stoppt sich selbst.

Der Container existiert weiterhin nach seiner Ausführung, aber er befindet sich in einem gestoppten Zustand. Sie können
auch über die Konsole
den gestoppten Container mit Befehlen wie `docker ps -a` sehen, der alle Container anzeigt, einschließlich der gestoppten.
Um den Container und seine Ressourcen zu entfernen, müssten Sie ihn explizit mit `docker rm` löschen. Sie können ihn auch
über das Dashboard löschen.