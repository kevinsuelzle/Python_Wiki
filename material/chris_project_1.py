vins = ['6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b',
 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35',
 '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce',
 '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a',
 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d',
 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683',
 '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451',
 '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3',
 '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7',
 '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5',
 '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8',
 '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918',
 '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278',
 '8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61',
 'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb',
 'b17ef6d19c7a5b1ee83b907c595526dcb1eb06db8227d650d5dda0a9f4ce8cd9',
 '4523540f1504cd17100c4835e85b7eefd49911580f8efff0599a8f283be6b9e3',
 '4ec9599fc203d176a301536c2e091a19bc852759b255bd6818810a42c5fed14a',
 '9400f1b21cb527d7fa3d3eabba93557a18ebe7a2ca4e471cfe5e4c5b4ca7f767',
 'f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b',
 '6f4b6612125fb3a0daecd2799dfd6c9c299424fd920f9b308110a2c1fbd8f443',
 '785f3ec7eb32f30b90cd0fcf3657d388b5ff4297f2f9716ff66e9b69c05ddd09',
 '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790',
 'c2356069e9d1e79ca924378153cfbbfb4d4416b1f99d41a2940bfdb66c5319db',
 'b7a56873cd771f2c446d369b649430b65a756ba278ff97ec81bb6f55b2e73569',
 '5f9c4ab08cac7457e9111a30e4664920607ea2c115a1433d7be98e97e64244ca',
 '670671cd97404156226e507973f2ab8330d3022ca96e0c93bdbdb320c41adcaf',
 '59e19706d51d39f66711c2653cd7eb1291c94d9b55eb14bda74ce4dc636d015a',
 '35135aaa6cc23891b40cb3f378c53a17a1127210ce60e125ccf03efcfdaec458']

vehicle_models = ['Golf',
 'Tiguan',
 'Tiguan',
 'Golf',
 'Golf',
 'Tiguan',
 'Tiguan',
 'Golf',
 'Passat',
 'ID.4',
 'Golf',
 'Arteon',
 'Arteon',
 'Arteon',
 'Passat',
 'Tiguan',
 'Tiguan',
 'Golf',
 'Passat',
 'Tiguan',
 'Golf',
 'Tiguan',
 'Arteon',
 'Arteon',
 'Passat',
 'Golf',
 'Golf',
 'Passat',
 'Golf']

registration_dates = [datetime.date(2019, 7, 12),
 datetime.date(2017, 9, 23),
 datetime.date(2014, 3, 26),
 datetime.date(2018, 9, 25),
 datetime.date(2015, 2, 28),
 datetime.date(2014, 9, 13),
 datetime.date(2017, 12, 29),
 datetime.date(2021, 5, 2),
 datetime.date(2021, 2, 11),
 datetime.date(2018, 5, 13),
 datetime.date(2017, 5, 2),
 datetime.date(2014, 6, 10),
 datetime.date(2019, 7, 31),
 datetime.date(2019, 1, 7),
 datetime.date(2022, 8, 3),
 datetime.date(2014, 12, 21),
 datetime.date(2017, 7, 18),
 datetime.date(2021, 3, 27),
 datetime.date(2014, 10, 23),
 datetime.date(2021, 1, 10),
 datetime.date(2023, 6, 15),
 datetime.date(2016, 3, 7),
 datetime.date(2023, 9, 6),
 datetime.date(2018, 1, 15),
 datetime.date(2019, 8, 18),
 datetime.date(2022, 5, 21),
 datetime.date(2016, 5, 8),
 datetime.date(2015, 5, 30),
 datetime.date(2019, 4, 10)]

service_contract_durtions = [2,
 4,
 1,
 1,
 2,
 3,
 1,
 4,
 2,
 5,
 5,
 5,
 3,
 1,
 5,
 3,
 5,
 3,
 5,
 2,
 1,
 3,
 1,
 2,
 2,
 1,
 2,
 2,
 5]

Service_Pauschale = "30 Euro"

### Aufgabe:
# Berechne eine Liste, die angibt, wie viele Tage das jeweilige Fahrzeug nicht mehr in der Werkstatt war.


### Aufgabe:
# Wie lang ist die maximale Anzahl an Tagen, an denen ein Fahrzeug nicht in der Werkstatt war?
# Um welches Fahrzeug handelt es sich?


### Aufgabe: 
# Folgende Funktion produziert Fehler. Woran liegt es? 
# Kannst du den Bug fixen indem du eine neue Funktion schreibst, die das Problem ein für alle Mal löst?

### Aufgabe:
#Berechne die Servicekosten, welche sich aus der Servicegebühr und der Servicepauschale zusammensetzt. 
#Beachte dabei jedoch, dass diese nur anfällt, falls das Fahrzeug im aktuellen Betriebsjahr noch nicht in der Werkstatt war. Sonst soll der Wert mit "0 Euro" angegeben werden.


### Aufgabe: 
#gefahrene Kilometer, Schreibweise sowohl mit Komma als auch mit Punkt. Dadurch kein float mehr und Rechnung geht kaputt.
#Funktion testst, ob gefahrene Kilometer 50.000 übersteigen.
# -> Bremsbeläge


### Aufgabe:
# Prüfe das Format aller Telefonnummern (sie sollen mit +49 anfangen und die Führende 0 soll weggelassen werden.
# Schreibe eine funktion, die das Prüft bzw in den Standard überführt.


### Aufgabe:
#Prüfe, ob jedes Fahrzeug einem Servicepartner zugeordnet ist, damit dieser den Fahrzeughalten kontaktieren kann.
# Falls nein, dann erstelle eine .txt Datei in der die Liste aller nicht-zugeordneten VINs inklusive der gegebenen Informationen, damit die Qualitätssicherung das Problem angehen kann.


### Aufgabe:
# Stelle die VIN mit der längsten Werkstattabwesenheit exemplarisch in einem Steckbrief dar. Verwende hierzu ein Foto des Fahrzeugmodells aus dem Internet und stelle mit einer Text-Bild-Kombination eine schöne Darstellung für deine Präsentation zusammen.
# Leite eine Handlungsempfehlung für das Qualitätsmanagement dafür ab. Kann man hier den Service oder das System etwas verbessern?


### Aufgabe:
# Du wirst sicherlich schon bemerkt haben, dass die einzelen Listen sehr unpraktisch oder unbequem sind. Es wäre doch toll, alle Information in einem Objekt zu haben. Später wirst du lernen wie das geht.
# Heute solst du noch für die Fachabteilung eine Datei erstellen, in der die Informationen geordnet zusammengestellt sind. Verwende hierzu bitte ein JSON/DICTIONARY/... und gebe die Ergebnisse in einer .txt Datei aus.


### Aufgabe:
# Aus den gefahrenen Kilometern kannst du die Gesamtkilometerleistung der Flotte bestimmen. Mal angenommen die Flotte gehört zu einem Unternehmen, welches seinen Mitarbeitern die Fahrzeuge zur Verfügung gestellt hat. 
# Der Kunde überlegt seinen Mitarbeitern freies Tanken mit diesen Fahrzeugen zu als Benefit zu schenken. Stell eine plausible Rechnung auf, mit der du die ungefähren Jahreskosten für die Flotte ausrechnest und dem Kunden präsentierst.
# Was kostet es pro Mitarbeiter und Jahr in etwa? Würdest du dem Unternehmen diese Maßnahme empfehlen?


### Aufgabe:
# Lade deinen Code ins GIT Repository.