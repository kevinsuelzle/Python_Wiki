
# Lösungen

Selbstverständlich, hier sind Lösungen zu den Übungsaufgaben zu Strings in Python:

### 1. Länge eines Strings ermitteln:
```python
text = "Dies ist ein Beispiel"
laenge = len(text)
print(f"Länge des Strings: {laenge}")
```

### 2. String rückwärts ausgeben:
```python
text = "Python"
rueckwaerts = text[::-1]
print(rueckwaerts)
```

### 3. String in Großbuchstaben konvertieren:
```python
text = "python"
grossbuchstaben = text.upper()
print(grossbuchstaben)
```

### 4. Anzahl der Vokale zählen:
```python
text = "Python ist großartig."
anzahl_vokale = sum(1 for char in text if char.lower() in "aeiou")
print(anzahl_vokale)
```

### 5. Erster und letzter Buchstabe eines Strings:
```python
text = "Python"
erster_buchstabe = text[0]
letzter_buchstabe = text[-1]
print(f"Erster Buchstabe: {erster_buchstabe}, Letzter Buchstabe: {letzter_buchstabe}")
```

### 6. Zeichen ersetzen:
```python
text = "Python ist großartig."
neuer_text = text.replace("groß", "super")
print(neuer_text)
```

### 7. Funktion zur Überprüfung einer E-Mail-Adresse:
```python
import re

def ist_gueltige_email(email):
   pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   return re.match(pattern, email) is not None

print(ist_gueltige_email("beispiel@email.com"))  # True
print(ist_gueltige_email("keine-email"))  # False
```

### 8. Leerzeichen entfernen:
```python
text = " Text mit Leerzeichen "
ohne_leerzeichen = text.strip()
print(ohne_leerzeichen)
```

### 9. String in Wörter aufteilen:
```python
text = "Dies ist ein Satz."
woerter = text.split()
print(woerter)
```

### 10. Häufigster Buchstabe in einem String finden:
```python
text = "Mississippi"
haeufigster_buchstabe = max(set(text), key=text.count)
print(haeufigster_buchstabe)
```

### 11. Überprüfung, ob ein String nur aus Zahlen besteht:
```python
text = "12345"
if text.isdigit():
   print("Der String besteht nur aus Zahlen.")
else:
   print("Der String enthält andere Zeichen als Zahlen.")
```

### 12. Funktion zur Überprüfung von Anagrammen:
```python
def sind_anagramme(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(sind_anagramme("listen", "silent"))  # True
print(sind_anagramme("Python", "Java"))  # False
```

### 13. Anzahl der Wörter in einem String zählen:
```python
text = "Dies ist ein Beispiel Satz."
woerter = text.split()
anzahl_woerter = len(woerter)
print(f"Anzahl der Wörter: {anzahl_woerter}")
```

### 14. Anzahl der Zeichen in einem String zählen:
```python
text = "Python ist großartig."
anzahl_zeichen = sum(1 for char in text)
print(f"Anzahl der Zeichen: {anzahl_zeichen}")
```

### 15. Überprüfung, ob ein String eine gültige URL ist (mithilfe einer regulären Ausdrucks):
```python
import re

def ist_gueltige_url(url):
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return re.match(pattern, url) is not None

print(ist_gueltige_url("https://www.example.com"))  # True
print(ist_gueltige_url("www.invalid-url"))  # False
```

### 16. String in Titel-Case umwandeln:
```python
text = "python ist großartig"
titel_case = text.title()
print(titel_case)
```

### 17. Anzahl der Zeichen, die keine Buchstaben oder Zahlen sind, zählen:
```python
text = "Python 123!?"
anzahl_sonderzeichen = sum(1 for char in text if not char.isalnum())
print(f"Anzahl der Sonderzeichen: {anzahl_sonderzeichen}")
```

### 18. Extrahieren von URLs aus einem Text (mithilfe einer regulären Ausdrucks):
```python
import re

text = "Besuchen Sie meine Website unter https://www.example.com. Weitere Informationen finden Sie unter www.invalid-url."
urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print(urls)
```

### 19. Funktion für Palindrom-Überprüfung:
```python
def ist_palindrom(text):
    text = text.lower()  # Um Groß-/Kleinschreibung zu ignorieren
    return text == text[::-1]

print(ist_palindrom("anna"))  # True
print(ist_palindrom("Python"))  # False
```
