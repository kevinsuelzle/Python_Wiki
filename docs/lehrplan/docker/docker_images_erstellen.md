# Erstellung von Docker-Images:

Docker-Images werden üblicherweise mit einem **Dockerfile** erstellt. Ein Dockerfile ist eine Textdatei, die eine Reihe von
Anweisungen enthält, die beschreiben, wie das Image aufgebaut werden soll. Diese Anweisungen können das Hinzufügen von
Dateien, das Ausführen von Befehlen und das Setzen von Umgebungsvariablen umfassen.

## Grundlagen der Docker-Image-Erstellung

Ein Docker-Image dient
als Vorlage für das Erstellen von Containern und enthält alles, was für das Ausführen einer Anwendung benötigt wird –
von Binärdateien und Bibliotheken bis hin zu Systemeinstellungen.


### Erstellen einer Python-Anwendung:
Erstellen Sie eine Datei namens `app.py` mit folgendem Inhalt:

```python
print("Hello World from Docker using Python!")
```


### Erstellen des Dockerfiles:

**Dockerfile erstellen:** Ein Dockerfile ist eine Textdatei, die eine Reihe von Anweisungen enthält,
um ein Docker-Image zu erstellen. Jede Anweisung im Dockerfile fügt eine neue Schicht zum Image hinzu.
Wir Erstellen eine Datei namens `Dockerfile`:

```Dockerfile
FROM python:3.8-slim
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
```

In den Zeilen passiert nacheinander das folgendes:

**Definieren der Basisumgebung:** Die erste Anweisung in einem Dockerfile ist in der Regel `FROM`, 
die ein Basis-Image angibt, auf dem das neue Image aufbaut. Hier nutzen wir das Image `python` 
in der Version `3.8-slim`, das aus
dem [Docker Hub Repository](https://hub.docker.com/_/python) heruntergeladen wird. 
Es enthält einen Python-Interpreter, sodass wir Pythoncode in unserer `app.py` innerhalb des Containers
ausführen können. Es handelt sich um ein offizielles Image, das für seine Zuverlässigkeit und Sicherheit bekannt ist.

**Hinzufügen von Anwendungsdateien:** Mit den Befehlen `COPY` oder `ADD` werden Anwendungsdateien
und -verzeichnisse in das Image kopiert. Aus dem Hostsystem (dem lokalen Verzeichnis) werden alle Dateien (daher `.`) des
aktuellen Ordners in den Container kopiert, und zwar in den Ordner `app`.

**Installieren von Abhängigkeiten:** Der `RUN` Befehl werden verwendet, um Softwarepakete zu installieren und 
Konfigurationen vorzunehmen. Dies ist hier nicht nötig, da alles schon fertig konfiguriert ist.

**Konfigurieren von Startbefehlen:** Die `CMD`- oder `ENTRYPOINT`-Anweisungen definieren, welcher Befehl ausgeführt 
wird, wenn ein Container aus dem Image gestartet wird. Hier wird die Datei `app.py` mit Python gestartet.

### Bauen des Docker-Images:
Führen Sie den folgenden Befehl im Terminal aus, um das Image zu erstellen:

```bash
docker build -t hello-world-python .
```

Achten Sie auf den Punkt `.` am Ende der Anweisung.

In dem Befehl `docker build -t hello-world-python .` gibt der Punkt `.` das Kontextverzeichnis für den Build-Prozess
an, typischerweise das Verzeichnis, in dem sich das Dockerfile befindet. 
Der Punkt repräsentiert das aktuelle Verzeichnis in Unix- und Linux-basierten Systemen.

Der Teil `-t hello-world-python` des Befehls legt den Namen des zu erstellenden Images
fest. In diesem Fall wird das Image `hello-world-python` genannt.

### Ausführen des Containers:
Starten Sie einen Container basierend auf Ihrem Image mit:

```bash
docker run hello-world-python
```
Sie sollten die Ausgabe "Hello World from Docker using Python!" im Terminal sehen.

Prüfen Sie mithilfe des Docker Dashboards ihre Container. Der Container `hello-world-python` sollte da sein, aber nicht
aktiv laufen.

## Ablauf Zusammenfassung

Hier sind die Schritte, die im Detail passieren:

1. Container Start: Der Container startet und führt das Python-Skript aus.
2. Skriptausführung: Das Python-Skript führt seine Befehle aus, in diesem Fall `print('hello world')`.
3. Prozessende: Nachdem das Skript ausgeführt wurde und keine weiteren Anweisungen vorhanden sind, endet der
   Python-Prozess.
4. Container Stopp: Da der Hauptprozess (Python-Skript) beendet wurde, hat der Container keine weiteren Aufgaben mehr
   und stoppt sich selbst.

Der Container existiert weiterhin nach seiner Ausführung, aber er befindet sich in einem _gestoppten_ Zustand. Sie können
auch über die Konsole
den gestoppten Container mit Befehlen wie `docker ps -a` sehen, der alle Container anzeigt, einschließlich der gestoppten.
Um den Container und seine Ressourcen zu entfernen, müssten Sie ihn explizit mit `docker rm` löschen. Sie können ihn auch
über das Dashboard löschen.