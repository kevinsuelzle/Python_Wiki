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
TODO: Es ist unklar, was du meinst, wenn du "**offizielles** Pythonimage" sagst.
- Dieses Dockerfile verwendet das offizielle Python-Image als Basis, kopiert die Anwendungsdateien in das Image und
  definiert den Befehl zum Starten der Python-Anwendung.

### **Bauen des Docker-Images:**

- Führen Sie den folgenden Befehl im Terminal aus, um das Image zu erstellen:

```bash
docker build -t hello-world-python .
```

- Achten Sie auf den Punkt am Ende der Anweisung. **TODO: Warum? Welche Bedeutung hat der Punkt?**
- Der `-t`-Flag weist Docker an, dem Image einen Namen (in diesem Fall `hello-world-python`) zu geben.

### **Ausführen des Containers:**

- Starten Sie einen Container basierend auf Ihrem Image mit:

```bash
docker run hello-world-python
```

- Sie sollten die Ausgabe "Hello World from Docker using Python!" im Terminal sehen.

TODO: Hier wäre es vllt gut noch mal zu erklären, in wie fern jetzt ein DockerContainer läuft und ob er immernoch läuft.

### **Aufgabe: Arbeitsschritte nachvollziehen und Ausführung prüfen. 🌶️**

