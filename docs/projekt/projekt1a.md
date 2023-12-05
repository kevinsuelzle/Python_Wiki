# Projekt 1: Thema Qualitätssicherung im Aftersales - "Einladung zum Werkstattbesuch"
Versetze dich in die Situation eines Verantwortlichen im Bereich Aftersales und Qualitätsmanagement. Ziel der Abteilung ist es, dass jeder Besitzer eines neuen Fahrzeugs eindeutig einem VW-Servicepartner zugeordnet ist und rechtzeitig in die Werkstatt eingeladen wird.
Dazu sind natürlich pro Fahrzeug mit einer Fahrzeugidentifikationsnummer (VIN = vehicle identification number) bestimmte Angaben gegeben.
Da es viele Fahrzeug gibt, soll die Verarbeitung natürlich mit einer Logik automatisiert ablaufen.
Deine Aufgabe ist es die Logik in einem Code zu entwickelt.

# Aufgabenstellung

### Aufgabe:
Clone das repository und mache dich mit dem Code vertraut. Kannst du mit eigenen Worten beschreiben, was der Code machen soll?
Hier findest du den Link zum Repo: https://git.qualidy.de/fakultaet73/data-science/project_1b

### Aufgabe:
Du findest eine readme.txt Datei im Repository, welche die Bedeutung der verschiedenen Listen beschreibt. 
Erkläre jede einzelne Liste in deinen eigenen Worten zusammen.
Schreibe eine kurze Einleitung über die Bedeutung des Qualitätsmanagements im Aftersales für Werkstattbesuche.

### Aufgabe:
Lese die Listen mit den benötigten Datei ein. Verwende hierzu den  Code aus dem Scropt qualitaetsicherung.py.
Hier siehst du einen Ausschnitt, welcher die Daten einliest.

```python 
with open("../wiki/material/vins.txt") as f:
        vins = f.readlines()

with open("../wiki/material/emails.txt") as f:
        emails = f.readlines()

with open("../wiki/material/last_workshop_visit.txt") as f:
        last_workshop_visit = f.readlines()
```

Der code ist leider noch nicht perfekt. Verbessere ihn, sodass die Daten richtig eingelesen werden und führe anschließend die Unittests durch, um dich zu überprüfen.

### Aufgabe:
Berechne eine Liste, die angibt, wie viele Tage das jeweilige Fahrzeug nicht mehr in der Werkstatt war. Überprüfe deine Angaben, indem du die Listen vergleichst.

### Aufgabe:
Wie lang ist die maximale Anzahl an Tagen, an denen ein Fahrzeug nicht in der Werkstatt war?
Um welches Fahrzeug handelt es sich?


### Aufgabe: 
Folgende Funktion ist aus dem Scipt entnommen und produziert Fehler. Eigentlich soll man damit die Dauer eines vorhandenen Service-Vertrages um eine anzahl von Jahren verlängern können. 
Was geht schief? Kannst du den Bug fixen? 
Beschreibe zunächst was die Funktion macht. Gehe dabei auf die Argumente ein und folge der Logik im Code.
Du findest eine test_aftersales.py Datei im selben Ordner, die einen Unittest ausführt, und dir sagt, wann du fertig bist.

```python 
def extend_service_duration(service_contract_durations, vins, vin , years):
    
    position = [i for i,x in enumerate(vins) if x == vin]
    service_contract_durations[position[0]] + years

    return service_contract_durations
```


### Aufgabe:
Berechne die Servicekosten, welche sich aus der Servicegebühr und der Servicepauschale zusammensetzt. 
Beachte dabei jedoch, dass diese nur anfällt, falls das Fahrzeug im aktuellen Betriebsjahr noch nicht in der Werkstatt war. 
Sonst soll der Wert mit "0 Euro" angegeben werden.


### Aufgabe: 
Schreibe eine Funktion, die pro Fahrzeug ausspuckt, ob der Kunde für einen Bremsbelagwechsel in die Werkstatt eingeladen werden soll.
Sofern seit dem letzten Besuch mindestens 30.000km zurückgelegt wurden, soll dies geschehen. Der Output soll wieder eine Liste sein.
Du darfst die Input-Listen nicht verändern.


### Aufgabe:
Prüfe das Format aller Telefonnummern (sie sollen mit +49 anfangen und die Führende 0 soll ggf. weggelassen werden.)
Schreibe eine Funktion, die das Prüft und ggf in diesen Standard überführt. Schreibe auch einen Unittest für deine Funktion in die bereits vorhandene Datei test_aftersales.py


### Aufgabe:
Prüfe, ob jedes Fahrzeug einem Servicepartner zugeordnet ist, damit dieser den Fahrzeughalten kontaktieren kann.
Falls nein, dann erstelle eine .txt Datei in der die Liste aller nicht-zugeordneten VINs inklusive der gegebenen Informationen, damit die Qualitätssicherung das Problem angehen kann.


### Aufgabe:
"Stelle die VIN mit der längsten Werkstattabwesenheit exemplarisch in einem Steckbrief dar. Verwende hierzu ein Foto des Fahrzeugmodells aus dem Internet und stelle mit einer Text-Bild-Kombination eine schöne Darstellung für deine Präsentation zusammen.
Leite eine Handlungsempfehlung für das Qualitätsmanagement dafür ab. Kann man hier den Service oder das System etwas verbessern?
Verwende hierzu das Python-Modul tkinter und stelle eine Schaltfläche bereit, mit welcher der Nutzer aus der Liste aller vorhandenen VINs auswählen kann.
Lass deiner Kreativität freien Lauf.


### Aufgabe:
Du wirst sicherlich schon bemerkt haben, dass die einzelen Listen sehr unpraktisch oder unbequem sind. Es wäre doch toll, alle Information in einem Objekt zu haben. Später wirst du lernen wie das geht.
Heute solst du noch für die Fachabteilung eine Datei erstellen, in der die Informationen geordnet zusammengestellt sind. Verwende hierzu bitte das JSON Format und gebe die Daten in einer .txt-Datei aus.


### Aufgabe:
Aus den gefahrenen Kilometern kannst du die Gesamtkilometerleistung der Flotte bestimmen. Mal angenommen die Flotte gehört zu einem Unternehmen, 
welches seinen Mitarbeitern die Fahrzeuge zur Verfügung gestellt hat. 
Der Kunde überlegt seinen Mitarbeitern freies Tanken mit diesen Fahrzeugen als Benefit zu schenken. 
Stell eine plausible Rechnung auf, mit der du die ungefähren Jahreskosten für die Flotte ausrechnest und dem Kunden präsentierst.
Was kostet es pro Mitarbeiter und Jahr in etwa? Würdest du dem Unternehmen diese Maßnahme empfehlen? Kannst du eine Auswahlfunktion in deiner App entwickeln, sodass die Kosten für die ausgewählte Flotte dort in der App angezeigt werden?


### Aufgabe:
Lade deine Ergebnisse ins remote GIT Repository hoch.

