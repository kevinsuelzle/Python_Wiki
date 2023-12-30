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