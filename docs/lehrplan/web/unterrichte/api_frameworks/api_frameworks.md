# Web API Frameworks
[60 min]

## Flask & Django
Flask und Django bieten zwei sehr unterschiedliche Ansätze für die Entwicklung von Webanwendungen und APIs in Python. Flask ist ideal für schnelle Entwicklung, kleine Projekte oder wenn eine hohe Flexibilität erforderlich ist. Django hingegen bietet ein umfassendes Ökosystem für größere und komplexere Anwendungen. **Die Wahl zwischen Flask und Django hängt von den spezifischen Anforderungen des Projekts, der bevorzugten Arbeitsweise des Entwicklerteams und der Komplexität der zu entwickelnden Anwendung ab**.

## Flask: Das Mikro-Framework
### Konzept und Philosophie
Flask ist ein leichtgewichtiges und flexibles Mikro-Framework für Python, entworfen für kleine bis mittelgroße Anwendungen und einfache Web-Dienste.
Es legt großen Wert auf Einfachheit und Erweiterbarkeit und bietet die Freiheit, die meisten Aspekte der Anwendung nach Bedarf zu gestalten.

### Hauptmerkmale von Flask:

**Minimalistischer Kern**: Flask kommt mit sehr wenig eingebauter Funktionalität. Dies ermöglicht eine hohe Anpassungsfähigkeit, erfordert aber auch, dass Entwickler viele Funktionen selbst implementieren oder Erweiterungen nutzen.

**Erweiterungen**: Eine breite Palette von Erweiterungen verfügbar, die nahtlos integriert werden können, um Funktionen wie Datenbankanbindung, Formularverarbeitung, Authentifizierung etc. hinzuzufügen.

**Einfache Routengestaltung**: Flask ermöglicht eine einfache und intuitive Routendeklaration mit Python-Dekoratoren.

### Einrichtung einer API mit Flask
**1. Installation**: Beginne mit der Installation von Flask mittels `pip install flask`.

**2. Anwendungserstellung**: Erstelle eine neue Python-Datei und importiere Flask.

**3. Route definieren**: Beachte, dass in Flask eine API oft als eine einfache Funktion beginnt, die über eine Annotation mit einem URL-Endpunkt verknüpft wird.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/') # Flask URL-Endpunkt Annotation
def hello_world():
    return 'Hallo Welt!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```
**4. Server starten**: Führe die Anwendung aus, um den lokalen Server zu starten.

## Django: Das "Batterien-inbegriffen"-Framework
### Konzept und Philosophie
Django ist ein leistungsstarkes und voll ausgestattetes Web-Framework für größere Anwendungen und Plattformen.
Sein Ansatz „Batterien inbegriffen“ bedeutet, dass es mit vielen integrierten Funktionen für die gängigsten Entwicklungsaufgaben kommt.

### Hauptmerkmale von Django
**Vollständige Entwicklungsumgebung**: Es bietet eine robuste Basis für Datenbankmodelle, Benutzerverwaltung, Sicherheitsmechanismen und mehr.

**ORM (Object-Relational Mapping)**: Eines der Kernmerkmale von Django ist sein ORM-System, das eine Abstraktionsschicht über die Datenbank bietet und SQL-Abfragen durch Python-Code ersetzt.

**Admin-Oberfläche**: Eine eingebaute Admin-Oberfläche ermöglicht einfache Verwaltung von Datenmodellen und Benutzerkonten.

### Einrichtung einer API mit Django
Im direkten Vergleich wird der Unterschied von Flask und Django klar, denn es erfordert ein wenig mehr Setup als Flask, bietet aber von Anfang an mehr Funktionalität.

**1. Installation und Projektstart**: Installiere Django und starten ein neues Projekt mit `django-admin startproject myproject`.

**2. Anwendung erstellen**: Erstelle eine neue Anwendung mit `python manage.py startapp myapp`.

**3. Views und URLs definieren**: Django verwendet keine Annotations sondern ein Muster von Views und URLs um Anfragen zu verarbeiten.
- In `views.py`, erstelle eine Funktion, die eine HTTP-Antwort zurückgibt. 
- In `urls.py`, definiere eine URL-Route, die der View-Funktion entspricht.

```python
# views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hallo Welt!')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
```
**4. Server starten**: Führe `python manage.py runserver 8000` aus, um den Server zu starten. 

## Lokaler HTTP Server
Ein lokaler HTTP(S) Server ermöglicht es, Webanwendungen und APIs auf einem lokalen Rechner zu entwickeln und zu testen. Sowohl Flask als auch Django bieten eingebaute Entwicklungsserver, die für Testzwecke und während der Entwicklung verwendet werden können. Diese Server sind jedoch nicht für den produktiven Einsatz gedacht, da sie nicht für hohe Lasten oder Sicherheitsanforderungen optimiert sind.

Für Produktionsumgebungen sollten auf jeden Fall robustere Serverlösungen wie [Apache](https://httpd.apache.org/) verwendet und [HTTPS](https://www.cloudflare.com/de-de/learning/ssl/what-is-https/) konfiguriert werden.


## Aufgaben
[45 min]

### Hello World Flask & Django API 🌶️️🌶️️
Erstellt jeweils einen GET Endpunkt der den Text "Hallo Welt!" als Response zurückgibt in Flask und Django.

### Reflexionsrunden Django vs Flask 🌶️️ 
In Gruppen von 2, vergleicht gemeinsam die Lesbarkeit, Einfachheit und den Syntax der beiden Frameworks.