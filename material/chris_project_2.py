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
