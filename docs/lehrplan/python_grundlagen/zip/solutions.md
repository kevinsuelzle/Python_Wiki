# Lösungen

### 1: Einführung in `zip` 

```python
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
ergebnis = list(zip(liste1, liste2))
print(ergebnis)
```

### 2: Liste der Tupel 

```python
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
tupel_liste = list(zip(liste1, liste2))
print(tupel_liste)
```

### 3: Elementweise Addition 

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
ergebnis = [x + y for x, y in zip(liste1, liste2)]
print(ergebnis)
```

### 4: Parallele Zuweisung 

```python
namen = ['Alice', 'Bob', 'Charlie']
alter = [25, 30, 35]
for name, age in zip(namen, alter):
    print(f"{name} ist {age} Jahre alt.")
```

### 5: Elemente filtern 

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
ergebnis = [x for x, y in zip(liste1, liste2) if x % 2 == 0]
print(ergebnis)
```

### 6: Dictionary erstellen 

```python
schlüssel = ['A', 'B', 'C']
werte = [1, 2, 3]
ergebnis = dict(zip(schlüssel, werte))
print(ergebnis)
```

### 7: Sortierte Paare 

```python
liste1 = [5, 2, 8]
liste2 = [7, 1, 6]
paare = list(zip(liste1, liste2))
sortierte_paare = sorted(paare, key=lambda x: x[0] + x[1])
print(sortierte_paare)
```

### 8: Zusammenführen von Wörtern 

```python
adjektive = ['rot', 'schnell']
nomen = ['Auto', 'Hund']
kombinationen = [adj + ' ' + nom for adj, nom in zip(adjektive, nomen)]
print(kombinationen)
```

### 9: Elemente multiplizieren 

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
ergebnis = [x * y for x, y in zip(liste1, liste2)]
print(ergebnis)
```

### 10: Elemente vergleichen 

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 2, 1, 4, 5]
unterschiede = [(x, y) for x, y in zip(liste1, liste2) if x != y]
print(unterschiede)
```

### 11: Maximaler Wert pro Position 

```python
liste1 = [5, 2, 8]
liste2 = [7, 1, 6]
max_werte = [max(x, y) for x, y in zip(liste1, liste2)]
print(max_werte)
```

### 12: Mittelwert berechnen 

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
mittelwerte = [(x + y) / 2 for x, y in zip(liste1, liste2)]
print(mittelwerte)
```

### 13: Elemente gruppieren 

```python
tupel_liste = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
gruppiert = {}
for key, value in tupel_liste:
    if key in gruppiert:
        gruppiert[key].append(value)
    else:
        gruppiert[key] = [value]
print(gruppiert)
```

### 14: Teile und erobere 

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gerade_zahlen = []
ungerade_zahlen = []
for zahl in zahlen:
    if zahl % 2 == 0:
        gerade_zahlen.append(zahl)
    else:
        ungerade_zahlen.append(zahl)
print("Gerade Zahlen:", gerade_zahlen)
print("Ungerade Zahlen:", ungerade_zahlen)
```

### 15: Prüfung von Bedingungen 

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 2, 1, 4, 5]
bedingung_erfüllt = [x == y for x, y in zip(liste1, liste2)]
print(bedingung_erfüllt)
```

### 16: Entfernen von Duplikaten 

```python
liste = [1, 2, 2, 3, 4, 4, 5]
ohne_duplikate = list(set(zip(liste)))
print(ohne_duplikate)
```

### 17: Anzahl der Übereinstimmungen zählen 

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 2, 1, 4, 5]
anzahl_übereinstimmungen = sum(1 for x, y in zip(liste1, liste2) if x == y)
print(anzahl_übereinstimmungen)
```

### 18: Slices erstellen 

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slices = []
for i, j in zip(range(0, len(zahlen), 2), range(1, len(zahlen), 2)):
    slices.append(zahlen[i:j + 1])
print(slices)
```

### 19: Elemente tauschen 

```python
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
liste1, liste2 = list(zip(liste2, liste1))
print(liste1)
print(liste2)
```

### 20: Verschlüsselung mit `zip` 

```python
def verschlüsseln(text):
    verschlüsselt = ''.join(chr(ord(char) + 1) for char in text)
    return verschlüsselt


def entschlüsseln(verschlüsselt_text):
    entschlüsselt = ''.join(chr(ord(char) - 1) for char in verschlüsselt_text)
    return entschlüsselt


text = "Hallo, Welt!"
verschlüsselter_text = verschlüsseln(text)
print("Verschlüsselt:", verschlüsselter_text)
entschlüsselter_text = entschlüsseln(verschlüsselter_text)
print("Entschlüsselt:", entschlüsselter_text)
```

# Lösungen Komplex Aufgaben


### Lösung 1: Datenanalyse mit `zip` und Bedingungen 

```python
temperaturen = [25, 30, 20, 35]
städte = ["Berlin", "München", "Hamburg", "Frankfurt"]

max_temperatur = max(temperaturen)
min_temperatur = min(temperaturen)

heißeste_stadt = [stadt for temperatur, stadt in zip(temperaturen, städte) if temperatur == max_temperatur]
kälteste_stadt = [stadt for temperatur, stadt in zip(temperaturen, städte) if temperatur == min_temperatur]

print(f"Die heißeste Stadt ist {', '.join(heißeste_stadt)} bei {max_temperatur}°C.")
print(f"Die kälteste Stadt ist {', '.join(kälteste_stadt)} bei {min_temperatur}°C.")
```

### Lösung 2: Wörter zählen mit `zip` und Dictionaries

```python
def wort_zählen(text):
    wörter = text.split()
    wort_dict = {}

    for wort in wörter:
        wort = wort.strip(".,!?")
        wort_dict[wort] = wort_dict.get(wort, 0) + 1

    return wort_dict


text = "Das ist ein Beispiel. Ein einfaches Beispiel."
ergebnis = wort_zählen(text)
print(ergebnis)
```

### Lösung 3: Multi-dimensionale Datenanalyse

```python
schüler = [
    {"name": "Max", "noten": [80, 90, 75]},
    {"name": "Anna", "noten": [95, 85, 70]},
    {"name": "Erik", "noten": [75, 80, 60]}
]

schwellenwert = 80


def durchschnitt_berechnen(noten):
    return sum(noten) / len(noten)


schüler_unter_schwellenwert = [schüler["name"] for schüler in schüler if
                               durchschnitt_berechnen(schüler["noten"]) < schwellenwert]

print(f"Schüler mit Durchschnittsnote unter {schwellenwert}: {', '.join(schüler_unter_schwellenwert)}")
```
