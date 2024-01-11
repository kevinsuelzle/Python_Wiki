
# Lösungen

## for-Schleifen

Natürlich, hier sind die Lösungen zu den Übungsaufgaben zu `for`-Schleifen:

### 1. Zählen
```python
for zahl in range(1, 11):
   print(zahl)
```

### 2. Städtetrip
```python
staedte = ["Berlin", "Paris", "London", "New York"]
for stadt in staedte:
   print(stadt)
```

### 3. Summierung
```python
summe = 0
for zahl in range(1, 101):
   summe += zahl
print(summe)
```

### 4. Längster Name
```python
namen = ["Anna", "Max", "Benjamin", "Alexandra"]
laengster_name = ""
for name in namen:
   if len(name) > len(laengster_name):
       laengster_name = name
print("Längster Name:", laengster_name)
```

### 5. Quadratzahlen
```python
for zahl in range(1, 11):
   quadrat = zahl ** 2
   print(quadrat)
```

### 6. Suchen einer Frucht
```python
fruechte = ["Apfel", "Banane", "Kirsche", "Erdbeere"]
gesuchte_frucht = "Banane"
for frucht in fruechte:
   if frucht == gesuchte_frucht:
       print(f"{gesuchte_frucht} wurde gefunden!")
       break
else:
   print(f"{gesuchte_frucht} wurde nicht gefunden.")
```

### 7. Verdreht
```python
wort = "Python"
for buchstabe in reversed(wort):
   print(buchstabe)
```


### 8. Fakultät
```python
n = 5
faktor = 1
for zahl in range(1, n + 1):
    faktor *= zahl
print(f"Fakultät von {n} ist {faktor}")
```

### 9. Thermometer für Amerikaner 
```python
temperaturen_celsius = [0, 10, 25, 32, 100]
for celsius in temperaturen_celsius:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C entspricht {fahrenheit}°F")
```

### 10. Vokale
```python
wort = "Python"
anzahl_vokale = 0
for buchstabe in wort:
    if buchstabe.lower() in "aeiou":
        anzahl_vokale += 1
print(f"Anzahl der Vokale im Wort '{wort}': {anzahl_vokale}")
```

### 11. Häufigkeit
```python
text = "Python ist eine Programmiersprache, und Python ist großartig."
gesuchtes_wort = "Python"
anzahl = 0
woerter = text.split()
for wort in woerter:
    if wort == gesuchtes_wort:
        anzahl += 1
print(f"Anzahl von '{gesuchtes_wort}' im Text: {anzahl}")
```

## while-Schleifen

### 1. Zählen

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### 2. Gerade Zahlen

```python
i = 2
while i <= 20:
    print(i)
    i += 2
```

### 3. Liste von hinten ausgeben

```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

### 4. Die ersten Fünf

```python
meine_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < 5:
    print(meine_liste[i])
    i += 1
```

### 5. Summe von 1 bis 100

```python
summe = 0
i = 1
while i <= 100:
    summe += i
    i += 1
print(summe)
```

### 6. Fast endlose Schleife

```python
import random

zahl = 0
while zahl != 5:
    zahl = random.randint(1, 10)
    print(zahl)
```

### 7. Fakultät

```python
n = 5  # Beispielzahl
fakultaet = 1
i = 1
while i <= n:
    fakultaet *= i
    i += 1
print(fakultaet)
```

### 8. Wiederholung nach Länge

```python
text = "Hallo"
i = 0
while i < len(text):
    print(text)
    i += 1
```

### 9. Fibonacci

```python
a, b = 0, 1
i = 0
while i < 10:
    print(a)
    a, b = b, a + b
    i += 1
```

### 10. Stopp-Bedingung

```python
liste = ["Hallo", "Welt", "Stopp", "Python"]
i = 0
while i < len(liste):
    if liste[i] == "Stopp":
        break
    print(liste[i])
    i += 1
```

## Komplex-Aufgaben

### Lösung zu Aufgabe 1: Benutzerdefinierte Passwortüberprüfung

```python
password = input("Bitte gib ein Passwort ein: ")

if len(password) < 8:
    print("Das Passwort muss mindestens 8 Zeichen lang sein.")
elif not any(char.isdigit() for char in password):
    print("Das Passwort muss mindestens eine Zahl enthalten.")
elif not any(char.isalpha() for char in password):
    print("Das Passwort muss mindestens einen Buchstaben enthalten.")
else:
    print("Das Passwort ist gültig.")
```

### Lösung zu Aufgabe 2: Textbasierter Quiz

```python
fragen = ["Hauptstadt von Deutschland?", "2+2=?", "Name des aktuellen US-Präsidenten?", "7 * 8=?",
          "Farbe des Himmels bei klarem Wetter?"]
antworten = ["Berlin", "4", "Biden", "56", "Blau"]
punkte = 0

for i in range(len(fragen)):
    antwort = input(fragen[i] + " ")
    if antwort.lower() == antworten[i].lower():
        punkte += 1

print(f"Du hast {punkte} von 5 Punkten erreicht.")

if punkte <= 2:
    print("Anfänger")
elif punkte <= 4:
    print("Fortgeschritten")
else:
    print("Experte")
```

### Lösung zu Aufgabe 3: Einfacher Zahlenraten

```python
import random

zahl = random.randint(1, 100)
versuche = 0
max_versuche = 10

while versuche < max_versuche:
    raten = int(input("Rate die Zahl: "))
    versuche += 1

    if raten == zahl:
        print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
        break
    elif raten < zahl:
        print("Die Zahl ist höher.")
    else:
        print("Die Zahl ist niedriger.")

if raten != zahl:
    print(f"Leider falsch. Die gesuchte Zahl war {zahl}.")
```

### Lösung zu Aufgabe 4: Bestellung in einem virtuellen Café

```python
menu = {"Kaffee": 2.50, "Tee": 2.00, "Kuchen": 3.00}
bestellung = []
summe = 0

print("Menü:")
for artikel, preis in menu.items():
    print(f"{artikel}: {preis} Euro")

while True:
    artikel = input("Wähle einen Artikel (oder 'fertig' zum Abschließen): ")
    if artikel.lower() == "fertig":
        break
    elif artikel in menu:
        menge = int(input(f"Wie viele von {artikel} möchtest du? "))
        summe += menu[artikel] * menge
    else:
        print("Artikel nicht im Menü.")

print(f"Gesamtsumme: {summe} Euro")
zahlung = input("Zahlst du bar oder mit Karte? ")
print(f"Bezahlt mit {zahlung}. Vielen Dank für deine Bestellung!")
```
