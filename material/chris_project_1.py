from datetime import datetime, timedelta, date


Service_Pauschale = "30 Euro"

with open("../wiki/material/vins.txt") as f:
        vins = f.readlines()

with open("../wiki/material/emails.txt") as f:
        emails = f.readlines()

with open("../wiki/material/last_workshop_visit.txt") as f:
        last_workshop_visit = f.readlines()

with open("../wiki/material/locations.txt") as f:
        locations = f.readlines()

with open("../wiki/material/mileage_readings.txt") as f:
        mileage_readings = f.readlines()

with open("../wiki/material/mileage_at_last_service.txt") as f:
        mileage_at_last_service = f.readlines()

with open("../wiki/material/mobile_numbers.txt") as f:
        mobile_numbers = f.readlines()

with open("../wiki/material/registration_dates.txt") as f:
        registration_dates = f.readlines()

with open("../wiki/material/service_contract_durations.txt") as f:
        service_contract_durations = f.readlines()

with open("../wiki/material/service_fees.txt") as f:
        service_fees = f.readlines()

with open("../wiki/material/service_partner_ids.txt") as f:
        service_partner_ids = f.readlines()

with open("../wiki/material/vehicle_models.txt") as f:
        vehicle_models = f.readlines()


### Aufgabe:
# Du findest eine readme.txt Datei im Repository, welche die Bedeutung der verschiedenen Listen beschreibt. Erkläre jede einzelne Liste in deinen eigenen Worten zusammen.
# Schreibe eine kurze Einleitung über die Bedeutung des Qualitätsmanagements im Aftersales für Werkstattbesuche.

### Aufgabe:
# Berechne eine Liste, die angibt, wie viele Tage das jeweilige Fahrzeug nicht mehr in der Werkstatt war.

### Aufgabe:
# Wie lang ist die maximale Anzahl an Tagen, an denen ein Fahrzeug nicht in der Werkstatt war?
# Um welches Fahrzeug handelt es sich?


### Aufgabe: 
# Folgende Funktion produziert Fehler. Woran liegt es? 
# Kannst du den Bug fixen? 
# Du findest eine test_aftersales.py Datei im selben Ordner, die einen Unittest ausführt, und dir sagt, wann du fertig bist.

def function_mit_fehler(input):

    result = 50

    return result


### Aufgabe:
#Berechne die Servicekosten, welche sich aus der Servicegebühr und der Servicepauschale zusammensetzt. 
#Beachte dabei jedoch, dass diese nur anfällt, falls das Fahrzeug im aktuellen Betriebsjahr noch nicht in der Werkstatt war. Sonst soll der Wert mit "0 Euro" angegeben werden.


### Aufgabe: 
# Schreibe eine Funktion, die pro Fahrzeug ausspuckt, ob der Kunde für einen Bremsbelagwechsel in die Werkstatt eingeladen werden soll.
# Sofern seit dem letzten Besuch mindestens 30.000km zurückgelegt wurden, soll dies geschehen. (Output wieder als Liste)


### Aufgabe:
# Prüfe das Format aller Telefonnummern (sie sollen mit +49 anfangen und die Führende 0 soll weggelassen werden.
# Schreibe eine funktion, die das Prüft bzw in den Standard überführt. Schreibe auch einen Unittest für deine Funktion in die bereits vorhandene Datei test_aftersales.py


### Aufgabe:
#Prüfe, ob jedes Fahrzeug einem Servicepartner zugeordnet ist, damit dieser den Fahrzeughalten kontaktieren kann.
# Falls nein, dann erstelle eine .txt Datei in der die Liste aller nicht-zugeordneten VINs inklusive der gegebenen Informationen, damit die Qualitätssicherung das Problem angehen kann.


### Aufgabe:
# Stelle die VIN mit der längsten Werkstattabwesenheit exemplarisch in einem Steckbrief dar. Verwende hierzu ein Foto des Fahrzeugmodells aus dem Internet und stelle mit einer Text-Bild-Kombination eine schöne Darstellung für deine Präsentation zusammen.
# Leite eine Handlungsempfehlung für das Qualitätsmanagement dafür ab. Kann man hier den Service oder das System etwas verbessern?
# Notiz: welches module dafür verwenden????
### Zusatzaufgabe:
# Mit dem Modul XXXXX kannst du die vorherige Aufgabe gerne bearbeiten und hier deiner Kreativität freien Lauf lassen.


### Aufgabe:
# Du wirst sicherlich schon bemerkt haben, dass die einzelen Listen sehr unpraktisch oder unbequem sind. Es wäre doch toll, alle Information in einem Objekt zu haben. Später wirst du lernen wie das geht.
# Heute solst du noch für die Fachabteilung eine Datei erstellen, in der die Informationen geordnet zusammengestellt sind. Verwende hierzu bitte ein JSON/DICTIONARY/... und gebe die Ergebnisse in einer .txt Datei aus.

#import json
#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)

### Aufgabe:
# Aus den gefahrenen Kilometern kannst du die Gesamtkilometerleistung der Flotte bestimmen. Mal angenommen die Flotte gehört zu einem Unternehmen, 
# welches seinen Mitarbeitern die Fahrzeuge zur Verfügung gestellt hat. 
# Der Kunde überlegt seinen Mitarbeitern freies Tanken mit diesen Fahrzeugen als Benefit zu schenken. 
# Stell eine plausible Rechnung auf, mit der du die ungefähren Jahreskosten für die Flotte ausrechnest und dem Kunden präsentierst.
# Was kostet es pro Mitarbeiter und Jahr in etwa? Würdest du dem Unternehmen diese Maßnahme empfehlen?


### Aufgabe:
# Lade deine Ergebnisse ins remote GIT Repository hoch.


if __name__ == "__main__":
      print(emails)