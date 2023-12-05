# Tag 4 - Advanced Web Frontends

Inhalt:

- Website Basics-Recap 

- Wie werden Websites Interaktiv?
    - JS
      - Basics
      - Eventhandler
      - DOM-Manipulation
      - Fetch API

  - Web applications and static websites
    - JavaScript außerhalb des Browsers
    - Rendering (Ausblick)
      - Templates (Flask)
    - Server-Side vs. Client-Side
      - React
      - Vue

# Website Basics-Recap 
...

## Fragen
Zeit: 1-2 min / Frage
1. Was ist der Zweck des `<div>`-Elements in HTML?
2. Wie unterscheiden sich Klassen- und ID-Selektoren in CSS?
3. Was ist das Box-Modell in CSS und welche Komponenten beinhaltet es?
4. Wie unterscheidet sich das Flexbox-Layout von traditionellen Layout-Techniken in CSS?
5. Was sind die Hauptfunktionen von Bootstrap als CSS-Framework?
6. Wie funktioniert responsives Design mit Media Queries?
7. Wozu dient das `<label>`-Element in HTML und wie wird es richtig eingesetzt?
8. Was ist der Unterschied zwischen Inline-Styling und externen CSS-Stylesheets?
9.  Erkläre die Funktionsweise und Anwendung von `<select>` und `<option>` in HTML.
10. Wie kann JavaScript in ein HTML-Dokument eingebunden werden?


# Wie werden Websites Interaktiv?
...


## Tagesprojekt
Ziel des heutigen Tages ist es, die simple Website zum Buchen von Testfahrten mit verschiedenen VW-Fahrzeugen mit Funktionalität zu erweitern und die gebuchten Fahrten, anstelle einer Flask API Integration, im Local Storage zu speichern.

![Projekt](../assets/js_kalender_testfahrt.png)


## Interaktivität mit JavaScript
- JS
  - Basics
    - Syntax und Struktur: Einführung in die Grundlagen von JavaScript, inklusive Variablen, Datentypen, Operatoren und Kontrollstrukturen (wie Schleifen und Verzweigungen).
    - Funktionen: Verständnis der Definition und Verwendung von Funktionen, einschließlich des Unterschieds zwischen benannten Funktionen und Arrow Functions.
    - Objekte und Arrays: Umgang mit komplexen Datentypen und deren Methoden zur Datenmanipulation.
  - Eventhandler
    - Event Handling Basics: Erläuterung von Events (wie Clicks, Hover) und wie JavaScript darauf reagieren kann.
    - Event Listeners: Verwendung von addEventListener zur Reaktion auf Benutzeraktionen.
    - Event Propagation: Verstehen der Event-Weiterleitung (Bubbling und Capturing).
  - DOM-Manipulation
    - Was ist das DOM? (Recap): Einführung in das Document Object Model (DOM) als Struktur des Webdokuments.
    - Elementauswahl und -manipulation: Verwendung von Methoden wie getElementById, querySelector zum Auswählen und Manipulieren von DOM-Elementen.
    - Dynamische Inhaltsänderung: Erstellen, Ändern und Löschen von DOM-Elementen zur Laufzeit.
  - Fetch API
    - Asynchrone Anfragen: Verstehen der Bedeutung von asynchronem Code in JavaScript, insbesondere im Kontext von Webanfragen.
    - Verwendung der Fetch API: Durchführen von HTTP-Anfragen, Umgang mit Promises und Verarbeitung der Antwortdaten.
    - Error Handling: Behandlung von Fehlern bei der Datenabfrage und Fehlerbehandlungsmethoden.

- Modernes JavaScript (ES6+): Einführung in moderne JavaScript-Features wie Template Literals, Destructuring, Spread Operator.

- Asynchrone Programmierung: Vertiefung in asynchrone Muster wie Promises, Async/Await.

- JavaScript Frameworks und Libraries: Einblick in beliebte Frameworks und Bibliotheken wie React, Vue oder Angular zur Erstellung komplexer Anwendungen.

- Modularität: Verständnis von JavaScript-Modulen und deren Einsatz zur Strukturierung größerer Codebasen.

- Web APIs: Erkundung weiterer Web-APIs, die JavaScript zur Interaktion mit Browserfunktionen und -hardware nutzen kann.

- Debugging und Tools: Einführung in Debugging-Techniken und die Nutzung von Entwicklerwerkzeugen in Browsern.

- Static Websites


## Aufgaben
Zeit: 5-10 min / Aufgabe
1. **Einfache JavaScript Alert-Box**: Implementiert ein einfaches JavaScript-Skript, das beim Laden der Webseite eine Alert-Box anzeigt, die "Hallo Welt!" enthält.

2. **Dynamische Textänderung mit JavaScript**: Fügt ein HTML-Element hinzu (z.B. ein `<p>`-Tag) und verwendet JavaScript, um den Text dieses Elements beim Klicken auf einen Button zu ändern. Zum Beispiel könnte der Text von `"Vor dem Klick"` zu `"Nach dem Klick"` geändert werden.

3. **Einfaches Formular mit Event Listener**: Erstellt ein einfaches HTML-Formular mit einem Texteingabefeld und einem Submit-Button. Verwendet JavaScript, um einen Event Listener hinzuzufügen, der den eingegebenen Text in einer Alert-Box anzeigt, wenn das Formular abgesendet wird.

4. **Einfache DOM-Manipulation**: Implementiert eine Funktion, die ein HTML-Element (z.B. eine Liste) dynamisch basierend auf JavaScript-Array-Daten ändert. Beispielsweise könnte ein Array von Farbnamen verwendet werden, um eine Liste von farbigen Div-Elementen zu erstellen.

5. **Einsatz der Fetch API für eine einfache HTTP-Anfrage**: Schreibt ein JavaScript-Skript, das eine `GET`-Anfrage an eine öffentliche API (wie die [Wetter API](https://open-meteo.com/)) sendet und das Ergebnis in der Konsole oder auf der Webseite anzeigt.

### Musterlösungen
<details>
  <summary>1. Einfache JavaScript Alert-Box</summary>

  ```html
  <!DOCTYPE html>
<html>
<head>
    <title>Einfache Alert-Box</title>
</head>
<body>
    <script>
        alert("Hallo Welt!");
    </script>
</body>
</html>
  ```
</details>

<details>
  <summary>2. Dynamische Textänderung mit JavaScript</summary>

  ```html
  <!DOCTYPE html>
<html>
<head>
    <title>Dynamische Textänderung</title>
</head>
<body>
    <p id="text">Vor dem Klick</p>
    <button onclick="changeText()">Text ändern</button>

    <script>
        function changeText() {
            document.getElementById("text").innerHTML = "Nach dem Klick";
        }
    </script>
</body>
</html>
  ```
</details>

<details>
  <summary>3. Einfaches Formular mit Event Listener</summary>

  ```html
  <!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <title>Formular mit Event Listener</title>
</head>
<body>
    <form id="meinFormular">
        <input type="text" id="eingabefeld">
        <input type="submit" value="Absenden">
    </form>

    <script>
        document.getElementById("meinFormular").addEventListener("submit", function(event){
            event.preventDefault();
            alert(document.getElementById("eingabefeld").value);
        });
    </script>
</body>
</html>
  ```
</details>

<details>
  <summary>4. Einfache DOM-Manipulation</summary>

  ```html
  <!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <title>DOM Manipulation</title>
</head>
<body>
    <div id="farbenListe"></div>

    <script>
        const farben = ["Rot", "Grün", "Blau"];
        const liste = document.getElementById("farbenListe");

        farben.forEach(farbe => {
            const element = document.createElement("div");
            element.innerText = farbe;
            liste.appendChild(element);
        });
    </script>
</body>
</html>
  ```
</details>

<details>
  <summary>5. Einsatz der Fetch API für eine einfache HTTP-Anfrage</summary>

  ```html
  <!DOCTYPE html>
<html>
<head>
    <title>Fetch API Wetteranfrage</title>
</head>
<body>
    <div id="wetterdaten"></div>

    <script>
        const apiUrl = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.405&hourly=temperature_2m';

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const wetterdaten = JSON.stringify(data, null, 2);
                document.getElementById("wetterdaten").innerText = wetterdaten;
            })
            .catch(error => console.error('Fehler:', error));
    </script>
</body>
</html>
  ```
</details>


## Modern Web Applications
### Responsive Design und JavaScript
   - **Grundlagen des responsiven Webdesigns**: Einführung in Media Queries, flexible Layouts und responsive Bilder.
   - **JavaScript im responsiven Design**: Einsatz von JavaScript zur dynamischen Anpassung von Layouts, Inhalten und Funktionen basierend auf der Gerätegröße und -orientierung.
   - **Frameworks und Bibliotheken**: Vorstellung von Tools und Frameworks wie Bootstrap, die JavaScript verwenden, um responsives Design zu unterstützen.

### JavaScript außerhalb des Browsers
   - **Einführung in Node.js**: Geschichte, Aufbau und Kernkonzepte von Node.js.
   - **NPM und Module**: Umgang mit dem Node Package Manager (NPM) und Erstellung eigener Module.
   - **Serverseitige Programmierung**: Erstellen einfacher serverseitiger Anwendungen mit Node.js und Express.

### Rendering (Ausblick)
   - **Client-Side vs. Server-Side Rendering**: Vor- und Nachteile beider Ansätze.
   - **Universelles (Isomorphic) Rendering**: Konzepte und Techniken für das Rendern von Webseiten sowohl auf dem Server als auch auf dem Client.
   - **Single Page Applications (SPA)**: Funktionsweise und Implementierung mit Fokus auf das Rendering-Verhalten.

### Templates (Flask)
   - **Template-Engines in Flask**: Einführung in Jinja2 und die Grundlagen der Template-Erstellung.
   - **Dynamische Inhalte in Templates**: Verwendung von Flask-Route-Daten in Templates zur Erzeugung dynamischer Webseiten.
   - **Template-Vererbung**: Effiziente Nutzung von Template-Vererbung zur Strukturierung des Webseiten-Layouts.

### Server-Side vs. Client-Side
   - **Vergleich der Architekturen**: Vor- und Nachteile von Server-Side- und Client-Side-Rendering.
   - **Moderne JavaScript-Frameworks und -Bibliotheken**: 
      - **React**: Grundlagen, JSX, Komponenten, State Management (z.B. mit Hooks).
      - **Vue**: Einführung in Vue, dessen reaktives System, und wie es für den Aufbau interaktiver UIs verwendet wird.

### Ergänzende Themen
   - **Progressive Web Apps (PWA)**: Prinzipien und Techniken zur Erstellung von PWAs mit Service Workers und Manifest-Dateien.
   - **Modernes Frontend-Build-Management**: Einführung in Tools wie Webpack und Babel für die Optimierung und das Bundling von JavaScript-Dateien.
   - **Echtzeit-Anwendungen mit WebSockets**: Entwicklung von Echtzeit-Kommunikationsmechanismen zwischen Client und Server.


## Komplex-Aufgaben (Capstone Projekt)
**Interaktive Website für Testfahrten mit einem VW-Fahrzeug**
Zeit: 60-90 min 

Das Ziel dieses Projektes ist es, die zuvor erstellte HTML + CSS Website mit interaktivität zu versehen. Die Nutzer sollen einen vollen Kalender sehen, die dynamisch mit neuen Testfahrten befüllt wird. Anstelle einer echten Flask API sollen gebuchte Fahrten im Local Storage des Browsers gespeichert werden.
Außerdem soll bei Klick auf die einzelnen Tage angezeigt werden, wer die jeweilige Fahrt gebucht hat.

**Anforderungen**
- Überlege eine passende Struktur um die Form-Daten im Local Storage zu speichern
- Nutzer Event-Listener um den Namen der Testfahrt bei Klick auf eine existierende Buchung anzuzeigen 
- Nutze die [FullCalendar](https://fullcalendar.io/docs) Javascript Library um eine interaktive Ansicht einzubauen.
- Implementiere eine Funktion, die den Kalender automatisch aktualisiert, wenn neue Buchungen hinzugeefügt werden.
- Stell sicher, dass die Nutzer gültige und vollständige Informationen eingeben, bevor sie ihre Buchung abschicken.

**Bonus**
- **Design Upgrade**: Mache deine Website visuell noch schöner indem du mit einer richtigen Website-Struktur arbeitest. (Header, Farben, Logo)
- **Erweiterte Interaktivität**: Füge Funktionen wie die Möglichkeit hinzu, Buchungen zu bearbeiten oder zu löschen, direkt im Kalender.
- **Benutzer-Authentifizierung**: Implementiere eine Art von Benutzerverwaltung, damit Nutzer sich anmelden und nur ihre eigenen Buchungen verwalten können.
- **Flask API** Erstelle eine simple Flask API mit SQL Datenbank um die Testfahrten zu kommunizieren und persitieren.


**Ressourcen**
- [FullCalendar-Dokumentation](https://fullcalendar.io/docs)
- [JavaScript-Formularvalidierung](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

<details>
  <summary>Musterlösung</summary>

  ```html
  <!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VW Testfahrt Buchung</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
    <!-- FullCalendar CSS -->
    <link href='https://fullcalendar.io/js/fullcalendar-3.1.0/fullcalendar.min.css' rel='stylesheet' />
</head>
<body>
    <div class="container">
        <!-- Kalenderansicht hinzugefügt -->
        <div id='calendar'></div>

        <br />

        <h2>Buchen Sie Ihre Testfahrt</h2>
        <form id="testDriveForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" required>
            </div>
            <div class="form-group">
                <label for="email">E-Mail:</label>
                <input type="email" class="form-control" id="email" required>
            </div>
            <div class="form-group">
                <label for="model">Fahrzeugmodell:</label>
                <select class="form-control" id="model">
                    <option>Golf</option>
                    <option>Passat</option>
                    <option>Tiguan</option>
                </select>
            </div>
            <div class="form-group">
                <label for="date">Wunschtermin:</label>
                <input type="date" class="form-control" id="date" required>
            </div>
            <div class="form-group">
                <label for="time">Uhrzeit:</label>
                <select class="form-control" id="time">
                    <option>10:00</option>
                    <option>11:00</option>
                    <option>12:00</option>
                    <option>13:00</option>
                    <option>14:00</option>
                    <option>15:00</option>
                    <option>16:00</option>
                    <option>17:00</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Testfahrt buchen</button>
        </form>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.9/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <!-- FullCalendar JS -->
    <script src='https://fullcalendar.io/js/fullcalendar-3.1.0/lib/moment.min.js'></script>
    <script src='https://fullcalendar.io/js/fullcalendar-3.1.0/fullcalendar.min.js'></script>
    <script src="script.js"></script> <!-- Ihr eigenes JavaScript-Datei -->
</body>
</html>
  ```

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.container {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h2 {
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

.form-control {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    width: 100%;
}

.btn-primary {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.btn-primary:hover {
    background-color: #0056b3;
}
```

```js
document.getElementById('testDriveForm').addEventListener('submit', function(e){
    e.preventDefault();

    // Daten aus dem Formular extrahieren
    let booking = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        model: document.getElementById('model').value,
        date: document.getElementById('date').value,
        time: document.getElementById('time').value
    };

    // Speichern im Local Storage
    let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
    bookings.push(booking);
    localStorage.setItem('bookings', JSON.stringify(bookings));

    // Kalender aktualisieren
    $('#calendar').fullCalendar('renderEvent', {
        title: booking.name + ' - ' + booking.model,
        start: booking.date,
        allDay: true
    });
});

// Kalender initialisieren
$(document).ready(function() {
    $('#calendar').fullCalendar({
        height: 600,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        // Klick auf einen Tag im Kalender
        dayClick: function(date, jsEvent, view) {
            let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
            let bookingsOnDate = bookings.filter(booking => booking.date === date.format());
            let message = bookingsOnDate.map(booking => `${booking.name}, ${booking.model} um ${booking.time}`).join('\n');
            if (message) {
                alert(`Buchungen am ${date.format()}:\n\n${message}`);
            } else {
                alert('Keine Buchungen an diesem Datum.');
            }
        },
        // Buchungen aus Local Storage laden
        events: function(start, end, timezone, callback) {
            let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
            let events = bookings.map(booking => ({
                title: booking.name + ' - ' + booking.model,
                start: booking.date,
                allDay: true
            }));
            callback(events);
        }
    });
});
```
</details>

## Weiterführende Materialien
- **...**: ...