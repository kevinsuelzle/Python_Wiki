# **Arbeiten mit Docker-Registries:**

Nachdem Sie ein Docker-Image erstellt haben, ist der nächste Schritt oft, dieses Image in einem Repository zu sichern.
Dies ermöglicht es Ihnen, das Image zu teilen, es auf verschiedenen Maschinen zu verwenden und eine Versionierung Ihrer
Container-Umgebungen zu haben.

## Warum Docker-Images in Repositories speichern?

### **Versionierung und Wiederverwendbarkeit:**

Repositories ermöglichen es Ihnen, verschiedene Versionen eines Images zu
speichern und bei Bedarf darauf zurückzugreifen.

### **Kollaboration:**

Durch das Hochladen von Images in ein Repository können Teams gemeinsam an Anwendungen arbeiten
und sicherstellen, dass jeder auf die gleiche Umgebung zugreift.

### **Deployment:**

Images aus Repositories können leicht auf Produktions- oder Entwicklungsservern bereitgestellt
werden.

## Schritte zum Sichern eines Docker-Images in einem Repository

### **Wählen eines Docker-Repositorys:**

- Das bekannteste Docker-Repository ist Docker Hub, aber es gibt auch andere Optionen wie AWS Elastic Container
  Registry (ECR), Google Container Registry (GCR) oder private Repositories.

### **Taggen des Docker-Images:**

- Bevor Sie ein Image in ein Repository hochladen, sollten Sie es taggen. Dies gibt dem Image einen Namen und
  optional eine Version.
- Befehl zum Taggen eines Images:

```bash
docker tag hello-world-python yourusername/hello-world-python:version
```

- Ersetzen Sie `yourusername` mit Ihrem Benutzernamen im Repository und `version` mit dem gewünschten Versions-Tag.

### **Anmelden am Docker-Repository:**

- Um Images hochzuladen, müssen Sie sich bei dem Repository anmelden.
- Befehl zum Anmelden bei Docker Hub:

```bash
docker login
```

- Folgen Sie den Anweisungen, um Ihre Anmeldeinformationen einzugeben.

### **Hochladen (Push) des Images:**

- Nachdem das Image getaggt und Sie angemeldet sind, können Sie es in das Repository hochladen.
- Befehl zum Hochladen des Images:

```bash
docker push yourusername/hello-world-python:version
```

### **Überprüfen des Images im Repository:**

- Nach dem Hochladen können Sie sich in Ihrem Repository anmelden und überprüfen, ob das Image erfolgreich
  hochgeladen wurde.

## Best Practices

- **Konsistente Tagging-Konventionen:** Verwenden Sie klare und konsistente Tags für Ihre Images, um die Verwaltung zu
  erleichtern.
- **Sicherheit:** Achten Sie darauf, keine sensiblen Daten in Ihren Images zu speichern, bevor Sie diese hochladen.
- **Regelmäßige Updates:** Halten Sie Ihre Images im Repository aktuell, um von Sicherheitsupdates und neuen Features zu
  profitieren.

### **Aufgabe: Nacharbeiten der Schritte 🌶️**

### **Aufgabe: Löschen von Containern und Images zur Erzeugung einer leeren Docker Umgebung. 🌶️🌶️.**

### **Aufgabe: Anmelden und Abmelden am Repo, Laden des Images mit pull 🌶️🌶️.️**

## Erstellung eines privaten Docker-Repositories

Neben der Nutzung öffentlicher Repositories wie Docker Hub kann es für Teams und Organisationen sinnvoll sein, ein
privates Docker-Repository zu erstellen. Ein privates Repository bietet mehr Kontrolle über den Zugriff und die
Sicherheit Ihrer Docker-Images. Hier erfahren Sie, wie Sie ein privates Docker-Repository einrichten können.

### Vorteile eines privaten Repositories

1. **Sicherheit:** Kontrollieren Sie, wer Zugriff auf Ihre Docker-Images hat.
2. **Datenschutz:** Ideal für Images, die sensible oder proprietäre Informationen enthalten.
3. **Anpassung:** Passen Sie das Repository an Ihre spezifischen Bedürfnisse und Workflows an.

### Optionen für private Docker-Repositories

1. **Docker Hub Private Repositories:**
    - Docker Hub bietet die Möglichkeit, private Repositories zu erstellen, die nicht öffentlich zugänglich sind.
    - Einfach zu verwenden, aber es gibt Kosten für private Repositories auf Docker Hub.

2. **Selbst gehostete Repositories:**
    - Sie können Ihr eigenes Docker-Registry auf einem Server hosten.
    - Docker bietet eine offizielle Registry-Software namens "Docker Registry", die Sie selbst hosten können.

### Schritte zur Einrichtung eines selbst gehosteten Docker-Repositories

#### **Vorbereitung:**

- Stellen Sie sicher, dass Sie einen Server haben, auf dem Sie die Registry hosten können.
- Installieren Sie Docker auf diesem Server.

#### **Starten der Docker Registry:**

- Führen Sie den folgenden Befehl aus, um eine Docker Registry als Container zu starten:

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

- Dies startet eine Docker Registry, die auf Port 5000 lauscht.

#### **Taggen und Pushen eines Images zur privaten Registry:**

- Taggen Sie Ihr lokales Image für die private Registry:

```bash
docker tag hello-world-python localhost:5000/hello-world-python
```

- Pushen Sie das Image zur privaten Registry:

```bash
docker push localhost:5000/hello-world-python
```

#### **Zugriff auf das private Repository:**

- Um auf Images aus der privaten Registry zuzugreifen, verwenden Sie den vollständigen Pfad in Ihren
  Docker-Befehlen, z.B. `localhost:5000/hello-world-python`.

### Sicherheitsaspekte

- **HTTPS:** Es wird empfohlen, Ihre Registry mit HTTPS zu sichern, um die Übertragung von Images zu schützen.
- **Authentifizierung:** Implementieren Sie Authentifizierungsmechanismen, um den Zugriff auf Ihre Registry zu
  kontrollieren.

### **Aufgabe: Nacharbeiten der Schritte 🌶️**

### **Aufgabe: Löschen von Containern und Images zur Erzeugung einer leeren Docker Umgebung. 🌶️🌶️.**

### **Aufgabe: Anmelden und Abmelden am Repo, Laden des Images mit pull 🌶️🌶️.️**

## Images finden

Das Durchsuchen und Erkunden öffentlicher Repositories ist eine wichtige Fähigkeit, um verfügbare Docker-Images zu
entdecken und zu verstehen, was die Docker-Community und Unternehmen anbieten. Hier sind einige Methoden, um öffentliche
Repositories zu erkunden:

### Docker Hub

Docker Hub ist das bekannteste und am häufigsten genutzte öffentliche Repository für Docker-Images. Es bietet eine
Vielzahl von offiziellen und Community-basierten Images.

### **Web-Oberfläche:**

- Besuchen Sie [Docker Hub](https://hub.docker.com/).
- Nutzen Sie die Suchfunktion, um nach spezifischen Images oder Anbietern zu suchen.
- Durchstöbern Sie Kategorien oder verwenden Sie Tags, um relevante Images zu finden.

### **Docker CLI:**

- Verwenden Sie den `docker search` Befehl, um Docker Hub direkt über die Kommandozeile zu durchsuchen. Zum
  Beispiel:

```bash
docker search python
```

- Dieser Befehl zeigt eine Liste von Python-Images mit Beschreibungen und weiteren Informationen an.

### Andere Öffentliche Repositories

Neben Docker Hub gibt es auch andere öffentliche Repositories wie das Google Container Registry (GCR), Amazon Elastic
Container Registry (ECR) und Microsoft Container Registry (MCR).

1. **Google Container Registry (GCR):**
    - GCR bietet eine Sammlung von öffentlichen Images, die Sie über
      die [Google Cloud Console](https://console.cloud.google.com/) oder die gcloud CLI durchsuchen können.

2. **Amazon Elastic Container Registry (ECR):**
    - ECR ist hauptsächlich für private Repositories gedacht, bietet aber auch öffentliche Repositories. Diese können
      über die AWS Management Console oder die AWS CLI durchsucht werden.

3. **Microsoft Container Registry (MCR):**
    - MCR hostet Microsoft-basierte Images wie Windows Server und SQL Server. Diese können über die MCR-Webseite oder
      die Docker CLI durchsucht werden.

### Best Practices beim Durchsuchen Öffentlicher Repositories

- **Überprüfen Sie die Quelle:** Achten Sie darauf, dass das Image von einer vertrauenswürdigen Quelle stammt,
  insbesondere wenn es um offizielle Images geht.
- **Lesen Sie die Dokumentation:** Viele Images auf Docker Hub und anderen Repositories haben umfangreiche
  Dokumentationen, die erklären, wie das Image verwendet wird.
- **Bewertungen und Downloads:** Berücksichtigen Sie die Anzahl der Downloads und die Bewertungen eines Images, um seine
  Popularität und Zuverlässigkeit einzuschätzen.
- **Aktualität:** Achten Sie darauf, dass das Image regelmäßig aktualisiert wird, um sicherzustellen, dass Sie die
  neuesten Funktionen und Sicherheitsupdates erhalten.

Das Durchsuchen öffentlicher Repositories ist ein wesentlicher Bestandteil der Arbeit mit Docker, da es Ihnen
ermöglicht, von der Arbeit der Community zu profitieren und schnell auf vorbereitete und konfigurierte Umgebungen
zuzugreifen.
