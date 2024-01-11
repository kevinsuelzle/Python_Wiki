# Planung einer RESTful API in Flask
[60 min]

## Schritt 1: Zieldefinition und Funktionsumfang
**Ermittlung der Kernfunktionen**: Definiere die Hauptaufgaben, die Ihre API erfüllen soll. Ein Beispiel könnte das Verwalten von Benutzerkonten, das Posten von Nachrichten in einem sozialen Netzwerk oder das Abwickeln von Transaktionen in einem E-Commerce-System sein.

**Anwendungsfälle identifizieren**: Überlege, welche Aktionen die Benutzer durchführen sollen. Dazu gehören das Erstellen, Lesen, Aktualisieren und Löschen von Daten (CRUD-Operationen).

**Sicherheitsmaßnahmen planen**: Überlege, ob und wie die API gesichert wird. Das könnte z.B. über Authentifizierungstoken, OAuth oder andere Mechanismen funktionieren. Hierfür gibt es Flask-Erweiterungen wie Flask-JWT oder Flask-OAuthlib.

## Schritt 2: Endpoint-Strukturierung
**Ressourcenbasiertes Design**: RESTful APIs sind in der Regel ressourcenorientiert. Dies bedeutet, dass die Endpoints um die Ressourcen (wie Benutzer, Produkte, Nachrichten) herum strukturiert werden sollten. Zum Beispiel also wie folgend.

- `/users` für das Auflisten aller Benutzer oder das Erstellen eines neuen Benutzers.
- `/users/<id>` für das Abrufen, Aktualisieren oder Löschen eines spezifischen Benutzers.
- `/products/<id>/reviews` für das Anzeigen oder Hinzufügen von Bewertungen zu einem bestimmten Produkt.

## Schritt 3: Datenmodellierung
**Datenstruktur festlegen**: Definiere, wie die Daten strukturiert sein sollen. Welche Attribute hat beispielsweise ein Benutzer? Name, E-Mail, Passwort usw. sind gängige Felder.

**Beziehung zwischen Datenmodellen**: Bestimme die Beziehungen zwischen den Modellen. Zum Beispiel könnte ein Benutzer mehrere Bestellungen haben, und jede Bestellung könnte mehrere Produkte enthalten.

**Datenbankintegration mit SQLAlchemy**:
Flask arbeitet nicht direkt mit einer Datenbank, aber z.B. kann SQLAlchemy verwendet werden, um Modelle zu definieren, die Ihre Datenstrukturen repräsentieren.
Beispiele hierfür findest du in [Woche 6-7](../../datenbanken/datenbanken.md).