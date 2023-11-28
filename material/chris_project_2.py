# Stücklistenauflösung


def stuecklistenaufloesung(bestellungen):

    bedarf_A = 0
    bedarf_B = 0
    bedarf_C = 0
    bedarf_D = 0
    bedarf_E = 0
    bedarf_F = 0

    for bestellung in bestellungen:

        if bestellung.split()[2] == "Modul_A":
            bedarf_A += 5*int(bestellung.split()[0])
            bedarf_C += 7*int(bestellung.split()[0])
            bedarf_D += 200*int(bestellung.split()[0])
            bedarf_E += 10.7*int(bestellung.split()[0])


        if bestellung.split()[2] == "Modul_B":
            bedarf_A += 7*int(bestellung.split()[0])
            bedarf_B += 10*int(bestellung.split()[0])
            bedarf_E += 30.5*int(bestellung.split()[0])
            bedarf_F += 23.5*int(bestellung.split()[0])

        if bestellung.split()[2] == "Modul_C":

            bedarf_C += 34*int(bestellung.split()[0])
            bedarf_D += 600*int(bestellung.split()[0])
            bedarf_E += 90.7*int(bestellung.split()[0])
            bedarf_F += 3*int(bestellung.split()[0])


    return bedarf_A, bedarf_B, bedarf_C, bedarf_D, bedarf_E, bedarf_F 


bestellungen = [ "30 mal Modul_A", "50 mal Modul_B" , "70 mal Modul_C"]

bedarfe = stuecklistenaufloesung(bestellungen)

print(bedarfe)


### Aufgabe:
# Clone das repository und mache dich mit dem Code vertraut. Kannst du mit eigenen Worten beschreiben, was der Code machen soll?

### Aufgabe:
# Die Funktion stuecklistenaufloesung hat einen bug. Dein Kollege meint, der Code sieht gut aus, er versteht den Fehler auch nicht. Kannst du ihm helfen?
# Notiz: aus int(bestellung.split()[0]) nur bestellung.split()[0] machen, da strings als Eingabe gegeben werden, und man dran denken soll, sie umzuformatieren.
# Notiz: Weitere Bugs einbauen... 
# Notiz: Die Anzahlen/Faktoren aus einer Datei herauslesen. Sinn erklären und einen Bug einbauen.

### Aufgabe:
# Was ist eine große Schwäche dieser Funktion, wenn man bedenkt, dass man sie gerne im Produktionsbetrieb verwenden möchte?
# Kannst du die Funktion so umschreiben, dass ein unerfahrener Endnutzer möglichst wenig Falsch machen kann?
# Notiz: Klar definierte Argumente für die jeweiligen Module. Abfrage, ob Einagbe Integer ist. Fehlermeldung als Exception auswerfen usw.

### Aufgabe:
# Schreib eine Funktion, die aus der Liste der Bestellungen eine passende Liste für deine Funktion macht.
# Führe beides hintereinander aus und lass dir eine Fehlermeldung auspucken, falls die erste Funktion nicht erfolgreich war.

### Aufgabe:
# Erstelle eine Oberfläche, mit der ein Nutzer Eingabefelder hat und per Knopfdruck die Stücklistenauflösung berechnen kann.
# Es sollte pro Modul ein Eingabefeld geben, in welches der Nutzer die gewünschte Anzahl eingeben kann. Es sollten nur valide Eingaben gemacht werden können. 
# Entsprechende Fehlermeldungen sollen dem Nutzer helfen sich zu korrigieren. Die Darstellung soll leicht verständlich sein.
# LAss dir tolle Features für die Software einfallen, zum Beispiel kannst du dir Namen für die Module und die Bedarfe einfallen lassen und diese mit Fotos aus dem 
# Internet visualisieren. Zum Beispiel könnte Modul_A ja ein Motor sein, der aus verschiedenen Einzelteilen zusammengesetzt wird.
# Du kannst die Einzelteile natürlich zu "Sets" zusammenfassen, damit die Anzahl nicht so hoch wird.

### Aufgabe:
# Lade das Projekt wieder in git hoch.



### Weiter gehts: Lagerbestand abfragen:

# Mit folgender Funktion kannst du auf eine Datei zugreifen und den aktuellen Lagerbestand abfragen.

def lagerbestand():
    # read csv
    # transform to lists
    
    bestand_A = 5 
    bestand_B = 3 
    bestand_C = 7 
    bestand_D = 1 
    bestand_E = 200 
    bestand_F = 7000

    return bestand_A, bestand_B, bestand_C, bestand_D, bestand_E, bestand_F




### Aufgabe
# Beschreibe was sie macht und prüfe die Funktion, ob sie richtig arbeitet. Korrigiere ggf vorhandene Fehler.

### Aufgabe:
# Stelle den aktuellen Lagerbestand visuell dar und verwende gerne deine Bilder und Bezeichungen aus dem Aufgabenteil davor.

### Aufgabe 
# Schreibe eine Funktion, mit der du die benötigten Bauteile aus der Stücklistenauflösung mit dem Lagerbestand abgleichst und ermittelts, wie viele Bauteile jeweils
# nachbestellt werden müssen. Du kannst davon ausgehen, dass die Datei mit dem Lagerbestand immer in demselben Format bereitgestellt wird.

### Aufgabe
# Schreibe und Präsentiere ein Programm, das beide Funktionen in einer netten Anwendung vereint. 
# Der Nutzer soll wieder seine Bestellung eingeben können und nach Betätigung eines Buttons folgende Angaben angezeigt bekommen:
# Wie viele Bauteile werden jeweils für die Bestellung benötigt?
# Wie viele Bauteile sind bereits im Lagerbestand vorhanden?
# Wie viele Bauteile müssen jeweils nachbestellt werden?
# Verwende gerne eine Farbliche Kodierung der Zahlen, falls der Lagerbestand nicht ausreicht.


