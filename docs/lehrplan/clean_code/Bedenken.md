# Bedenken

## Begriffsdefinition

In diesem Kontext bezieht sich der Begriff "Bedenken" (engl. "concerns") auf verschiedene Aspekte, Elemente oder
Interessen, die in der Softwareentwicklung berücksichtigt werden müssen. Es handelt sich um eine Art der Kategorisierung
oder Segmentierung von Funktionalitäten oder Verantwortlichkeiten innerhalb eines Softwareprojekts. Einige
Schlüsselpunkte dazu:
## Trennung von Bedenken (Separation of Concerns):
- Dies ist ein Designprinzip in der Softwareentwicklung, das darauf abzielt, ein Programm in verschiedene Teile
  aufzuteilen, wobei jeder Teil eine separate Aufgabe oder Bedenken behandelt.
- Ziel ist es, die Komplexität zu reduzieren und die Wartbarkeit zu erhöhen, indem jede Komponente oder Modul sich
  nur mit einem spezifischen Aspekt oder Problem befasst.
## Beispiele für Bedenken:
- **Datenzugriff:** Wie und wo Daten gespeichert und abgerufen werden.
- **Geschäftslogik:** Regeln und Verfahren, die die Geschäftsprozesse steuern.
- **Benutzeroberfläche:** Alles, was mit der Darstellung und Interaktion mit dem Benutzer zu tun hat.
- **Sicherheit:** Authentifizierung, Autorisierung, Verschlüsselung usw.
- **Performance:** Optimierung der Ausführungsgeschwindigkeit und Ressourcennutzung.

## Vorteile der Trennung von Bedenken:
- **Wartbarkeit:** Änderungen in einem Bereich des Systems beeinflussen nicht andere Teile.
- **Testbarkeit:** Einfacheres Testen, da jeder Teil isoliert betrachtet werden kann.
- **Erweiterbarkeit:** Neue Funktionalitäten können hinzugefügt werden, ohne bestehende zu beeinträchtigen.
- **Verständlichkeit:** Klar definierte Verantwortlichkeiten erleichtern das Verständnis des Codes.

In der Praxis bedeutet die Anwendung des Prinzips der Trennung von Bedenken, dass Entwickler darauf achten, dass
verschiedene Aspekte der Anwendung klar voneinander getrennt sind und nicht miteinander vermischt werden, was zu einem
saubereren, besser organisierten und wartbaren Code führt.

**Hinweis**:

Das Prinzip der Trennung von Bedenken (Separation of Concerns) ist eng mit den Ansätzen von Domain-Driven Design (DDD)
verbunden. DDD ist eine Methodik in der Softwareentwicklung, die sich darauf konzentriert, die Komplexität großer
Software-Systeme zu bewältigen, indem sie die Organisation des Codes um die Geschäftsdomäne (also den Bereich, für den
die Software entwickelt wird) herum zentriert.

[zurück](../Refactoring)