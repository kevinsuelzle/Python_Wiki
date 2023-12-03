# Einführung in Python-Funktionen

Bereits in unseren bisherigen Python-Lektionen haben wir verschiedene eingebaute Funktionen verwendet, die
verdeutlichen, wie nützlich und vielseitig Funktionen in Python sind. Auch in der Startphase haben wir bereits
unsere eigenen Funktionen geschrieben.

Ein klassisches Beispiel ist die `print()`-Funktion, die wir häufig verwendet haben, um Werte auf dem Bildschirm
auszugeben. Sie ist ein einfaches, aber mächtiges
Werkzeug für die Ausgabe von Informationen während der Ausführung eines Programms.

Eine weitere bisher häufig genutzte Funktion ist `input()`, die es uns ermöglicht, Benutzereingaben zu erfassen. Diese
Eingaben können dann für eine Vielzahl von Zwecken innerhalb des Programms verwendet werden.

Schließlich haben wir auch die `random`-Bibliothek und ihre Funktionen wie `random.randint()` verwendet, um 
Zufallszahlen zu generieren.

Diese Funktionen sind Beispiele dafür, wie eingebaute und modul-spezifische Funktionen in Python die Entwicklung von
Programmen vereinfachen und bereichern können, indem sie
komplexe Aufgaben hinter einfach zu verstehenden und zu verwendenden Schnittstellen verbergen.

Funktionen haben immer einen eindeutigen Namen, eine Menge an Parametern, die das Verhalten der Funktion modifizieren
und sehr oft auch einen Rückgabewert, mit dem wir zum Beispiel Ergebnisse an den aufrufenden Code zurückgeben können.

## Bedeutung und Zweck von Funktionen

1. **Modularität**: Funktionen ermöglichen es, den Code in kleinere, wiederverwendbare Teile zu unterteilen. Das macht
   den Code übersichtlicher und wartbarer.

2. **Wiederverwendbarkeit**: Einmal definierte Funktionen können in verschiedenen Teilen eines Programms oder sogar in
   verschiedenen Programmen wiederverwendet werden.

3. **Abstraktion**: Durch Funktionen kann man komplexe Abläufe hinter einer einfachen Schnittstelle verbergen. Nutzer
   der Funktion müssen nicht wissen, wie die Funktion intern arbeitet.

4. **Testbarkeit**: Funktionen ermöglichen es, kleine Teile des Codes isoliert zu testen.

## Definition von Funktionen

- **Syntax**:

```python
def funktionsname(parameter1, parameter2, ...):
    # Funktionskörper
    return ergebnis
```

Daran erkennt man die grundlegende Syntax von einer Funktionsdefinition. Mit dem Keyword `def` zeigen wir Python an,
dass wir eine Funktion erstellen wollen. 

Im Funktionskörper können alle Dinge, die wir aus Python kennen ganz normal verwendet werden. Der Code im Funktionsblock
unterscheidet sich nicht von anderem Python-Code.

- **Beispiel**:

```python
def begruessung(name):
    return f"Hallo, {name}!"
```

## Definition von Parametern

- Parameter sind Variablen, die beim Aufruf der Funktion Werte erhalten.

- **Beispiel**:

```python
def addiere(a, b):
    return a + b
```

## Rückgabewerte

- Der Rückgabewert ist das Ergebnis, das eine Funktion zurückgibt.
- Verwendet wird hierfür das `return`-Statement.

- **Beispiel**:

```python
def multipliziere(x, y):
    ergebnis = x * y
    return ergebnis
```

## Codebeispiele

1. **Einfache Funktion**

 ```python
def gruessen():
    return "Hallo Welt!"

print(gruessen())
```

2. **Funktion mit Parametern**

```python
def quadrat(zahl):
    return zahl * zahl

print(quadrat(4))
```

3. **Funktion mit mehreren Parametern**

```python
def vollstaendiger_name(vorname, nachname):
    return f"{vorname} {nachname}"


print(vollstaendiger_name("Max", "Mustermann"))
```

4. **Funktion mit optionalen Parametern**

```python
def begruessung(name, formal=False):
    if formal:
        return f"Sehr geehrte/r {name},"
    else:
        return f"Hallo, {name}!"

print(begruessung("Anna"))
print(begruessung("Prof. Dr. Müller", formal=True))
```

Durch diese Beispiele wird deutlich, wie Funktionen in Python definiert und genutzt werden können, um Code modular,
wiederverwendbar und gut strukturiert zu gestalten. Funktionen sind ein zentrales Konzept in der Programmierung und
unerlässlich für die Erstellung von sauberem und effizientem Code.

### Aufgaben

### Übungsaufgaben zum Erstellen von Funktionen in Python

1. **Einfache Begrüßungsfunktion**: Schreibe eine Funktion `begruesse()`, die "Hallo Welt!" ausgibt.

2. **Quadratzahlen**: Schreibe eine Funktion `quadrat()`, die das Quadrat einer übergebenen Zahl zurückgibt.

3. **Maximum von zwei Zahlen**: Schreibe eine Funktion `max_zwei()`, die zwei Zahlen als Argumente nimmt und die größere
   Zahl zurückgibt.

4. **Summierung**: Schreibe eine Funktion `summiere()`, die die Summe von drei übergebenen Zahlen berechnet und
   zurückgibt.

5. **String-Wiederholung**: Schreibe eine Funktion `wiederhole_string(str, n)`, die einen String `str` und eine Zahl `n`
   nimmt und den String `n`-mal wiederholt.

6. **Fahrenheit in Celsius**: Schreibe eine Funktion `fahrenheit_in_celsius()`, die eine Temperatur in Fahrenheit nimmt
   und in Celsius umrechnet.

7. **Kreisumfang**: Schreibe eine Funktion `kreisumfang()`, die den Radius eines Kreises als Parameter nimmt und den
   Umfang des Kreises berechnet.

8. **Listenelemente addieren**: Schreibe eine Funktion `addiere_liste()`, die eine Liste von Zahlen nimmt und ihre Summe
   zurückgibt.

9. **Check Gerade Zahl**: Schreibe eine Funktion `ist_gerade()`, die prüft, ob eine übergebene Zahl gerade ist.

10. **Countdown**: Schreibe eine Funktion `countdown()`, die eine Zahl nimmt und einen Countdown von dieser Zahl bis 0
    ausgibt.

11. **Minimum in Liste finden**: Schreibe eine Funktion `finde_minimum()`, die eine Liste von Zahlen nimmt und das
    kleinste Element zurückgibt.

12. **Länge eines Strings**: Schreibe eine Funktion `laenge_string()`, die die Länge eines übergebenen Strings
    zurückgibt.

13. **Multiplikationstabelle**: Schreibe eine Funktion `multiplikationstabelle()`, die eine Zahl nimmt und ihre
    Multiplikationstabelle bis 10 ausgibt.

14. **Palindrome prüfen**: Schreibe eine Funktion `ist_palindrom()`, die einen String nimmt und prüft, ob es ein
    Palindrom ist.

15. **Fibonacci-Folge**: Schreibe eine Funktion `fibonacci()`, die eine Zahl `n` nimmt und die ersten `n` Zahlen der
    Fibonacci-Folge zurückgibt.

## Gültigkeitsbereich von Variablen - Scopes

Der Begriff "Scope" bezieht sich in der Programmierung auf den Bereich eines Programms, in dem eine Variable zugänglich
ist. In Python gibt es im Wesentlichen zwei Hauptbereiche (Scopes): global und lokal. Um den Scope von Variablen in und
außerhalb von Funktionen zu erläutern, betrachten wir ein konkretes Beispiel:

### Beispiel zur Erläuterung des Scopes

#### Globale Variable

Eine Variable, die außerhalb einer Funktion definiert wird, ist global. Das bedeutet, sie ist überall im Code
zugänglich. Bisher haben wir alle Variablen global definiert, da wir Funktionen noch nicht kannten.

```python
globale_variable = "Ich bin global!"


def meine_funktion():
    print(globale_variable)  # Zugriff auf die globale Variable ist möglich


meine_funktion()  # Gibt "Ich bin global!" aus
print(globale_variable)  # Gibt ebenfalls "Ich bin global!" aus
```

In diesem Beispiel ist `globale_variable` außerhalb der Funktion `meine_funktion` definiert und kann sowohl innerhalb
als auch außerhalb der Funktion verwendet werden.

**Anmerkung**:
Obwohl dieses Vorgehen möglich ist, sollten wir das möglichst nicht verwenden. Natürlich gibt es Ausnahmen in denen das
eine sinnvolle Vorgehensweise ist. Globale Variablen sollten allerdings so selten wie möglich und nur mit gutem Grund
angewendet werden. Sinnvollerweise übergibt man die notwendigen Variablen als Argumente an die Funktion.

#### Lokale Variable

Eine innerhalb einer Funktion definierte Variable ist lokal und nur innerhalb dieser Funktion gültig.

```python
def eine_andere_funktion():
    lokale_variable = "Ich bin lokal!"
    print(lokale_variable)  # Gültig innerhalb dieser Funktion


eine_andere_funktion()  # Gibt "Ich bin lokal!" aus
# print(lokale_variable)  # Fehler: lokale_variable ist außerhalb ihrer Funktion nicht definiert
```

In diesem Beispiel ist `lokale_variable` nur innerhalb der `eine_andere_funktion` gültig. Ein Versuch, auf sie außerhalb
ihrer Funktion zuzugreifen, führt zu einem Fehler.

#### Shadowing

Wenn eine lokale Variable denselben Namen wie eine globale Variable hat, wird die globale Variable innerhalb der
Funktion "verdeckt" oder "überschattet":

```python
variable = "Ich bin global!"


def schatten_funktion():
    variable = "Ich bin lokal!"
    print(variable)  # Gibt die lokale Variable aus


schatten_funktion()  # Gibt "Ich bin lokal!" aus
print(variable)  # Gibt die globale Variable aus, also "Ich bin global!"
```

In diesem Beispiel gibt es sowohl eine globale als auch eine lokale Variable namens `variable`. Innerhalb der
Funktion `schatten_funktion` bezieht sich `variable` auf die lokale Instanz.

**Anmerkung**: Auch hier gilt, dass man das möglichst vermeiden sollte. Moderne Python-IDEs geben auch eine Warnung aus,
wenn dies getan wird.

### Zusammenfassung - Scopes

- **Globale Variablen**: Außerhalb von Funktionen definiert; im gesamten Code gültig.
- **Lokale Variablen**: Innerhalb von Funktionen definiert; nur in ihrer eigenen Funktion gültig.
- **Schattenbildung**: Lokale Variablen können den gleichen Namen wie globale Variablen haben, aber sie sind separate
  Instanzen.

Das Verständnis des Scopes von Variablen ist entscheidend, um zu verstehen, wie Informationen und Daten in einem
Programm gespeichert und zugänglich gemacht werden. Es hilft auch dabei, Fehler zu vermeiden, die durch unbeabsichtigte
Überschneidungen von Variablennamen entstehen können.

### Aufgaben

### Übungsaufgaben zum Thema Scopes in Python

#### Aufgaben

1. **Globale Variable**: Definiere eine globale Variable und gib sie innerhalb einer Funktion aus.
2. **Lokale Variable**: Definiere eine lokale Variable innerhalb einer Funktion und gib sie innerhalb dieser Funktion
   aus.
3. **Globale und lokale Variable mit demselben Namen**: Definiere eine globale und eine lokale Variable mit demselben
   Namen und gib beide innerhalb der Funktion aus.
4. **Änderung einer globalen Variable innerhalb einer Funktion**: Versuche, eine globale Variable innerhalb einer
   Funktion zu ändern, ohne das `global`-Keyword zu verwenden.
5. **Verwenden des `global`-Keywords**: Ändere eine globale Variable innerhalb einer Funktion mit Hilfe des `global`
   -Keywords.
6. **Nested Functions Scope**: Definiere eine verschachtelte Funktion und greife auf eine Variable aus der umgebenden
   Funktion zu.
7. **Lokale Variable in einer Schleife**: Definiere eine lokale Variable innerhalb einer for-Schleife in einer Funktion
   und gib sie aus.
8. **Funktionsargument Scope**: Übergebe eine Variable als Argument an eine Funktion und ändere sie innerhalb der
   Funktion.
9. **Rückgabewerte und Scope**: Gib einen Wert aus einer Funktion zurück und weise ihn einer globalen Variable zu.

## Argumente vs Parameter - Was ist der Unterschied?

In der Programmierung, insbesondere in Python, ist es wichtig, die Unterschiede zwischen Parametern und Argumenten zu
verstehen, da sie oft fälschlicherweise synonym verwendet werden, obwohl sie unterschiedliche Konzepte darstellen.

#### Parameter

- **Definition**: Parameter sind die Variablen, die in der Definition einer Funktion aufgeführt werden. Sie agieren wie
  Platzhalter für die Werte, die die Funktion beim Aufruf erhält.
- **Beispiel**: In der Funktionsdefinition `def addiere(a, b):`, sind `a` und `b` die Parameter. Sie definieren, welche
  Art von Werten die Funktion erwartet.

#### Argumente

- **Definition**: Argumente sind die tatsächlichen Werte, die beim Aufruf einer Funktion an diese übergeben werden. Sie
  ersetzen die Parameter, wenn die Funktion ausgeführt wird.
- **Beispiel**: Beim Aufruf `addiere(3, 5)`, sind `3` und `5` die Argumente. Sie sind die konkreten Werte, die für `a`
  und `b` eingesetzt werden.

#### Zusammenfassung

- **Parameter**: Variablen in der Funktionsdefinition, die den Typ und die Anzahl der Werte angeben, die die Funktion
  erwartet.
- **Argumente**: Tatsächliche Werte, die an die Funktion übergeben werden, wenn sie aufgerufen wird.
- **Analogie**: Man kann sich Parameter als die "Beschreibung" eines Produkts und Argumente als das "tatsächliche
  Produkt" vorstellen.

Durch das Verständnis des Unterschieds zwischen Parametern und Argumenten kann man die Funktionsweise von Funktionen in
Python klarer erfassen und effektiver programmieren. Es hilft auch dabei, Missverständnisse zu vermeiden, die bei der
Verwendung von Funktionen auftreten können.

# Lösungen

## Funktionen definieren

Hier sind die Lösungen für die vorgeschlagenen Übungsaufgaben:

1. **Einfache Begrüßungsfunktion**
```python
def begruesse():
   print("Hallo Welt!")
begruesse()
```

2. **Quadratzahlen**
  ```python
  def quadrat(zahl):
      return zahl * zahl
  print(quadrat(4))
  ```

3. **Maximum von zwei Zahlen**
  ```python
  def max_zwei(a, b):
      if a > b:
          return a
      else:
          return b
  print(max_zwei(3, 5))
  ```

4. **Summierung**
  ```python
  def summiere(a, b, c):
      return a + b + c
  print(summiere(1, 2, 3))
  ```

5. **String-Wiederholung**
  ```python
  def wiederhole_string(str, n):
      return str * n
  print(wiederhole_string("Hallo", 3))
  ```

6. **Fahrenheit in Celsius**
  ```python
  def fahrenheit_in_celsius(f):
      return (f - 32) * 5/9
  print(fahrenheit_in_celsius(100))
  ```

7. **Kreisumfang**
  ```python
  def kreisumfang(radius):
      return 2 * 3.14159 * radius
  print(kreisumfang(5))
  ```

8. **Listenelemente addieren**
  ```python
  def addiere_liste(liste):
      return sum(liste)
  print(addiere_liste([1, 2, 3, 4, 5]))
  ```

9. **Check Gerade Zahl**
  ```python
  def ist_gerade(zahl):
      return zahl % 2 == 0
  print(ist_gerade(4))
  ```

10. **Countdown**
   ```python
   def countdown(zahl):
       for i in range(zahl, -1, -1):
           print(i)
   countdown(5)
   ```

11. **Minimum in Liste finden**
   ```python
   def finde_minimum(liste):
       return min(liste)
   print(finde_minimum([5, 3, 8, 2, 9]))
   ```

12. **Länge eines Strings**
   ```python
   def laenge_string(str):
       return len(str)
   print(laenge_string("Python"))
   ```

13. **Multiplikationstabelle**
   ```python
   def multiplikationstabelle(zahl):
       for i in range(1, 11):
           print(f"{zahl} * {i} = {zahl * i}")
   multiplikationstabelle(3)
   ```

14. **Palindrome prüfen**
   ```python
   def ist_palindrom(str):
       return str == str[::-1]
   print(ist_palindrom("radar"))
   ```

15. **Fibonacci-Folge**
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

#### Lösungen

1. **Globale Variable**
   ```python
   global_var = "Ich bin global"

   def test_global():
       print(global_var)

   test_global()
   ```

2. **Lokale Variable**
   ```python
   def test_lokal():
       lokal_var = "Ich bin lokal"
       print(lokal_var)

   test_lokal()
   ```

3. **Globale und lokale Variable mit demselben Namen**
   ```python
   var = "Ich bin global"

   def test_gleichnamig():
       var = "Ich bin lokal"
       print(var)  # Lokale Variable
       print(globals()['var'])  # Globale Variable

   test_gleichnamig()
   ```

4. **Änderung einer globalen Variable innerhalb einer Funktion**
   ```python
   global_var = "Ursprünglich global"

   def test_aendern():
       global_var = "Geändert lokal"
       print(global_var)

   test_aendern()
   print(global_var)  # Bleibt unverändert "Ursprünglich global"
   ```

5. **Verwenden des `global`-Keywords**
   ```python
   global_var = "Ursprünglich global"

   def test_global_keyword():
       global global_var
       global_var = "Geändert global"
       print(global_var)

   test_global_keyword()
   print(global_var)  # Wird zu "Geändert global"
   ```

6. **Nested Functions Scope**
   ```python
   def außen():
       außen_var = "Variable von außen"

       def innen():
           print(außen_var)

       innen()

   außen()
   ```

7. **Lokale Variable in einer Schleife**
   ```python
   def test_schleife():
       for i in range(3):
           schleifen_var = i
       print(schleifen_var)

   test_schleife()
   ```

8. **Funktionsargument Scope**
   ```python
   def test_argument(arg):
       arg = "Geändert"
       print(arg)

   var = "Original"
   test_argument(var)
   print(var)  # Bleibt "Original"
   ```

9. **Rückgabewerte und Scope**
   ```python
   def gib_zurueck():
       return "Rückgabewert"

   global_var = gib_zurueck()
   print(global_var)
   ```
