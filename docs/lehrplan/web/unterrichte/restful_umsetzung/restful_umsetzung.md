# Umsetzung einer RESTful API in Flask
[60 min]

## Routen
Das Kernstück jeder Flask-Anwendung sind die Routen, die bestimmen, wie Anfragen an verschiedene URLs gehandhabt werden. Ein Beispiel für eine einfache Route haben wir bereits im Teil [Einrichtung einer API mit Flask](#einrichtung-einer-api-mit-flask) gesehen.


```python
@app.route('/')
def home():
    return "Hallo Welt!"
```

RESTful Design definiert die Existenz der CRUD Operationen. Mit Flask können wir diese Endpoints wie folgt abbilden. Das explizite Angeben der unterstützen Methoden macht den Code auszeichnender und hilft bei der späteren Generierung der Dokumentation.

**GET**: Abrufen von Nutzerdaten. (Basisroute):
```python
@app.route('/users', methods=['GET'])
def get_users():
    # Logik, um Benutzerdaten abzurufen
```

**POST**: Erstellen eines neuen Nutzers (Basisroute).
```python
@app.route('/users', methods=['POST'])
def create_user():
    # Logik, um einen neuen Benutzer zu erstellen
```

**PUT**: Aktualisieren eines bestehenden Nutzers (Variable Route).
```python
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    # Logik, um Benutzerdaten zu aktualisieren
```

**DELETE**: Löschen eines Nutzers (Variable Route).
```python
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Logik, um einen Benutzer zu löschen
```


## Datenverarbeitung
Die Datenverarbeitung, z.B. von JSON Daten, sowohl als Payload in der Anfrage als auch in der Antwort ist für die effiziente Nutzung von APIs relevant. Deshalb bietet Flask das `request`-Objekt um Daten aus Anfragen abzurufen.
```python
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    # Verarbeiten von user_data
```

Für das einfach Senden von JSON-Objekten in der Antwort nutzen wir `jsonify`.
```python
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Angenommene Hilfsfunktion zur Datenbankabfrage
    user = get_user_by_id(id)  
    return jsonify(user)
```

Für das handling von Form-Daten gibt es ein Objektattribute namens `form`. Es beinhaltet alle request-Formular Daten.
```python
@app.route('/submit-form', methods=['POST'])
def handle_data():
    name = request.form['name']
    age = request.form['age']
    # Verarbeiten der Daten
    return jsonify({"message": "Formular erhalten"}), 200
```


## Fehlercodes und Ausnahmebehandlung
Bei der Behandlung von Fehlern ist die korrekte Verwendung von HTTP-Fehlercodes entscheidend, um dem Client-Ende nützliches Feedback zu geben. Alle Status Codes sind standardisiert und können z.B. auf der [SelfHTML Seite](https://wiki.selfhtml.org/wiki/HTTP/Statuscodes) eingesehen werden. Es sollte immer der präzise HTTP-Statuscodes gesendet werden um den Zustand der Anfrage zu kommunizieren.

**`404 Nicht gefunden`**
```python
@app.route('/users/<int:id>')
def get_user(id):
    user = get_user_by_id(id)
    if not user:
        return jsonify({"error": "Benutzer nicht gefunden"}), 404 
    return jsonify(user)
```

**`400 Schlechte Anfrage`**
```python
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    if not valid_car_data(data):
        return jsonify({"error": "Ungültige Daten"}), 400
    # Erstellen eines neuen Autos
    return jsonify({"message": "Auto erstellt"}), 201
```

**`401 Unautorisiert`**
```python
@app.route('/secure-area')
def secure_area():
    if not user_is_authenticated():
        return jsonify({"error": "Unautorisiert"}), 401
    return jsonify({"message": "Willkommen im sicheren Bereich"})
```


## Aufgaben
[90 min]

### Einfache GET-Route für Benutzerliste 🌶️
Erstelle eine Route, die eine simulierte Liste von Benutzern zurückgibt.

### POST-Route zum Hinzufügen neuer Benutzer 🌶️🌶️
Erstelle eine Route, um neue Benutzer hinzuzufügen. Nimm Benutzerdaten aus der Anfrage auf und füge sie der Benutzerliste hinzu.


### PUT-Route zum Aktualisieren von Benutzerdaten 🌶️🌶️🌶️
Implementiere eine PUT-Route (`/users/<id>`), um die Daten eines bestehenden Benutzers zu aktualisieren.

### DELETE-Route zum Löschen eines Benutzers 🌶️🌶️🌶️
Implementiere eine DELETE-Route, um einen Benutzer zu löschen.


## Komplex-Aufgaben
[90 min]

### Kombinierte GET- und POST-Anfragen mit Fehlerhandling 🌶️🌶️🌶️
Kombiniere GET- und POST-Anfragen und implementiere umfassendes Fehlerhandling.

- Sende zuerst eine GET-Anfrage, um Daten abzurufen.
- Verwende die Daten aus der GET-Anfrage, um eine Bedingung für eine POST-Anfrage zu definieren.
- Implementiere Fehlerhandling für beide Anfragen.

### Authentifizierung für eine sichere Route hinzufügen 🌶️🌶️🌶️🌶️
Erstelle eine gesicherte Route, die eine Authentifizierung erfordert.

**Schritte**:
1. Definiere eine neue Route `/secure`.
2. Implementiere eine einfache Authentifizierungslogik (z.B. überprüfe einen statischen API-Schlüssel).
3. Erlaube den Zugriff nur, wenn die Authentifizierung erfolgreich ist.

[Lösungen](./solutions.md)




