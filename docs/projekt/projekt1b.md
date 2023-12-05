# Projekt 2: Thema Einkauf und Disposition - Stücklistenauflösung

Versetze dich hinein in einen Abteilungsverantwortlichen im Einkauf. Im Verantwortungsbereich der Leitenden Person liegen drei Module, welche in ausreichender Zahl 
rechtzeitig bestellt werden müssen, um eine durchgängige Produktion zu gewährleisten. 
Die Module selbst sind wiederum aus Bauteilen in bestimmter Menge zusammengesetzt. Gibt es nun eine Bestellung für ein Modul, so kann man relativ leicht ermitteln, wie viele Bauteile man jeweils insgesamt benötigt. Diese Auflösung der Stückliste benötigter Bauteile soll nun durch eine Software bequem bedienbar sein.
Diese Software wirst du entwickeln. Allerdings kannst du auf Code deines Vorgängers zugreifen. Mal schauen, wieviel bereits erledigt wurde.

# Aufgabenstellungen

### Aufgabe:
Clone das repository und mache dich mit dem Code vertraut. Kannst du mit eigenen Worten beschreiben, was der Code machen soll?
Hier findest du den Link zum Repo: https://git.qualidy.de/fakultaet73/data-science/project_1b

### Aufgabe:
Im Repository findest du ein Python Script namens stuecklistenaufloesung.py. Damit wirst du in diesem Projekt arbeiten. Codebeispiele in diesen Aufgaben sind diesem Script entnommen.
Die Funktion stuecklistenaufloesung hat einen Bug. Dein Kollege meint, der Code sieht gut aus, er versteht den Fehler auch nicht. Kannst du ihm helfen?
Die Liste "bestellungen" darf nicht verändert werden. Es darf nur die Funktion an sich bearbeitet werden.




```python 

def stuecklistenaufloesung(bestellungen):

    bedarf_A = 0
    bedarf_B = 0
    bedarf_C = 0
    bedarf_D = 0
    bedarf_E = 0
    bedarf_F = 0

    for bestellung in bestellungen:

        if bestellung.split()[2] == "Modul_A":
            bedarf_A += 5*bestellung.split()[0]
            bedarf_C += 7*bestellung.split()[0]
            bedarf_D += 200*bestellung.split()[0]
            bedarf_E += 10.7*bestellung.split()[0]


        if bestellung.split()[2] == "Modul_B":
            bedarf_A += 7*bestellung.split()[0]
            bedarf_B += 10*bestellung.split()[0]
            bedarf_E += 30.5*bestellung.split()[0]
            bedarf_F += 23.5*bestellung.split()[0]

        if bestellung.split()[2] == "Modul_C":

            bedarf_C += 34*bestellung.split()[0]
            bedarf_D += 600*bestellung.split()[0]
            bedarf_E += 90.7*bestellung.split()[0]
            bedarf_F += 3*bestellung.split()[0]


    return bedarf_A, bedarf_B, bedarf_C, bedarf_D, bedarf_E, bedarf_F 


bestellungen = [ "345 mal Modul_A", "123 mal Modul_B" , "456 mal Modul_C"]

bedarfe = stuecklistenaufloesung(bestellungen)

print(bedarfe)
```



### Aufgabe:
Was ist eine große Schwäche dieser Funktion, wenn man bedenkt, dass man sie gerne im Produktionsbetrieb verwenden möchte?
Kannst du die Funktion so umschreiben, dass ein unerfahrener Endnutzer möglichst wenig Falsch machen kann?

* `Notiz:` - Klar definierte Argumente für die jeweiligen Module. Abfrage, ob Einagbe Integer ist. Fehlermeldung als Exception auswerfen usw.

### Aufgabe:
Schreib eine Funktion, die aus der Liste der Bestellungen eine passende Liste für deine neue Funktion macht.
Führe beides hintereinander aus und lass dir eine Fehlermeldung auspucken, falls die erste Funktion nicht erfolgreich war.

### Aufgabe:
Erstelle eine Oberfläche mit dem Python-Modul "tkinter" , mit der ein Nutzer Eingabefelder hat und per Knopfdruck die Stücklistenauflösung berechnen kann.
Es sollte pro Modul ein Eingabefeld geben, in welches der Nutzer die gewünschte Anzahl eingeben kann. Es sollten nur valide Eingaben gemacht werden können. 
Entsprechende Fehlermeldungen sollen dem Nutzer helfen sich zu korrigieren. Die Darstellung soll leicht verständlich sein.
Lass dir tolle Features für die Software einfallen, zum Beispiel kannst du dir Namen für die Module und die Bedarfe einfallen lassen und diese mit Fotos aus dem 
Internet visualisieren. Zum Beispiel könnte Modul_A ein Motor sein, der aus verschiedenen Einzelteilen zusammengesetzt wird.
Du kannst die Einzelteile natürlich zu "Sets" zusammenfassen, damit die Liste der Bauteile nicht so hoch wird.





### Aufgabe
Mit folgender Funktion kannst du auf eine Datei zugreifen und den aktuellen Lagerbestand abfragen.
Beschreibe was sie macht und prüfe die Funktion, ob sie richtig arbeitet. Korrigiere ggf vorhandene Fehler.
Auch hier darfst du wieder nur die Funktion ändern und nicht die Schnittstelle (den Input)


```python 

def lagerbestand():
    # read txt
    with open("./bestand.txt") as f:
        lines = f.readlines()
    
    # extract values
    bestand_A = lines[0].split(" ")[2]
    bestand_B = lines[1].split(" ")[2]
    bestand_C = lines[2].split(" ")[2]
    bestand_D = lines[3].split(" ")[2]
    bestand_E = lines[4].split(" ")[2]
    bestand_F = lines[5].split(" ")[2]

    return bestand_A, bestand_B, bestand_C, bestand_C, bestand_E, bestand_F
```


### Aufgabe:
Stelle den aktuellen Lagerbestand in deiner App visuell dar und verwende gerne deine Bilder und Bezeichungen aus dem Aufgabenteil davor.

### Aufgabe 
Schreibe eine Funktion, mit der du die benötigten Bauteile aus der Stücklistenauflösung mit dem Lagerbestand abgleichst und ermittelts, wie viele Bauteile jeweils
nachbestellt werden müssen. Du kannst davon ausgehen, dass die Datei mit dem Lagerbestand immer in demselben Format bereitgestellt wird und es an der Stelle nicht zu Fehlern kommt.

### Aufgabe
Schreibe und Präsentiere ein Programm, das beide Funktionen in einer netten Anwendung vereint. 
Der Nutzer soll wieder seine Bestellung eingeben können und nach Betätigung eines Buttons folgende Angaben angezeigt bekommen:

- Wie viele Bauteile werden jeweils für die Bestellung benötigt?
- Wie viele Bauteile sind bereits im Lagerbestand vorhanden?
- Wie viele Bauteile müssen jeweils nachbestellt werden?

Verwende gerne eine farbliche Kodierung der Zahlen, falls der Lagerbestand nicht ausreicht. Lass deine Kreativität freien Lauf.

### Aufgabe:
Lade das Projekt wieder in git hoch.