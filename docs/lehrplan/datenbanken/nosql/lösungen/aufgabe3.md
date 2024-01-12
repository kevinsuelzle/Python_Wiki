
# CRUD Operations

**1. Lesen (Read):** Lies alle Dokumente in der Sammlung "Benutzer" und gib sie aus.

```bash
use benutzer
db.benutzer.find()
```

**2. Suchen (Read):** Finde alle Dokumente in der Sammlung "Produkte" mit einem Preis über 50.

```bash
use produkte
db.produkte.find({ "preis": { $gt: 50 } })
```

**3. Einfügen (Create):** Füge ein neues Dokument zur Sammlung "Kunden" hinzu. Das Dokument soll Informationen wie "Name", "E-Mail" und "Adresse" enthalten.

```bash
use kunden
db.kunden.insertOne({
    "name": "Max Muster",
    "email": "max.muster@example.com",
    "adresse": "Hauptstraße 456"
})
```

**4. Aktualisieren (Update):** Aktualisiere den Preis aller Produkte in der Sammlung "Warenkorb" um 10%.

```bash
use warenkorb
db.warenkorb.updateMany({}, { $mul: { "preis": 1.1 } })
```

**5. Löschen (Delete):** Lösche alle Dokumente in der Sammlung "Bestellungen", die älter als 30 Tage sind.

```bash
use bestellungen
db.bestellungen.deleteMany({ "datum": { $lt: ISODate("2022-11-30") } })
```

**6. Filtern und Auswählen (Read):** Finde alle Dokumente in der Sammlung "Bücher", die den Autor "John Doe" haben, und gib nur die Buchtitel aus.

```bash
use bücher
db.bücher.find({ "autor": "John Doe" }, { "titel": 1, "_id": 0 })
```

**7. Skip und Limit für Produkte:** Überspringe die ersten 2 Produkte und gib die nächsten 3 Produkte aus.
```javascript
db.produkte.find().skip(2).limit(3)
```

**8. Sortiere Bestellungen nach Datum absteigend:** Sortiere die Bestellungen nach dem Datum in absteigender Reihenfolge.
```javascript
db.bestellungen.find().sort({ datum: -1 })
```

**9. Count der Kunden in Berlin:** Zähle die Anzahl der Kunden, die in Berlin leben.
```javascript
db.benutzer.find({ stadt: "Berlin" }).count()
```

**10. Erstes Buch im Alphabet:** Finde das erste Buch im Alphabetisch sortierten Titel.
```javascript
db.bücher.find().sort({ titel: 1 }).limit(1)
```

**11. Suche nach einem bestimmten Produkt:** Finde ein Produkt in der Sammlung "Produkte" nach einem bestimmten Kriterium.
```javascript
db.produkte.findOne({ marke: "ABC" })
```

**12. Anzahl der Bestellungen für jedes Produkt:** Zähle die Anzahl der Bestellungen für jedes Produkt.
```javascript
db.bestellungen.aggregate([
    { $group: { _id: "$produkt", count: { $sum: 1 } } }
])
```


