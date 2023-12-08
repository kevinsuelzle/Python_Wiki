# Lösungen

### **Quadrate erstellen**

```python
quadrate = [i ** 2 for i in range(1, 11)]
```

### **Gerade Zahlen**

```python
gerade = [i for i in range(1, 21) if i % 2 == 0]
```

### **Ungerade Zahlen umwandeln**

```python
ungerade_quadrate = [i ** 2 for i in range(1, 11) if i % 2 != 0]
```

### **Zeichenkettenlängen**

```python
wortlaengen = [len(wort) for wort in ["Hallo", "Welt", "Python"]]
```

### **Absolute Werte**

```python
absolute = [abs(i) for i in [-1, -2, 3, -4, 5]]
```

### **Filtern nach Bedingung**

```python
teilbar_durch_3 = [i for i in range(1, 21) if i % 3 == 0]
```

### **String in Großbuchstaben**

```python
grossbuchstaben = [s.upper() for s in ["hallo", "welt", "python"]]
```

### **Tupel erstellen**

```python
tupel_liste = [(i, i * i) for i in range(1, 11)]
```

### **Nicht-leere Strings**

```python
nicht_leer = [s for s in ["Hallo", "", "Welt", ""] if s]
```

### **Negative Zahlen umkehren**

```python
positive = [abs(i) for i in [-1, 2, -3, 4, -5]]
```

### **Fizz Buzz**

```python
fizz_buzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for
             i in range(1, 16)]
```

### **Wurzeln ziehen**

```python
wurzeln = [i ** 0.5 for i in [1, 4, 9, 16, 25]]
```

### **Filtern und Umwandeln**

```python
verdoppelte_gerade = [i * 2 for i in range(1, 11) if i % 2 == 0]
```

### **Teile von Strings**

```python
erste_zeichen = [wort[0] for wort in ["Hallo", "Welt", "Python"]]
```

### **Vokale entfernen**

```python
ohne_vokale = [''.join([buchstabe for buchstabe in wort if buchstabe.lower() not in "aeiou"]) for wort in
               ["Hallo", "Welt", "Python"]]
```

### **Einzigartige Werte**

```python
einzigartig = list(set([1, 2, 2, 3, 3, 4, 4, 5]))
```

### **Index und Wert**

```python
index_wert = [(index, wert) for index, wert in enumerate(["a", "b", "c", "d"])]
```

### **Summe von Paaren**

```python
paare = [(i, j) for i in range(1, 11) for j in range(1, 11) if i + j == 10]
```

### **Durchschnittswerte**

```python
durchschnitt = [(liste[i] + liste[i + 1]) / 2 for i in range(len(liste) - 1)]
```

### **Liste von Listen abflachen**

```python
abgeflacht = [element for sublist in [[1, 2], [3, 4], [5, 6]] for element in sublist]
```