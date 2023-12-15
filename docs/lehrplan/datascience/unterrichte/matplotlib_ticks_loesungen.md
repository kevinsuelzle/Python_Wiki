# Lösungen

### A1: Einfache Tick-Einstellung 🌶️

Erstelle ein Liniendiagramm mit x-Werten [0, 1, 2, 3, 4] und y-Werten [20, 35, 30, 35, 27]. Setze Ticks auf der x-Achse bei jedem ganzzahligen Wert und auf der y-Achse bei jedem Wert der y-Daten.


```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [20, 35, 30, 35, 27]

plt.plot(x, y)
plt.xticks(x)
plt.yticks(y)
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_2_0.png)
    


### A2: Rotieren von Tick-Beschriftungen 🌶️

Erstelle ein Balkendiagramm für das Dataset ['Apple', 'Banana', 'Orange', 'Grapes', 'Cherries'] mit zufälligen Verkaufszahlen. Rotiere die x-Achsen-Tick-Beschriftungen um 30 Grad.


```python
import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Cherries']
sales = np.random.randint(50, 200, size=len(fruits))

plt.bar(fruits, sales)
plt.xticks(rotation=30)
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_4_0.png)
    


### A3: Logarithmische Skala 🌶️

Erstelle ein Liniendiagramm für exponentiell wachsende Daten. Verwende eine logarithmische Skala für die y-Achse.


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 100)
y = np.exp(x) * x**3

plt.plot(x, y)
plt.yscale('log')
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_6_0.png)
    


### A4: Anpassen der Tick-Dichte 🌶️🌶️

Erstelle ein Liniendiagramm mit x-Werten von 0 bis 20 und y-Werten als deren Quadrat. Setze Ticks auf der x-Achse in 2er Schritten.


```python
import matplotlib.pyplot as plt

x = range(21)
y = [i**2 for i in x]

plt.plot(x, y)
plt.xticks(range(0, 21, 2))
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_8_0.png)
    


### A5: Formatierung der Tick-Beschriftungen 🌶️🌶️🌶️

Erstelle ein Balkendiagramm für das Dataset ['A', 'B', 'C', 'D'] mit Werten [3, 7, 2, 5]. Formatiere die y-Achsen-Ticks als Prozente.


```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.bar(categories, values)
plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=10))
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_10_0.png)
    


### A6: Benutzerdefinierte Tick-Beschriftungen 🌶️🌶️

Erstelle ein Liniendiagramm mit x-Werten [1, 2, 3, 4, 5] und y-Werten [2, 3, 5, 7, 11]. Benenne die Ticks auf der x-Achse als ['eins', 'zwei', 'drei', 'vier', 'fünf'].


```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
labels = ['eins', 'zwei', 'drei', 'vier', 'fünf']

plt.plot(x, y)
plt.xticks(x, labels)
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_12_0.png)
    


### A7: Verstecken von Ticks 🌶️

Erstelle ein Liniendiagramm und "verstecke" alle Ticks auf der y-Achse.


```python
import matplotlib.pyplot as plt

x = range(10)
y = [i**2 for i in x]

plt.plot(x, y)
plt.yticks([])
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_14_0.png)
    


### A8: Tick-Beschriftungen mit wissenschaftlicher Notation 🌶️🌶️🌶️

Erstelle ein Balkendiagramm mit großen Zahlen und stelle die y-Achsen-Ticks in wissenschaftlicher Notation dar.


```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

categories = ['A', 'B', 'C', 'D']
values = [1000000, 2000000, 3000000, 4000000]

plt.bar(categories, values)
plt.gca().yaxis.set_major_formatter(mticker.ScalarFormatter(useMathText=True))
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_16_0.png)
    


### A9: Anpassen von Tick-Farben 🌶️🌶️

Erstelle ein Liniendiagramm und ändere die Farbe der Ticks auf der x-Achse in Rot.


```python
import matplotlib.pyplot as plt

x = range(5)
y = [i**3 for i in x]

plt.plot(x, y)
ax = plt.gca()
ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='green')
plt.show()
```


    
![png](matplotlib_ticks_loesungen_files/matplotlib_ticks_loesungen_18_0.png)
    

