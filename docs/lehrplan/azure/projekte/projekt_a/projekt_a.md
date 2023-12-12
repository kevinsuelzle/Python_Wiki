# Projekt A - Car Rental App

**Cloud Web App zum leihen von Fahrzeugen**: Entwickle eine Web App zur Selektion und der Anmietung von Fahrzeugen. Hierfür soll sowohl eine Flask API mit Anbindung zur Datenbank sowie ein simples Frontend mit Bootstrap erstellt werden.

Projektthema: API und Web App Entwicklung mit Deployment auf Azure

![App Screenshot](./assets/car_rent_1.png)
[App Demo](./assets/Car-rental-recording.mp4)

## Normalsprachliche Beschreibung des Projektes

### Überblick

Die Softwarelösung ist eine vollständig deployte Web App, die es den Nutzern erlaubt, Fahrzeuge über einen Kalender für spezifizierte Zeiträume zu buchen. Die bereits existierenden Buchungen verschiedener Nutzer werden in einer Kalenderansicht pro Fahrzeug angezeigt.

### Kernaspekte

1. **Fahrzeugverwaltung:**
    - Speicherung und Verwaltung von Fahrzeuginformationen wie Name, Farbe und Modell.
    - Möglichkeit, neue Buchungsanfragen in einer Datenbank zu speichern.
    - Fahrzeugbuchungen werden verwendet nicht verfügbare Zeiträume zu kennzeichnen.

2. **Dokumentation und Testing:**
    - Dokumentation der Struktur und folgen der Clean Code Prinzipien.
    - Simples Testing des Backends über Python Unit Tests sowie Postman Integration Tests.

3. **Deployment auf Azure:**
    - Aufteilung und Deployment der Web App in zwei separaten Teilen (Backend und Frontend).
    - Vernetzung der einzelnen Deployments über die Azure Oberfläche.

### Benutzeroberfläche und Interaktion

- Die Software bietet eine benutzerfreundliche Oberfläche, die es den Nutzern ermöglicht, effizient auf
  Informationen zuzugreifen und Operationen durchzuführen.
- Einfache Einsicht in die verschiedenen Fahrzeuge und deren Verfügbarkeit.
- Simpler Prozess zur Reservierung eines Fahrzeuges für den gewollten Zeitraum.

### Erweiterbarkeit und Skalierbarkeit

- Die Software ist so konzipiert, dass sie mit dem Wachstum des Unternehmens skaliert werden kann.
- Modularer Aufbau, der es ermöglicht, das Frontend und Backend separat zu erwitern und veröffentlichen.

### Deployment und Verfügbarkeit 

- Veröffentlichung der App für Nutzer über ein Azure Deployment als Web App.
- Einhaltung der Datenschutzbestimmungen, um den Schutz der persönlichen Informationen der Kunden zu garantieren.

## Zusammenfassung

Diese Softwarelösung zielt darauf ab, ein Service für Autovermieter bereitzustellen, mit dem es Nutzern erleichtert wird, direkt die bereits ausgebuchten Zeitslots zu sehen. Durch die Kombination aus Flask Backend, Datenbank Integration über ein ORM, Web Frontend mit Bootstrap und dem Deployment als Web App auf Azure, wird ein vollständiger Entwicklungszyklus durchlaufen.