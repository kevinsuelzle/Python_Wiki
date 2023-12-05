# Tabellen erstellen

## Grundform

Wir erstellen eine Tabelle, die die Anzahl und Eigenschaften der Werkzeuge in unserer Werkstatt aufnehmen soll.

      create table Werkzeuge (
          id int primary key, 
          bezeichnung text,
          gewicht real,
          farbe text 
      );

Man kann darüber streiten, ob die folgende Schreibweise **besser** ist oder nicht.

      create table Werkzeuge (
          id int primary key 
          , bezeichnung text
          , gewicht real
          , farbe text 
      );

Aber die Praxis zeigt, dass es beim Einfügen und Löschen von Spalten immer wieder zu Fehlern bei der Kommasetzung kommt.
Die zweite Form wirkt dem entgegen.

## Ändern der Tabelle

Wir haben erkannt, dass die Werkzeuge in verschiedene Kategorien eingeordnet werden können.

      alter table Werkzeuge
      add column waren_gruppe text;
    
      alter table Werkzeuge
      add column waren_untergruppe text;

Das Gewicht erscheint uns überflüssig.

In SQLite ist das direkte Löschen einer Spalte aus einer Tabelle mit dem `ALTER TABLE`-Befehl nicht möglich. Stattdessen
müssen Sie einen mehrstufigen Prozess durchführen, um eine Spalte zu entfernen. Dieser Prozess beinhaltet das Erstellen
einer neuen Tabelle, die alle gewünschten Spalten der ursprünglichen Tabelle enthält (außer der zu entfernenden Spalte),
das Kopieren der Daten von der alten in die neue Tabelle, das Löschen der alten Tabelle und schließlich das Umbenennen
der neuen Tabelle in den ursprünglichen Tabellennamen.

Hier ist, wie Sie die Spalte `Gewicht` aus Ihrer Tabelle `Werkzeuge` entfernen können:

1. **Erstellen Sie eine neue Tabelle**:
   Erstellen Sie eine neue Tabelle, die identisch mit der ursprünglichen Tabelle `Werkzeuge` ist, aber ohne die
   Spalte `Gewicht`.

         CREATE TABLE Werkzeuge_neu (
             id INT PRIMARY KEY,
             bezeichnung TEXT,
             farbe TEXT,
             Warengruppe TEXT,
             Warenuntergruppe TEXT
         );

2. **Kopieren Sie die Daten**:Kopieren Sie alle Daten von der alten Tabelle `Werkzeuge` in die neue
   Tabelle `Werkzeuge_neu`, ohne die Spalte `Gewicht`.

         INSERT INTO Werkzeuge_neu (id, bezeichnung, farbe, Warengruppe, Warenuntergruppe)
         SELECT id, bezeichnung, farbe, Warengruppe, Warenuntergruppe FROM Werkzeuge;

3. **Löschen Sie die alte Tabelle**:
   Löschen Sie nun die alte Tabelle `Werkzeuge`.

         DROP TABLE Werkzeuge;
   
4. **Benennen Sie die neue Tabelle um**:
   Benennen Sie die neue Tabelle `Werkzeuge_neu` in `Werkzeuge` um.

         ALTER TABLE Werkzeuge_neu RENAME TO Werkzeuge;

   
Nachdem Sie diese Schritte ausgeführt haben, haben Sie effektiv die Spalte `Gewicht` aus Ihrer Tabelle `Werkzeuge`
entfernt. Stellen Sie sicher, dass Sie vor dem Durchführen dieser Operationen eine Sicherungskopie Ihrer Datenbank
erstellen, um Datenverlust zu vermeiden.

Im Zuge der Normalisierung stellen sie fest, dass die beiden neuen Spalten den falschen Typ haben. Sie sollen als
Fremdschlüssel dienen und keinen Text enthalten.

Da hätte man besser planen müssen:

Um die Datentypen der Spalten `Warengruppe` und `Warenuntergruppe` in Ihrer `Werkzeuge`-Tabelle von `TEXT` auf `INT` zu
ändern und sie als Fremdschlüssel zu definieren, müssen Sie ähnliche Schritte wie beim Entfernen einer Spalte
durchführen. SQLite erlaubt es nicht, den Datentyp einer Spalte direkt zu ändern, wenn sie bereits Daten enthält.
Stattdessen müssen Sie eine neue Tabelle erstellen, die Daten übertragen, die alte Tabelle löschen und die neue Tabelle
umbenennen.

Bevor Sie beginnen, stellen Sie sicher, dass die Tabellen, auf die sich die Fremdschlüssel beziehen, bereits existieren.
Angenommen, Sie haben zwei Tabellen `Warengruppen` und `Warenuntergruppen`, und jede hat eine Spalte `ID` vom Typ `INT`,
die als Primärschlüssel dient.

**Aufgabe:**

1. **Erstellen Sie eine neue Tabelle**:

2. **Kopieren Sie die Daten**:
   Kopieren Sie die Daten von der alten Tabelle in die neue. Beachten Sie, dass Sie die Werte für `Warengruppe`
   und `Warenuntergruppe` entsprechend anpassen müssen, damit sie gültige Fremdschlüsselreferenzen darstellen.

3. **Löschen Sie die alte Tabelle**:

4. **Benennen Sie die neue Tabelle um**:

**Aufgabe:** Wir haben vergessen, die FOREIGN KEYS anzugeben.

Das Hinzufügen von Fremdschlüsselbeziehungen zu einer bestehenden Tabelle in SQLite, nachdem die Tabelle bereits
erstellt wurde, erfordert ähnliche Schritte wie das Ändern des Datentyps einer Spalte. SQLite unterstützt das direkte
Hinzufügen oder Ändern von Fremdschlüsseln in einer bestehenden Tabelle nicht. Sie müssen eine neue Tabelle mit den
gewünschten Fremdschlüsselbeziehungen erstellen, die Daten übertragen, die alte Tabelle löschen und die neue Tabelle
umbenennen.

Hier sind die Schritte, um Fremdschlüsselbeziehungen für die `Werkzeuge`-Tabelle hinzuzufügen:

1. **Erstellen Sie eine neue Tabelle mit Fremdschlüsseln**:
   Angenommen, Sie haben die Tabellen `Warengruppen` und `Warenuntergruppen` mit den Primärschlüsseln `ID`. Erstellen
   Sie eine neue Tabelle, die die Fremdschlüsselbeziehungen enthält:

2. **Kopieren Sie die Daten**:
   Kopieren Sie die Daten von der alten Tabelle `Werkzeuge` in die neue Tabelle `Werkzeuge_neu`. Stellen Sie sicher,
   dass die Werte in den Spalten `Warengruppe` und `Warenuntergruppe` gültige Fremdschlüsselreferenzen sind.

3. **Löschen Sie die alte Tabelle**:

4. **Benennen Sie die neue Tabelle um**:

[zurück](datenbanken.md)
