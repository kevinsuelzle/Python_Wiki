## Komplexere CSS Konzepte 
In der modernen Webentwicklung sind fortgeschrittene CSS-Konzepte entscheidend, um responsive und benutzerfreundliche Webseiten zu erstellen. Zwei Schlüsselkonzepte in diesem Bereich sind das Responsive Design, realisiert durch Techniken wie Flexbox, und Frameworks wie Bootstrap, die eine Vielzahl von vorgefertigten Komponenten und Layout-Optionen bieten.

### Responsive CSS
Responsive CSS ist der Ansatz, Webseiten so zu gestalten, dass sie auf verschiedenen Geräten und Bildschirmgrößen gut aussehen und funktionieren. Das wird durch den Einsatz von Media Queries und flexiblen Layouts erreicht. Beide Konzepte haben wir bereits kurz besprochen.

#### Media Queries (Rückblick)
Media Queries ermöglichen es, CSS-Regeln basierend auf bestimmten Bedingungen wie Bildschirmgröße, Auflösung oder Seitenverhältnis anzuwenden.
Im folgenden Beispiel wird die Klasse `.container` auf Geräten mit einer maximalen Bildschirmbreite von 600px auf die volle Breite gesetzt.

```css
@media (max-width: 600px) {
    .container {
        width: 100%;
    }
}
```

#### Flexible Layouts

**`grid`-Layouts**: Moderne CSS-Grid-Layouts ermöglichen komplexe, mehrspaltige Anordnungen, die sich dynamisch an die Bildschirmgröße anpassen.

**`flexbox`**: Flexbox ist ein eindimensionales Layoutmodell, das effiziente Möglichkeiten bietet, Elemente innerhalb eines Containers auszurichten und zu verteilen.

#### Responsive Design mit Flexbox
Flexbox ist ein mächtiges Werkzeug, das ein flexibles Box-Modell zur Verfügung stellt.

**`flex`-Container**: Ein Element, das mit `display: flex;` definiert wird, wird zum Flex-Container, und seine Kinder werden zu `flex-items`.

**Responsive Anpassung**: Flexbox kann außerdem mit Media Queries kombiniert werden, um responsive Layouts zu erstellen.

**Ausrichtung und Verteilung**: Flexbox bietet Eigenschaften wie justify-content, align-items, flex-direction, die es ermöglichen, die Inhalte sowohl horizontal als auch vertikal auszurichten und anzuordnen. Im folgenden Beispiel wird ein Flex-Container erstellt, dessen Kinder gleichmäßig im verfügbaren Raum verteilt werden.

```css
.container {
    display: flex;
    justify-content: space-between;
}
```

### Bootstrap
Während traditionelles CSS umfangreiche Kontrolle und Flexibilität bietet, erleichtert Bootstrap den Prozess erheblich, insbesondere für Entwickler, die schnell responsive Layouts und Komponenten implementieren möchten. Bootstrap ist ideal für schnelle Entwicklungen und Prototyping, während traditionelles CSS besser für maßgeschneiderte Designs und spezifische Stilbedürfnisse geeignet ist. Beide Ansätze haben ihre Stärken und Einsatzbereiche in der Webentwicklung.

Um die Vorteile von Bootstrap im Vergleich zum traditionellen CSS zu verstehen, ist es hilfreich, einige der Kernkonzepte und Anwendungsfälle zu betrachten.

#### 1. Grid-System

**Bootstrap** verwendet ein 12-Spalten-Grid-System, das auf Flexbox basiert. Es ermöglicht eine einfache und schnelle Erstellung von responsiven Layouts.
Im folgenden Beispiel erstellt die Klasse `col-md-6` zwei Spalten, die jeweils 50% der Containerbreite einnehmen, wenn der Bildschirm mittelgroß (`md`) oder größer ist.

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">Linke Hälfte</div>
    <div class="col-md-6">Rechte Hälfte</div>
  </div>
</div>
```

Mit **traditionellem CSS** muss das Grid-System manuell erstellt werden, was mehr Aufwand und detailliertere Kenntnisse in CSS erfordert. Der folgende CSS-Code bewirkt eine ähnliche Aufteilung in zwei Spalten, erfordert jedoch eine explizite Definition der Flexbox-Eigenschaften.

```css
.container > .row {
  display: flex;
}
.container > .row > div {
  flex: 0 0 50%;
}
```

#### 2. Komponenten
**Bootstrap** bietet eine Vielzahl von vorgefertigten Komponenten wie Buttons, Navigationsleisten und Modals, die einfach durch das Hinzufügen von Klassen genutzt werden können. Im folgenden Beispiel wird ein stilisierten Button mit geringem Aufwand erstellt.

```html
<button class="btn btn-primary">Primary Button</button>
```

Im **traditionellen CSS** muss jede Eigenschaft des Buttons manuell definiert werden. Folgend der Stil für einen ähnlichen Button definiert, aber mit deutlich mehr Code.

```css
.button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```

#### 3. Responsive Design
**Bootstrap** beinhaltet Hilfsklassen für die schnelle Implementierung von responsivem Design, wie das Anzeigen oder Verbergen von Inhalten auf bestimmten Bildschirmgrößen. Diese Bootstrap-Klassen machen das Element auf kleinen Bildschirmen unsichtbar und auf mittelgroßen oder größeren Bildschirmen sichtbar.

```html
<div class="d-none d-md-block">Nur auf mittelgroßen oder größeren Bildschirmen sichtbar</div>
```

Im **traditionellen CSS** werden Media Queries verwendet, um ähnliche responsive Verhaltensweisen zu erzielen. Dieser Code erreicht das gleiche Ziel, erfordert jedoch ein tieferes Verständnis von Media Queries und mehr Zeilen an Code.

```css
@media screen and (min-width: 768px) {
  .custom-class {
    display: block;
  }
}
@media screen and (max-width: 767px) {
  .custom-class {
    display: none;
  }
}
```

## Aufgaben
[90 min]

### Responsive Card-Layout mit Flexbox 🌶️
Erstelle ein responsives Card-Layout mit Flexbox, das Produkte oder Dienstleistungen darstellt.

- Jede "Card" sollte ein Bild, eine Überschrift, einen kurzen Text und einen Button enthalten.
- Verwende Flexbox, um die Cards nebeneinander in einer Zeile anzuordnen.
- Implementiere Media Queries, damit sich das Layout auf kleineren Bildschirmen anpasst (z.B. die Cards untereinander statt nebeneinander).

### Erstellung eines responsiven Menüs mit Bootstrap 🌶️🌶️
Erstelle eine Navigationsleiste mit Bootstrap, die auf kleineren Bildschirmen zu einem Hamburger-Menü wird.

- Nutze Bootstrap-Klassen, um eine Navigationsleiste mit Links zu erstellen.
- Implementiere das Hamburger-Menü für kleinere Bildschirme mithilfe von Bootstrap's eingebautem JavaScript.

### Fortgeschrittenes Grid-Layout mit CSS Grid 🌶️🌶️🌶️
Erstelle ein komplexes Grid-Layout mit dem CSS Grid-System, um Inhalte wie einen Blog oder eine Nachrichtenseite anzuordnen.

- Verwende das CSS Grid-System, um einen Hauptbereich und mehrere Nebenbereiche zu erstellen.
- Nutze unterschiedliche grid-template-columns und grid-template-rows, um ein vielseitiges Layout zu gestalten.
- Setze Media Queries ein, um das Layout für verschiedene Bildschirmgrößen anzupassen.

[Lösungen](./solutions.md)