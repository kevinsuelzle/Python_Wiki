# Lösungen

### Tupel erstellen
```python
fruechte = ("Apfel", "Banane", "Kirsche", "Orange", "Mango")
```
### 2. Auf Tupelelemente zugreifen
```python 
print(fruechte[1]) # Gibt 'Banane' aus
```
### 3.Tupelelemente ändern
Dies ist nicht möglich, da Tupel unveränderlich sind.
### 4. Ist das Element im Tupel?
```python
print("Apfel" in fruechte) # Gibt True aus, falls Apfel enthalten ist
```
### 5. Zählen
```python
print(fruechte.count("Banane")) # Gibt die Anzahl der 'Banane' aus
```
### 6. Umgekehrte Reihenfolge
```python
umgekehrtes_tupel = fruechte[::-1]
```
### 7. Tupel vom Tupel
```python
erste_drei = fruechte[:3]
```
### 8. Tupel kombinieren
```python
gemuese = ("Karotte", "Brokkoli", "Zwiebel")
kombiniert = fruechte + gemuese
```
### 9. Multiplikation
```python 
dreifach = fruechte * 3
```
### 10. Tupel verschachteln
```python
verschachtelt = (fruechte, gemuese)
```
### 11. Index zum Element finden
```python
print(fruechte.index("Kirsche")) # Gibt den Index von 'Kirsche' aus
```
### 12. Summe der Tupelelemente
```python
zahlen = (1, 2, 3, 4, 5)
print(sum(zahlen)) # Gibt die Summe aus, also 15
```
### 13. Sortieren
```python
sortierte_zahlen = tuple(sorted(zahlen, reverse=True))
```
### 14. Subtupel
```python
print(fruechte in verschachtelt) # Gibt True aus, falls fruechte ein Subtupel ist
```
### 15. Reingelegt
Dies druckt jedes String-Element im Tupel in Großbuchstaben aus.

### Komplex-Aufgabe: Einkaufslistenmanager

**Lösung:**

```python
einkaufsliste = []

while True:
    aktion = input("Wähle eine Aktion: Hinzufügen (h), Entfernen (e), Anzeigen (a), Beenden (b): ")

    if aktion == "h":
        produkt = input("Gib den Produktnamen ein: ")
        menge = input("Gib die Menge ein: ")
        einkaufsliste.append((produkt, menge))
    elif aktion == "e":
        produkt = input("Gib den Namen des zu entfernenden Produkts ein: ")
        einkaufsliste = [item for item in einkaufsliste if item[0] != produkt]
    elif aktion == "a":
        for produkt, menge in einkaufsliste:
            print(f"{produkt}: {menge}")
    elif aktion == "b":
        break
    else:
        print("Ungültige Eingabe.")
```

