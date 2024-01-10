# Arten von APIs
[45 min]

Beim durchschauen verschiedener APIs kann es sein, dass man unterschiedliche API-Arten findet. Je nach Anforderung an Einsatzszenario, Skalierbarkeit und Performance in der Entwicklung gibt es unter anderen diese 3 Arten.

## REST (Representational State Transfer)
REST basiert auf den Prinzipien des HTTP-Protokolls und ist für Einfachheit und Leistungsfähigkeit bekannt.
So genannten "RESTful" APIs verwenden standardisierte HTTP-Methoden (GET, POST, PUT, DELETE) und sind zustandslos, was bedeutet, dass jede Anfrage unabhängig ist. Das bedeutet auch, dass z.B. keine Nutzerinformationen gespeichert werden.

Im vorherigen Kapitel zu Datenbanken haben wir bereits das Konzept CRUD kennen gelernt. Die grundlegenden Operationen in CRUD (Erstellen, Lesen, Aktualisieren, Löschen) lassen sich auf die HTTP-Methoden abbilden, die in RESTful APIs verwendet werden
- **Read** entspricht **GET**.
- **Create** in CRUD entspricht **POST** in REST.
- **Update** entspricht **PUT** oder PATCH.
- **Delete** entspricht **DELETE**.

**Beispiel**
Eine neue Bestellung aufgeben:

```js
HTTP-Methode: GET
URI: /essen/{gericht}
``````

Wichtig zu verstehen ist, dass die Struktur der Antwort vom Server ist fest definiert ist. Diese könnte z.B. so aussehen:
```js
"order": {
    "id": "1",
    "name": "Bolognese",
    "kellner_id": "25123",
    "zubereitungszeit": "350"
}
```


## GraphQL

Entwickelt von Facebook, ist GraphQL eine Umgebung und Abfragesprache für APIs, die es Nutzern ermöglicht, genau zu spezifizieren, welche Daten sie benötigen.
Im Gegensatz zu REST, bei dem der Server die Struktur der Antwort bestimmt, ermöglicht GraphQL dem Nutzer, die Struktur der Anfrage zu definieren. Das führt zu effizienteren und flexibleren API-Aufrufen.

Hierbei existiert eine Schema Definition durch die bekannt wird, welche Informationen abrufbar sind.

```js
type Bestellung {
  id: ID
  kellner_id: ID
  essen: [Essen]
  zubereitungszeit: INT
}

type Essen {
  id: ID
  name: String
}
```

Eine Abfrage mit gleichem Ergebnis wie beim RESTful Beispiel wäre dann:

```js
query {
  bestellung(id: "1") {
    id
    kellner_id
    essen {
      name
    }
    zubereitungszeit
  }
}
```

Und zu folgender Antwort führen würde:

```js
{
  "bestellung": {
    "id": "1",
    "kellner_id": "25123",
    "essen": [
      {
        "name": "Bolognese",
      }
    ],
    "zubereitungszeit": "350"
  }
}
```

## WebSockets

WebSockets sind eine weitere Möglichkeit zwischen Nutzer (Client) und Server zu kommunizieren. Anders als bei REST und GraphQL bieten Websockets eine dauerhafte Verbindung und ermöglichen Echtzeitdatenübertragung. Deshalb sind sie ideal für Anwendungen, die kontinuierliche Datenupdates benötigen.
Beispiele hierfür sind Chat-Anwendungen oder Online-Spiele.
Im Gegensatz zu HTTP, das eine unidirektionale Verbindung darstellt, ermöglichen WebSockets eine bidirektionale Kommunikation, sodass Server und Client Daten gleichzeitig senden und empfangen können.