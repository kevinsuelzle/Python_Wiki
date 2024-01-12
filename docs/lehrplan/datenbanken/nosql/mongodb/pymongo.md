# Pymongo
[15 min]

Wie auch für SQL gibt es für MongoDB Bibliotheken, die uns die Arbeit mit der Datenbank erleichtern, indem sie einen direkten Zugriff auf die Datenbank aus Python ermöglichen. Eine dieser Bibliotheken ist `pymongo`. Diese Bibliothek können wir mit `pip` installieren.

```bash
pip install pymongo
```

Um eine Verbindung zu einer MongoDB Datenbank herzustellen, müssen wir zunächst eine Verbindung zu einem MongoDB Server herstellen. Dies können wir mit der `MongoClient` Klasse aus der `pymongo` Bibliothek erreichen. Diese Klasse erwartet als Parameter die URL des MongoDB Servers. Standardmäßig ist der Port `27017`. Wenn wir uns mit einem lokalen MongoDB Server verbinden wollen, können wir die URL `mongodb://localhost:27017` verwenden.

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
```

Nachdem die Verbindung zum MongoDB-Server mit der `MongoClient`-Klasse hergestellt wurde, können wir auf die Datenbanken zugreifen und verschiedene Operationen durchführen.

### Zugriff auf eine Datenbank:
[5 min]

```python
# Beispiel: Zugriff auf eine Datenbank mit dem Namen 'mydatabase'
database = client['mydatabase']
```

Dokumente werden in python als Dictionary dargestellt. Ein Dokument könnte also wie folgt aussehen:

```python
my_document = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "MongoDB"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}
```

### Einfügen von Dokumenten:
[10 min]

Möchten wir Dokumente in eine Sammlung einfügen, können wir die `insert_one()` Methode verwenden. Diese Methode erwartet ein Dictionary als Parameter, das das einzufügende Dokument enthält. Die Methode gibt ein `InsertOneResult` Objekt zurück, das die ID des eingefügten Dokuments enthält.

```python
# Beispiel: Einfügen eines Dokuments in eine Sammlung mit dem Namen 'mycollection'
collection = database['mycollection']
document = {"name": "John", "age": 30, "city": "New York"}
result = collection.insert_one(document)
```

### Lesen von Dokumenten:
[5 min]

Zum lesen von Dokumenten können wir die `find()` Methode verwenden. Diese Methode gibt ein `Cursor` Objekt zurück, das alle Dokumente in der Sammlung enthält. Um die Daten aus dem Cursor zu lesen, können wir die `forEach()` Methode verwenden. Diese Methode erwartet eine Funktion als Parameter, die für jedes Dokument in der Sammlung ausgeführt wird. Die Funktion erhält das aktuelle Dokument als Parameter.

```python
# Beispiel: Abfrage aller Dokumente in einer Sammlung
documents = collection.find()

# Beispiel: Abfrage mit Filter
filtered_documents = collection.find({"city": "New York"})

# Beispiel: Abfrage aller Dokumente in einer Sammlung mit forEach
documents.forEach(lambda doc: print(doc))
```

### Aktualisieren von Dokumenten:
[5 min]

Das Aktualisieren von Dokumenten können wir mit der `update_one()` Methode erreichen. Diese Methode erwartet zwei Parameter: ein Objekt, das das zu aktualisierende Dokument enthält, und ein Objekt, das die Aktualisierungen enthält. Die Methode gibt ein `UpdateResult` Objekt zurück, das die Anzahl der aktualisierten Dokumente enthält.

```python
# Beispiel: Aktualisierung eines Dokuments
update_criteria = {"name": "John"}
new_values = {"$set": {"age": 31}}
update_result = collection.update_one(update_criteria, new_values)
```

### Löschen von Dokumenten:
[5 min]

Das Löschen von Dokumenten können wir mit der `delete_one()` Methode erreichen. Diese Methode erwartet ein Objekt, das das zu löschende Dokument enthält. Die Methode gibt ein `DeleteResult` Objekt zurück, das die Anzahl der gelöschten Dokumente enthält.

```python
# Beispiel: Löschen eines Dokuments
delete_criteria = {"name": "John"}
delete_result = collection.delete_one(delete_criteria)
```


Bei den vorgestellen CRUD Beispielen wird bereits deutlich, dass die Syntax von der mongos und pymongo weitestgehend identisch ist. Beide basieren auf der MongoDB Query Language (MQL), wodurch die Abfrage- und Update-Operationen in beiden Umgebungen ähnlich sind. Daher werden wir uns die weiteren Methoden nicht noch einmal explizit ansehen. Für weitere Informationen zu den Methoden und deren Syntax können wir bei Bedarf die [Dokumentation](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html) verwenden. Stattdessen sehen wir uns eine Beispielaufgabe zur Verwendung von pymongo an.

### Beispielaufgabe:
[30 min]

Gegeben ist eine MongoDB-Datenbank mit dem Namen "blog" und einer Sammlung (Collection) namens "articles". Die Struktur der Dokumente in der Sammlung sieht folgendermaßen aus:

```json
{
  "_id": ObjectId("5f9c7c6c0e79b3f6a7f22c50"),
  "title": "Introduction to MongoDB",
  "author": "John Doe",
  "views": 1500,
  "tags": ["NoSQL", "Database", "MongoDB"]
}
```

- Als erstes möchten wir eine Verbindung zur Datenbank herstellen. Dafür verwenden wir die `MongoClient` Klasse aus der `pymongo` Bibliothek. 

```python
from pymongo import MongoClient

# Verbindung zur Datenbank herstellen
client = MongoClient('mongodb://localhost:27017')
db = client.blog
collection = db.articles
```

- Die zweite Aufgabe besteht darin, alle Dokumente der "articles" Sammlung anzuzeigen. Dafür verwenden wir die `find()` Methode. 

```python
# Aufgabe 2: Alle Dokumente anzeigen
all_documents = collection.find()
for doc in all_documents:
    print(doc)
```

- Nun möchten wir eine Abfrage schreiben, die alle Dokumente mit dem Autor "John Doe" zurückgibt. Dafür verwenden wir die `find()` Methode mit einem Filter.

```python
# Aufgabe 3: Filtern nach Autor (z. B. "John Doe")
author_documents = collection.find({"author": "John Doe"})
for doc in author_documents:
    print(doc)
```

- Nachdem wir erfolgreich aus der Datenbank lesen konnten, wollen wir jetzt die Anzahl der "views" für einen bestimmten Artikel (z. B. den Artikel mit dem Titel "Introduction to MongoDB") auf 2000 aktualisieren.

```python
# Aufgabe 4: Dokument aktualisieren (Aufrufe auf 2000 setzen)
update_filter = {"title": "Introduction to MongoDB"}
update_data = {"$set": {"views": 2000}}
collection.update_one(update_filter, update_data)
```

- Wir sollen einen neuen Artikel hinzufügen. Der Artikel hat den Titel "Advanced MongoDB Techniques" und wurde von "Jane Smith" geschrieben. Der Artikel hat 1200 Aufrufe und die Tags "NoSQL", "Database" und "Advanced".

```python
# Aufgabe 5: Artikel hinzufügen
new_article = {
    "title": "Advanced MongoDB Techniques",
    "author": "Jane Smith",
    "views": 1200,
    "tags": ["NoSQL", "Database", "Advanced"]
}
collection.insert_one(new_article)
```

- Mit den neum neuen Eintrag in der Datenbank wollen wir nun die Anzahl der Artikel mit dem Tag "Advanced" zählen. Dafür verwenden wir die `count_documents()` Methode.

```python
# Aufgabe 6: Anzahl der Artikel mit dem Tag "Advanced" zählen
advanced_count = collection.count_documents({"tags": "Advanced"})
print(advanced_count)
```

- Außerdem möchten wir eine Abfrage schreiben, welche Artikel mit mehr als 1000 Aufrufen anzeigt. Dafür verwenden wir die `find()` Methode mit einem Filter.

```python
# Aufgabe 7: Filtern und Sortieren
filtered_and_sorted = collection.find({"views": {"$gt": 1000}}).sort("views", -1)
for doc in filtered_and_sorted:
    print(doc)
```

- Zuletzt sollen wir alle Artikel mit dem Tag "Database" löschen. Dafür verwenden wir die `delete_many()` Methode.

```python
# Aufgabe 8: Löschen von Dokumenten
delete_filter = {"tags": "Database"}
collection.delete_many(delete_filter)
```

- Um zu überprüfen, ob die Artikel mit dem Tag "Database" gelöscht wurden, geben wir alle Dokumente in der Sammlung aus.

```python
# Aufgabe 9: Alle Dokumente anzeigen
all_documents = collection.find()
for doc in all_documents:
    print(doc)
```

Mit Abschluss der Aufgabe schließen wir noch die Verbindung zur Datenbank.

```python
# Verbindung zur Datenbank schließen
client.close()
```

## Aufgabe TODO-APP:
[90 min]
Erstelle eine ToDo-Liste-Anwendung, die MongoDB als Datenbank verwendet. Die Anwendung sollte CRUD-Operationen (Create, Read, Update, Delete) für Aufgaben ermöglichen. Jede Aufgabe besteht aus einem Titel, einer Beschreibung und einem Status (z.B., "To Do", "In Progress", "Done").

**Schritte:**

1. **Datenbank und Sammlung erstellen:** 🌶
    - Erstelle eine MongoDB-Datenbank mit dem Namen "ToDoDB".
    - In dieser Datenbank erstelle eine Sammlung mit dem Namen "tasks".

2. **PyMongo-Verbindung einrichten:** 🌶
    - Nutze PyMongo, um eine Verbindung zur MongoDB-Datenbank herzustellen.

3. **Funktionen für CRUD-Operationen erstellen:** 🌶🌶
    - Implementiere Funktionen für das Erstellen, Lesen, Aktualisieren und Löschen von Aufgaben in der Datenbank.
    - Beispiel: `create_task(title, description, status)`, `get_tasks()`, `update_task(task_id, new_title, new_description, new_status)`, `delete_task(task_id)`.

4. **CLI-Benutzerschnittstelle erstellen:** 🌶🌶🌶
    - Erstelle eine einfache Befehlszeilenschnittstelle (CLI), die es dem Benutzer ermöglicht, Aufgaben hinzuzufügen, anzuzeigen, zu aktualisieren und zu löschen.
    - Beispiel: `python todo_app.py add "Task Title" "Task Description" "To Do"`, `python todo_app.py list`, `python todo_app.py update task_id "New Title" "New Description" "In Progress"`, `python todo_app.py delete task_id`.

5. **Zusätzliche Funktionen (optional):** 🌶🌶🌶🌶
    - Implementiere eine Funktion zum Suchen von Aufgaben nach Titel oder Status.
    - Füge eine Funktion hinzu, um alle Aufgaben nach ihrem Status zu zählen.
    - Erweitere die Datenbankstruktur, um Benutzerinformationen zu speichern und weise Aufgaben bestimmten Benutzern zu.

[Link zur Lösung](../lösungen/aufgabe8.md)