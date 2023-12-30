# CRUD Operationen

In dem letzten Abschnitt haben wir uns angesehen, wie wir über einen Docker Container eine MongoDB Datenbank starten können und wie wir uns mit dieser Datenbank verbinden können. In diesem Abschnitt werden wir uns nun mit den CRUD Operationen beschäftigen. Die CRUD Operationen kennen wir bereits aus den vergangenen Einheiten zu Datenbanken.

## Create

Um Daten in MongoDB zu erstellen, können wir die `insert_one()` Methode verwenden. Diese Methode erwartet ein Dictionary als Parameter. Das Dictionary enthält die Daten, die wir in die Datenbank einfügen möchten. Die Methode gibt ein `InsertOneResult` Objekt zurück, das die ID des eingefügten Dokuments enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Einfügen eines Dokuments in eine Collection
db.meineCollection.insertOne({
  name: 'Beispiel',
  alter: 25,
  ort: 'Irgendwo'
})
```

## Read

Um Daten aus MongoDB zu lesen, können wir die `find()` Methode verwenden. Diese Methode gibt ein `Cursor` Objekt zurück, das alle Dokumente in der Collection enthält. Um die Daten aus dem Cursor zu lesen, können wir die `forEach()` Methode verwenden. Diese Methode erwartet eine Funktion als Parameter, die für jedes Dokument in der Collection ausgeführt wird. Die Funktion erhält das aktuelle Dokument als Parameter.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Anzeigen aller Dokumente in der Collection
db.meineCollection.find()

# Anzeigen con Dokumenten mit einer bestimmten Eigenschaft
db.meineCollection.find({ name: 'Beispiel' })

# Anzeigen aller Dokumente in der Collection mit forEach
db.meineCollection.find().forEach(function(doc) {
  print(doc)
})

```

## Update

Um Daten in MongoDB zu aktualisieren, können wir die `updateOne()` Methode verwenden. Diese Methode erwartet zwei Parameter: ein Objekt, das das zu aktualisierende Dokument enthält, und ein Objekt, das die Aktualisierungen enthält. Die Methode gibt ein `UpdateResult` Objekt zurück, das die Anzahl der aktualisierten Dokumente enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Aktualisieren eines Dokuments in einer Collection
db.meineCollection.updateOne(
  { name: 'Beispiel' },
  { $set: { name: 'Neuer Name' } }
)
```

## Delete

Um Daten in MongoDB zu löschen, können wir die `deleteOne()` Methode verwenden. Diese Methode erwartet ein Objekt, das das zu löschende Dokument enthält. Die Methode gibt ein `DeleteResult` Objekt zurück, das die Anzahl der gelöschten Dokumente enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Löschen eines Dokuments in einer Collection
db.meineCollection.deleteOne({ name: 'Beispiel' })

# Löschen aller Dokumente in einer Collection
db.meineCollection.deleteMany({})
```

## Weitere Methoden

Neben den hier vorgestellten Methoden gibt es noch viele weitere Methoden, die wir verwenden können. Eine vollständige Liste der Methoden findest du in der [MongoDB Dokumentation](https://docs.mongodb.com/manual/reference/method/). Hier werden wir lediglich einige der weiteren Methoden gemeinsam ansehen.

### findOne()

Die `findOne()` Methode gibt das erste Dokument in der Collection zurück. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften des gesuchten Dokuments enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Anzeigen des ersten Dokuments in der Collection
db.meineCollection.findOne()
```

### count()

Die `count()` Methode gibt die Anzahl der Dokumente in der Collection zurück. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften der gesuchten Dokumente enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Anzeigen der Anzahl der Dokumente in der Collection
db.meineCollection.count()
```

### sort()

Die `sort()` Methode sortiert die Dokumente in der Collection. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften enthält, nach denen die Dokumente sortiert werden sollen.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Sortieren der Dokumente in der Collection
db.meineCollection.find().sort({ name: 1 })
```

### limit()

Die `limit()` Methode begrenzt die Anzahl der zurückgegebenen Dokumente. Diese Methode erwartet eine Zahl als Parameter, die die Anzahl der zurückgegebenen Dokumente angibt.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Begrenzen der Anzahl der zurückgegebenen Dokumente
db.meineCollection.find().limit(5)
```

### skip()

Die `skip()` Methode überspringt eine bestimmte Anzahl von Dokumenten. Diese Methode erwartet eine Zahl als Parameter, die die Anzahl der zu überspringenden Dokumente angibt.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Überspringen der ersten 5 Dokumente
db.meineCollection.find().skip(5)
```

Dies sind einfache Funktionen, welche wir in Ähnlicher Weise bereits aus den SQL Datenbanken kennen. In den folgenden Abschnitten werden wir uns mit etwas komplexeren Funktionen beschäftigen, die MongoDB uns bietet.

## Aufgaben
Für die folgenden Aufgaben kannst du folgenden Code kopieren, umd ie entsprechenden Sammlungen zu erstellen:

```bash
# Beispiel für die Erstellung von Sammlungen in der MongoDB-Shell
use benutzer
use produkte
use kunden
use warenkorb
use bestellungen
use bücher

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Benutzer"
db.benutzer.insertMany([
  { "name": "Max Mustermann", "alter": 30, "stadt": "Berlin" },
  { "name": "Anna Schmidt", "alter": 25, "stadt": "München" }
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Produkte"
db.produkte.insertMany([
  { "name": "Smartphone", "preis": 500, "marke": "XYZ" },
  { "name": "Laptop", "preis": 1000, "marke": "ABC" }
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Kunden"
db.kunden.insertMany([
  { "name": "John Doe", "email": "john.doe@example.com", "adresse": "Hauptstraße 123" },
  { "name": "Jane Doe", "email": "jane.doe@example.com", "adresse": "Nebenstraße 456" }
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Warenkorb"
db.warenkorb.insertMany([
  { "produkt": "Smartphone", "preis": 500, "menge": 2 },
  { "produkt": "Laptop", "preis": 1000, "menge": 1 }
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Bestellungen"
db.bestellungen.insertMany([
  { "datum": ISODate("2022-12-01"), "produkt": "Smartphone", "menge": 2 },
  { "datum": ISODate("2022-11-15"), "produkt": "Laptop", "menge": 1 }
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Bücher"
db.bücher.insertMany([
  { "titel": "The Great Gatsby", "autor": "F. Scott Fitzgerald" },
  { "titel": "To Kill a Mockingbird", "autor": "Harper Lee" }
])
```

1. **Lesen (Read):**
    - Lies alle Dokumente in der Sammlung "Benutzer" und gib sie aus.

2. **Suchen (Read):**
    - Finde alle Dokumente in der Sammlung "Produkte" mit einem Preis über 50.

3. **Einfügen (Create):**
    - Füge ein neues Dokument zur Sammlung "Kunden" hinzu. Das Dokument soll Informationen wie "Name", "E-Mail" und "Adresse" enthalten.

4. **Aktualisieren (Update):**
    - Aktualisiere den Preis aller Produkte in der Sammlung "Warenkorb" um 10%.

5. **Löschen (Delete):**
    - Lösche alle Dokumente in der Sammlung "Bestellungen", die älter als 30 Tage sind.

6. **Filtern und Auswählen (Read):**
    - Finde alle Dokumente in der Sammlung "Bücher", die den Autor "John Doe" haben, und gib nur die Buchtitel aus.

7. **Skip und Limit für Produkte:**
    - Überspringe die ersten 2 Produkte und gib die nächsten 3 Produkte aus.

8. **Sortiere Bestellungen nach Datum absteigend:**
    - Sortiere die Bestellungen nach dem Datum in absteigender Reihenfolge.

9. **Count der Kunden in Berlin:**
    - Zähle die Anzahl der Kunden, die in Berlin leben.

10. **Erstes Buch im Alphabet:**
    - Finde das erste Buch im Alphabetisch sortierten Titel.

11. **Suche nach einem bestimmten Produkt:**
    - Finde ein Produkt in der Sammlung "Produkte" nach einem bestimmten Kriterium.

12. **Anzahl der Bestellungen für jedes Produkt:**
    - Zähle die Anzahl der Bestellungen für jedes Produkt.








## Lösungen:
1. **Lesen (Read):**
    - Lies alle Dokumente in der Sammlung "Benutzer" und gib sie aus.

    ```bash
    use benutzer
    db.benutzer.find()
    ```

2. **Suchen (Read):**
    - Finde alle Dokumente in der Sammlung "Produkte" mit einem Preis über 50.

    ```bash
    use produkte
    db.produkte.find({ "preis": { $gt: 50 } })
    ```

3. **Einfügen (Create):**
    - Füge ein neues Dokument zur Sammlung "Kunden" hinzu. Das Dokument soll Informationen wie "Name", "E-Mail" und "Adresse" enthalten.

    ```bash
    use kunden
    db.kunden.insertOne({
        "name": "Max Muster",
        "email": "max.muster@example.com",
        "adresse": "Hauptstraße 456"
    })
    ```

4. **Aktualisieren (Update):**
    - Aktualisiere den Preis aller Produkte in der Sammlung "Warenkorb" um 10%.

    ```bash
    use warenkorb
    db.warenkorb.updateMany({}, { $mul: { "preis": 1.1 } })
    ```

5. **Löschen (Delete):**
    - Lösche alle Dokumente in der Sammlung "Bestellungen", die älter als 30 Tage sind.

    ```bash
    use bestellungen
    db.bestellungen.deleteMany({ "datum": { $lt: ISODate("2022-11-30") } })
    ```

6. **Filtern und Auswählen (Read):**
   - Finde alle Dokumente in der Sammlung "Bücher", die den Autor "John Doe" haben, und gib nur die Buchtitel aus.

    ```bash
    use bücher
    db.bücher.find({ "autor": "John Doe" }, { "titel": 1, "_id": 0 })
    ```

7. **Skip und Limit für Produkte:**
    - Überspringe die ersten 2 Produkte und gib die nächsten 3 Produkte aus.
    ```javascript
    db.produkte.find().skip(2).limit(3)
    ```

8. **Sortiere Bestellungen nach Datum absteigend:**
    - Sortiere die Bestellungen nach dem Datum in absteigender Reihenfolge.
    ```javascript
    db.bestellungen.find().sort({ datum: -1 })
    ```

9. **Count der Kunden in Berlin:**
    - Zähle die Anzahl der Kunden, die in Berlin leben.
    ```javascript
    db.benutzer.find({ stadt: "Berlin" }).count()
    ```

10. **Erstes Buch im Alphabet:**
    - Finde das erste Buch im Alphabetisch sortierten Titel.
    ```javascript
    db.bücher.find().sort({ titel: 1 }).limit(1)
    ```

11. **Suche nach einem bestimmten Produkt:**
    - Finde ein Produkt in der Sammlung "Produkte" nach einem bestimmten Kriterium.
    ```javascript
    db.produkte.findOne({ marke: "ABC" })
    ```

12. **Anzahl der Bestellungen für jedes Produkt:**
    - Zähle die Anzahl der Bestellungen für jedes Produkt.
    ```javascript
    db.bestellungen.aggregate([
        { $group: { _id: "$produkt", count: { $sum: 1 } } }
    ])
    ```


