# Tag 2 - APIs Bauen

### Inhalt
- Wie baut man eine API?
  - Wie funktionieren APIs intern?
    - Flussdiagram
    - API Architektur Prinzipien
      - JSON (und XML)
    - Deployment (Ausblick)
      - Cloud (Azure)
      - Docker
    - Flask & Django
      - Intro & Unterschiede
      - Beispiele
        - Hallo Welt der APIs
          - Live-Coding zur Demonstration der "Einfachheit"
        - localhost / HTTP(S) Server
          - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
            - Ports

    - Flask Advanced
      - Restful API Designs
      - ORMs
      - Routen
      - Data Handling
      - Fehler Codes
      - Postman & Python Requests Testing
        - Wie testet man einfach APIs? (Rückblick Testing 4-5)
        - Postman Collections Repeatable Testing mit Postman

# Wie baut man eine API?
... todo


## Tagesprojekt
Ziel des heutigen Tages ist es, eine Wetterabfrage mit Python in einer CLI Anwendung zu integrieren und informationen zum Wetter einer Stadt zu bekommen.

![Projekt](../assets/)



## Wie funktionieren APIs intern?
... todo


## API Architektur Prinzipien
- JSON (und XML)


### Deployment (Ausblick)
- Cloud (Azure)
- Docker

# Web API Frameworks
## Flask & Django
- Intro & Unterschiede
- Beispiele
  - Hallo Welt der APIs
    - Live-Coding zur Demonstration der "Einfachheit"
  - localhost / HTTP(S) Server
    - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
      - Ports
- Intro & Unterschiede
- Beispiele
  - Hallo Welt der APIs
    - Live-Coding zur Demonstration der "Einfachheit"
  - localhost / HTTP(S) Server
    - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
      - Ports

## Aufgaben
Zeit: 10-15 min / Aufgabe
1. **Hello World Flask & Django API**: In Gruppen von 2, erstellt jeweils einen GET Endpunkt der den Text "Hallo Welt!" als Response zurückgibt in Flask und Django.
2. **Reflexionsrunden Django vs Flask**: Vergleicht gemeinsam die Lesbarkeit, Einfachheit und den Syntax der beiden Frameworks.
3. **GET API**: ...todo
4. **Simple CRUD Api**: ...todo

# Flask Advanced
- Restful API Designs
  - Planning
- ORMs
- Routen
- Data Handling
- Fehler Codes
- Postman & Python Requests Testing
  - Wie testet man einfach APIs? (Rückblick Testing 4-5)
  - Postman Collections Repeatable Testing mit Postman

## Komplex-Aufgabe (Capstone Projekt)
**CRUD Inventory Management API**

- Start with Planning
  - Integration Test-Driven
  - Postman Tests
- Flask

API, über die der Benutzer Aufgaben mit Titel und Fälligkeitsdatum erstellen und ihre To-Do-Liste verwalten können.

Zeit: 45-60 min 

- Postman Test Requests (GET, POST, PUT, DELETE)
- User CRUD-API
- SQL Datenbank als Speicher


## Weiterführende Materialien
- **Rate Limiting**: API Einschränkungen mit dem offiziellen [Flask Limiter Extension](https://flask-limiter.readthedocs.io/en/stable/)