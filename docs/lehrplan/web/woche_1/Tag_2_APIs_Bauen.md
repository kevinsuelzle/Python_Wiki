# Tag 2 - APIs Bauen

### Inhalt
- Wie baut man eine API?
  - Wie funktionieren APIs intern?
    - Flussdiagram
    - API Architektur Prinzipien
      - JSON (und XML)
    - Deployment (Ausblick)
      - Cloud (Azure)
      - Docker
    - Flask & Django
      - Intro & Unterschiede
      - Beispiele
        - Hallo Welt der APIs
          - Live-Coding zur Demonstration der "Einfachheit"
        - localhost / HTTP(S) Server
          - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
            - Ports

    - Flask Advanced
      - Restful API Designs
      - ORMs
      - Routen
      - Data Handling
      - Fehler Codes
      - Postman & Python Requests Testing
        - Wie testet man einfach APIs? (Rückblick Testing 4-5)
        - Postman Collections Repeatable Testing mit Postman

# Wie baut man eine API?
## Rückblick - Was ist eine API?
Im letzten Kapitel haben wir gelernt, dass API für Application Programming Interface steht. APIs ermöglichen es Entwicklern, komplexe Funktionen zu nutzen, ohne diese von Grund auf neu entwickeln zu müssen. So können beispielsweise Entwickler einer Wetter-App die API eines Wetterdienstes nutzen, um aktuelle Wetterdaten abzurufen, anstatt selbst eine umfassende Wetterdateninfrastruktur aufzubauen.

## Tagesprojekt
Ziel des heutigen Tages ist es, eine eigene RESTful FLASK API mit CRUD Funktion für das Management von Stellplätzen in einer Garage zu erstellen und diese mit einer Postman Collection zu testen.

![Projekt](../assets/postman_collection_run.png)

## Entwerfen einer API
Der Aufbau einer effektiven API erfordert ein solides Verständnis der Grundprinzipien und besten Praktiken in der Softwareentwicklung.
**Deshalb beginnt der Entwurf einer API mit der Definition ihrer Funktionalität und der Daten, die sie verwalten soll.**

### Festlegung der Anforderungen und Endpoints
Endpoints sind die spezifischen Ansprechpartner innerhalb einer API, über die Interaktionen stattfinden. Sie bestimmen, wie die API aufgerufen wird und welche Ressourcen oder Dienste sie bietet.

#### Designprinzipien
Beim entwerfen einer API liegt der Fokus auf die Verständlichkeit und Nutzbarkeit der späteren Nutzer. Deshalb ist es umso wichtiger folgende Prinzipien zu kennen.

**Klarheit und Einfachheit**: Endpoints sollten intuitiv und leicht zu verstehen sein. Ein guter Endpoint beschreibt die Ressource oder Aktion, die er repräsentiert. Wie im Kapitel zu Clean Code beschrieben, kann man z.B. über die Bezeichnung der Endpunkte bereits viel Klarheit geben.

Für die Funktion, einen Nutzer per ID abzufragen, ist der Endpoint `get_user_by_id` besser als z.B. nur `get_user`. 

**Konsistenz**: Einheitliche Benennung und Strukturierung der Endpoints erleichtern die Nutzung der API. Vor allem das [Schema](#definition-des-schemas-für-requests-und-responses) der Responses muss so konsistent wie möglich gewählt sein, sodass den Nutzern die Einarbeitung erleichtert wird.

**Ressourcenorientierung**: In RESTful APIs repräsentiert jeder Endpoint idealerweise eine spezifische Ressource oder eine Sammlung von Ressourcen. Das [Single Responsibility Prinzip](https://www.linkedin.com/pulse/single-responsibility-principle-software-design-sanjoy-kumar-malik/) ist vor allem beim API-Design ein wichtiges Konzept. 

### Definition des Schemas für Requests und Responses
#### Request und Response Struktur
Jeder API-Request und -Response folgt einem spezifischen Schema, normalerweise in JSON oder XML. Dieses Schema definiert, wie Daten gesendet und empfangen werden.

#### JSON und XML
**JSON (JavaScript Object Notation)**: Leichtgewichtig und die am häufigsten verwendete Formatierung für API-Interaktionen. Es ist leicht lesbar und zu schreiben und wird heutzutage für fast alle APIs verwendet.

**XML (eXtensible Markup Language)**: Eine ältere, oft in Legacy-Projekten verwednete, Alternative zu JSON, die in manchen Systemen immer noch verwendet wird. XML ist strenger strukturiert als JSON und enthält meist konkrete Informationen zu Dateitypen. Anstelle von Objektnotation (`user.name`) wird XPath (`//user/name`) zur Abfrage einzelner Werte verwendet.


## Entwicklungswerkzeuge
Wie für die Entwicklung von anderen Spezialthemen gibt es auch für APIs ein zusätzlichen Toolset. Da vor allem großen Wert auf das Testen und die Dokumentation von APIs gelegt wird, sind **API-Design-Tools** wie [Postman](https://www.postman.com/), zum einfachen Testen, und [Swagger](https://swagger.io/), zur Dokumentation, hilfreich.

[Postman]() werden wir im Lauf des heutigen Tages näher behandelt. Swagger wird später näher behandelt und Teil Projektwoche.


## Implementierung
Die Implementierung einer API kann eine komplexe Aufgabe sein und umfasst folgende Schritte. Speziell bei der Entwicklung von APIs kann ein Test-Driven Developmentansatz unerwünschte Probleme vermeiden und zusätzlichen Aufwand durch den Fokus auf die Planung verhindern.

### 1. Planung
### Funktionsanforderungen

#### Anforderungsdokument
Die Erstellung eines umfassenden Anforderungsdokuments ist der erste Schritt in der Planungsphase. Es spezifiziert die funktionalen und nicht-funktionalen Anforderungen der API. Dazu gehört die Definition der zu unterstützenden Operationen, Sicherheitsanforderungen, Datenmodelle und Integrationen mit externen Diensten oder Datenbanken. Gerade für Projekte mit mehreren Teammitgliedern liegt der Erfolg in der Schaffung einer klaren und strukturierten Grundlage für die Entwicklung, die sicherstellt, dass alle Teammitglieder ein gemeinsames Verständnis der Ziele und Anforderungen haben.

#### API Architektur Prinzipien 
Auch die Wahl einer Architektur hängt von den spezifischen Anforderungen und dem Kontext ab. REST ist eine gängige Wahl für Web-APIs. Die Verwendung von JSON als Datenformat ist weit verbreitet, leichtgewichtig und einfach zu integrieren, was z.B. besonders wichtig für die Leistung und Skalierbarkeit der API ist.

### Auswahl der Technologie 
Die Auswahl des richtigen Frameworks und der Technologien erfolgt stets auf Basis der Anforderungen. Die meisten Frameworks unterstützen Grundlegende Funktionalitäten. Bei kleineren Projekten ist die Wahl der TEchnologie also deutlich weniger kritisch. API Frameworks wie [Flask oder Django](#web-api-frameworks) bieten eine robuste Basis für die Entwicklung von APIs in Python. Beide haben eingebaute Tools für Routing, Fehlerbehandlung und mehr.

### 2. Umsetzung
### Testen
Wie bereits in Wochen 4-5 erwähnt, sind Tests entscheidend, um die Zuverlässigkeit und Sicherheit der API zu gewährleisten. Dabei unterscheidet man zwischen verschiedenen Stufen.

**Unit-Tests** konzentrieren sich auf die kleinsten Teile der Anwendung, wie einzelne Funktionen oder Klassen, und stellen sicher, dass diese wie erwartet funktionieren.

**Integrationstests** prüfen das Zusammenspiel zwischen verschiedenen Komponenten der API, um sicherzustellen, dass sie zusammen korrekt funktionieren. Im heutigen Tagesprojekt werden wir uns vor allem auf diese Art der Tests mit Postman fokussieren. 

**End-to-End-Tests** hingegen simulieren reale Benutzerszenarien und prüfen die gesamte Anwendung in einer Umgebung, die der Produktionsumgebung ähnlich ist.

### Implementierung
Die Implementierung der API und der dafür nötigen Funktionalität nimmt of nur einen kleinen Teil der Entwicklung von Backend-Anwendungen in Anspruch. Im Falle, dass alle Anforderungen sowie die Tests bereits vordefiniert sind (TDD-Ansatz), ist die Entwicklung der Funktionen vergleichsweise unkompliziert.


### 3. Dokumentation
Auch wenn das Dokumentieren die am meisten vernachlässigte Aufgabe bei der Projekterstellung ist, ist sie doch unerlässlich für die Benutzerfreundlichkeit und Wartbarkeit der API. Sie sollte klar, vollständig sein und bei Änderungen konstant aktualisiert werden. Eine gute Dokumentation ermöglicht es Entwicklern, die API effizient zu nutzen und zu verstehen, und reduziert den Aufwand für Support und Fehlerbehebung.

Zu den Best Practices gehören unter anderem:

**Klarheit, Vollständigkeit und Konsistenz**: Die Dokumentation sollte umfassend sein, alle wichtigen Aspekte wie Endpoints, Parameter, Datenformate und Fehlercodes abdecken. Sie muss klar und präzise formuliert sein, um Missverständnisse zu vermeiden.

**Zielgruppenorientierung und Zugänglichkeit**: Die Dokumentation muss auf die Bedürfnisse der Zielgruppe, insbesondere Entwickler, zugeschnitten sein, einschließlich technischer Details und praktischer Beispiele.
Sie sollte leicht zugänglich, benutzerfreundlich und suchfreundlich gestaltet sein, um eine effiziente Nutzung zu ermöglichen.

**Interaktive Elemente und Versionierung**: Moderne API-Dokumentation sollte interaktive Beispiele enthalten, die das Testen der API direkt aus der Dokumentation heraus ermöglichen.
Eine klare Dokumentation der Versionsgeschichte hilft Benutzern, Änderungen und deren Auswirkungen auf ihre Anwendungen zu verstehen.


### 4. Deployment (Ausblick)
Der letze Schritt der Projektentwicklung ist die Veröffentlichung und Bereitstellung der API für die interne oder externe Nutzung. Jede (API)-Anwendung läuft auf einer Infrastruktur, heutzutage in den meisten Fällen einem virtuellen Cloud-Server.

#### Cloud 
Die Bereitstellung der Applikation über die Cloud bietet Skalierbarkeit, Zuverlässigkeit und oft Kosteneffizienz. Azure, welches in der kommenden Woche behandelt wird, ist eine beliebte Wahl mit einer breiten Palette von Diensten und Tools, die die Bereitstellung und das Management von APIs erleichtern. Im Kontext einer Cloudumgebung stoßen wir vermehrt auch auf den Begriff Docker-Container.

#### Docker
Die Verwendung von Containern wie [Docker](https://www.docker.com/) für das Deployment bietet zahlreiche Vorteile, wie Portabilität, Konsistenz und Isolation. Docker erleichtert das Deployment und das Management von Anwendungen und ihrer Abhängigkeiten, was besonders in komplexen oder skalierenden Umgebungen nützlich ist.


# Web API Frameworks
## Flask & Django
- Intro & Unterschiede
- Beispiele
  - Hallo Welt der APIs
    - Annotations
    - Live-Coding zur Demonstration der "Einfachheit"
  - localhost / HTTP(S) Server
    - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
      - Ports
- Intro & Unterschiede
- Beispiele
  - Hallo Welt der APIs
    - Live-Coding zur Demonstration der "Einfachheit"
  - localhost / HTTP(S) Server
    - Wie kann ein lokales Programm auf HTTP Requests nach "außen" hören?
      - Ports

## Aufgaben
Zeit: 10-15 min / Aufgabe
1. **Hello World Flask & Django API**: In Gruppen von 2, erstellt jeweils einen GET Endpunkt der den Text "Hallo Welt!" als Response zurückgibt in Flask und Django.
2. **Reflexionsrunden Django vs Flask**: Vergleicht gemeinsam die Lesbarkeit, Einfachheit und den Syntax der beiden Frameworks.
3. **GET API**: ...todo
4. **Simple CRUD Api**: ...todo

# Flask Advanced
- Restful API Designs
  - Planning
- ORMs
- Routen
- Data Handling
- Fehler Codes
- Postman & Python Requests Testing
  - Wie testet man einfach APIs? (Rückblick Testing 4-5)
  - Python Requests und Testing
  - Postman Collections 
    - Repeatable Testing mit Postman

## Komplex-Aufgabe (Capstone Projekt)
**CRUD Garagen Management API**
> Zeit: 45-60 min 

Erstelle eine FLASK RESTful API mit CRUD Funktion für das Management von Stellplätzen in einer Garage.
Hierbei sollen Fahrzeuge mit ihrem Kennzeichen eingebucht und einem Stellplatz zugewiesen werden.
Beim Abholen des Fahrzeuges wird das Datum ebenfalls persistiert.
Zusätzlich soll es auch möglich sein, Fahrzeuge neue Stellplätze zuzuweisen.

**Anforderungen**
- Flask API mit CRUD Funktionalität
  - Anzeigen aller Fahrzeuge in der Garage
  - Anzeigen des Stellplatzes eines einzelnen Fahrzeugs basierend auf dem Kennzeichen
  - Einbuchen eines neuen Fahrzeugs (und zuweisen des Parkplatzes) 
  - Updaten einzelner Fahrzeuge um den Stellplatz zu ändern 
  - Updaten einzelner Fahrzeuge bei Abholung
  - Löschen einzelner Fahrzeuge per ID
- Plane die API zuerst mit Stift und Papier
- Definiere dann die Integration Tests mit Postman als Collection für einen Test Driven Development Anstatz
- Nutze SQLALCHEMY als Toolkit

**Bonus**
- **Automatische Parkplatzzuweisung** - Ändere die Parkplatzzuweisung von Nutzerangabe auf automatisch. Neue Fahrzeuge sollen automatisch auf leere Parkplatze zugewisen werden.
- **Größenbasiertes Parken** - Füge weitere Informationen zu Fahrzeugen und Stellplätzen hinzu. (Kleines Auto - kleiner Parkplatz)
- **Kostenberechnung** - Bei Abholung des Fahrzeuges soll die Zeitdifferenz mit einem Kostenfaktor berechnet und mit ausgegeben werden.

**Ressourcen**
- [SQLAlchemy Dokumentation](https://docs.sqlalchemy.org/en/20/)
- [Postman Testing Docu](https://learning.postman.com/docs/writing-scripts/test-scripts/)

<details>
  <summary>Musterlösung</summary>
  
  ```python
  from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garage.db'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(80), nullable=False)
    check_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pick_up = db.Column(db.DateTime, nullable=True)
    parking_spot = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Car {self.license_plate}>'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/car', methods=['POST'])
def check_in_car():
    data = request.get_json()
    existing_car = Car.query.filter_by(license_plate=data['license_plate']).first()

    if existing_car:
        return jsonify({'success': False, 'message': f"Auto mit dem Kennzeichen '{data['license_plate']}' ist bereits geparkt."}), 400
    
    new_car = Car(license_plate=data['license_plate'], parking_spot=data.get('parking_spot'))
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'success': True, 'message': f"Auto mit dem Kennzeichen '{new_car.license_plate}' eingecheckt mit ID {new_car.id}"}), 201

@app.route('/car/<license_plate>', methods=['GET'])
def get_car_by_license_plate(license_plate):
    car = Car.query.filter_by(license_plate=license_plate).first()
    if car:
        parking_spot_msg = f"Das Fahrzeug mit dem Kennzeichen {car.license_plate} steht auf Parkplatz {car.parking_spot}." if car.parking_spot else f"Das Fahrzeug mit dem Kennzeichen {car.license_plate} hat keinen zugewiesenen Parkplatz."
        return jsonify({'success': True, 'message': parking_spot_msg}), 200
    else:
        return jsonify({'success': False, 'message': 'Auto mit dem angegebenen Kennzeichen wurde nicht gefunden.'}), 404

@app.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    car_data = [
        {'id': car.id, 
         'license_plate': car.license_plate, 
         'check_in': car.check_in.strftime("%Y-%m-%d %H:%M:%S"), 
         'pick_up': car.pick_up.strftime("%Y-%m-%d %H:%M:%S") if car.pick_up else None,
         'parking_spot': car.parking_spot
        } for car in cars
    ]
    return jsonify({'success': True, 'cars': car_data}), 200

@app.route('/car/<int:id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get_or_404(id)
    data = request.get_json()
    action = data.get('action')

    if action == 'change_parking':
        car.parking_spot = data.get('parking_spot')
        db.session.commit()
        return jsonify({'success': True, 'message': f'Parkplatz des Autos mit dem Kennzeichen {car.license_plate} aktualisiert zu {car.parking_spot}.'}), 200
    elif action == 'pick_up':
        car.pick_up = datetime.utcnow()
        db.session.commit()
        return jsonify({'success': True, 'message': f'Auto mit dem Kennzeichen {car.license_plate} wurde abgeholt.'}), 200
    else:
        return jsonify({'success': False, 'error': 'Ungültige Aktion spezifiziert.'}), 400

@app.route('/car/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'success': True, 'message': f'Auto mit dem Kennzeichen {car.license_plate} und ID {id} gelöscht.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
  ```

### Tests
[Postman Collection](../assets/Garage%20CRUD%20API%20Tests.postman_collection.json)

![Postman Collection Image](../assets/postman_crud_collection.png)
</details>


## Weiterführende Materialien
- **Rate Limiting**: API Einschränkungen mit dem offiziellen [Flask Limiter Extension](https://flask-limiter.readthedocs.io/en/stable/)