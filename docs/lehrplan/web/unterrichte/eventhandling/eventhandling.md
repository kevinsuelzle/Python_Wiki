### Eventhandler
[60 min]

Events sind Aktionen oder Vorkommnisse, die im Browser stattfinden und von JavaScript erkannt werden können. Diese können Benutzerinteraktionen wie Klicks, Mausbewegungen, Tastendrücke oder auch Systemereignisse wie das Laden einer Seite sein.

**`click`-Event**: Wird ausgelöst, wenn der Benutzer auf ein Element klickt.

```javascript
document.getElementById("meinButton").onclick = function() {
    alert("Button geklickt!");
};
```

**`hover`-Event**: Wird ausgelöst, wenn der Mauszeiger über ein Element bewegt wird.

```javascript
document.getElementById("meinElement").onmouseover = function() {
    console.log("Maus ist über dem Element");
};
```

#### Event Listeners
Um über JavaScript beliebige Event Listener einzubauen, gibt es die `addEventListener` Methode. Hiermit können DOM-Element mit variablem Eventhandling verbunden werden.

Hinzufügen eines `click`-Listeners
```javascript
let button = document.getElementById("meinButton");
button.addEventListener("click", function() {
    console.log("Button wurde geklickt!");
});
```

Reaktion auf ein Tastatur `keydown`-Event:
```javascript
document.addEventListener("keydown", function(event) {
    console.log("Taste gedrückt: " + event.key);
});
```

#### Event Propagation: Bubbling und Capturing
Event Propagation bezeichnet den Weg, den ein Event durch den DOM-Baum nimmt. Es gibt zwei Phasen: Bubbling und Capturing.

Bei komplexen Benutzeroberflächen mit verschachtelten Elementen ermöglicht Event Propagation z.B. dass in einem Menü das Klicken auf ein Untermenü-Element spezielle Aktionen auslösen, während ein Klick auf das Hauptmenü andere Aktionen ausführt.

**Bubbling**: Events "blubbern" von dem Element, das das Event auslöst, bis zum Root-Element des DOM.

```javascript
document.getElementById("kindElement").addEventListener("click", function() {
    console.log("Kind-Element geklickt!");
}, false); // False für Bubbling-Phase
```
**Capturing**: Events werden zuerst auf dem höchsten Level des DOM abgefangen, bevor sie zum auslösenden Element heruntergehen.

```javascript
document.getElementById("elternElement").addEventListener("click", function() {
    console.log("Eltern-Element geklickt!");
}, true); // True für Capturing-Phase
```


### DOM-Manipulation
Im vorherigen Kapitel haben wir bereits das DOM kennen gelernt und verstanden, dass es aus einer Baumstruktur besteht, die die Website aus Eltern- und Kindbeziehungen modelliert.

```css
        html
      /    \
    /        \
  head         body
    |         /  |  \
  title header section footer
            /     /  \     \
          h1     p   img    p
```

#### Elementauswahl und -manipulation
**`getElementById`**: Greift auf ein Element basierend auf seiner ID zu.

```javascript
document.getElementById("meinElement").innerHTML = "Geänderter Text";
```

**``querySelector``**: Ermöglicht eine feinere Auswahl mit CSS-Selektoren.
  
```javascript
document.querySelector(".meineKlasse").style.color = "blau";
```

**`createElement`**: Erstellt dynamisch neue Elemente und fügt diese in den DOM-Baum ein.

```javascript
let neuerAbsatz = document.createElement("p");
neuerAbsatz.innerText = "Ein neuer Absatz";
document.body.appendChild(neuerAbsatz);
```

**`removeChild`**: Enfernt Elemente aus dem DOM.

```javascript
let zuEntfernendesElement = document.getElementById("zuEntfernen");

zuEntfernendesElement.parentNode.removeChild(zuEntfernendesElement);
```

## Aufgaben
[60 min]

### Toggle-Schalter 🌶️️
Erstelle einen Button, der bei jedem Klick die Farbe eines Div-Elements zwischen Rot und Grün wechselt.

### Dynamische Liste 🌶️️🌶️️
Erstelle ein Formular, das es Benutzern ermöglicht, Elemente zu einer Liste hinzuzufügen.

### Tastatur-Event-Handler 🌶️️🌶️️
Erstelle eine Anwendung, die auf Tastendrücke reagiert und eine Aktion ausführt.

### Bildergalerie mit Hover-Effekt 🌶️️🌶️️🌶️️
Erstelle eine Bildergalerie, bei der das Überfahren eines Bildes mit der Maus Informationen zum Bild anzeigt.

## Komplex-Aufgaben
[45 min]

### Drag-and-Drop-Interface 🌶️️🌶️️🌶️️🌶️️🌶️️
Implementiere eine Drag-and-Drop-Funktionalität, bei der Elemente auf der Seite verschoben werden können.

- Erstelle mehrere draggable Elemente und einen Drop-Bereich.
- Verwende `drag`- und `drop`-Events, um die Elemente innerhalb des Drop-Bereichs zu bewegen.


[Lösungen](./solutions.md)

