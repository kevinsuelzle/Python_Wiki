# Autorenleitfaden

## Ansprechpartner

| Aufgabe   | Ansprechpartner  | Mail                                                  |
|-----------|------------------|-------------------------------------------------------|
| Allgemein | Viktor Reichert  | viktor.reichert@qualidy.de                            |
| Fachlich  | *Bene*dikt Boehm | benedikt@co-dex.de / benedikt.boehm-extern@qualidy.de |
| Buchungen | Daniel Schmidt   | daniel.schmidt@qualidy.de                             |
| Git       | Benedikt Boehm   | benedikt@co-dex.de / benedikt.boehm-extern@qualidy.de |
| Markdown  | Yoshi Kiel       | yoshi.kiel@qualidy.de                                 |
| Styling   |                  |                                                       |

## Autoren

| Name      | Mail                                                  |
|-----------|-------------------------------------------------------|
| Bene      | benedikt@co-dex.de / benedikt.boehm-extern@qualidy.de |
| Christian | chris@christian-marek-analytics.de                    |
| David     | david.kiss@qualidy.de                                 |
| Felix     | felix.tillmann@qualidy.de                             |
| Joachim   | waltherj@web.de                                       |
| Jürgen    | dr.juergen.brauer@gmail.com                           |
| Orell     | orell.garten-extern@qualidy.de                        |


## Das Skript

### Das Ziel

Das Skript soll den Unterrichtsleitfaden für die Trainer im Python Pathway bilden. Der Unterricht kann anhand des Skripts direkt abgehalten werden.
Das Skript wird chronologisch im Unterricht bearbeitet. Fällt ein Teilnehmer, weiß er genau, was er verpasst hat.
Das große Vorbild ist das Matheskript von Qualidy.

### Aufbau einzelner Kapitel

* Kurze Einführung in das Kapitel
* Erklärtexte und Übungsaufgaben im Wechsel, alles mit Videos versehen.
* Weitere Übungsaufgaben fürs Eigenstudium & Klausurvorbereitung.
* Liste aller neuen Vokabeln & Befehle mit Link zur Doku
* LZK (Lernzielkontrolle) **Mehr Infos folgen**
* Checkliste

## Zum Hauptblock

* Unterricht geht von 8:30 bis 16:15 min 45 Minuten Mittagspause (insg. 6,75 h)
* Bei jedem Erklärtext ungefähre Zeit im Unterricht schätzen
* Bei jeder Übungsaufgabe ungefähre Bearbeitungs- und Korrekturzeit.
* Erklärtexte in einfacher Sprache formulieren und ansprechend gestalten (keine Textwüsten, kurze Absätze, wenig Nebensätze, Tabellen & Auflistungen verwenden).
* Ganze Sätze schreiben und nicht kryptische Stichpunkte. Der Teilnehmer muss bei Fehlen im Unterricht auch mit dem Skript nacharbeiten können.
* Im Video kann mehr und ausführlicher erklärt werden.
* **Übungsaufgaben können gerne so konzipiert werden, dass die Inhalte über diese beigebracht werden**

### Bei allen Übungsaufgaben gilt

* Wenn aus einer Quelle übernommen, diese angeben.
* Chillis (1-4) verwenden, um Schwierigkeit anzuzeigen. Dabei ist 1 bis 3 Chillis klausurrelevant, 4 Chillis gehen über Klausurniveau hinaus.
  Immer eine ausprogrammierte Lösung mit einreichen

## Wer macht was?

| Zeit               |                        | Autor     | Reviewer  | Fertig bis |
|--------------------|------------------------|-----------|-----------|------------|
| Woche 1-3          | Python Grundlagen      | Orell     | Christian | 6.12.      |
| Woche 4-5          | Python Grundlagen      | Felix     | Christian | 6.12.      |
| Woche 3-5 je 1 Tag | git                    | Christian | Viktor    | 6.12.      |
| Projekt 1          | Lokale Applikation     | Christian | Felix     | 6.12.      |
| Woche 6-7          | DB + Clean Code        | Joachim   | Bene      | 13.12.     |
| Woche 8-10         | Web + Azure            | Joachim   | Bene      | 13.12.     |
| Projekt 2          | Webanwendung           | Joachim   | Bene      | 13.12.     |
| Woche 11-12.5      | DB2                    | Joachim   | Bene      | 22.12.     |
| Woche 12.5-13      | Pandas+matplot         | Jürgen    | David     | 22.12.     |
| Woche 14           | Python Fortgeschritten | Christian | David     | 22.12.     |
| Woche 15           | Robotik                | Jürgen    | Bene      | 22.12.     |
| Projekt 3          | Robotik                | Jürgen    | Bene      | 22.12.     |

## Inhalte des Skriptes

**Woche 1-3 Grundlagen Python**

* Einführung Programmierumgebungen
* Variablen & Datentypen & Input & output
* Mathematische Operatoren
* Debugger
* Boolean & Verzweigungen (if, else, elif)


* Listen, Tupel, Strings
* f-String und dazugehörige methoden
* Schleifen (for, while)
* Dictionaries und Sets
* Bytecode & Maschinencode


* Funktionen
* Type-Hints (Pep 484)
* Listen-Comprehensions
* zip


**Woche 4-5 Grundlagen Python**

* try, except, finally
* Module & Pakete
* pip
* Tests schreiben (TDD)
  * Testing bei VW/Guidelines
  * assert
  * pytest
  * Testhirarchie
* Dateioperationen


* Objektorientierte Programmierung
  * Einführung
  * Self
  * Attribute
  * Methoden
  * Getter und Setter
  * Staticmethod und classmethod
  * Klassen
  * Vererbung
  * Projektstrukturen MVC, MVVC
  * Objektorientierte vs. Funktionale Programmierung
  * Magic Methods
  * Args & Kwargs ?
* ggf. library für Projekt	
* PEP 8, 20, 257 (Style Guide, Zen, Docstring)	
* Design Pattern	


**Woche 3-5 je 1 Tag git**
* wozu Git?
* Ziele eines VCS?
* Terminologie
* Was ist ein Repository
* Vor- & Nachteile DVCS
* Working Area / Stage / Repo
* Konfiguration von Git
* Repo anlegen
* add & commit
* branch / referenzen
* mergen / cherry-pick / rebase
* remote
* fetch pull push
* standards


**Projekt 1**
* Lokale Applikation


**Woche 6-7 DB + Clean Code**
* Clean Code
* Einführung
  * Aufgreifen von sql aus Nebenfächern
  * Ergänzen nach Notwendigkeit
  * SQLITE
* DB-API2.0
* CRUD Operationen
* ORM
* Aufgabenteilung in großen Projekten
* SQL Alchemy oder Datenbanken mit Django

**Woche 8-10 Web + Azure**
* Domain Driven Design
* Request library
* Was ist eine API
* HTML
* CSS
* JS Grundlagen
  * Syntax & Basics
  * Fetch API
* Flask
* Projektplanung
* UML
  * Einführung und Motivation
  * Classdiagramms
  * Class, Class Types, Inherentance
  * Associations & Multiplicity
  * Aggregation & Composition
* Azure
  * Einführung ud Motivation
    * Warum Cloud
    * Was ist Azure
    * Alternativen zu Azure (AWS, GCP, IBM CLOUD)
    * Mandaten Überprüfen
    * Sensibilisieren (Default Zustand)
      * Wo liegt der Azure Server
      * Was sollte ich beachten
      * Wer kann meine Anwendungen sehen
  * Serverstandorte
  * Freigabe von Applikationen (IP-Freigabe)
  * Service Pläne
  * Überblick Services
  * App Service erstellen
  * Datenbank erstellen
  * App Deployment
    * Oberfläche
    * Konsole
    * VSCODE


**Projekt 2**
Webanwendung


**Woche 11-12.5 Docker + DB2**
* Docker
  * Motivation
  * Was sind Docker Container
  * Was sind Docker Images
  * Wo finde ich Container und Images
  * Verwendung von Docker in der CLI und mit Docker Desktop
  * Docker Compose
    * Motivation und Einführung
    * Vorher mit VW Infrastruktur testen
    * Eigene Compose Files schreiben
  * Fertige Images Laden
  * Eigene Images erstellen
* Datenbanken
  * NoSQL
    * Mongo DB & Pymongo
    * Cosmo DB
  * Evtl. Graph Datenbanken (NEO4J)
    * Neomodel
  * Datenbanken erstellen und bereitstellen
  * Welche Datenbank für welche Anwendungen
    * Alltemeiner Vergleich mit Vor- und Nachteilen
    * Beispiel
  * ACID
  * Datenbank Refactoring
  * SQL-Injection

**Woche 12.5-13 Pandas+matplot**
* numpy
* pandas
* matplotlib
  * Figure, Axes genau erklärt
* seaborn
* grafiken richtig interpretieren
* Datenverschleiherung/Betonung durch geschickte Darstellung
* Naive Bayes Classifier

**Woche 14 Python Fortgeschritten**
* Generatoren und Iteratoren
* Dekoratoren (Memoisation)
* args & kwargs
* lambda
* Abstract Class, Dataclass
* weitere fortgeschrittene Themen


**Woche 15 Robotik**
* Gezebo?
* Was ist ein SBC
* Hardware über SBC Ansprechen
* IOT?
* SBC mit Azure verbinden


**Projekt 3**
* Robotik   

## Quellen

Als Quelle für Pythonthemen bitte nur folgendes Buch verwenden (die Teilnehmer erhalten dieses Buch von VW gestellt):
…

Für weiterführende Bibliotheken, Inhalte und mehr Übungsaufgaben können natürlich auch andere Bücher verwendet werden. Die Teilnehmer haben eine Onlinebibliothek bei VW mit vielen Büchern.

## Organisatorisches

### Timeline


| Termin                                               | Block+Projekt 1 | Block+Projekt 2 | Block+Projekt 3 |
|------------------------------------------------------|-----------------|-----------------|-----------------|
| schriftlicher Teil an VW                             | 6.12.23         | 13.12.23        | 22.12.23        |
| VW überprüft schriftlichen Teil                      | 11.12.23        | 18.12.23        | 3.1.24          |
| Schriftlicher Teil überarbeitet & Videos aufgenommen | 20.12.23        | 4.1.24          | 9.1.24          |
| Absolut Finale Abgabe bei VW                         |                 | 12.1.24         |                 |
