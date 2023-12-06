# Lösungen

## Funktionen definieren

### 1. **Einfache Begrüßungsfunktion**
```python
def begruesse():
   print("Hallo Welt!")
begruesse()
```

### 2. **Quadratzahlen**
```python
def quadrat(zahl):
    return zahl * zahl
print(quadrat(4))
```

###  3. **Maximum von zwei Zahlen**
```python
def max_zwei(a, b):
  if a > b:
      return a
  else:
      return b
print(max_zwei(3, 5))
```

### 4. **Summierung**
```python
def summiere(a, b, c):
  return a + b + c
print(summiere(1, 2, 3))
```

### 5. **String-Wiederholung**
```python
def wiederhole_string(str, n):
  return str * n
print(wiederhole_string("Hallo", 3))
```

### 6. **Fahrenheit in Celsius**
```python
def fahrenheit_in_celsius(f):
  return (f - 32) * 5/9
print(fahrenheit_in_celsius(100))
```

### 7. **Kreisumfang**
```python
def kreisumfang(radius):
  return 2 * 3.14159 * radius
print(kreisumfang(5))
```

### 8. **Listenelemente addieren**
```python
def addiere_liste(liste):
  return sum(liste)
print(addiere_liste([1, 2, 3, 4, 5]))
```

### 9. **Check Gerade Zahl**
```python
def ist_gerade(zahl):
  return zahl % 2 == 0
print(ist_gerade(4))
```

### 10. **Countdown**
```python
def countdown(zahl):
   for i in range(zahl, -1, -1):
       print(i)
countdown(5)
```

### 11. **Minimum in Liste finden**
```python
def finde_minimum(liste):
   return min(liste)
print(finde_minimum([5, 3, 8, 2, 9]))
```

### 12. **Länge eines Strings**
```python
def laenge_string(str):
   return len(str)
print(laenge_string("Python"))
```

### 13. **Multiplikationstabelle**
```python
def multiplikationstabelle(zahl):
   for i in range(1, 11):
       print(f"{zahl} * {i} = {zahl * i}")
multiplikationstabelle(3)
```

### 14. **Palindrome prüfen**
```python
def ist_palindrom(str):
   return str == str[::-1]
print(ist_palindrom("radar"))
```

### 15. **Fibonacci-Folge**
```python
def fibonacci(n):
   a, b = 0, 1
   ergebnis = []
   for _ in range(n):
       ergebnis.append(a)
       a, b = b, a + b
   return ergebnis
print(fibonacci(5))
```


## Scopes

### 1. **Globale Variable**
```python
global_var = "Ich bin global"

def test_global():
   print(global_var)

test_global()
```

### 2. **Lokale Variable**
```python
def test_lokal():
   lokal_var = "Ich bin lokal"
   print(lokal_var)

test_lokal()
```

### 3. **Globale und lokale Variable mit demselben Namen**
```python
var = "Ich bin global"

def test_gleichnamig():
   var = "Ich bin lokal"
   print(var)  # Lokale Variable
   print(globals()['var'])  # Globale Variable

test_gleichnamig()
```

### 4. **Änderung einer globalen Variable innerhalb einer Funktion**
```python
global_var = "Ursprünglich global"

def test_aendern():
   global_var = "Geändert lokal"
   print(global_var)

test_aendern()
print(global_var)  # Bleibt unverändert "Ursprünglich global"
```

### 5. **Verwenden des `global`-Keywords**
```python
global_var = "Ursprünglich global"

def test_global_keyword():
   global global_var
   global_var = "Geändert global"
   print(global_var)

test_global_keyword()
print(global_var)  # Wird zu "Geändert global"
```

### 6. **Nested Functions Scope**
```python
def außen():
   außen_var = "Variable von außen"

   def innen():
       print(außen_var)

   innen()

außen()
```

### 7. **Lokale Variable in einer Schleife**
```python
def test_schleife():
   for i in range(3):
       schleifen_var = i
   print(schleifen_var)

test_schleife()
```

### 8. **Funktionsargument Scope**
```python
def test_argument(arg):
   arg = "Geändert"
   print(arg)

var = "Original"
test_argument(var)
print(var)  # Bleibt "Original"
```

### 9. **Rückgabewerte und Scope**
```python
def gib_zurueck():
   return "Rückgabewert"

global_var = gib_zurueck()
print(global_var)
```
