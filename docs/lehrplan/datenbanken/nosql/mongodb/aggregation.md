# Weitere Funktionen


### aggregate()

Die `aggregate()` Methode führt eine Aggregation auf der Collection aus. Diese Methode erwartet ein Array von Objekten als Parameter, die die Aggregationsschritte enthalten. Das Vorgehen über mehrere Schritte in der Agrregation wird auch als als Pipeline bezeichnet.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Aggregation der Dokumente in der Collection
db.meineCollection.aggregate([
  { $match: { name: 'Beispiel' } },
  { $group: { _id: '$name', count: { $sum: 1 } } }
])
```

***Beispiel***

Angenommen, wir haben eine Collection `meineCollection` mit Dokumenten, die Benutzerinformationen enthalten:

```json
{ "_id": 1, "name": "Beispiel", "age": 25 }
{ "_id": 2, "name": "Beispiel", "age": 30 }
{ "_id": 3, "name": "Anderes Beispiel", "age": 25 }
```

#### Aggregationsstufen in MongoDB-Shell-Code

```bash
[
  // Stufe 1: Filtere Dokumente mit dem Namen 'Beispiel'
  { $match: { name: 'Beispiel' } },

  // Stufe 2: Gruppiere nach dem Namen und zähle die Dokumente pro Gruppe
  { $group: { _id: '$name', count: { $sum: 1 } } }
]
```

Die Aggregationsstufen entsprechen den Schritten:

1. **$match**: Filtert die Dokumente, bei denen der Name gleich 'Beispiel' ist.
2. **$group**: Gruppiert die verbleibenden Dokumente nach dem Namen und zählt die Anzahl der Dokumente in jeder Gruppe.

#### Ausführung der `aggregate()`-Methode in der MongoDB-Shell

```bash
db.meineCollection.aggregate([
  { $match: { name: 'Beispiel' } },
  { $group: { _id: '$name', count: { $sum: 1 } } }
])
```

Das Ergebnis der Aggregation wäre:

```json
{ "_id": "Beispiel", "count": 2 }
```

In diesem Beispiel haben wir eine einfache Aggregation durchgeführt, um die Anzahl der Dokumente mit dem Namen 'Beispiel' zu zählen.

Es sind auch Pipelines mit mehr Schritten möglich:

```bash
db.meineCollection.aggregate([
  { $match: { status: 'aktiv' } },
  { $group: { _id: '$department', total: { $sum: '$salary' } } },
  { $sort: { total: -1 } },
  { $limit: 5 }
])

```


### mapReduce()

Die `mapReduce()` Methode führt eine Map-Reduce-Operation auf der Collection aus. Diese Methode erwartet zwei Funktionen als Parameter: eine Map-Funktion und eine Reduce-Funktion.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Map-Reduce-Operation auf der Collection
db.meineCollection.mapReduce(
  function() { emit(this.name, 1) },
  function(key, values) { return Array.sum(values) },
  { out: 'map_reduce_example' }
)
```

***Beispiel***

Angenommen, wir haben eine Collection `meineCollection` mit Dokumenten, die Benutzerinformationen enthalten:

```json
{ "_id": 1, "name": "Alice", "age": 25 }
{ "_id": 2, "name": "Bob", "age": 30 }
{ "_id": 3, "name": "Charlie", "age": 25 }
{ "_id": 4, "name": "Alice", "age": 28 }
```

Die Map-Funktion wird auf jedes Dokument in der Collection angewendet und erzeugt Schlüssel-Wert-Paare (Emit). Im Beispiel zählen wir die Anzahl der Dokumente pro `name`:

```javascript
function mapFunction() {
  emit(this.name, 1);
}
```

Das Ergebnis der Map-Funktion für unsere Collection wäre:

```json
{ "_id": "Alice", "value": 1 }
{ "_id": "Bob", "value": 1 }
{ "_id": "Charlie", "value": 1 }
{ "_id": "Alice", "value": 1 }
```

Die Reduce-Funktion wird auf die emiteten Werte angewendet und kombiniert sie. Im Beispiel addieren wir die Werte, um die Gesamtanzahl pro Name zu erhalten:

```bash
function reduceFunction(key, values) {
  return Array.sum(values);
}
```

#### Ausführung der `mapReduce()`-Methode

Die `mapReduce()`-Methode führt die Map- und Reduce-Funktionen aus und speichert das Ergebnis in einer neuen Collection `map_reduce_example`:

```bash
db.meineCollection.mapReduce(
  function() { emit(this.name, 1) },
  function(key, values) { return Array.sum(values) },
  { out: 'map_reduce_example' }
)
```

Das Ergebnis in der `map_reduce_example`-Collection wäre:

```json
{ "_id": "Alice", "value": 2 }
{ "_id": "Bob", "value": 1 }
{ "_id": "Charlie", "value": 1 }
```

In diesem Beispiel haben wir eine einfache Zählung der Vorkommen jedes Namens in der `meineCollection` durchgeführt.


## Aufgaben

1. **Gesamtpreis der Bestellungen pro Produkt:**
      - Verwende MapReduce, um den Gesamtpreis der Bestellungen pro Produkt zu berechnen.

2. **Durchschnittsalter der Benutzer in jeder Stadt:**
      - Berechne mithilfe von MapReduce das Durchschnittsalter der Benutzer in jeder Stadt.

3. **Anzahl der Bestellungen pro Tag:**
      - Verwende MapReduce, um die Anzahl der Bestellungen für jeden Tag zu zählen.

4. **Gesamtpreis der Produkte in jedem Warenkorb:**
      - Berechne mithilfe von MapReduce den Gesamtpreis der Produkte in jedem Warenkorb.

5. **Anzahl der Bestellungen pro Kunde:**
      - Zähle mithilfe von MapReduce die Anzahl der Bestellungen für jeden Kunden.

6. **Durchschnittliche Anzahl der Produkte in den Warenkörben:**
      - Berechne mithilfe von MapReduce die durchschnittliche Anzahl der Produkte in den Warenkörben.

7. **Durchschnittlicher Warenkorbpreis:**
    - Berechne den durchschnittlichen Gesamtpreis aller Artikel im Warenkorb (Sammlung: Warenkorb).

8. **Häufigkeit der Produktkäufe:**
    - Gruppiere die Bestellungen nach Produkt und zähle, wie oft jedes Produkt gekauft wurde (Sammlungen: Bestellungen, Produkte).

9. **Gesamtwert aller Bestellungen:**
    - Berechne den Gesamtwert aller Bestellungen unter Berücksichtigung der Produktmenge und des Einzelpreises (Sammlungen: Bestellungen, Produkte).

10. **Anzahl der Kunden pro Stadt:**
    - Zähle die Anzahl der Kunden pro Stadt in der Benutzersammlung.

11. **Durchschnittsalter der Kunden:**
    - Berechne das durchschnittliche Alter aller Kunden in der Benutzersammlung.

12. **Liste der Bücher pro Autor:**
    - Gruppiere die Bücher nach Autoren und erstelle eine Liste der Büchertitel für jeden Autor (Sammlungen: Bücher).



## Lösungen


1. **Gesamtpreis der Bestellungen pro Produkt:**
      - Verwende MapReduce, um den Gesamtpreis der Bestellungen pro Produkt zu berechnen.
      ```javascript
      db.bestellungen.mapReduce(
        function() { emit(this.produkt, this.menge * db.produkte.findOne({ name: this.produkt }).preis); },
        function(key, values) { return Array.sum(values); },
        { out: { inline: 1 } }
      )
      ```

2. **Durchschnittsalter der Benutzer in jeder Stadt:**
      - Berechne mithilfe von MapReduce das Durchschnittsalter der Benutzer in jeder Stadt.
      ```javascript
      db.benutzer.mapReduce(
        function() { emit(this.stadt, this.alter); },
        function(key, values) { return Array.avg(values); },
        { out: { inline: 1 } }
      )
      ```

3. **Anzahl der Bestellungen pro Tag:**
      - Verwende MapReduce, um die Anzahl der Bestellungen für jeden Tag zu zählen.
      ```javascript
      db.bestellungen.mapReduce(
        function() { emit(this.datum.toISOString().split('T')[0], 1); },
        function(key, values) { return Array.sum(values); },
        { out: { inline: 1 } }
      )
      ```

4. **Gesamtpreis der Produkte in jedem Warenkorb:**
      - Berechne mithilfe von MapReduce den Gesamtpreis der Produkte in jedem Warenkorb.
      ```javascript
      db.warenkorb.mapReduce(
        function() { emit(this._id, this.preis * this.menge); },
        function(key, values) { return Array.sum(values); },
        { out: { inline: 1 } }
      )
      ```

5. **Anzahl der Bestellungen pro Kunde:**
      - Zähle mithilfe von MapReduce die Anzahl der Bestellungen für jeden Kunden.
      ```javascript
      db.bestellungen.mapReduce(
        function() { emit(this.kunde, 1); },
        function(key, values) { return Array.sum(values); },
        { out: { inline: 1 } }
      )
      ```

6. **Durchschnittliche Anzahl der Produkte in den Warenkörben:**
      - Berechne mithilfe von MapReduce die durchschnittliche Anzahl der Produkte in den Warenkörben.
      ```javascript
      db.warenkorb.mapReduce(
        function() { emit(this._id, 1); },
        function(key, values) { return Array.avg(values); },
        { out: { inline: 1 } }
      )
      ```



7. **Durchschnittlicher Warenkorbpreis:**
   ```javascript
   db.warenkorb.aggregate([
     { $group: { _id: null, total: { $sum: { $multiply: ["$preis", "$menge"] } } } }
   ])
   ```

8. **Häufigkeit der Produktkäufe:**
   ```javascript
   db.bestellungen.aggregate([
     { $group: { _id: "$produkt", count: { $sum: 1 } } }
   ])
   ```

9. **Gesamtwert aller Bestellungen:**
   ```javascript
   db.bestellungen.aggregate([
     { $lookup: { from: "produkte", localField: "produkt", foreignField: "name", as: "productInfo" } },
     { $unwind: "$productInfo" },
     { $group: { _id: null, totalValue: { $sum: { $multiply: ["$menge", "$productInfo.preis"] } } } }
   ])
   ```

10. **Anzahl der Kunden pro Stadt:**
   ```javascript
   db.benutzer.aggregate([
     { $group: { _id: "$stadt", count: { $sum: 1 } } }
   ])
   ```

11. **Durchschnittsalter der Kunden:**
   ```javascript
   db.benutzer.aggregate([
     { $group: { _id: null, averageAge: { $avg: "$alter" } } }
   ])
   ```

12. **Liste der Bücher pro Autor:**
   ```javascript
   db.bücher.aggregate([
     { $group: { _id: "$autor", books: { $push: "$titel" } } }
   ])
   ```
