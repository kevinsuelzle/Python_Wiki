## Komplexere HTML Elemente
[60 min]

Für die Erstellung des Tagesprojektes und komplexeren Websites benötigen wird noch weitere, interaktivere HTML Elemente.

### `<form>`
Definiert ein Formular, das vom Benutzer ausgefüllt werden kann. Wird zusammen mit anderen Formular-Elementen wie `<input>`, `<textarea>` und `<button>` verwendet.

```html
<form action="/submit-form" method="post">
  <input type="text" name="name">
  <input type="submit" value="Absenden">
</form>
```

### `<input>`
Eines der vielseitigsten Formularelemente, das verschiedene Arten von Benutzereingaben akzeptiert, wie Text, Datum, Dateiauswahl und mehr.

```html
<input type="text" name="vorname" placeholder="Gib deinen Vornamen ein">
<input type="password" name="passwort" placeholder="Gib dein Passwort ein">
<input type="email" name="email" placeholder="Gib deine E-Mail-Adresse ein">
<input type="number" name="alter" placeholder="Gib dein Alter ein">
<input type="date" name="geburtstag">
<input type="checkbox" name="newsletter" value="Ja"> Newsletter abonnieren
<input type="file" name="lebenslauf">
<input type="range" name="lautstärke" min="0" max="100">
```

### `<table>`
Wird verwendet, um tabellarische Daten darzustellen. Zusammen mit `<tr>` (table row), `<th>` (table header) und `<td>` (table data) für die Strukturierung der Tabelle.

```html
<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Daten 1</td>
    <td>Daten 2</td>
  </tr>
</table>
```

### `<button>`
Ein klickbares Button-Element, das in Formularen oder zum Auslösen von JavaScript-Funktionen verwendet wird.

```html
<button type="button" onclick="alert('Hallo Welt!')">Klick mich</button>
```

### `<iframe>`
Ermöglicht das Einbetten eines anderen HTML-Dokuments innerhalb des aktuellen Dokuments, oft verwendet für Karten, Videos oder externe Inhalte.

```html
<iframe src="https://www.beispiel.de" width="300" height="200"></iframe>
```

### `<br>`
Ein Zeilenumbruch, der verwendet wird, um einen neuen Absatz zu beginnen, ohne einen neuen <p>-Tag zu verwenden.

```html
Dies ist eine Zeile.<br>Und das ist eine neue Zeile.
```

### `<meta>`
Wird im `<head>`-Bereich eingesetzt, um Metadaten wie Zeichensatz, Beschreibung, Schlüsselwörter und Autor der Seite anzugeben. Wichtig für SEO und die Darstellung der Seite in Suchmaschinen.

```html
<meta charset="UTF-8">
<meta name="description" content="Beschreibung der Webseite">
```

### `<label>`
Das `<label>`-Tag wird verwendet, um Beschriftungen für Formularelemente bereitzustellen. Es verbessert die Zugänglichkeit, indem es die Klickfläche für die assoziierten Formularelemente wie Checkboxen, Radiobuttons oder Textfelder vergrößert. Im folgenden Beispiel wird ein `<label>` für ein Textfeld mit der ID `name` verwendet. Klickt man auf das Label, wird das zugehörige Textfeld fokussiert.

```html
<label for="name">Name:</label>
<input type="text" id="name" name="name">
```

### `<select>` und `<option>`
Das `<select>`-Element erstellt ein Dropdown-Menü zur Auswahl.
Das `<option>`-Element definiert die einzelnen verfügbaren Auswahlmöglichkeiten innerhalb des Dropdown-Menüs.

Im folgenden Beispiel können Benutzer aus verschiedenen Automarken wählen. Das `<select>`-Element enthält mehrere `<option>`-Elemente, die die verfügbaren Optionen darstellen.

```html
<label for="car">Wähle ein Auto:</label>
<select id="car" name="car">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```

### `<script>`
Das `<script>`-Tag wird verwendet, um JavaScript-Code in eine HTML-Seite einzubinden. Dies kann entweder direkt in das Element geschriebener Code sein oder eine externe JavaScript-Datei, die über das src-Attribut eingebunden wird.

```html
<!-- Direkte Einbindung von JavaScript -->
<script>
  function sayHello() {
    alert('Hallo Welt!');
  }
</script>

<!-- Einbindung einer externen JavaScript-Datei oder CDN URL -->
<script src="script.js"></script>
```

## Aufgaben
[90 min]

### Kontaktformular mit Validierung 🌶️️
Erstelle ein Kontaktformular mit verschiedenen Eingabefeldern und füge einfache Validierung hinzu.

- Das Formular sollte Felder für Namen, E-Mail, Nachricht und einen „Absenden“-Button enthalten.
- Verwende `<input type="text">` für den Namen, `<input type="email">` für die E-Mail und `<textarea>` für die Nachricht.
- Füge required-Attribute hinzu, um sicherzustellen, dass alle Felder ausgefüllt werden müssen.
- Implementiere ein Dropdown-Menü (`<select>`) für die Auswahl eines Betreffs.

### Tabellarische Darstellung von Daten 🌶️️🌶️️
Erstelle eine Tabelle, die Daten dynamisch darstellt.

- Nutze das `<table>`-Element, um eine Tabelle mit mindestens 4 Spalten (z.B. Produktname, Preis, Kategorie, Bewertung) zu erstellen.
- Jede Zeile der Tabelle soll ein Produkt repräsentieren.
- Füge Kopfzeilen mit `<th>`-Elementen hinzu und nutze `<td>` für die Datenzellen.
- Optional: Style die Tabelle mit CSS, um sie visuell ansprechender zu gestalten.

### Integration einer OpenStreetMap-Karte mit `<iframe>` 🌶️️🌶️️🌶️️
Integriere eine interaktive Karte von OpenStreetMap auf der Webseite.

- Verwende das `<iframe>`-Element, um eine OpenStreetMap-Karte einzubetten.
- Die Karte sollte einen spezifischen Ort anzeigen, z.B. eine Stadt oder eine bekannte Sehenswürdigkeit. Im Beispiel wird die Karte auf den Koordinaten 51.324/7.712 zentriert sein.
- Passe die Größe des `<iframe>` an, um sicherzustellen, dass die Karte gut in das Layout der Webseite passt.
- Füge zusätzliche Informationen oder Anweisungen neben der Karte hinzu, z.B. Wegbeschreibungen oder interessante Orte in der Nähe.

[Lösungen](./solutions.md)