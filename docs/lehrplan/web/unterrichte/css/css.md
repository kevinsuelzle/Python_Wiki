# CSS
[90 min]

Um die grobe Struktur der angelegten HTML Seite (`index.html`) im zweiten Schritt mit einem Designlayout zu verbessern, nutzen wir ein CSS Stylesheet.

## Wie verbinde ich HTML und CSS
CSS kann auf verschiedene Arten in HTML-Dokumente eingebunden werden, die gängigsten sind Inline-Styling und das Verlinken externer CSS-Dateien.

### Inline-Styling
Inline-Styling bedeutet, dass der CSS-Code direkt im HTML-Tag über das style-Attribut eingefügt wird. Jedes HTML-Element kann individuell gestaltet werden, aber diese Methode wird oft als weniger effizient angesehen, besonders bei größeren Webseiten, da sie die Wartung und Konsistenz erschweren kann.

```html
<p style="color: blue; font-size: 18px;">Dies ist ein Absatz mit Inline-Styling.</p>
```

### Externes CSS-Dokument
Eine andere, oft bevorzugte Methode ist das Einbinden von externen CSS-Dateien. Hierbei wird der CSS-Code in separaten `.css`-Dateien geschrieben und dann im `<head>`-Bereich des HTML-Dokuments über das `<link>`-Tag eingebunden. Diese Methode fördert die Wiederverwendbarkeit und erleichtert die Pflege des Codes, da der Stil von mehreren Seiten aus einer zentralen Datei gesteuert werden kann.

**`styles.css`**
```css
p {
    color: blue;
    font-size: 18px;
}
```

**`index.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <p>Dies ist ein Absatz, der durch eine externe CSS-Datei gestaltet wird.</p>
</body>
</html>
```

## Box-Modell
Das Box-Modell ist ein grundlegendes Konzept in CSS und beschreibt, wie Elemente auf der Seite dargestellt und positioniert werden.

Jedes Element wird als Rechteck dargestellt, das aus `margin` (Außenabstand), `border` (Rahmen), `padding` (Innenabstand) und dem eigentlichen Inhalt besteht.

```css
.box {
    width: 100px;             /* Breite des Inhalts */
    padding: 10px;            /* Innenabstand */
    border: 5px solid black;  /* Rahmen */
    margin: 20px;             /* Außenabstand */
}

+-------------------------------+
|           Margin              |
|  +-------------------------+  |
|  |        Border           |  |
|  |  +-------------------+  |  |
|  |  |     Padding       |  |  |
|  |  |  +-------------+  |  |  |
|  |  |  |   Content   |  |  |  |
|  |  |  +-------------+  |  |  |
|  |  +-------------------+  |  |
|  +-------------------------+  |
+-------------------------------+
```

### Positionierung
Die Platzierung und Orientierung von Elementen auf einer Website ist für das Layoutdesign essentiell. CSS bietet verschiedene Möglichkeiten, Elemente auf der Seite zu positionieren.

**`static`**: Standard-Positionierung, bei der Elemente in der normalen Flussordnung angezeigt werden.

**`relative`**: Positioniert ein Element relativ zu seiner ursprünglichen Position.

**`absolute`**: Positioniert ein Element absolut innerhalb eines relativ positionierten Elternelements.

**`fixed`**: Positioniert ein Element relativ zum Viewport, es bleibt also bei Scrollen an der gleichen Stelle.

**`sticky`**: Eine Mischung aus relativer und fester Positionierung. Das Element "klebt" beim Scrollen an der bestimmten Position.

## Selektoren
Selektoren sind Muster, die definieren, welche HTML-Elemente durch die CSS-Regeln gestaltet werden.

### Tag-Selektoren
Selektieren HTML-Elemente direkt. Folgendes Beispiel wendet den Stil auf alle `<p>`-Elemente an.

```css
p { 
  color: blue; 
}
```

### Klassen-Selektoren (`.`)
Selektieren Elemente basierend auf dem class-Attribut. Folgendes Beispiel wendet den Stil auf alle Elemente mit der Klasse `navbar` an.

```css
.navbar { 
  font-size: 14px; 
}
```

### ID-Selektoren (`#`)
Selektieren ein spezifisches Element basierend auf dem id-Attribut. Folgendes Beispiel wendet den Stil auf das Element mit der ID `header` an.

```css
#header { 
  background-color: #333; 
}
```

### Attribut-Selektoren (`[type=]`)
Selektieren Elemente basierend auf einem Attribut oder Attributwert. Folgendes Beispiel selektiert alle Texteingabefelder.

```css
input[type='text'] { 
  border-color: red; 
}
```

### Pseudo-Klassen und Pseudo-Elemente (`:`)
Selektieren Elemente in einem bestimmten Zustand oder bestimmte Teile eines Elements. Folgendes Beispiel ändert die Farbe von Links beim Überfahren mit der Maus.

```css
a:hover { 
  color: red; 
}
```

## Kombinatoren
Kombinatoren definieren Beziehungen zwischen Selektoren.

### Nachfahren-Selektor (` `)
Selektiert alle Elemente, die innerhalb eines anderen Elements liegen. Folgendes Beispiel wählt alle `<p>` innerhalb von `<div>`.

```css
div p { 
  color: green; 
}
```

### Kind-Selektor (`>`)
Selektiert direkte Kinder eines Elements. Folgendes Beispiel wählt direkte `li`-Kinder von `ul`.

```css
ul > li { 
  list-style-type: square; 
}
```

### Nachbar-Selektor (`+`)
Selektiert ein Element, das direkt auf ein anderes folgt. Folgendes Beispiel wählt das erste `<p>` direkt nach einem `<h1>`.

```css
h1 + p { 
  margin-top: 0; 
}
```

### Geschwister-Selektor (`~`)
Selektiert alle Elemente auf dem gleichen Level nach einem bestimmten Element. Folgendes Beispiel wählt alle `<p>`, die auf dem gleichen Level nach einem `<h1>` stehen.

```css
h1 ~ p { 
  font-size: 14px; 
}
```

## CSS Attribute
Auch für CSS schauen wir uns eine kurze Auflistung einiger relevanter CSS Attribute und deren Verwendung an, die in bei den kommenden Aufgaben helfen werden.

### Schriftart definieren (`font-family`)
Legt die Schriftart für den Text im body fest und sorgt für eine einheitliche Schriftart auf der gesamten Webseite.

```css
body {
    font-family: Arial, sans-serif;
}
```

### Hintergrundfarbe und Textfarbe (`background-color`, `color`)
`background-color` wird verwendet, um die Hintergrundfarbe des header festzulegen, während `color` die Textfarbe bestimmt.

```css
header {
    background-color: #4CAF50;
    color: white;
}
```

### Textausrichtung (`text-align`)
Bestimmt, wie Text innerhalb eines Elements ausgerichtet wird, hier zentral im header und footer.

```css
header, footer {
    text-align: center;
}
```

### Padding (`padding`)
Definiert den Abstand zwischen dem Inhalt eines Elements und seinem Rand und verbessert den visuellen Abstand und die Ästhetik von Elementen.

```css
header {
    padding: 10px 0;
}
```

### Listen-Styling (`list-style-type`, `margin`)
Entfernt Bullet Points von Listen und setzt Außen- und Innenabstände und erzeugt z.B. eine saubere Navigationsleiste.

```css
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
```

### Float-Layout (`float`)
Bestimmt, wie ein Element im Fluss des Dokuments schwimmt. Hier werden z.B. li-Elemente nebeneinander statt untereinander angeordnet.

```css
nav ul li {
    float: left;
}
```

### Hyperlink-Styling (`text-decoration`, `:hover`):
Entfernt die Unterstreichung von Links und definiert Hover-Effekte, was die Benutzerinteraktion mit Links verbessern kann.

```css
nav ul li a {
    text-decoration: none;
}
nav ul li a:hover {
    background-color: #111;
}
```

### Border und Border-Radius (`border`, `border-radius`)
Definiert die Art und das Aussehen der Ränder eines Elements und erzeugt z.B. abgerundete Ecken und Grenzlinien für Bilder.

```css
.gallery img {
    border: 1px solid #ddd;
    border-radius: 4px;
}
```

### Flexbox (`display: flex`, `justify-content`)
Flexbox ist ein modernes Layout-Modell, das die Anordnung von Elementen in einem Container erleichtert. Im Beispiel werden Bilder in einer Galerie gleichmäßig verteilt.

```css
.gallery {
    display: flex;
    justify-content: space-around;
}
```

### Responsive Design mit Media Queries (`@media`)
Passt das Layout an basierend auf der Größe des Browserfensters oder Gerätes an und gewährleistet so, dass die Webseite auf verschiedenen Geräten gut aussieht.

```css
@media screen and (max-width: 600px) {
    .gallery {
        flex-direction: column;
    }
}
```

## Aufgaben
[60 min]

### Grundlegendes CSS-Styling 🌶️🌶️**
Wende grundlegende CSS-Styles auf die Komplex-Aufgabe von HTML an, um das visuelle Erscheinungsbild der Webseite zu verbessern. Dies umfasst die Farbgebung, Schriftarten und grundlegende Layout-Anpassungen.

- Erstelle und verlinke eine CSS-Datei mit Ihrem HTML-Dokument.
- Setze eine Hintergrundfarbe und Textfarbe für den Header.
- Gestalte den Footer mit einer anderen Hintergrundfarbe und zentriertem Text.

### Navigationsleiste stylen 🌶️
Nutze CSS, um die Navigationsleiste horizontal anzuordnen und die Links ansprechend zu gestalten.

### Bildergalerie für Automodelle stylen 🌶️🌶️
Verwende CSS, um die Bilder nebeneinander anzuordnen und ästhetisch zu rahmen.

### Responsive Design 🌶️🌶️🌶️
Passe das Design der Webseite an, damit sie auf verschiedenen Bildschirmgrößen und Geräten gut aussieht und funktioniert. Dies ist ein wichtiger Schritt, um die Zugänglichkeit und Benutzerfreundlichkeit der Website zu gewährleisten.

- Implementiere CSS-Media-Queries, um das Layout der Seite für kleinere Bildschirme wie Smartphones und Tablets anzupassen.
Stell sicher, dass die Navigationsleiste und die Bildergalerie auch auf kleineren Bildschirmen gut aussehen und nutzbar sind.

[Lösungen](./solutions.md)




