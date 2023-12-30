# Aufgabe: Kanban Board mit Flask und PyMongo

Erweitere das zuvor erstellte ToDo-Liste-Projekt, um ein Kanban Board als Webanwendung mit Flask zu entwickeln. Das Board soll es Benutzern ermöglichen, Aufgaben in verschiedenen Phasen zu organisieren, z.B., "To Do", "In Progress", "Done".

**Schritte:**

1. **Flask-App erstellen:**
   - Erstelle eine Flask-Anwendung mit einer Startseite und den erforderlichen Routen für die Anzeige des Kanban Boards.

2. **Datenbankanbindung mit PyMongo:**
   - Verwende PyMongo, um eine Verbindung zur MongoDB-Datenbank herzustellen, in der die Aufgaben gespeichert werden.

3. **HTML-Vorlagen erstellen:**
   - Erstelle HTML-Vorlagen für die verschiedenen Ansichten des Kanban Boards (z.B., "To Do", "In Progress", "Done").
   - Nutze Bootstrap oder andere CSS-Frameworks, um das Design zu verbessern.

4. **Flask-Routen implementieren:**
   - Implementiere Flask-Routen für das Anzeigen von Aufgaben in verschiedenen Phasen des Kanban Boards.
   - Beispiel: `/board/todo`, `/board/in_progress`, `/board/done`.

5. **Flask-Formulare für CRUD-Aktionen:**
   - Integriere Flask-Formulare, um Benutzern das Hinzufügen, Aktualisieren und Löschen von Aufgaben direkt über die Webanwendung zu ermöglichen.

6. **Drag-and-Drop-Funktionalität (optional):**
   - Erweitere die Webanwendung um Drag-and-Drop-Funktionalität, um Aufgaben zwischen verschiedenen Phasen des Kanban Boards zu verschieben.

7. **Benutzerauthentifizierung (optional):**
   - Implementiere eine einfache Benutzerauthentifizierung, um sicherzustellen, dass nur authentifizierte Benutzer das Kanban Board nutzen können.

8. **Hosting (optional):**
   - Hoste die Webanwendung in Azure.