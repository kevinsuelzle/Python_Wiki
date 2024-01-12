### Fetch API in JavaScript
[60 min]

Auch für JavaScript gibt es die Möglichkeit, eigene und externe APIs anzusprechen. Die `fetch`-API ermöglicht es, wie mit `requests` in Python, HTTP-Anfragen zu stellen und Antworten und Fehler zu handeln.

Ein wesentlicher Unterschied zwischen Python und JavaScript ist, dass `requests` in Python **synchron** ist, während die Fetch API in JavaScript **asynchron** arbeitet.

#### Asynchrone Anfragen und asynchrone Programmierung
Asynchrone Anfragen sind wichtig, um Daten im Hintergrund zu laden, ohne die Benutzeroberfläche zu blockieren. In JavaScript wird dies oft über `Promises` und das `Async/Await`-Pattern realisiert.

**`Promises`**: Ein Promise ist ein Objekt, das für einen Wert steht, der in der Zukunft verfügbar sein könnte. Es kann sich in einem von drei Zuständen befinden: erfüllt, abgelehnt oder ausstehend.

```javascript
fetch('https://api.example.com/data')
    .then(data => console.log('Geladene Daten:', data))
    .catch(error => console.error('Fehler:', error));
```

**`Async/Await`**: Ist eine moderne Art, asynchronen Code zu schreiben. `async` markiert eine Funktion als asynchron, und `await` wartet auf das Ergebnis eines Promises.

```javascript
try {
    let response = await fetch('https://api.example.com/data');

    let data = await response.json();
    console.log('Geladene Daten:', data);
} catch (error) {
    console.error('Fehler:', error);
}
```

#### Requests mit der Fetch API
Die Fetch API bietet natürlich, wie Python `requests`, zugang zu allen HTTP-Methoden wie GET, POST, PUT und DELETE.

`GET`
```javascript
fetch('https://api.example.com/data')
  .then(data => console.log('Geladene Daten:', data))
  .catch(error => console.error('Fehler:', error));
```

`POST`
```javascript
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({name: 'Neuer Eintrag'})
})
  .then(response => response.json())
  .then(data => console.log(data));
```

#### Error Handling
Durch die Struktur der `fetch`-API und der Nutzung vom `Promise`-Modell ist die Fehlerbehandlung durch die `.catch`-Funktion bereits gegeben.

```javascript
fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Netzwerkantwort nicht ok');
        }
        return response.json();
    })
    .catch(error => console.error('Fetch-Fehler:', error));
```


## Aufgaben
[60 min]

### Abrufen und Anzeigen von Header-Informationen 🌶️️🌶️️
Verwende JavaScript, um eine GET-Anfrage an die JSON-Placeholder API zu senden und die Header der Antwort anzuzeigen.

### Aktuelle Wetterdaten abrufen 🌶️️🌶️️
Verwende die Fetch API, um aktuelle Wetterdaten von der [Open-Meteo API](https://open-meteo.com/) abzurufen und in der Konsole anzuzeigen.

### Wetteranfrage basierend auf Benutzereingabe 🌶️️🌶️️🌶️️
Erstelle eine interaktive Benutzeroberfläche, bei der Benutzer einen Standort eingeben können und das Wetter für diesen Ort angezeigt wird.

## Anspruchsvolle Aufgaben
[45 min]

### Wettervorhersage für mehrere Tage abrufen 🌶️️🌶️️🌶️️🌶️️
Entwickle eine Anwendung, die eine 7-Tage-Wettervorhersage für einen eingegebenen Standort liefert.

- Sende eine GET-Anfrage an die Open-Meteo API, um die 7-Tage-Wettervorhersage für den angegebenen Standort zu erhalten.
- Zeige die Wettervorhersage (z.B. Temperatur, Wetterbedingungen) für jeden Tag auf der Webseite an.

[Lösung](./solutions.md)

