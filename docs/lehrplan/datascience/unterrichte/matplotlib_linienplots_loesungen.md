# Lösungen

### A1: Grundlegender Linienplot 🌶️

Erstelle einen einfachen Linienplot mit den x-Werten [0, 1, 2, 3, 4] und den y-Werten [0, 13, 6, 19, 12].


```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 13, 6, 19, 12]

plt.plot(x, y)
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_2_0.png)
    


### A2: Linienplot mit Titel und Achsenbeschriftungen 🌶️

Erstelle einen Linienplot mit x-Werten von 1 bis 10 und y-Werten als deren Quadrate. Füge dem Plot einen Titel und Achsenbeschriftungen hinzu.


```python
import matplotlib.pyplot as plt

x = range(1, 11)
y = [xi**2 for xi in x]

plt.plot(x, y)
plt.title("Quadratzahlen")
plt.xlabel("Zahl")
plt.ylabel("Quadrat der Zahl")
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_4_0.png)
    


### A3: Mehrfarbiger Linienplot 🌶️

Erstelle einen Linienplot für die Funktionen y = x und y = x^2 auf dem Intervall [0, 5], wobei jede Linie eine andere Farbe haben soll.


```python
import matplotlib.pyplot as plt

x = range(0, 6)
y1 = x
y2 = [xi**2 for xi in x]

plt.plot(x, y1, 'r') # Rot für die erste Linie
plt.plot(x, y2, 'b') # Blau für die zweite Linie
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_6_0.png)
    


### A4:  Gestrichelter Linienplot 🌶️🌶️

Erstelle einen Linienplot für die Funktion y = x^3 von -20 bis +20, wobei die Linie gestrichelt und in Grün dargestellt werden soll.


```python
import matplotlib.pyplot as plt

x = range(-20, 20)
y = [xi**3 for xi in x]

plt.plot(x, y, 'g--') # Grüne, gestrichelte Linie
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_8_0.png)
    


### A5: Linienplot mit Anmerkungen 🌶️🌶️🌶️

Erstelle einen Linienplot für y = x^5 von -15 bis +15 und füge eine Anmerkung bei dem Punkt (0,0) hinzu.


```python
import matplotlib.pyplot as plt

x = range(-15, +15)
y = [xi**5 for xi in x]

plt.plot(x, y)
plt.annotate('Punkt (0, 0)',
             xy=(0, 0),
             xytext=(10, -600000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_10_0.png)
    


### A6: Linienplot mit Markierungen für Datenpunkte 🌶️

Erstelle einen Linienplot für die Funktion y = x^2 auf dem Intervall [1, 4]. Verwende unterschiedliche Markierungen für die Datenpunkte.


```python
import matplotlib.pyplot as plt

x = range(1, 5)
y = [xi**2 for xi in x]

plt.plot(x, y, marker='o') # Kreismarkierungen
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_12_0.png)
    


### A7: Linienplots mit Legende 🌶️🌶️🌶

Erzeuge 5 Linienplots mit Legenden für x, x^2, x^3, x^4, x^5 im Bereich -100 bis +100.
Zeige auch noch ein Gitter an.


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,+2, 0.01)
y1 = x
y2 = [xi**2 for xi in x]
y3 = [xi**3 for xi in x]
y4 = [xi**4 for xi in x]
y5 = [xi**5 for xi in x]

plt.plot(x, y1, label='y = x')
plt.plot(x, y2, label='y = x^2')
plt.plot(x, y3, label='y = x^3')
plt.plot(x, y4, label='y = x^4')
plt.plot(x, y5, label='y = x^5')
plt.legend()
plt.grid()
plt.show()
```


    
![png](matplotlib_linienplots_loesungen_files/matplotlib_linienplots_loesungen_14_0.png)
    

