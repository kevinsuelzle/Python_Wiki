# Test Driven Development
[30 min]

Um die Relevanz von Test Driven Developments nochmals hervorzuheben und die Konzepte zu festigen, schauen wir uns den Ansatz nochmal kurz an.

Wichtig zu verstehen ist, dass Test Driven Development eine umgekehrte Vorgehensweise fördert als ein normaler Entwicklungszyklus. Zuerst werden die Anforderungen als spezifische Testfälle definiert und dann wird der Code so entwickelt, dass diese Tests bestanden werden. 

Es erfordert natürlich eine initiale Zeitinvestition, um Tests zu schreiben, die sich jedoch langfristig auszahlt. Gerade für Teams, die neu in TDD sind, kann es eine zusätzliche Herausforderung sein, effektive Testfälle zu schreiben und den TDD-Rhythmus zu erlernen.

## Der TDD-Zyklus
Der TDD-Prozess folgt einem wiederholenden Zyklus, bekannt als "Red-Green-Refactor":

**Red**: Schreiben eines neuen Tests, der fehlschlägt, weil die geforderte Funktionalität noch nicht implementiert ist.

**Green**: Schreiben des minimal notwendigen Codes, um den Test zu bestehen.

**Refactor**: Überarbeiten des Codes, um Redundanzen zu beseitigen und die Qualität zu verbessern.

## Praktisches Beispiel
Bei der Entwickelung einer Anwendung zur Verwaltung von Kundendaten könnte ein TDD-Prozess folgendermaßen aussehen.

**Schreiben eines Tests für eine neue Funktion**: Überprüft, ob ein neuer Kunde korrekt zur Datenbank hinzugefügt wird.

  ```python
  def test_add_customer():
      customer = Customer(name="John Doe", age=30)
      customer_id = customer_service.add_customer(customer)
      assert customer_service.get_customer(customer_id) == customer
  ```

**Implementieren der Funktion**:
 - Schreiben des minimalen Codes, um den Test zu bestehen.
 - Beispiel: Implementierung der `add_customer`- und `get_customer`-Methoden in `customer_service`.

**Refaktorisieren**: Überarbeiten des Codes, um Duplikationen zu entfernen und die Lesbarkeit zu verbessern.


# Domain Driven Design
Domain Driven Design ist ein Ansatz in der Softwareentwicklung, der den Fokus auf das Herzstück der Anwendung, die Geschäftslogik und Prozesse, legt. Es basiert auf der engen Zusammenarbeit zwischen technischen Experten und Domain-Experten, um ein tiefes Verständnis der Domain zu erreichen und dieses in der Softwarestruktur widerzuspiegeln. In Woche 9 wird das Konzept DDD nochmals aufgegriffen und mit konkreten Aufgaben trainiert.

## Kernkonzepte von DDD
Im Herzen des Domain Driven Designs stehen mehrere Schlüsselkonzepte, die zusammen ein starkes Fundament für die Entwicklung komplexer Softwaresysteme bilden.

**Ubiquitous Language**: Eine einheitliche Sprache, die von allen Beteiligten verwendet wird, um Missverständnisse zu vermeiden und Klarheit zu schaffen. Ubiquitous Language erleichtert die Kommunikation zwischen technischen und nicht-technischen Teammitgliedern.

**Entitäten**: Objekte mit einer eindeutigen Identität, die über ihre Lebensdauer hinweg konstant bleibt, auch wenn sich ihre Eigenschaften ändern.

**Wertobjekte**: Objekte, die durch ihre Attribute definiert werden und keine eigene Identität haben.

**Aggregate**: Eine Gruppe von Entitäten und Wertobjekten, die als Einheit betrachtet werden, mit einer klar definierten Root-Entität.

**Repositories**: Schnittstellen, die den Zugriff auf Aggregate und deren Persistierung in einer Datenquelle ermöglichen.

## Designprinzipien
Domain Driven Design ist nicht nur eine Ansammlung von Praktiken und Mustern, sondern auch eine Denkweise, die tiefgreifende Prinzipien in den Vordergrund stellt.

**Modellzentrierter Ansatz**: Das Domain-Modell steht im Mittelpunkt der Entwicklung. Durch die Fokussierung auf die Geschäftslogik und -prozesse wird die Softwareentwicklung zielgerichteter und effizienter.

**Isolation der Domain**: Geschäftslogik sollte von technischen Aspekten der Anwendung isoliert sein. Das Design ist dadurch anpassungsfähiger an sich ändernde Geschäftsanforderungen.

**Subdomains**: Identifizierung verschiedener Teilbereiche innerhalb der Gesamtdomain, die unabhängig modelliert werden können.

**Bounded Contexts**: Klare Abgrenzung, innerhalb derer ein spezifisches Domain-Modell Gültigkeit hat.

## Praktisches Beispiel
Das folgende Beispiel zeigt, wie DDD dabei helfen kann, ein komplexes System in der Automobilproduktion zu strukturieren und zu managen, indem es ein klares Modell der Geschäftsdomäne bietet.

**Ubiquitous Language** alle Teammitglieder (Ingenieuren, Managern, Vertriebsmitarbeitern und Softwareentwicklern) müssen dieselben Begriffe für Produktionsprozesse und -komponenten verwenden. Z.B. `„Modell“`, `„Bauteil“`, `„Fertigungsstraße“`, `„Bestellung“`.

**Auto**: Eine **Entität** mit Eigenschaften wie `Seriennummer`, `Modell`, `Herstellungsdatum`. Die `Seriennummer` dient als eindeutige Identität.

**Mitarbeiter**: Eine **Entität** mit `Mitarbeiter-ID`, `Name`, `Rolle`.

**Adresse**: Ein **Wertobjekt** im Zusammenhang mit Lieferanten oder Kunden, `definiert durch Straße, Stadt, Postleitzahl`. Es hat keine eigene Identität und wird immer im Kontext einer Entität wie „Lieferant“ oder „Kunde“ verwendet.

**Fertigungsauftrag**: Ein **Aggregate** Root, das mehrere Entitäten wie `Auto`, `Bauteil`, `Mitarbeiter` umfasst. Es definiert den gesamten Prozess der Autoproduktion, von der Auswahl der Bauteile bis zur endgültigen Montage.

**Auto Repository**: Eine Schnittstelle, die den Zugriff auf Auto-Entitäten ermöglicht, z. B. `um nach fertigen Autos zu suchen` oder den Status eines Autos zu aktualisieren.

**Mitarbeiter Repository**: Ermöglicht den Zugriff auf Mitarbeiterdaten, `um Informationen wie Arbeitszeiten oder Zuweisungen zu verwalten`.


## Aufgaben
[45 min]

### Modellierung eines Domain-Modells für ein Autohaus 🌶️️🌶️️
Entwickle ein vereinfachtes Domain-Modell für ein Autohaus, das den Verkauf und die Reparatur von Autos verwaltet. Berücksichtige dabei die Kernkonzepte von DDD.

- Identifiziere relevante Entitäten und Wertobjekte, wie Kunde, Auto, Reparaturauftrag und Adresse.
- Definiere die Attribute und Methoden für jede Entität und jedes Wertobjekt.
- Erstelle Aggregates, die logische Gruppen von Entitäten und Wertobjekten darstellen, z.B. Verkaufsauftrag als Aggregate, das Kunde, Auto und Adresse enthält.
- Skizziere Repositories für den Zugriff auf die Aggregate, wie KundenRepository und AutoRepository.

### Entwicklung eines Bounded Contexts für die Lagerverwaltung 🌶️️🌶️️🌶️️
Entwerfe einen Bounded Context für die Lagerverwaltung innerhalb einer größeren Domäne eines Automobilherstellers.

- Definiere den Bounded Context für die Lagerverwaltung, einschließlich der Abgrenzung zu anderen Bereichen wie Produktion oder Vertrieb.
- Identifiziere die wichtigsten Entitäten innerhalb dieses Bounded Contexts, z.B. Lagereinheit, Bauteil, Lieferant.
- Lege die Beziehungen zwischen den Entitäten fest und bestimmen Sie, welche Entitäten Aggregate Roots sind.
- Erarbeite Ubiquitous Language, die spezifisch für den Lagerverwaltungskontext ist, und stellen Sie sicher, dass diese Sprache in Ihrem Modell und in Ihrer Kommunikation konsistent verwendet wird.
- Skizziere ein Repositorium, z.B. BauteilRepository, das den Zugriff auf Bauteile im Lager verwaltet.