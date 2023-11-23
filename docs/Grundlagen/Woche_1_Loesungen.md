
------


# Lösungen

## Variablen und Datentypen
1. `a = 5`
2. `begrüßung = "Hallo Python"`
3. `a = 10`
4. `name = "Dein Name"; alter = Dein Alter`
5. `anzahl_aepfel = 5`
6. 
```python 
vorname = "Max"
nachname = "Mustermann"
voller_name = vorname + " " + nachname
print(voller_name)
```
7. 
```python
meine_variable = 15.5
print(type(meine_variable))
```
8. `ist_schüler = True`
9.`farben = ["Rot", "Grün", "Blau"]`
10`print(farben[1])`
11`koordinaten = (4, 5)`
12`print(koordinaten[0])`
13.
```python
zahl_string = "10"
zahl_int = int(zahl_string)
print(zahl_int)
```
14. `farben.append("Gelb")`

## Input & Output
1. `print("Hallo Welt")`
2. `text = "Python"; print(text)`
3. `print(100)`
4. `print("Hallo", "Welt")`
5. `print("Hallo!", end="")`
6. `name = input("Wie heißt du? ")`
7. 
```python
name = input("Wie heißt du? ")
print(f"Hallo, {name}!")
```
8. 
```python
alter = int(input("Wie alt bist du? "))
print(alter)
```
9. 
```python
`essen = input("Was ist dein Lieblingsessen? ")
print(f"Ich mag auch {essen}!")
```
10. 
```python
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
print(f"Name: {name}, Alter: {alter}")
```
11. 
```python
vorname = input("Vorname: ")
nachname = input("Nachname: ")
print(f"Vollständiger Name: {vorname} {nachname}")
```
12. 
```python
zahl1 = int(input("Erste Zahl: "))
zahl2 = int(input("Zweite Zahl: "))
print(f"Ergebnis: {zahl1 + zahl2}")
```
13. 
```python
try: 
    zahl = int(input("Gib eine Zahl ein: "))
    print(zahl) 
except ValueError: 
    print("Das war keine gültige Zahl!")
```
14. 
```python
farben = [input("Erste Farbe: "), input("Zweite Farbe: "), input("Dritte Farbe: ")]
print(farben)
```
15. 
```python 
passwort1 = input("Passwort: ")
passwort2 = input("Passwort wiederholen: ")
if passwort1 == passwort2:
    print("Erfolg")
else:
    print("Die Passwörter stimmen nicht überein!")
```
## Mathematische Operationen
1. `print(5 + 3)  # 8`
2. `print(10 - 2)  # 8`
3. `print(4 * 2)  # 8`
4. `print(16 / 2)  # 8.0`
5. `print(17 // 2)  # 8`
6. `print(18 % 10)  # 8`
7. `print(2 ** 3)  # 8`
8. `import math; print(math.sqrt(64))  # 8.0`
9. `import math; print(math.exp(3))  # etwa 20.085`
10. `import math; print(math.log(8, math.e))  # etwa 2.079`

11. `print((3 + 4) * 5)  # 35`
12. `print(2 * 3 == 6)  # True`
13. `print(round(2.7))  # 3`
14. `print(-3 * 3)  # -9`
15. `x = 5; print(x * x)  # 25`
16. `print(2 + 3 * 5)  # 17, da die Multiplikation zuerst ausgeführt wird`
17. `print((2 + 3) * 5)  # 25, da die Klammer zuerst ausgewertet wird`
18. `print(4 ** 2 / 8)  # 2.0, da zuerst potenziert und dann dividiert wird`
19. `print(3 + 4 * 2 - 1)  # 10, da Multiplikation vor Addition und Subtraktion ausgeführt wird`
20. `print((3 + 4) * (5 - 2) ** 2)  # 49, da zuerst die Klammern, dann die Potenzierung und zuletzt die Multiplikation ausgeführt wird`

## Debugger

Die Lösungen beziehen sich auf die Aktionen, die ausgeführt werden sollen, um mit dem Debugger zu interagieren:

1. Füge `pdb.set_trace()` vor `return a + b` ein. Starte das Programm und verwende den Befehl `p a` und `p b`, 
um die Werte zu überprüfen.
2. Starte das Programm und verwende `n`, um jede Zeile auszuführen. Beobachte, wie die Variable `ergebnis` berechnet 
wird.
3. Starte das Programm und benutze `s`, um in die Funktion `berechne_differenz` einzutreten. Verwende `p x` und `p y`, 
um die Werte zu überprüfen.
4. Starte das Programm und verwende `p ergebnis`, um den Wert der Variable `ergebnis` auszugeben, dann `c`, um das 
Programm zu beenden.
5. Starte das Programm im Debug-Modus mit `python -m pdb script.py`. Setze einen Haltepunkt mit `b multipliziere` und 
überprüfe `x` und `y` mit `p x` und `p y`, bevor du `c` ausführst.


## Verzweigungen
1. 
```python
if x > 10: 
    print("x ist größer als 10.")
```
2. 
```python
if zahl % 2 == 0: 
    print("Die Zahl ist gerade.") 
else:   
    print("Die Zahl ist ungerade.")
```
3. 
```python
if zahl > 0: 
    print("Positiv") 
elif zahl < 0: 
    print("Negativ") 
else: 
    print("Null")
```
4. 
```python
if a > b: 
    print("a ist größer als b") 
elif a < b: 
    print("a ist kleiner als b") 
else: 
    print("a ist gleich b")
```
5. 
```python
if alter >= 18: 
    print("Volljährig") 
else: 
    print("Minderjährig")
```
6. 
```python
if eingegebenes_passwort == gespeichertes_passwort: 
    print("Passwort korrekt!") 
else: 
    print("Falsches Passwort!")
```
7. 
```python
if zahl1 > zahl2: 
    print(zahl1) 
else: 
print(zahl2)
```
8. 
```python
if note >= 1.0 and note < 1.5: 
    print("sehr gut") 
elif note < 2.5: 
    print("gut") 
elif note < 3.5: 
    print("befriedigend") 
elif note < 4.0: 
    print("ausreichend") 
else: 
    print("nicht ausreichend")
```
9. 
```python
if temperatur < 10: 
    print("Kalt") 
elif temperatur < 25:
    print("Warm") 
else: 
    print("Heiß")
```
10. 
```python
if operation == '+': 
    print(a + b) 
elif operation == '-': 
    print(a - b) 
elif operation == '*': 
    print(a * b) 
elif operation == '/':
    print(a / b)
```

11. 
```python
if monat in [3, 4, 5]: 
    print("Frühling") 
elif monat in [6, 7, 8]: 
    print("Sommer") 
elif monat in [9, 10, 11]: 
    print("Herbst") 
else: 
    print("Winter")
```
12. 
```python
if zahl1 % zahl2 == 0: 
    print("Teilbar") 
else: 
    print("Nicht teilbar")
```
13. 
```python
if artikel in einkaufsliste: 
    print("Artikel vorhanden") 
else: 
    print("Artikel nicht vorhanden")
```
14. 
```python
if a > b and a > c: 
    print(a) 
elif b > a and b > c: 
    print(b) 
else: 
    print(c)
```
15. 
```python
if einkaufswert >= 100: 
    print("Rabatt: 20%") 
elif einkaufswert >= 50: 
    print("Rabatt: 10%") 
else: 
    print("Kein Rabatt")
```
16. 
```python
if lichtstatus: 
    print("Licht an") 
else: 
    print("Licht aus")
```
17. 
```python
if gewicht < 1000: 
    print("Leicht") 
elif gewicht < 3000: 
    print("Mittel") 
else: 
    print("Schwer")
```
18. 
```python
if wochentag == "Montag": 
    print("Preis: 5 Euro") 
else: 
    print("Preis: 10 Euro")
```

20. 
```python
if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0): 
    print("Schaltjahr")
else: 
    print("Kein Schaltjahr")
```

## Komplex-Aufgaben
### **Persönliche Statistik**

```python
# Eingabe der persönlichen Informationen
name = input("Gib deinen Namen ein: ")
alter = int(input("Gib dein Alter ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))
lieblingsfarben = input("Gib deine Lieblingsfarben ein, getrennt durch Kommas: ").split(',')

# Berechnung der Anzahl der Lieblingsfarben
anzahl_farben = len(lieblingsfarben)

# Ausgabe der Informationen
print("\n--- Persönliche Statistiken ---")
print(f"Name: {name}")
print(f"Alter: {alter} Jahre")
print(f"Größe: {groesse} Meter")
print(f"Anzahl der Lieblingsfarben: {anzahl_farben}")
print(f"Lieblingsfarben: {', '.join(lieblingsfarben)}")
```

### **Zinsrechner**
```python
# Benutzereingaben
anfangskapital = float(input("Gib das Anfangskapital ein: "))
zinssatz = float(input("Gib den Zinssatz in Prozent ein: "))
jahre = float(input("Gib die Anlagedauer in Jahren ein: "))

# Berechnung der Endsumme
endsumme = anfangskapital * (1 + zinssatz/100 * jahre)

# Ausgabe
print(f"Die Endsumme nach {jahre} Jahren beträgt: {endsumme:.2f} Euro")

```

### **Umrechner für Temperaturen**

```python
# Benutzereingaben
temperatur = float(input("Gib die Temperatur ein: "))
einheit = input("Ist die Temperatur in Celsius (C) oder Fahrenheit (F)? ")

# Umrechnung
if einheit.lower() == 'c':
    umgerechnet = temperatur * 9/5 + 32
    zieleinheit = "Fahrenheit"
elif einheit.lower() == 'f':
    umgerechnet = (temperatur - 32) * 5/9
    zieleinheit = "Celsius"

# Ausgabe
print(f"Die Temperatur in {zieleinheit} beträgt: {umgerechnet:.2f}°")

```