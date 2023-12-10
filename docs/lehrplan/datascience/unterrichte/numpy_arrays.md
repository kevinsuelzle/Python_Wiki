# NumPy: Einführung und NumPy Arrays

## Einführung [15min]

NumPy, ein Akronym für Numerical Python, ist eine wesentliche Bibliothek im Python-Ökosystem und dient als Grundlage für eine Vielzahl von wissenschaftlichen und numerischen Berechnungen. Entwickelt, um komplexe mathematische Operationen zu vereinfachen und zu beschleunigen, hat sich NumPy als unverzichtbares Werkzeug in den Bereichen Datenwissenschaft, Maschinelles Lernen, Ingenieurwesen und wissenschaftliche Forschung etabliert.

## Kernfunktionen von NumPy

Das Herzstück von NumPy ist das `ndarray`-Objekt, ein effizientes, multidimensionales Array, das schnelle Operationen auf großen Datenmengen ermöglicht. Diese Arrays unterscheiden sich von den Standard-Python-Listen durch ihre Fähigkeit, Operationen auf Vektorbasis durchzuführen, was eine bedeutende Beschleunigung gegenüber herkömmlichen Schleifenoperationen bietet.

NumPy bietet auch eine umfangreiche Sammlung von mathematischen Funktionen. Dazu gehören lineare Algebra, statistische Operationen, Fourier-Transformationen und vieles mehr. NumPy arbeitet hierbei eng mit anderen Bibliotheken wie scikit-learn und Pandas zusammen.

## Bedeutung im Bereich Data Science

Im Data Science Bereich hat sich NumPy als unerlässliches Werkzeug etabliert. Es ermöglicht die effiziente Manipulation und Analyse großer Datensätze, ein grundlegender Bestandteil vieler Datenverarbeitungs-Workflows. NumPy-Arrays dienen als Rückgrat für Pandas DataFrames, eine weitere Schlüsselkomponente in der Datenanalyse.

## Integration mit anderen Bibliotheken

NumPy interagiert eng mit anderen wichtigen Python-Bibliotheken. In Kombination mit Bibliotheken wie Matplotlib ermöglicht NumPy die Erstellung anspruchsvoller Datenvisualisierungen. In Verbindung mit maschinellem Lernen und Deep-Learning-Bibliotheken wie TensorFlow und PyTorch ermöglicht NumPy die Durchführung komplexer Berechnungen und Modellierungen.

## Performance-Aspekte

Einer der Hauptvorteile von NumPy ist seine Geschwindigkeit. Durch die Nutzung optimierter C-Bibliotheken bietet NumPy Leistungsverbesserungen, die mit reinem Python nicht zu erreichen sind. Diese Geschwindigkeit ist entscheidend für die Verarbeitung großer Datensätze und die Durchführung zeitintensiver Berechnungen.

## Codebeispiele [30 min]

### Beispiel 1: Erstellen eines einfachen NumPy Arrays


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

    [1 2 3 4 5]


Dieses Beispiel demonstriert das Erstellen eines einfachen eindimensionalen NumPy Arrays. Mit np.array(), einer grundlegenden Funktion von NumPy, wird eine Python-Liste in ein NumPy Array umgewandelt. Das Array arr speichert dann die Zahlen 1 bis 5 und identifiziert aufgrund der Initialisierungswerte auch einen geeigneten Datentyp:


```python
arr.dtype
```




    dtype('int64')



### Beispiel 2: Durchführen von mathematischen Operationen auf einem Array


```python
arr = np.array([1, 2, 3, 4, 5])
arr = arr * 2
print(arr)
```

    [ 2  4  6  8 10]


Hier wird ein Array mit den Zahlen 1 bis 5 erstellt und dann jede Zahl im Array verdoppelt. Die Operation arr * 2 multipliziert jedes Element im Array mit 2. Dies demonstriert die Vektorisierung, bei der Operationen auf jedes Element des Arrays angewendet werden, ohne eine Schleife zu verwenden.

### Beispiel 3: Erzeugen einer 2D-Matrix und Zugriff auf Elemente


```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix[0, 1])
```

    [[1 2 3]
     [4 5 6]]
    2


In diesem Beispiel wird eine 2D-Matrix (ein zweidimensionales Array) erstellt. Der Zugriff auf ein spezifisches Element erfolgt durch Angabe seiner Indizes - hier wird auf das Element in der ersten Zeile und zweiten Spalte zugegriffen (matrix[0, 1]), was den Wert 2 ergibt.

### Beispiel 4: Reshape eines Arrays


```python
arr = np.arange(1, 10)
reshaped_arr = arr.reshape(3, 3)
print(reshaped_arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


Dieses Beispiel zeigt, wie ein eindimensionales Array in eine 3x3-Matrix umgeformt wird. np.arange(1, 10) erzeugt ein Array mit den Zahlen von 1 bis 9. reshape(3, 3) formt dieses Array dann in eine 3x3-Matrix um.

### Beispiel 5: Berechnung von statistischen Kennzahlen


```python
arr = np.array([1, 2, 3, 4, 5])
print("Mittelwert:", np.mean(arr))
print("Standardabweichung:", np.std(arr))
```

    Mittelwert: 3.0
    Standardabweichung: 1.4142135623730951


Hier werden grundlegende statistische Berechnungen auf einem Array durchgeführt. Mit np.mean(arr) wird der Durchschnittswert und mit np.std(arr) die Standardabweichung der Elemente im Array berechnet.

## Aufgaben [90 min]

### A1: Erstellen eines NumPy Arrays 🌶️

Erstellen Sie ein NumPy Array mit den Werten von 10 bis 20.


```python
import numpy as np

arr = np.array(range(10, 21))
print(arr)
```

    [10 11 12 13 14 15 16 17 18 19 20]



```python
arr = np.arange(10,21)
print(arr)
```

    [10 11 12 13 14 15 16 17 18 19 20]


### A2: Summe der Elemente eines Arrays 🌶️

Berechnen Sie die Summe aller Elemente in einem NumPy Array [8, 4, 6, 0, 2].


```python
arr = np.array([8, 4, 6, 0, 2])
summe = np.sum(arr)
print(summe)
```

    20


### A3: Maximalwert in einem Array finden 🌶️

Bestimmen Sie den größten Wert in dem Array [3, -1, 7, 4, 2]. Wie können wir herausfinden an welcher Stelle dieser Maximalwert steht?


```python
arr = np.array([3, 1, 7, 4, 2])
max_value = np.max(arr)
print(max_value)
```

    7



```python
max_pos = np.argmax(arr)
print(max_pos)
```

    2


### A4: 2D-Array erstellen 🌶️🌶️

Erstellen Sie ein 2D-Array der Größe 3x3, das die Zahlen von 1 bis 9 enthält.


```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]



```python
arr = np.arange(1,10).reshape(3,3)
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


### A5: Zeilensummen einer Matrix berechnen 🌶️🌶️

Berechnen Sie die Summe jeder Zeile in der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].


```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

row_sums = np.sum(matrix, axis=1)
print(row_sums)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [ 6 15 24]


### A6: Spaltensummen einer Matrix berechnen 🌶️🌶️

Berechnen Sie die Spaltensummen der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].


```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

col_sums = np.sum(matrix, axis=0)
print(col_sums)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [12 15 18]


### A7: Elementweise Multiplikation zweier Arrays 🌶️

Multiplizieren Sie die Elemente der Arrays [1, 2, 3] und [4, 5, 6] elementweise.


```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
product = np.multiply(arr1, arr2)
print(product)
```

    [ 4 10 18]


### A8: Zufälliges Array erzeugen 🌶️🌶️

Erzeugen Sie ein eindimensionales Array mit 5 zufälligen Ganzzahlen zwischen 0 und 10.


```python
arr = np.random.randint(0, 11, 5)
print(arr)
```

    [ 2  5  9  3 10]


### A9: Negative Werte in einem Array 🌶️🌶️🌶️

Ersetzen Sie alle negativen Werte in dem Array [-1, 2, -3, 4, -5] durch 0.


```python
arr = np.array([-1, 2, -3, 4, -5])
arr[arr < 0] = 0
print(arr)
```

    [0 2 0 4 0]


### A10: Transposition einer Matrix 🌶️🌶️

Transponieren Sie die Matrix [[1, 2], [3, 4], [5, 6]].


```python
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix)

transposed_matrix = np.transpose(matrix)
print(transposed_matrix)
```

    [[1 2]
     [3 4]
     [5 6]]
    [[1 3 5]
     [2 4 6]]


[Lösungen](numpy_arrays_loesungen.md)


```python

```
