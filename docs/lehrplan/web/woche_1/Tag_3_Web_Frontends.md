# Tag 3 - Simple Web Frontends

Inhalt:

- API-Recap 
  - Fragerunde (Fragen 1-5)
  - Hinter "fast jeder" Website steckt ein Backend

- Wie entsteht eine Website?
  - Web Basics
    - Websites Building Blocks
      - Das Dokument Objekt Model (DOM) 
      - Anschauen einer Website mit den Webtools
        - Elemente
        - Console
        - Cookies & Localstorage
    - HTML, CSS, JS
      - Markup (HTML, XML) Vergleich Markdown
    - HTTP(S)
    - Web-Accessibility

  - HTML Deep Dive
    - Die wichtigsten Tags
    - CSS 
        - Basics

    - Formulare
    - Responsive CSS 
      - Responsive Design
        - Flexbox
      - Bootstrap


# API-Recap 
Hinter fast jeder modernen Website oder Webanwendung steht ein Backend, das häufig über eine API (Application Programming Interface) mit dem Frontend kommuniziert. 

## Fragen
Zeit: 1-2 min / Frage
1. Was ist eine API und warum ist sie wichtig?
2. Beschreibe das Prinzip einer RESTful API
3. Was sind die Hauptunterschiede zwischen Flask und Django?
4. Wie kann die Sicherheit einer API gewährleistet werden?
5. Warum ist die Dokumentation einer API wichtig?
6. Wie werden Daten in einer RESTful API übertragen und welche Formate werden typischerweise verwendet?
7. Welche Rolle spielen HTTP-Statuscodes in einer RESTful API und wie sollten sie verwendet werden?


# Wie entsteht eine Website?
...

## Tagesprojekt
Ziel des heutigen Tages ist es, eine eigene RESTful FLASK API mit CRUD Funktion für das Management von Stellplätzen in einer Garage zu erstellen und diese mit einer Postman Collection zu testen.

![Projekt](../assets/postman_crud_collection.png)


## Web Basics
    - Websites Building Blocks
      - Das Dokument Objekt Model (DOM) 
      - Anschauen einer Website mit den Webtools
        - Elemente
        - Console
        - Cookies & Localstorage
    - HTTP(S)
    - Web-Accessibility
    
## HTML
- Markup (HTML, XML) Vergleich Markdown

## CSS

## JS

## Aufgaben
Zeit: 5-10 min / Aufgabe

**1. Grundstruktur der Automobil-Website**
Erstelle das Grundgerüst einer HTML-Seite für ein Automobilunternehmen. Diese Seite soll als Basis für die weiteren Schritte dienen und die grundlegenden Elemente wie Header, Hauptinhalt und Footer enthalten.
Anforderungen:

- Füge einen Header (`<header>`) mit dem Namen des Unternehmens ein.
- Im Hauptteil (`<body>`) soll ein Absatz (`<p>`) mit einer kurzen Beschreibung des Unternehmens stehen.
- Der Footer (`<footer>`) soll Kontaktinformationen wie eine E-Mail-Adresse enthalten.

**2. Grundlegendes CSS-Styling**
Wende grundlegende CSS-Styles an, um das visuelle Erscheinungsbild der Webseite zu verbessern. Dies umfasst die Farbgebung, Schriftarten und grundlegende Layout-Anpassungen.

- Erstelle und verlinke eine CSS-Datei mit Ihrem HTML-Dokument.
- Setze eine Hintergrundfarbe und Textfarbe für den Header.
- Gestalte den Footer mit einer anderen Hintergrundfarbe und zentriertem Text.

**3. Navigationsleiste**
Erweitere die Website um eine Navigationsleiste, die eine verbesserte Benutzerführung ermöglicht. Diese Leiste soll Links zu verschiedenen Abschnitten der Webseite enthalten.
Anforderungen:

- Füge im Header eine Navigationsleiste (`<nav>` mit `<ul>` und `<li>`) hinzu.
- Erstelle Links zu fiktiven Seiten wie "Home", "Modelle" und "Kontakt".
- Nutze CSS, um die Navigationsleiste horizontal anzuordnen und die Links ansprechend zu gestalten.

**4. Bildergalerie für Automodelle**
Erstelle eine Bildergalerie, die verschiedene Modelle des Autoherstellers präsentiert. Ziel ist es, visuellen Content ansprechend zu integrieren.

- Füge unterhalb der Unternehmensbeschreibung eine Bildergalerie ein.
- Nutze `<img>`-Tags für mindestens drei verschiedene Automodelle.
- Verwende CSS, um die Bilder nebeneinander anzuordnen und ästhetisch zu rahmen.

**5. Responsive Design**
Passe das Design der Webseite an, damit sie auf verschiedenen Bildschirmgrößen und Geräten gut aussieht und funktioniert. Dies ist ein wichtiger Schritt, um die Zugänglichkeit und Benutzerfreundlichkeit der Website zu gewährleisten.

- Implementiere CSS-Media-Queries, um das Layout der Seite für kleinere Bildschirme wie Smartphones und Tablets anzupassen.
Stell sicher, dass die Navigationsleiste und die Bildergalerie auch auf kleineren Bildschirmen gut aussehen und nutzbar sind.

### Musterlösungen
<details>
  <summary>1. Grundstruktur der Automobil-Website</summary>

  ```html
  <!DOCTYPE html>
<html>
<head>
    <title>Mein Autohersteller</title>
</head>
<body>
    <header>
        <h1>Mein Autohersteller</h1>
    </header>
    <p>Willkommen bei Mein Autohersteller, dem Ort für innovative Fahrzeuge.</p>
    <footer>
        Kontakt: info@meinautohersteller.de
    </footer>
</body>
</html>
  ```
</details>

<details>
  <summary>2. Grundlegendes CSS-Styling</summary>

  ```css
  body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 10px 0;
}

footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 10px 0;
}
  ```
</details>

<details>
  <summary>3. Navigationsleiste</summary>

  ```html
  <nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Modelle</a></li>
        <li><a href="#">Kontakt</a></li>
    </ul>
</nav>
  ```

  ```css
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

nav ul li {
    float: left;
}

nav ul li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

nav ul li a:hover {
    background-color: #111;
}
  ```
</details>

<details>
  <summary>4. Bildergalerie für Automodelle</summary>

  ```html
  <div class="gallery">
    <img src="auto1.jpg" alt="Auto Modell 1">
    <img src="auto2.jpg" alt="Auto Modell 2">
    <img src="auto3.jpg" alt="Auto Modell 3">
</div>
  ```

  ```css
  .gallery {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.gallery img {
    width: 30%;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
}
  ```
</details>

<details>
  <summary>5. Responsive Design</summary>

  ```css
  @media screen and (max-width: 600px) {
    nav ul, .gallery {
        flex-direction: column;
    }

    .gallery img {
        width: 100%;
    }
}
  ```
</details>

<details>
  <summary>Ganzes Aufgabe</summary>
  
  ```html
  <!DOCTYPE html>
<html>
<head>
    <title>Mein Autohersteller</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <header>
        <h1>Mein Autohersteller</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Modelle</a></li>
                <li><a href="#">Kontakt</a></li>
            </ul>
        </nav>
    </header>
    <p>Willkommen bei Mein Autohersteller, dem Ort für innovative Fahrzeuge.</p>
    <div class="gallery">
        <img src="auto1.jpg" alt="Auto Modell 1">
        <img src="auto2.jpg" alt="Auto Modell 2">
        <img src="auto3.jpg" alt="Auto Modell 3">
    </div>
    <footer>
        Kontakt: info@meinautohersteller.de
    </footer>
</body>
</html>
  ```

  ```css
  body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 10px 0;
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

nav ul li {
    float: left;
}

nav ul li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

nav ul li a:hover {
    background-color: #111;
}

.gallery {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.gallery img {
    width: 30%;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
}

footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 10px 0;
}

@media screen and (max-width: 600px) {
    nav ul, .gallery {
        flex-direction: column;
    }

    .gallery img {
        width: 100%;
    }
}
  ```
</details>

<br />


# HTML Deep Dive

## Die wichtigsten Tags
    - Formulare

## CSS 
  - Basics
  - Responsive CSS 
      - Responsive Design
        - Flexbox
      - Bootstrap





## Komplex-Aufgabe (Capstone Projekt)
**Webseite für Testfahrten mit einem VW-Fahrzeug**
> Zeit: 30-45 min 

Das Ziel dieses Projekts ist es, eine benutzerfreundliche Webseite zu erstellen, die es potenziellen Kunden ermöglicht, eine Testfahrt für ein VW-Fahrzeug zu buchen. Die Webseite soll ein intuitives Formular enthalten, das neben grundlegenden persönlichen Informationen auch die Auswahl des Fahrzeugmodells, des Wunschtermins und der Uhrzeit für die Testfahrt bietet.

**Anforderungen**
- Formular für Testfahrt-Buchung
  - Ein Formular zur Eingabe persönlicher Daten wie Name und E-Mail-Adresse.
  - Dropdown-Menü zur Auswahl des Fahrzeugmodells (z.B. Golf, Passat, Tiguan).
  - Datumswähler für den Wunschtermin der Testfahrt.
  - Zusätzliches Dropdown-Menü zur Auswahl der Uhrzeit für die Testfahrt mit 1-Stunden-Slots zwischen 10:00 und 17:00 Uhr.

- Styling mit Bootstrap:
  - Verwendung von Bootstrap, um das Formular und die gesamte Webseite ansprechend und responsiv zu gestalten.
  - Sichergestellt werden soll eine klare, intuitive Benutzeroberfläche, die die Benutzererfahrung verbessert.

- Reaktionsfähiges Design:
  - Die Webseite sollte auf verschiedenen Geräten gut aussehen und funktionieren, einschließlich Desktop-Computern, Tablets und Smartphones.
  - Anwendung von Responsive Design-Prinzipien, um eine optimale Darstellung auf verschiedenen Bildschirmgrößen zu gewährleisten.

**Bonus**
- **Dark Mode**: Erstelle einen Dark Mode für die Webseite, der nur mit CSS umgeschaltet werden kann, z.B. durch den Einsatz von CSS Custom Properties (CSS-Variablen).
- **Buchungstabelle**: Füge eine zusätzliche Platzhaltertabelle mit allen gebuchten Testfahrten an.
- **Visuelle Fahrzeugliste**: Füge weitere Fahrzeugmodelle zur Auswahl hinzu und zeige dem Nutzer je nach Wahl das Fahrzeug.

**Ressourcen**
- [Bootstrap Dokumentation](https://getbootstrap.com/docs/)
- [HTML Formulare - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Forms?retiredLocale=de)
- [CSS Grundlagen - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics?retiredLocale=de)

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
</head>
<body>
    <div class="container">
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
</details>


## Weiterführende Materialien
- **CSS Flexbox Game**: CSS Flexbox einfach lernen mit dem [Flexbox Froggy Web Game](https://flexboxfroggy.com/#de)
- **Web Security Basics**: Kurzer Überblick über potentielle Risiken in den [Mozilla Security Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Website_security)