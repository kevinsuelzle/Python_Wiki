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

Über das cursor Objekt können wir nun Datenbankoperationen ausführen. Dazu gehören das Erstellen von Tabellen, das Einfügen von Daten, das Abrufen von Daten und das Löschen von Daten. Wichtig ist, dass die Operationen nach dem Ausführen mit der commit()-Methode bestätigt werden müssen. Die Operationen selbst werdend durch die execute()-Methode ausgeführt.

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
### **Aufgabe 1: Datenbank erstellen 🌶️**
[3min]
Erstelle eine SQLite-Datenbank mit dem Namen "School.db". Füge eine Tabelle "Students" hinzu, die die Spalten "StudentID" (INTEGER), "Name" (TEXT) und "Grade" (INTEGER) enthält.

### INSERT
``` py
# Daten einfügen
cursor.execute('''INSERT INTO users (name, age) VALUES ('Max', 25)''')
```

### **Aufgabe 2: Daten einfügen 🌶️**
[3min]
Füge drei Datensätze in die "Students"-Tabelle ein. Verwende Platzhalter für StudentID, Name und Grade.


### UPDATE
``` py
# Daten aktualisieren
cursor.execute('''UPDATE users SET age = 26 WHERE id = 1''')
```
### **Aufgabe 3: Daten aktualisieren 🌶️**
[3min]
Aktualisiere den Namen eines Schülers mit der StudentID 1 auf "Emily Johnson".

### SELECT
``` py
# Daten abfragen
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### **Aufgabe 4: Daten abfragen 🌶️**
[3min]
Schreibe eine SQL-Abfrage, um alle Datensätze aus der "Students"-Tabelle abzurufen.

### **Aufgabe 5: Bedingte Abfrage 🌶️🌶️**
[6min]
Schreibe eine Abfrage, um alle Schüler mit einer Note besser als 3 abzurufen.

### DELETE
``` py
# Daten löschen
cursor.execute('''DELETE FROM users WHERE id = 1''')
```

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
