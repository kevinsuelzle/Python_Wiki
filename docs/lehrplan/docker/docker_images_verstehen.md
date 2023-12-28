# Einführung in Docker-Images

Docker-Images sind die Grundbausteine in der Docker-Technologie. Kurz gesagt sind sie schreibgeschützte Vorlagen,
die die Anweisungen zur Erstellung eines Docker-Containers enthalten. Ein Docker-Image beinhaltet alles, was für das
Ausführen einer Anwendung benötigt wird – den Code, eine Laufzeitumgebung, Bibliotheken, Umgebungsvariablen und
Konfigurationsdateien.

## Was ist ein Docker-Image?

Ein Docker-Image ist vergleichbar mit einer Blaupause für einen Container oder, um es mehr computertechnisch
auszudrücken, eine Klasse.

Es ist eine leichte, eigenständige, ausführbare Software, die eine spezifische Umgebung für eine Anwendung bereitstellt.
Wenn ein Container gestartet wird, wird das Docker-Image als Basis verwendet, um eine laufende Instanz – den Container –
zu erstellen. Das ist in etwa so zu verstehen, als würde eine Instanz aus einer Klasse erstellt werden.

## Merkmale von Docker-Images

1. **Unveränderlichkeit:** Einmal erstellt, wird ein Image nicht mehr verändert. Änderungen erfolgen durch Erstellen
   eines neuen Images, das auf dem bestehenden Image basiert.

2. **Schichtung und Wiederverwendung:** Docker-Images bestehen aus Schichten. Jede Schicht repräsentiert eine Reihe von
   Unterschieden zum vorherigen Image. Diese Schichtung ermöglicht es, gemeinsame Basen zu nutzen und Speicherplatz
   effizient zu verwenden.

   Die Schichtung kommt zustande, indem die Befehle zur Herstellung des Containers zu seiner aktuellen Form nacheinander
   abgearbeitet werden. Diese Befehle werden in einer Datei gesammelt: `Dockerfile` ohne Endung.

   So sieht das Laden von Images in der Konsole aus. Man erkennt, wie die einzelnen Schichten nach und nach dazu kommen:

[//]: # (TODO: iframe einbauen)

3. **Effizienz:** Durch die Wiederverwendung von Schichten sind Docker-Images sehr effizient in Bezug auf Speicherplatz
   und Geschwindigkeit. Änderungen an einem Image erfordern nur das Herunterladen der geänderten Schichten.

4. **Portabilität:** Docker-Images können auf jedem System ausgeführt werden, das Docker unterstützt, unabhängig von der
   zugrunde liegenden Infrastruktur. Dies gewährleistet Konsistenz über verschiedene Umgebungen hinweg.

[//]: # ()

[//]: # (TODO: Ich könnte diese Aufgabe jetzt nicht wirklich beantworten, außer die obigen Punkte zu wiederholen. )

[//]: # (   - stimmt, mehr soll es auch gar nicht sein. Deswegen auch nur ein Chilli. Wiederholen mit eigenen Worten festigt das Wissen.)

[//]: # ()

[//]: # (TODO: Aufgaben haben die Form: ### Aufgabe: Überschrift mit Chillis, in der nächsten Zeile dann den Aufgabentext.)

[//]: # (   - ok)

### **Aufgabe: Definition 🌶️**

Was ist ein Docker Image ist und welche Merkmale zeichnet es aus.


### **Aufgabe: Definition 🌶️**

Was ist der Unterschied zwischen Image und Container?