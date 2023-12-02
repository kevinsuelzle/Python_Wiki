# Tag 2 - APIs Bauen

Inhalt:

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

    - Aufgaben 1 + 2

    - Flask Advanced
      - Restful API Designs
      - Routen
      - Data Handling
      - Fehler Codes
      - CURL + Postman & Python Requests Testing
        - Wie testet man einfach APIs? (Rückblick Testing 4-5)
        - Repeatable Testing mit Postman

    - Aufgaben 3 + 4


## Aufgaben
Zeit: 5-10 min / Aufgabe
1. **Hello World Flask & Django API**: In Gruppen von 2, erstellt jeweils einen GET Endpunkt der den Text "Hallo Welt!" als Response zurückgibt in Flask und Django.
2. **Reflexionsrunden Django vs Flask**: Vergleicht gemeinsam die Lesbarkeit, Einfachheit und den Syntax der beiden Frameworks.
3. **Simple GET API Tested with Postman**:
4. **CRUD-API with Python Requests Test + Mocked API**: 


## Komplex-Aufgaben (Capstone Projekt)
**Todo CLI mit Postman Tests**

API, über die der Benutzer Aufgaben mit Titel und Fälligkeitsdatum erstellen und ihre To-Do-Liste verwalten können.

Zeit: 30-45 min 

- Postman Test Requests (GET, POST, PUT, DELETE)
- User CRUD-API
- SQL Datenbank als Speicher


## Weiterführende Materialien
- **Rate Limiting**: API Einschränkungen mit dem offiziellen [Flask Limiter Extension](https://flask-limiter.readthedocs.io/en/stable/)