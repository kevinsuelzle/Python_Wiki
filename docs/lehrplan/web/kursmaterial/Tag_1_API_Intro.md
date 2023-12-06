# Tag 1 - APIs Intro

# Was ist eine API?
API steht für Application Programming Interface. APIs ermöglichen es Entwicklern, komplexe Funktionen zu nutzen, ohne diese von Grund auf neu entwickeln zu müssen. So können beispielsweise Entwickler einer Wetter-App die API eines Wetterdienstes nutzen, um aktuelle Wetterdaten abzurufen, anstatt selbst eine umfassende Wetterdateninfrastruktur aufzubauen


## Tagesprojekt
Ziel des heutigen Tages ist es, eine Wetterabfrage mit Python in einer CLI Anwendung zu integrieren und informationen zum Wetter einer Stadt zu bekommen.

![Wetter CLI Projekt](../assets/1_wetter_cli.png)

## Wie funktioniert eine API?
Vergleichen kann man eine API mit Kellner*innen und der Küche in einem Restaurant. Die zwei wichtigsten Komponenten sind die Anfrage (Request) und die Antwort (Response).

Im Fall des Restaurants ist die Küche ein System mit vielen Funktionen. Der Kellner (API) ist aber die einzige Möglichkeit mit der Küche zu kommunizieren. Was genau in der Küche passiert, wissen wir nicht.

Als Nutzer stellen wir eine Anfrage (Request) mit einer Auswahl (URI) an den Kellner (API). Der Kellner gibt die Anfrage weiter an die Küche (Server) und das liefert uns das fertige Produkt (Response) zurück. 

Auf die gleiche Weise ermöglicht eine API die Kommunikation zwischen verschiedenen Softwarekomponenten oder Programmen. Es werden Anfragen für spezifische Aktionen oder Daten übermittelt und Ergebnisse zurückgeliefert.


## API Beispiele
**[Wetter API](https://open-meteo.com/)**: Kostenlose API die es ermöglicht, aktuelle Wetterdaten und Forecasts zu Geocoordinaten zu erhalten.

**[Google Maps API](https://developers.google.com/maps/documentation/places/web-service?hl=de)**: API die es ermöglicht, Karten und geografische Daten auf einfache Weise in Websites oder Apps zu integrieren.

**[RapidAI](https://rapidapi.com/)**: Plattform mit großer tausenden APIs für verschiedene Anwendungszwecke. 


# Arten von APIs

Beim durchschauen verschiedener APIs kann es sein, dass man unterschiedliche API-Arten findet. Je nach Anforderung an Einsatzszenario, Skalierbarkeit und Performance in der Entwicklung gibt es unter anderen diese 3 Arten.

## REST (Representational State Transfer)
REST basiert auf den Prinzipien des HTTP-Protokolls und ist für Einfachheit und Leistungsfähigkeit bekannt.
So genannten "RESTful" APIs verwenden standardisierte HTTP-Methoden (GET, POST, PUT, DELETE) und sind zustandslos, was bedeutet, dass jede Anfrage unabhängig ist. Das bedeutet auch, dass z.B. keine Nutzerinformationen gespeichert werden.

Im vorherigen Kapitel zu Datenbanken haben wir bereits das Konzept CRUD kennen gelernt. Die grundlegenden Operationen in CRUD (Erstellen, Lesen, Aktualisieren, Löschen) lassen sich auf die HTTP-Methoden abbilden, die in RESTful APIs verwendet werden
- **Read** entspricht **GET**.
- **Create** in CRUD entspricht **POST** in REST.
- **Update** entspricht **PUT** oder PATCH.
- **Delete** entspricht **DELETE**.

**Beispiel**
Eine neue Bestellung aufgeben:

```js
HTTP-Methode: GET
URI: /essen/{gericht}
``````

Wichtig zu verstehen ist, dass die Struktur der Antwort vom Server ist fest definiert ist. Diese könnte z.B. so aussehen:
```js
"order": {
    "id": "1",
    "name": "Bolognese",
    "kellner_id": "25123",
    "zubereitungszeit": "350"
}
```


## GraphQL

Entwickelt von Facebook, ist GraphQL eine Umgebung und Abfragesprache für APIs, die es Nutzern ermöglicht, genau zu spezifizieren, welche Daten sie benötigen.
Im Gegensatz zu REST, bei dem der Server die Struktur der Antwort bestimmt, ermöglicht GraphQL dem Nutzer, die Struktur der Anfrage zu definieren. Das führt zu effizienteren und flexibleren API-Aufrufen.

Hierbei existiert eine Schema Definition durch die bekannt wird, welche Informationen abrufbar sind.

```js
type Bestellung {
  id: ID
  kellner_id: ID
  essen: [Essen]
  zubereitungszeit: INT
}

type Essen {
  id: ID
  name: String
}
```

Eine Abfrage mit gleichem Ergebnis wie beim RESTful Beispiel wäre dann:

```js
query {
  bestellung(id: "1") {
    id
    kellner_id
    essen {
      name
    }
    zubereitungszeit
  }
}
```

Und zu folgender Antwort führen würde:

```js
{
  "bestellung": {
    "id": "1",
    "kellner_id": "25123",
    "essen": [
      {
        "name": "Bolognese",
      }
    ],
    "zubereitungszeit": "350"
  }
}
```

## WebSockets

WebSockets sind eine weitere Möglichkeit zwischen Nutzer (Client) und Server zu kommunizieren. Anders als bei REST und GraphQL bieten Websockets eine dauerhafte Verbindung und ermöglichen Echtzeitdatenübertragung. Deshalb sind sie ideal für Anwendungen, die kontinuierliche Datenupdates benötigen.
Beispiele hierfür sind Chat-Anwendungen oder Online-Spiele.
Im Gegensatz zu HTTP, das eine unidirektionale Verbindung darstellt, ermöglichen WebSockets eine bidirektionale Kommunikation, sodass Server und Client Daten gleichzeitig senden und empfangen können.


# Wie "spricht" man mit einer API?
Die Kommunikation mit APIs kann auf verschiedene Weisen erfolgen. Einige der gängigen Methoden sind CURL, die Python Requests Library und Postman. Natürlich gibt es aber in jeder Programmiersprache die Möglichkeit mit APIs zu kommunizierne.

## CURL
CURL (Client URL) ist ein Command Line Tool, das verwendet wird, um Daten zwischen einem Server und einem Client über verschiedene Protokolle wie HTTP, HTTPS und FTP zu übertragen. Es ist besonders nützlich für das **Testen** und Interagieren mit APIs direkt von der Kommandozeile aus.

### Vorteile
Ein großer Vorteil ist die Plattformunabhängig. CURL ist sowohl für Windows, Mac und Linux verfügbar. Zusätzlich ist es extrem vielseitig und unterstützt eine Vielzahl von Protokollen. und ist sowit ideal für schnelle Tests und Debugging.

### Nachteile
Die Orientierung in der Kommandozeile kann für Anfänger eine Herausforderung darstellen. Zusätzlich kann die Nutzung bei komplexeren Anfragen schnell unübersichtlich werden. Außerdem fehlt eine grafische Benutzeroberfläche, was die Bearbeitung von Anfragen erschwert.

### Beispiel
```js
curl https://api.example.com/data
```

## Python Requests
Die Python Requests Library wird für das Senden von HTTP-Anfragen verwendet. Sie ist bekannt für ihre Benutzerfreundlichkeit.

### Vorteile
Die requests Library hat eine besonders einfache und intuitive Syntax und ermöglicht so, mit wenigen Zeilen Code auch komplexe Anfragen durchzuführen.

### Nachteile
Der Benutzer muss natürlich mit Python vertraut sein und das Einrichten einer Python-Umgebung mit allen notwendigen Abhängigkeiten kann für einige Benutzer aufwendig sein.

### Beispiel
```python
import requests
response = requests.get('https://api.example.com/data')
print(response.json())
```

## Postman
[Postman](https://www.postman.com/) ist eine populäre API-Entwicklungsplattform, die verwendet wird, um API-Anfragen zu erstellen, zu testen und zu dokumentieren.

### Vorteile
Postman bietet eine grafische Benutzeroberfläche und ist damit sehr intuitiv. Zusätzlich ermöglicht es das Speichern, Organisieren und Teilen von API-Anfragen und eignet sich damit auch sehr gut für fortgeschrittenes API-Testing und Monitoring.

### Nachteile
Auf älteren oder weniger leistungsfähigen Computern kann Postman ressourcenintensiv sein und die Nutzung fortgeschrittener Funktionen bedarf eine gewisse Einarbeitungzeit. Für die kollaborative Nutzung können außerdem zusätzliche Kosten anfallen.

### Beispiel
Um eine API in Postman zu testen, erstellt man eine neue Anfrage, wählt z.B. die Methode GET und fügt dann einfah nur die URL hinzu.

![Postman GET Beispiel](../assets/postman_get_example.png)


# Echte APIs nutzen
Um ein besseres Verständnis mit dem Umgang mit API aufzubauen, nutzen wir zwei kostenlose APIs zur Abfrage des Wetters an einer Geokoordinate: https://open-meteo.com/ und https://brightsky.dev/.

## Aufgaben
Zeit: 5-10 min / Aufgabe
1. **Terminal CURL Wetter API abrufen**: Nutze CURL im Terminal, um die Wetterdaten von https://open-meteo.com/ für einen bestimmten Ort abzufragen.

2. **Python Wetter API abrufen**: Verwende die Python Request Library, um die Wetterdaten von https://open-meteo.com/ für einen bestimmten Ort abzufragen.

3. **Postman Wetter API abrufen**: Nutze Postman, um die Wetterdaten von https://open-meteo.com/ für einen bestimmten Ort abzufragen.

4. **API Request an weiteren Wetterservice**: Führe mit einer Methode deiner Wahl einen API Request für die selben Geokoordinaten an https://brightsky.dev/ aus.

5. **Analyse und Vergleich der API Responses**: Analysiere und vergleiche die Antworten beider APIs. Was fällt auf? Was ist der Grund dafür? 

6. **Vergleichsdiskussion**: Setzt euch in 2er Teams zusammen und tauscht euch über die drei Methoden zur API-Ansprache aus. Besprecht die Unterschiede, unerwartete Ergebnisse sowie Vor- und Nachteile jeder Methode.

### Musterlösungen
<details>
  <summary>1. CURL</summary>
  
  ```js
  curl "https://api.open-meteo.com/v1/forecast?latitude=52.5200&longitude=13.4050&current_weather=true"
  ```
</details>

<details>
  <summary>2. Python Requests</summary>
  
  ```python
  import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.5200&longitude=13.4050&current_weather=true")
weather_data = response.json()
print(weather_data)
  ```
</details>

<details>
  <summary>3. Postman</summary>
  
  ![Postman Wetter Request](../assets/postman_get_wetter.png)
</details>

## Reflexionsrunde (10min)
Warum sind die Antworten von Open-Meteo und Bright Sky unterschiedlich?

**Datenstruktur und Format**: Wie präsentieren die APIs ihre Daten? Sind die Daten in JSON, XML oder einem anderen Format?

**Detailgrad und Umfang**: Welche Art von Informationen liefern die APIs? Bieten sie grundlegende oder detaillierte Daten?

**Aktualität und Genauigkeit**: Wie aktuell sind die Daten? Gibt es Unterschiede in der Genauigkeit oder Zuverlässigkeit der Informationen?

**API-Design und Dokumentation**: Wie unterscheiden sich die APIs in Bezug auf Benutzerfreundlichkeit und Dokumentationsklarheit?


# HTTP Elemente Deep Dive
Auch wenn wir im späteren Verlauf der Woche Postman nochmals nutzen werden, fokussierne wir uns auf die Nutzung der Python Requests Library. Wir werden uns die verschiedenen Methoden, Header, Parameter und Payloads ansehen, die für die Kommunikation mit Webdiensten und APIs verwendet werden.

## HTTP Methoden
Im vorherigen Kapitel haben wir bereits kurz die [Methoden für HTTP Requests](#rest-representational-state-transfer) kennengelernt.
Wichtig zu verstehen ist, dass diese eine zentrale Rolle bei der Verwendung mit Python Requests einnehmen. 

Hier ein detaillierter Blick auf die wichtigsten HTTP-Methoden im Kontext der Python Requests.

### GET
Die GET-Methode wird verwendet, um Daten von einem Server abzurufen. Es ist die am häufigsten verwendete HTTP-Methode und wird für Anfragen eingesetzt, die keine Änderung des Serverzustands bewirken.
```python
response = requests.get('https://api.example.com/data')
```
Parameter für die Abfrage können über das `params` Attribut übergeben werden.
```python
params = {
  'key': 'value'
}

response = requests.get('https://api.example.com/data', params=params)
```

### POST
POST wird verwendet, um neue Daten an den Server zu senden. Es ist typischerweise die Methode der Wahl, wenn es darum geht, neue Ressourcen zu erstellen, wie z.B. einen neuen Eintrag in einer Datenbank. Daten ([Payloads](#payloads)) werden über das `data` Argument übergeben.

```python
response = requests.post('https://api.example.com/data', data={'key': 'value'})
```

### PUT
PUT wird eingesetzt, um bestehende Daten auf dem Server zu aktualisieren oder zu ersetzen. Wenn die spezifizierte Ressource nicht existiert, kann sie neu erstellt werden.
```python
response = requests.put('https://api.example.com/data/1', data={'key': 'new_value'})
```

### DELETE
Wie der Name schon sagt, wird die DELETE-Methode verwendet, um Ressourcen vom Server zu entfernen.
```python
response = requests.delete('https://api.example.com/data/1')
```

## Payloads
Bei HTTP-Requests, insbesondere bei POST und PUT, spielt der "Data Payload" (auch Request Body) eine zentrale Rolle. Data Payloads transportieren die erforderlichen Informationen, um eine Aktion auf dem Server auszuführen, wie z.B. das Hinzufügen eines neuen Benutzers oder das Aktualisieren eines Produkts. 

Payloads sind flexibel im Format und können sowohl Text, JSON, XML, Dateiuploads als auch andere Datenformate enthalten. Wichtig hierbei ist vor allem der [Content-Type Header](#headers) um den Typ des Payloads zu definieren (z.B. application/json für JSON-Daten).

## Headers
HTTP-Headers sind essentiell in HTTP-Anfragen und -Antworten. Es sind simple Key-Value-Paare, die wichtige Informationen über die Anfrage oder Antwort liefern. Headers können eine Vielzahl von Daten, wie Metadaten, Authentifizierungsinformationen und Informationen über Codierung, Sprache und Authentifizierung enthalten.

### Content-Type
Beschreibt den Medientyp (MIME-Typ) des Inhalts im Body der HTTP-Anfrage oder -Antwort.

`Content-Type: application/json` - für JSON-Daten.

`Content-Type: text/plain` - für Klartext.

`Content-Type: multipart/form-data` - für Formulardaten mit Datei-Uploads.

`Content-Type: application/x-www-form-urlencoded` - für  Formulardaten in URL-kodierter Form.

**Beispiel**
```python
data = {'key': 'value'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://api.example.com/data', json=data, headers=headers)
```

### Authorization
Übermittelt Authentifizierungsinformationen zum Server.

`Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` - für Basic Auth (Base64-kodierte Benutzername:Passwort-Kombination).

`Authorization: Bearer YOUR_TOKEN` - für Authentifizierungsstandards wie OAuth 2.0 

**Beispiel**
```python
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://api.example.com/protected', headers=headers)
```

### Cookie
Überträgt Cookies vom Client zum Server.
Beispiel:

`Cookie: session_id=abc123` - für Infos zur Session

`Cookie: id=a3fWa; isLoggedIn=true` - für mehrere Cookies.

**Beispiel**
```python
cookies = {'session_id': '123456'}
response = requests.get('https://api.example.com/data', cookies=cookies)
```


# Python Requests Library
Kernobjekt der Requests Library ist das `response` Objekt. Vor allem der Status Code kann bei der Implementierung des finalen Projektes helfen.

### Status Code (`response.status_code`)
Gibt den HTTP-Statuscode der Antwort zurück. Zum Beispiel steht `200` für Erfolg, `404` für nicht gefunden und `500` für einen Serverfehler.

```python
if response.status_code == 200:
    print("Erfolgreiche Anfrage!")
```

### Content (`response.content`)
Der rohe Antwortinhalt in Bytes is vor allem nützlich, wenn man mit binären Daten wie Bildern oder PDFs arbeitet.
```python
content = response.content
```

### Text (`response.text`)
Der Antwortinhalt als Unicode-String. Geeignet für Textantworten wie HTML oder JSON.
```python
html_content = response.text
```

### JSON (`response.json()`):
Eine Methode, die den Inhalt der Antwort als JSON interpretiert und in ein Python-Objekt (in der Regel ein Dictionary) umwandelt. Funktioniert nur, wenn der Antwortinhalt gültiges JSON ist.
```python
data = response.json()
```

### Headers (`response.headers`):
Ein Case-Insensitive Dictionary, das alle Antwort-Header enthält.
```python
content_type = response.headers['Content-Type']
```

### Cookies (`response.cookies`):
Ein Requests `CookieJar`-Objekt, das alle Cookies enthält, die in der Antwort gesetzt wurden.
```python
cookies = response.cookies
```

## Error Handling
Die Handhabung von HTTP-Error-Statuscodes in Python, insbesondere bei der Verwendung der Requests Library, ist ein wesentlicher Bestandteil der robusten Netzwerkprogrammierung. 

Fehlercodes wie `404` und `500` signalisieren Probleme, die entweder **clientseitig** (`4xx`) oder **serverseitig** (`5xx`) sind. Eine angemessene Behandlung dieser Fehler stellt sicher, dass Ihr Programm auf solche Probleme richtig reagiert.

Ein Beispiel für das Fehlerhandling kann wie folgt aussehen.
```python
import requests

url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Überprüft den Statuscode der Antwort
    
    # Weiterer Code zur Verarbeitung der Antwort, wenn kein Fehler auftritt
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as err:
    # Behandlung von HTTP-Fehlern, die von raise_for_status() geworfen werden
    print(f"HTTP-Fehler aufgetreten: {err}")
except requests.exceptions.RequestException as e:
    # Behandlung aller anderen Requests-bezogenen Fehler
    print(f"Fehler bei der Anfrage: {e}")
```


# Komplexe-Aufgabe (Capstone Projekt)
**Wetter API CLI Anwendung**
> Zeit: 45-60 min 

Erstelle ein Kommandozeilen-Programm bei dem der Nutzer um die Eingabe einer Stadt gebeten wird und dann das aktuelle Wetter für den gegebenen Standort bekommt.
Füge zusätzlich die Option hinzu, eine Vorhersage für die kommenden 7 Tage anzuzeigen.

**Anforderungen**
- Interaktive CLI Anwendung mit 3 Optionen
  - Wetter Aktuell (fragt den Nutzer nach der Stadt)
  - Wetter Vorhersage (fragt den Nutzer nach der Stadt)
  - Beenden
- Die CLI Anwendung soll mehrere Anfragen nacheinander annehmen können.
- Falls das Rate-Limit (Status-Code `429`) überschritten wird, soll das Programm den Fehler abfangen.
- Nutze die WMO Codes für den aktuellen Wetterstatus

**Bonus**
- Die CLI Anwendung soll visuell mit Emojis aufgebessert werden (Warm/Kalt, Wolkig/Gewitter)
- Es können mehrere Städte angebeben werden für die man im Vergleich die Wetterdaten sieht
- Nutze `bullet` um die CLI noch visueller und interaktiver zu machen.

**Ressourcen**
- API Wetter für Lat/Long: https://open-meteo.com/
- API für City to Lat/Long: https://geocode.maps.co/
- [`bullet`](https://github.com/bchao1/bullet): Beautiful Python Prompts Made Simple

<details>
  <summary>WMO Wetter Code Mapping</summary>
  
  ```python
wmo_codes = {
        0: 'Klarer Himmel',
        1: 'Hauptsächlich klar',
        2: 'Teilweise bewölkt',
        3: 'Bewölkt',
        45: 'Nebel',
        48: 'Nebel mit Reifbildung',
        51: 'Leichter Nieselregen',
        53: 'Mäßiger Nieselregen',
        55: 'Dichter Nieselregen',
        56: 'Leichter gefrierender Nieselregen',
        57: 'Dichter gefrierender Nieselregen',
        61: 'Leichter Regen',
        63: 'Mäßiger Regen',
        65: 'Starker Regen',
        66: 'Leichter gefrierender Regen',
        67: 'Starker gefrierender Regen',
        71: 'Leichter Schneefall',
        73: 'Mäßiger Schneefall',
        75: 'Starker Schneefall',
        77: 'Schneegriesel',
        80: 'Leichte Regenschauer',
        81: 'Mäßige Regenschauer',
        82: 'Starke Regenschauer',
        85: 'Leichte Schneeschauer',
        86: 'Starke Schneeschauer',
        95: 'Gewitter',
        96: 'Gewitter mit leichtem Hagel',
        99: 'Gewitter mit starkem Hagel'
}
```
</details>


<details>
  <summary>Musterlösung</summary>

```python
import requests

def get_weather_data(api_url, params):
    """Holt Wetterdaten von der API."""
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 429:
            print("Rate-Limit erreicht. Bitte später erneut versuchen.")
        else:
            print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def geocode_city(city_name):
    """Konvertiert einen Stadtnamen in geografische Koordinaten."""
    geocode_url = "https://geocode.maps.co/search"
    params = {'q': city_name}
    response = get_weather_data(geocode_url, params)
    if response:
        return response[0]['lat'], response[0]['lon']
    return None, None

def get_current_weather(city):
    """Ruft das aktuelle Wetter für eine Stadt ab."""
    lat, lon = geocode_city(city)
    if lat and lon:
        api_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': 'true'
        }
        weather_data = get_weather_data(api_url, params)
        if weather_data:
            return weather_data['current_weather']
    return None

def get_weather_forecast(city):
    """Ruft die Wettervorhersage für die nächsten 7 Tage für eine Stadt ab."""
    lat, lon = geocode_city(city)
    if lat and lon:
        api_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'daily': ['temperature_2m_max', 'temperature_2m_min', 'weathercode', 'precipitation_sum'],
            'timezone': 'auto'
        }
        weather_data = get_weather_data(api_url, params)
        if weather_data:
            return weather_data['daily']
    return None

def wmo_weather_interpretation(weather_code):
    """ Interpretiert den WMO-Wettercode in lesbare Wetterbedingungen. """
    wmo_codes = {
        0: 'Klarer Himmel',
        1: 'Hauptsächlich klar',
        2: 'Teilweise bewölkt',
        3: 'Bewölkt',
        45: 'Nebel',
        48: 'Nebel mit Reifbildung',
        51: 'Leichter Nieselregen',
        53: 'Mäßiger Nieselregen',
        55: 'Dichter Nieselregen',
        56: 'Leichter gefrierender Nieselregen',
        57: 'Dichter gefrierender Nieselregen',
        61: 'Leichter Regen',
        63: 'Mäßiger Regen',
        65: 'Starker Regen',
        66: 'Leichter gefrierender Regen',
        67: 'Starker gefrierender Regen',
        71: 'Leichter Schneefall',
        73: 'Mäßiger Schneefall',
        75: 'Starker Schneefall',
        77: 'Schneegriesel',
        80: 'Leichte Regenschauer',
        81: 'Mäßige Regenschauer',
        82: 'Starke Regenschauer',
        85: 'Leichte Schneeschauer',
        86: 'Starke Schneeschauer',
        95: 'Gewitter',
        96: 'Gewitter mit leichtem Hagel',
        99: 'Gewitter mit starkem Hagel'
    }
    return wmo_codes.get(weather_code, 'Unbekannte Bedingungen')

def get_weather_emoji(weather_condition, temperature):
    """ Gibt passende Emojis für Wetterbedingungen zurück. """
    if temperature > 25:
        temperature_emoji = "🌡️☀️"  # Warm
    elif temperature < 5:
        temperature_emoji = "🌡️❄️"  # Kalt
    else:
        temperature_emoji = "🌡️🌥️"  # Mild

    weather_emojis = {
        'Klarer Himmel': '☀️',
        'Hauptsächlich klar': '🌤️',
        'Teilweise bewölkt': '⛅',
        'Bewölkt': '☁️',
        'Nebel': '🌫️',
        'Nebel mit Reifbildung': '🌫️❄️',
        'Leichter Nieselregen': '🌦️',
        'Mäßiger Nieselregen': '🌧️',
        'Dichter Nieselregen': '🌧️',
        'Leichter gefrierender Nieselregen': '🌧️❄️',
        'Dichter gefrierender Nieselregen': '🌧️❄️',
        'Leichter Regen': '🌦️',
        'Mäßiger Regen': '🌧️',
        'Starker Regen': '🌧️☔',
        'Leichter gefrierender Regen': '🌧️❄️',
        'Starker gefrierender Regen': '🌧️❄️',
        'Leichter Schneefall': '🌨️',
        'Mäßiger Schneefall': '🌨️',
        'Starker Schneefall': '❄️',
        'Schneegriesel': '🌨️',
        'Leichte Regenschauer': '🌦️',
        'Mäßige Regenschauer': '🌧️',
        'Starke Regenschauer': '🌧️☔',
        'Leichte Schneeschauer': '🌨️',
        'Starke Schneeschauer': '❄️',
        'Gewitter': '⛈️',
        'Gewitter mit leichtem Hagel': '⛈️🌨️',
        'Gewitter mit starkem Hagel': '⛈️🧊'
    }
    weather_emoji = weather_emojis.get(weather_condition, '🌈')

    return f"{temperature_emoji} {weather_emoji}"

def print_current_weather(weather_data, city):
    """Druckt das aktuelle Wetter in einem lesbaren Format."""
    if weather_data:
        weather_condition = wmo_weather_interpretation(weather_data['weathercode'])
        emoji = get_weather_emoji(weather_condition, weather_data['temperature'])
        print(f"\nAktuelles Wetter in {city}: {emoji}")
        print(f"Temperatur: {weather_data['temperature']}°C")
        print(f"Wetterzustand: {weather_condition}")
        print(f"Niederschlag: {weather_data.get('precipitation', '0')} mm\n")
    else:
        print("Keine Wetterdaten verfügbar.")

def print_weather_forecast(weather_data, city):
    """Druckt die Wettervorhersage in einem lesbaren Format."""
    if weather_data:
        print(f"\nWettervorhersage für {city} für die nächsten 7 Tage:")
        for i, day in enumerate(weather_data['time']):
            max_temp = weather_data['temperature_2m_max'][i]
            weather_condition = wmo_weather_interpretation(weather_data['weathercode'][i])
            emoji = get_weather_emoji(weather_condition, max_temp)
            print(f"Datum: {day} {emoji}")
            print(f"Max Temperatur: {max_temp}°C")
            print(f"Min Temperatur: {weather_data['temperature_2m_min'][i]}°C")
            print(f"Wetterzustand: {weather_condition}")
            print(f"Niederschlag: {weather_data['precipitation_sum'][i]} mm\n")
    else:
        print("Keine Wetterdaten verfügbar.")

def main():
    while True:
        print("\nWetter CLI Anwendung")
        print("1. Wetter Aktuell")
        print("2. Wetter Vorhersage 7-Tage")
        print("3. Beenden")
        choice = input("Wähle eine Option: ")

        if choice == '1':
            city = input("Gib den Namen einer Stadt ein: ")
            weather_data = get_current_weather(city)
            print_current_weather(weather_data, city)
        elif choice == '2':
            city = input("Gib den Namen einer Stadt ein: ")
            weather_data = get_weather_forecast(city)
            print_weather_forecast(weather_data, city)
        elif choice == '3':
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")

if __name__ == "__main__":
    main()
```
</details>

# Weiterführende Materialien
- [Official Python Requests Library](https://docs.python-requests.org/en/latest/user/quickstart/#:~:text=,we%20need%20from%20this%20object)
- [A typical HTTP session](https://developer.mozilla.org/en-US/docs/Web/HTTP/Session)
- [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)