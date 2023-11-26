# DRY - Don't Repeat Yourself

![DRY](pictures/DRY.jpg "Don't repeat yourself")

Funktionen und Prozeduren sind dazu da, sich wiederholende Codeabschnitte zu vermeiden. Sie gehören zu den ältesten
Programmierparadigmen, die es gibt. Daher ist ihre Funktionsweise schon auf der Prozessorebene angelegt. Beim Aufruf
einer Funktion wird nämlich die Speicheradresse, zu man zurückkehrt, wenn die Funktion endet, in einen besonderen
Speicherbereich geschrieben. Somit kann ohne Zeitverlust das Programm fortgesetzt werden.

Einer der größten Vorteile davon ist es, dass man bei Änderungen nur in diesem einen Teil des Programmes arbeiten muss.

Die Schwierigkeit besteht heute darin, dass sich wiederholender Code nicht immer offen zeigt. In einer vielschichtigen
Anwendung ist es eher so, dass verschiedene Programmierer den gleichen Code produzieren, ohne es zu merken. Hier helfen
Code-Bibliotheken und der Blick über den eigenen Tellerrand und eine übergeordnete Software Architektur.

## Argumente gegen die strikte Anwendung des DRY-Prinzips

1. Über-Abstraktion
   Obwohl das DRY-Prinzip (Don't Repeat Yourself) generell als gute Praxis im Software-Engineering gilt, gibt es
   Situationen, in denen eine strikte Anwendung nicht ideal oder sogar kontraproduktiv sein kann. Hier sind einige
   Argumente, die gegen eine strikte Anwendung von DRY sprechen:
    - **Beschreibung:** Versuche, Wiederholungen zu vermeiden, können zu übermäßiger Abstraktion führen.
    - **Folge:** Der Code wird komplizierter und schwerer verständlich, besonders wenn die Abstraktionen nicht intuitiv
      oder schlecht dokumentiert sind.

2. Vorzeitige Optimierung

    - **Beschreibung:** Das vorzeitige Zusammenführen von Code in Funktionen oder Module kann problematisch sein.
    - **Folge:** Es entstehen starre Strukturen, die spätere Anpassungen erschweren.

3. Leichte Veränderungen in der Logik

    - **Beschreibung:** Ähnlicher, aber nicht identischer Code kann die Zusammenfassung komplex machen.
    - **Folge:** Es kann sinnvoller sein, ähnlichen Code separat zu halten, um Lesbarkeit und Wartbarkeit zu bewahren.

4. Leistungseinbußen

    - **Beschreibung:** In einigen Fällen kann die Vermeidung von Code-Duplikation zu Leistungseinbußen führen.
    - **Folge:** Ersetzen von Inline-Code durch Funktionsaufrufe kann Overhead verursachen, was in performancekritischen
      Anwendungen problematisch ist.

5. Erhöhte Kopplung

    - **Beschreibung:** Übermäßige Vermeidung von Duplikation kann zu einer erhöhten Kopplung zwischen Programmteilen
      führen.
    - **Folge:** Die Modularität kann beeinträchtigt werden, was den Code anfälliger für Fehler bei Änderungen macht.

6. Schwierigkeiten bei der Fehlerbehebung

    - **Beschreibung:** Wenn eine DRY-umsetzende Funktion einen Fehler aufweist, kann sich dieser auf mehrere
      Systemteile auswirken.
    - **Folge:** In manchen Fällen kann es sicherer sein, bestimmte Funktionalitäten zu duplizieren, besonders wenn sie
      kritisch sind und isoliert bleiben sollten.

### Zusammenfassung

DRY ist ein Leitprinzip und sollte nicht als unumstößliches Gesetz angesehen werden. Die Entscheidung, wann und wie DRY
angewendet wird, sollte auf einem Gleichgewicht zwischen Code-Effizienz, Lesbarkeit und Wartbarkeit basieren. Eine
Dokumentation der Gründe erscheint angebracht.
