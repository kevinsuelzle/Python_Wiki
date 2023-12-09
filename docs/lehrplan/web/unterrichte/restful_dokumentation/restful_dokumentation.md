# Dokumentation einer RESTful API in Flask
[45 min]

Wie bereits ausführlich im Kapitel [Dokumentation](#3-dokumentation) besprochen, ist eine ausführliche und gut strukturierte Dokumentation entscheidend für eine professionelle API. Auch hierfür gibt es nützliche Tools die die Dokumentation deutlich vereinfachen.

## Swagger / OpenAPI
[Swagger](https://swagger.io/) bietet eine grafische Benutzeroberfläche und Werkzeuge zur Erstellung interaktiver API-Dokumentationen. Flask-APIs können mit [Flask-Swagger](https://pypi.org/project/flask-swagger/) integrieren, um automatisch eine Dokumentation zu generieren.

## MkDocs oder Sphinx:
Für eine eher traditionelle Dokumentation können Werkzeuge wie [MkDocs](https://www.mkdocs.org/) verwendet werden, die z.B. Markdown nutzen, um Seiten und Navigation zu erstellen.

## Beispielstruktur einer API-Dokumentation

```python
# Meine RESTful API

## Übersicht
- Endpoints
- Fehlercodes

## Endpoints

### GET /users
- Beschreibung: Abrufen einer Liste aller Benutzer.
- Parameter: Keine.

- Beispielanfrage: GET /users

- Beispielantwort (JSON):
  {
    "users": [
      {"id": 1, "name": "John Doe"},
      {"id": 2, "name": "Jane Doe"}
    ]
  }

### POST /users
Beschreibung: Erstellen eines neuen Benutzers.
Parameter: name (String), email (String).

Beispielanfrage (JSON): POST /users
{
  "name": "Max Mustermann",
  "email": "max@example.com"
}

Beispielantwort (JSON):
{
  "message": "Benutzer erstellt",
  "userId": 3
}

### Fehlercodes
400 Bad Request: Ungültige Anfragedaten.
404 Not Found: Ressource nicht gefunden.
500 Internal Server Error: Allgemeiner Serverfehler.
```

