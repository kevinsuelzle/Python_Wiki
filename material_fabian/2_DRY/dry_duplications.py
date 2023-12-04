def verarbeite_daten(daten_liste, datentyp):
    # Verarbeite Daten (allgemeine Logik)
    verarbeitete_daten = []
    for daten in daten_liste:
        # Gemeinsame Logik für alle Datentypen
        verarbeitete_daten.append({
            "name": daten["name"],
            "email": daten["email"],
            # Weitere spezifische Logik für den gegebenen Datentyp
            "datentyp": datentyp,
        })
    return verarbeitete_daten

# Beispielaufrufe
kunden = [{"name": "Kunde1", "email": "kunde1@example.com"}]
mitarbeiter = [{"name": "Mitarbeiter1", "email": "mitarbeiter1@example.com"}]

verarbeitete_kunden = verarbeite_daten(kunden, "Kunde")
verarbeitete_mitarbeiter = verarbeite_daten(mitarbeiter, "Mitarbeiter")

print(verarbeitete_kunden)
print(verarbeitete_mitarbeiter)
