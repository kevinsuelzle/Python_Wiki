# Persistente Datenspeicherung in Docker

In Docker ist die persistente Datenspeicherung ein wesentlicher Aspekt, um sicherzustellen, dass wichtige Daten auch
nach dem Beenden oder Löschen von Containern erhalten bleiben. Dieses Kapitel behandelt die verschiedenen Methoden der
Datenspeicherung in Docker und wie sie effektiv genutzt werden können.

## Grundlagen der persistenten Datenspeicherung

### 1. **Container-Dateisystem:**

- Standardmäßig speichert jeder Docker-Container Daten in einem schreibbaren Layer, der über dem Image-Dateisystem
  liegt. Diese Daten gehen verloren, wenn der Container gelöscht wird.
TODO: Layer?

### 2. **Volumes:**

- Volumes sind der bevorzugte Weg, um persistente Daten in Docker zu speichern. Sie sind komplett vom Lebenszyklus
  des Containers getrennt und werden von Docker verwaltet.

### 3. **Bind Mounts:**

- Bind Mounts erlauben es, Daten auf dem Host-System zu speichern und direkt in den Container einzubinden. Sie sind
  nützlich für die Entwicklung oder wenn Sie spezifische Pfade auf Ihrem Host-System nutzen möchten.

### 4. **tmpfs Mounts:**

- tmpfs Mounts werden hauptsächlich für temporäre Daten verwendet, die nicht auf den Host persistiert werden sollen.

## Verwendung von Volumes

### 1. **Erstellen eines Volumes:**

```bash
docker volume create mein-volume
```
TODO: der Fachbegriff "Volume" ist mir unklar
Dieser Befehl erstellt ein neues Volume namens `mein-volume`.

### 2. **Einen Container mit einem Volume starten:**

```bash
docker run -d -v mein-volume:/pfad/im/container mein-image
```

Startet einen Container und bindet `mein-volume` an einen Pfad im Container.
TODO: Sowas tauchte vorher schon mal auf. Kann das dann da entfernt werden?

## Verwendung von Bind Mounts

### **Starten eines Containers mit einem Bind Mount:**

```bash
docker run -d -v /pfad/auf/host:/pfad/im/container mein-image
```

Bindet einen Pfad auf dem Host-System in den Container ein.

## Best Practices für die Datenspeicherung

### 1. **Datenverlust vermeiden:**

- Verwenden Sie Volumes oder Bind Mounts für alle Daten, die persistent gespeichert werden sollen.

### 2. **Sicherheit:**

- Achten Sie auf die Sicherheit der Daten, insbesondere wenn sensible Informationen gespeichert werden.

### 3. **Backup und Wiederherstellung:**
TODO: Ich finde solche anweisungen schwierig so ohne weiteres zu formulieren. das war jetzt schon öfter
Gut wäre es wenn man dazu schreibt, "wenn sie mehr mit Docker arbeiten, beachten sie..." oder so...
- Implementieren Sie Strategien für das Backup und die Wiederherstellung von Volumes, um Datenverlust zu verhindern.

### 4. **Volume-Management:**

- Überwachen und verwalten Sie Ihre Volumes regelmäßig, um sicherzustellen, dass sie wie erwartet funktionieren.

## Unterschied zwischen Docker Volumes und Bind Mounts

### Docker Volumes

#### 1. **Verwaltung durch Docker:**

- Volumes werden von Docker verwaltet und gespeichert. Sie befinden sich auf dem Host-System, aber der genaue
  Speicherort wird von Docker kontrolliert und ist für den Benutzer abstrahiert.

#### 2. **Isolation vom Host-System:**

- Volumes sind vom Host-Dateisystem isoliert. Dies bedeutet, dass sie nicht direkt einem bestimmten Verzeichnis auf
  dem Host zugeordnet sind.

#### 3. **Verwendung im Container:**

- Wenn ein Volume einem Container zugewiesen wird, wird es an einen spezifischen Pfad im Container gemountet. Der
  Container kann dann in dieses Volume schreiben und lesen, als ob es sich um ein lokales Verzeichnis im Container
  handelt.
- Änderungen, die im Volume vorgenommen werden, bleiben erhalten, auch wenn der Container gestoppt oder gelöscht
  wird.

#### 4. **Beispiel:**

   ```bash
   docker volume create mein-volume
   docker run -d -v mein-volume:/app/data mein-image
   ```
TODO; ich glaube jetzt verstehe ich es langsam. Vllt die erklärung zu volume nach oben packen.
In diesem Beispiel wird `mein-volume` an `/app/data` im Container gemountet. Daten, die in `/app/data` geschrieben
werden, werden im Volume gespeichert.

### Bind Mounts

#### 1. **Direkte Zuordnung zum Host-Dateisystem:**

- Bei einem Bind Mount wird ein spezifischer Pfad oder Verzeichnis auf dem Host-System direkt in den Container
  eingebunden.

#### 2. **Keine Verwaltung durch Docker:**

- Im Gegensatz zu Volumes werden Bind Mounts nicht von Docker verwaltet. Sie sind direkt an das Host-Dateisystem
  gebunden.

#### 3. **Verwendung im Container:**

- Wenn ein Bind Mount verwendet wird, kann der Container direkt auf den gemounteten Pfad des Host-Systems zugreifen
  und dort Daten lesen und schreiben.
- Änderungen, die im Bind Mount vorgenommen werden, sind sofort auf dem Host-System sichtbar und umgekehrt.

#### 4. **Beispiel:**

 ```bash
 docker run -d -v /pfad/auf/host:/app/data mein-image
 ```

Hier wird der Pfad `/pfad/auf/host` des Host-Systems an `/app/data` im Container gemountet.

### Zusammenfassung

- **Volumes:** Ideal für die Speicherung von Daten, die von Docker verwaltet werden sollen, und wenn Sie eine klare
  Trennung zwischen Host und Container wünschen.
- **Bind Mounts:** Nützlich, wenn Sie direkten Zugriff auf das Host-Dateisystem benötigen oder Daten zwischen Host und
  Container synchronisieren möchten.

In beiden Fällen ermöglichen diese Methoden der Datenspeicherung, dass Daten im Container persistent gespeichert werden
können, unabhängig vom Lebenszyklus des Containers selbst.
