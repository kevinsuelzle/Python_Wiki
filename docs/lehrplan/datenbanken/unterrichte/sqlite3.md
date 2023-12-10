# Python und SQL
[15min]

Python biete uns die Möglichkeit, über ein Modul auf eine SQLite-Datenbanken zuzugreifen. Dieses Modul heißt `sqlite3` und ist in der Standardbibliothek von Python enthalten. Wir müssen es also nicht extra installieren. `sqlite3` stellt damit eine eingebettete Datenbank-Engine dar, die direkt in Anwendungen integriert werden kann, ohne dass ein separater Datenbankserver erforderlich ist. Die Interaktionen mit der Datenbank erfolgen über SQL-Abfragen, die in Python-Strings (Docstrings) geschrieben werden.

## Verbindung zur Datenbank
[15min]
Eine Verbindung zur SQLite-Datenbank kann über die connect()-Methode verwenden. 

``` py
import sqlite3
# Verbindung zur Datenbank herstellen (erstellt eine neue Datenbank namens "example.db" falls nicht vorhanden)
connection = sqlite3.connect("example.db")
```

Wenn die Datenbank nicht vorhanden ist, wird sie erstellt. Die connect()-Methode gibt ein Verbindungsobjekt zurück, das für die Durchführung von Datenbankoperationen verwendet wird. Dieses Verbindungsobjekt wird dann für die Erstellung eines Cursor-Objekts verwendet, um SQL-Anweisungen auszuführen.

Es ist wichtig zu beachten, dass diese Verbindung offen bleibt, bis Sie sie ausdrücklich schließen. Das Schließen der Verbindung wird oft am Ende Ihrer Datenbankoperationen durchgeführt. Das Schließen der Verbindung ist wichtig, um sicherzustellen, dass alle Änderungen, die während der Datenbankoperationen vorgenommen wurden, korrekt gespeichert werden, und um Ressourcen freizugeben. Wenn Sie die Verbindung nicht schließen, können unerwartete Probleme auftreten, insbesondere wenn Sie Ihre Anwendung beenden oder weitere Datenbankoperationen durchführen möchten. Das Schließen der Datenbankverbindung erfolgt über die close()-Methode.

``` py
# Verbindung schließen
connection.close()
```

## Das Curser-Objekt
[10min]
Der Cursor in der SQLite-Bibliothek (und in vielen anderen Datenbank-Bibliotheken) fungiert als Arbeitsbereich oder Zeiger, der es ermöglicht, SQL-Anweisungen auf der Datenbank auszuführen und mit den Ergebnissen zu interagieren. Der Cursor wird aus der Verbindungsinstanz erstellt und stellt die Schnittstelle bereit, um SQL-Anweisungen auf der Datenbank auszuführen. Das Cursor-Objekt wird über die Methode cursor() des Verbindungsobjekts erstellt.

``` py
# Cursor-Objekt erstellen
cursor = connection.cursor()
```

## Datenbankoperationen
[15min]
Über das cursor Objekt können wir nun Datenbankoperationen ausführen. Dazu gehören das Erstellen von Tabellen, das Einfügen von Daten, das Abrufen von Daten und das Löschen von Daten. Wichtig ist, dass die Operationen nach dem Ausführen mit der commit()-Methode bestätigt werden müssen. 

``` py
# Transaktion bestätigen
connection.commit()
```

Die folgenden Beispiele zeigen, wie die verschiedenen Operationen ausgeführt werden können.

### CREATE TABLE
``` py
# Tabelle erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
```

### INSERT
``` py
# Daten einfügen
cursor.execute('''INSERT INTO users (name, age) VALUES ('Max', 25)''')
```

### UPDATE
``` py
# Daten aktualisieren
cursor.execute('''UPDATE users SET age = 26 WHERE id = 1''')
```

### SELECT
``` py
# Daten abfragen
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### DELETE
``` py
# Daten löschen
cursor.execute('''DELETE FROM users WHERE id = 1''')
```

## Parametrisierung von SQL-Abfragen
[10min]

Die Parametrisierung von SQL-Abfragen ist eine Möglichkeit, SQL-Abfragen zu erstellen, die Platzhalter für Daten enthalten, die zur Laufzeit eingesetzt werden. Dies ist eine gute Möglichkeit, um SQL-Injection-Angriffe zu verhindern. Die Parametrisierung von SQL-Abfragen wird durch die Verwendung von Platzhaltern erreicht, die in der SQL-Anweisung verwendet werden. Diese Platzhalter werden dann durch die Werte ersetzt, die zur Laufzeit eingesetzt werden. Die Platzhalter werden durch ein Fragezeichen dargestellt. Die Werte, die zur Laufzeit eingesetzt werden, werden als Tupel übergeben.

``` py
# Daten einfügen
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Max', 25))
```

### Exkurs: SQL-Injection
[10min]

SQL-Injection ist eine Art von Angriff, bei dem ein Angreifer SQL-Code in eine Webformular-Eingabe oder in die URL einer Webseite einfügt, um die Datenbank zu manipulieren und Informationen preiszugeben, die der Entwickler nicht beabsichtigt hat. SQL-Injection ist eine der häufigsten Webangriffstechniken.

SQL-Injektionen treten auf, wenn Benutzereingaben oder andere nicht vertrauenswürdige Daten direkt in SQL-Anweisungen eingefügt werden, ohne ordnungsgemäße Validierung oder Bereinigung. Über die Parametrisierung von SQL-Abfragen können SQL-Injektionen verhindert werden. Die Parametrisierung von SQL-Abfragen bietet drei Hauptvorteile:

1. **Trennung von Daten und Anweisung:**
   - Platzhalter ermöglichen es, die SQL-Anweisung und die Daten, die in die Anweisung eingefügt werden sollen, zu trennen. Dadurch wird verhindert, dass Benutzereingaben direkt in die Anweisung eingebettet werden.

2. **Automatische Typkonvertierung:**
   - Die Parameterisierung ermöglicht eine automatische Typkonvertierung. Wenn beispielsweise ein Platzhalter für einen INTEGER-Wert verwendet wird und der Benutzer einen String einschickt, wird der Treiber automatisch versuchen, den String in einen INTEGER umzuwandeln, was zu sichereren Abfragen führt.

3. **Bereinigung von Sonderzeichen:**
   - Die meisten Datenbanktreiber führen interne Bereinigungen durch, um sicherzustellen, dass die eingefügten Daten sicher sind. Dies kann das Entfernen oder Maskieren von potenziell schädlichen Zeichen beinhalten.

Beispiel ohne Platzhalter (anfällig für SQL-Injektion):

```python
# ACHTUNG: Nicht empfohlen, da anfällig für SQL-Injektionen
user_input = "John Doe'; DROP TABLE users --"
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
```

Beispiel mit Platzhaltern (verhindert SQL-Injektionen):

```python
# Verwendung von Platzhaltern
user_input = "John Doe'; DROP TABLE users --"
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```

In diesem Beispiel würde der Versuch, eine SQL-Injektion durchzuführen, scheitern, da der Wert von `user_input` sicher durch den Platzhalter eingefügt wird, und der Treiber kümmert sich um die richtige Behandlung der Daten. Platzhalter sind daher eine bewährte Praxis, um die Sicherheit von Datenbankabfragen zu verbessern.


## Aufgaben
[126min]

### **Aufgabe 1: Datenbank erstellen 🌶️**
[3min]
Erstelle eine SQLite-Datenbank mit dem Namen "School.db". Füge eine Tabelle "Students" hinzu, die die Spalten "StudentID" (INTEGER), "Name" (TEXT) und "Grade" (INTEGER) enthält.

### **Aufgabe 2: Daten einfügen 🌶️**
[3min]
Füge drei Datensätze in die "Students"-Tabelle ein. Verwende Platzhalter für StudentID, Name und Grade.

### **Aufgabe 3: Daten abfragen 🌶️**
[3min]
Schreibe eine SQL-Abfrage, um alle Datensätze aus der "Students"-Tabelle abzurufen.

### **Aufgabe 4: Bedingte Abfrage 🌶️🌶️**
[6min]
Schreibe eine Abfrage, um alle Schüler mit einer Note besser als 3 abzurufen.

### **Aufgabe 5: Daten aktualisieren 🌶️**
[3min]
Aktualisiere den Namen eines Schülers mit der StudentID 1 auf "Emily Johnson".

### **Aufgabe 6: Daten löschen 🌶️**
[3min]
Lösche einen Schüler mit der StudentID 2 aus der Tabelle.

### **Aufgabe 7: Transaktionen 🌶️**
[3min]
Führe eine Transaktion durch, um zwei neue Schüler in einer einzigen Operation einzufügen. Bestätige die Transaktion.

### **Aufgabe 8: Aggregatfunktionen 🌶️🌶️**
[6min]
Schreibe eine Abfrage, um den Durchschnitt der Noten aller Schüler zu berechnen.

### **Aufgabe 9: Join-Operation 🌶️🌶️**
[10min]
Erstelle eine zweite Tabelle "Courses" mit den Spalten "CourseID" (INTEGER) und "CourseName" (TEXT). Schreibe eine SQL-Abfrage, die die Schülerdaten mit den Kursdaten verbindet.

### **Aufgabe 10: Indizes erstellen 🌶️🌶️**
[6min]
Erstelle einen Index auf der Spalte "Name" der "Students"-Tabelle, um Abfragen nach Schülernamen zu optimieren.

### **Projektaufgabe: Online-Shop Datenbank modellieren und verwenden 🌶️🌶️🌶️**
[80min]

Angenommen, du bist damit beauftragt, eine SQLite-Datenbank für einen Online-Shop zu erstellen und zu verwalten. Die Datenbank soll Informationen über Produkte, Kunden und Bestellungen speichern. Hier sind mehrere Aufgaben, um die Funktionalität der Datenbank zu überprüfen:

1. **Datenbank erstellen 🌶️:**
   Erstelle eine SQLite-Datenbank mit dem Namen "OnlineShop.db". Lege die notwendigen Tabellen für Produkte, Kunden und Bestellungen an. Achte darauf, Beziehungen zwischen den Tabellen herzustellen.

2. **Daten einfügen 🌶️🌶️:**
    Füge einige Beispieldaten für Produkte, Kunden und Bestellungen in die entsprechenden Tabellen ein.

1. **Kundendaten abfragen 🌶️:**
    Schreibe eine Abfrage, um alle Kundendaten abzurufen, einschließlich ihrer Bestellungen.

1. **Produkte mit Bestellinformationen 🌶️🌶️:**
    Erstelle eine Abfrage, um alle Produkte anzuzeigen, die bestellt wurden, und füge Informationen über die Anzahl der verkauften Einheiten hinzu.

1. **Bestellhistorie eines Kunden 🌶️🌶️:**
    Schreibe eine Abfrage, um die Bestellhistorie eines bestimmten Kunden anzuzeigen, einschließlich der Produkte, die in jeder Bestellung enthalten sind.

1. **Gesamtumsatz berechnen 🌶️🌶️🌶️:**
    Schreibe eine SQL-Abfrage, um den Gesamtumsatz des Online-Shops zu berechnen. Berücksichtige dabei alle abgeschlossenen Bestellungen.

1. **Aktualisiere Produktpreise 🌶️:**
    Aktualisiere die Preise aller Produkte um 10%. Stelle sicher, dass dies nur für zukünftige Bestellungen gilt und nicht die Preise bereits abgeschlossener Bestellungen beeinflusst.

1. **Neuen Kunden hinzufügen 🌶️🌶️:**
    Füge einen neuen Kunden zur Datenbank hinzu und platziere eine Testbestellung für einige Produkte.

1.  **Rabatt auf bestimmte Produkte 🌶️🌶️:**
    Gewähre einen Rabatt von 15% auf alle Produkte der Kategorie "Elektronik" für alle Kunden, die bereits mindestens zwei Bestellungen getätigt haben.

1.  **Lagerbestand überprüfen 🌶️🌶️:**
    Schreibe eine Abfrage, um den aktuellen Lagerbestand jedes Produkts anzuzeigen und markiere diejenigen, die unter einem bestimmten Schwellenwert liegen (z.B., weniger als 10 Einheiten).
