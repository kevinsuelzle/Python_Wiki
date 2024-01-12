# Aggregationen


**1. Gesamtpreis der Bestellungen pro Produkt:** Verwende MapReduce, um den Gesamtpreis der Bestellungen pro Produkt zu berechnen.
```javascript
db.bestellungen.mapReduce(
  function() { emit(this.produkt, this.menge * db.produkte.findOne({ name: this.produkt }).preis); },
  function(key, values) { return Array.sum(values); },
  { out: { inline: 1 } }
)
```

**2. Durchschnittsalter der Benutzer in jeder Stadt:** Berechne mithilfe von MapReduce das Durchschnittsalter der Benutzer in jeder Stadt.
```javascript
db.benutzer.mapReduce(
  function() { emit(this.stadt, this.alter); },
  function(key, values) { return Array.avg(values); },
  { out: { inline: 1 } }
)
```

**3. Anzahl der Bestellungen pro Tag:** Verwende MapReduce, um die Anzahl der Bestellungen für jeden Tag zu zählen.
```javascript
db.bestellungen.mapReduce(
  function() { emit(this.datum.toISOString().split('T')[0], 1); },
  function(key, values) { return Array.sum(values); },
  { out: { inline: 1 } }
)
```

**Gesamtpreis der Produkte in jedem Warenkorb:** Berechne mithilfe von MapReduce den Gesamtpreis der Produkte in jedem Warenkorb.
```javascript
db.warenkorb.mapReduce(
  function() { emit(this._id, this.preis * this.menge); },
  function(key, values) { return Array.sum(values); },
  { out: { inline: 1 } }
)
```

**4. Anzahl der Bestellungen pro Kunde:** Zähle mithilfe von MapReduce die Anzahl der Bestellungen für jeden Kunden.
```javascript
db.bestellungen.mapReduce(
function() { emit(this.kunde, 1); },
function(key, values) { return Array.sum(values); },
{ out: { inline: 1 } }
)
```

**5. Durchschnittliche Anzahl der Produkte in den Warenkörben:** Berechne mithilfe von MapReduce die durchschnittliche Anzahl der Produkte in den Warenkörben.
```javascript
db.warenkorb.mapReduce(
  function() { emit(this._id, 1); },
  function(key, values) { return Array.avg(values); },
  { out: { inline: 1 } }
)
```



**6. Durchschnittlicher Warenkorbpreis:**
```javascript
db.warenkorb.aggregate([
    { $group: { _id: null, total: { $sum: { $multiply: ["$preis", "$menge"] } } } }
])
```

**7. Häufigkeit der Produktkäufe:**
```javascript
db.bestellungen.aggregate([
    { $group: { _id: "$produkt", count: { $sum: 1 } } }
])
```

**8. Gesamtwert aller Bestellungen:**
```javascript
db.bestellungen.aggregate([
    { $lookup: { from: "produkte", localField: "produkt", foreignField: "name", as: "productInfo" } },
    { $unwind: "$productInfo" },
    { $group: { _id: null, totalValue: { $sum: { $multiply: ["$menge", "$productInfo.preis"] } } } }
])
```

**9. Anzahl der Kunden pro Stadt:**
```javascript
db.benutzer.aggregate([
    { $group: { _id: "$stadt", count: { $sum: 1 } } }
])
```

**10. Durchschnittsalter der Kunden:**
```javascript
db.benutzer.aggregate([
    { $group: { _id: null, averageAge: { $avg: "$alter" } } }
])
```

**11. Liste der Bücher pro Autor:**
```javascript
db.bücher.aggregate([
  { $group: { _id: "$autor", books: { $push: "$titel" } } }
])
```
