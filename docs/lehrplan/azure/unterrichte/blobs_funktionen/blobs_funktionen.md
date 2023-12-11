# Blobs und Funktionen

- Datenspeicherung mit Azure Speicherkonten
  - Buckets & Blobs
  - Dateihandling und Upload

- Microtasks mit Azure Functions
  - Konzept
  - Event trigger
  

## Aufgaben
[60 min]

### Deployment einer simplen Flask API 🌶️🌶️
Erstelle eine Simple Flask API mit GET-Route die bei Request ein "Hallo Welt!" zurückgibt. Deploye die API als Azure Web App.


## Komplex-Aufgabe: Simples Excel Zeittracking (2er Teams) 🌶️🌶️🌶️🌶️🌶️
Simpler Dokumentupload für eine Zeiterfassungs-Excel Dokument in folgendem Format:
|Woche|M|D|M|D|F|
|-|-|-|-|-|-|
|1|8|7|9|9|5|
|2|8|7|9|9|5|
|3|8|7|9|9|5|
|4|8|7|9|9|5|

Zeit: 180 min 

Sobald das Dokument im Blob Store liegt, wird eine Azure Funktion getriggert, die die Stunden pro Woche summiert und die Über- oder Fehlstunden für den angegebenen Monat anzeigt.