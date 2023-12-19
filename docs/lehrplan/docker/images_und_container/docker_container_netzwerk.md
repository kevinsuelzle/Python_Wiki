# Netzwerk und Kommunikation in Docker
TODO: scheinbar ist hier alles entscheidend. Vllt können diese Formulieren am anfang raus/relativiert werden.
Das Verständnis von Netzwerk und Kommunikation ist entscheidend für die effektive Nutzung von Docker, insbesondere wenn
es um die Verbindung von Containern untereinander und mit der Außenwelt geht. In diesem Kapitel werden wir die
Grundlagen des Docker-Netzwerks und die verschiedenen Optionen zur Netzwerkkonfiguration erkunden.

## Grundlagen des Docker-Netzwerks

Docker verwendet verschiedene Netzwerk-Treiber, um die Kommunikation zwischen Containern zu ermöglichen. Die
gängigsten sind `bridge`, `host` und `overlay`.

| Netwerktyp | Erklärung                                                                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bridge`   | Das Standardnetzwerk für Docker-Container. Jeder Container, der diesem Netzwerk hinzugefügt wird, erhält eine eigene IP-Adresse, wodurch eine interne Netzwerkkommunikation ermöglicht wird. |
| `host`     | Container, die im Host-Netzwerkmodus laufen, teilen sich den Netzwerk-Stack des Hosts. Dies ist nützlich für Dienste, die auf dem Host-Netzwerk sichtbar sein müssen.                        |
| `overlay`  | Wird in Docker-Swarm-Umgebungen verwendet, um eine Netzwerkkommunikation zwischen Containern auf verschiedenen Docker-Hosts zu ermöglichen.                                                  |

## Netzwerkkommunikation und Port-Weiterleitung

1. **Port-Weiterleitung:**
    - Docker ermöglicht die Weiterleitung von Ports vom Host-System zu Containern, was den Zugriff auf Anwendungen
      innerhalb von Containern von außerhalb ermöglicht.

2. **Container-zu-Container-Kommunikation:**
    - Container innerhalb desselben Netzwerks können über ihre internen IP-Adressen oder Container-Namen kommunizieren.

TODO: vllt mal ein einfaches bild einfügen hier, um dinge zu erklären?

## Praktische Beispiele

- **Erstellen eines Bridge-Netzwerks und Verbinden von Containern:**
  ```bash
  docker network create mein-bridge-netzwerk
  docker run -d --network=mein-bridge-netzwerk --name container1 nginx
  docker run -d --network=mein-bridge-netzwerk --name container2 nginx
  ```
  Dieses Beispiel zeigt, wie man ein benutzerdefiniertes Bridge-Netzwerk erstellt und zwei Container darin startet.
TODO: im letzten abschnitt gabe es bereits sowas. soll es da vllt gelöscht werden?

- **Port-Weiterleitung für einen Webserver:**
  ```bash
  docker run -d -p 8080:80 --name mein-webserver nginx
  ```
  Startet einen Nginx-Webserver-Container und leitet den Port 8080 des Hosts auf den Port 80 des Containers um.
TODO: weiß immer noch nicht, was Nginx ist.
TODO: das mit den verschiedenen Ports sollte noch mal auf einem Bild erklärt werdne.
## Netzwerksicherheit

- **Firewall-Regeln und Netzwerk-Policies:**
    - Es ist wichtig, Firewall-Regeln und Netzwerk-Policies zu implementieren, um den Zugriff auf Container-Dienste zu
      kontrollieren. **TODO: was genau meinst du damit? Firewalls auf dem Hostsystem oder innerhalb des Containers?**

- **Sichere Kommunikation:**
    - Für sensible Anwendungen sollten Sie sichere Kommunikationsprotokolle wie HTTPS verwenden, um Datenübertragungen
      zu schützen.

## Zusammenfassung

Das Verständnis von Netzwerk und Kommunikation in Docker ist entscheidend für das Design und die Verwaltung von
containerisierten Anwendungen. Durch die Nutzung verschiedener Netzwerk-Treiber und -Optionen können Sie eine effiziente
und sichere Kommunikation zwischen Ihren Containern sowie zwischen Containern und der Außenwelt sicherstellen. Die
praktischen Beispiele bieten eine Grundlage, um diese Konzepte in realen Anwendungsfällen anzuwenden.

# Todo Beispiele zeigen erstellen
TODO: JA!