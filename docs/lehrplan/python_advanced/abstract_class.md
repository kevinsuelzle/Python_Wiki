# Abstract Class, Dataclass

## Python und Abstract Classes

Die objektorientierte Programmierung kennt Klassen, die man NICHT instanziieren kann! Wow! :D

Wozu sind die denn dann überhaupt da? Aaaahhh.. man kann aber dennoch Unterklassen aus ihnen bilden. 
Dadurch dienen sie als Blaupausen für den Code.

Analgo gibt es dann auch sogenannte Abstract Methods. Wie das konnkret aussieht zeigen die folgenden Zeilen, Beispiele und Erklärungen.
Es ist so, dass Python nicht direkt das Konzept von abstrakten Klassen liefert. Dafür gibt es aber ein Modul mit dem Namen "ABC"



Ein erstes Beispiel:

```python 
from abc import ABC

class AbstractClassName(ABC):
    pass
```
To define an abstract method, you use the @abstractmethod decorator:

```python 
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass
```

#### Ein konkretes Python 

Ein super seltenes Beispiel, welches überhaupt nicht oft vorkommt dreht sich um das Thema Mitarbeiter, Daten der Mitarbeiter, Gehaltsmanagement von Mitarbeiter und so ein Kram. und genau darum soll es auch jetzt wieder gehen:

Die Employee-Klasse soll dabei als Blaupause für alle anderen spezifischen Mitarbeiter-Klassen dienen:


```python 
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass
```

#### Die FulltimeEmployee Klasse

Der FulltimeEmployee ist ein Employee und bekommt monatlich ein festen Einkommen.

```python 
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

```

Der HourlyEmployee ist auch ein Employee bekommt aber nicht immer das gleiche Gehalt.

```python 
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate
```

#### Die Payroll Klasse

Wir wollen eine  Übersicht aller Mitarbeiter generieren und die Auszahlungen abbilden.

```python 
class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")

```
#### Das Hauptprogramm

Hier ein Programm, welches sich die eingeführten Klassen zunutze macht und ein praktisches Ergebnis generiert.

```python 
from fulltimeemployee import FulltimeEmployee
from hourlyemployee import HourlyEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()
```


#### Wann man abstrakte Klassen verwendet:

Wie chatGPT es sagen würde:
Wann man abstrakte Klassen rockt
In der Praxis schmeißt man abstrakte Klassen in den Code-Party-Mixer, um den Spaß zwischen mehreren eng miteinander verbundenen Klassen zu teilen. Stell dir das Gehaltsabrechnungsprogramm vor - alle Mitarbeiter-Klassen-Nachkommen tanzen gemeinsam zu dem gleichen "full_name"-Beat.

Zusammenfassung
Abstrakte Klassen sind die Klassen, die keine Instanz-Partygänger sein dürfen.
Das abc-Modul ist sozusagen der Türsteher für die abstrakten Klassen-Party.


## Beispielaufgaben:
- Beispiel 1

```python 
# Python program showing 
# abstract base class work 
from abc import ABC, abstractmethod 


class Animal(ABC): 

	def move(self): 
		pass

class Human(Animal): 

	def move(self): 
		print("I can walk and run") 

class Snake(Animal): 

	def move(self): 
		print("I can crawl") 

class Dog(Animal): 

	def move(self): 
		print("I can bark") 

class Lion(Animal): 

	def move(self): 
		print("I can roar") 

# Driver code 
R = Human() 
R.move() 

K = Snake() 
K.move() 

R = Dog() 
R.move() 

K = Lion() 
K.move() 
```

- Beispiel 2
```python 
# Python program invoking a 
# method using super() 

import abc 
from abc import ABC, abstractmethod 

class R(ABC): 
	def rk(self): 
		print("Abstract Base Class") 

class K(R): 
	def rk(self): 
		super().rk() 
		print("subclass ") 

# Driver code 
r = K() 
r.rk() 
```

## Verständnisfragen:
Was ist eine abstrakte Klasse in Python?

- Eine Klasse, die keine Methoden hat
- Eine Klasse, die nur von anderen Klassen geerbt werden kann
- Eine Klasse, die nicht instanziiert werden kann
- Eine Klasse, die keine Attribute hat

Welches Schlüsselwort wird verwendet, um eine abstrakte Klasse in Python zu deklarieren?

- abstract
- absclass
- abstractclass
- class

Was passiert, wenn man versucht, eine Instanz einer abstrakten Klasse zu erstellen?

- Es wird eine Warnung ausgegeben, aber die Instanz wird erstellt.
- Es wird eine Fehlermeldung ausgegeben und die Instanz wird nicht erstellt.
- Die Instanz wird ohne Fehler erstellt.
- Abstrakte Klassen können nicht instanziiert werden.

Welche der folgenden Aussagen über abstrakte Methoden ist korrekt?

- Abstrakte Methoden müssen immer privat sein.
- Abstrakte Methoden müssen in jeder abgeleiteten Klasse implementiert werden.
- Abstrakte Methoden können in der abstrakten Klasse selbst implementiert werden.
- Abstrakte Methoden sind optional und müssen nicht implementiert werden.

Wie wird eine abstrakte Methode in Python deklariert?

- abstract def method_name():
- def abstract method_name():
- def method_name abstract():
- @abstractmethod def method_name():


Was ist der Hauptzweck von abstrakten Klassen in Python?

- Das Erstellen von Instanzen für bestimmte Klassen
- Das Verbergen von Methodenimplementierungen in Unterklassen
- Das Verhindern von Vererbung in Unterklassen
- Das Erzwingen der Implementierung bestimmter Methoden in Unterklassen

Welches Modul in Python bietet die ABC-Klasse für die Erstellung abstrakter Klassen?

- abstract
- abc
- absclass
- abstractmethod

Wie können Sie in Python sicherstellen, dass alle abstrakten Methoden in einer abgeleiteten Klasse implementiert wurden?

- Durch das Hinzufügen der Deklaration @abstractmethod vor jede Methode
- Durch die Verwendung der Funktion check_abstract_methods()
- Automatisch - Python erzwingt die Implementierung von abstrakten Methoden
- Durch das Hinzufügen des Schlüsselworts implemented vor jede Methode

Was passiert, wenn eine Klasse eine abstrakte Klasse erbt, aber nicht alle abstrakten Methoden implementiert?

- Die Klasse wird eine Fehlermeldung bei der Instanziierung auslösen.
- Python wird automatisch leere Implementierungen für die fehlenden Methoden hinzufügen.
- Die Klasse wird keine Fehlermeldung auslösen, aber Instanzen dieser Klasse können nicht erstellt werden.
- Es gibt keine Auswirkungen, solange die abstrakten Methoden nicht aufgerufen werden.

Welches Schlüsselwort wird verwendet, um eine Methode in einer abstrakten Klasse zu deklarieren, ohne sie als abstrakt zu markieren?

- concrete
- nonabstract
- def
- @nonabstractmethod



## Weiterführende Übungsaufgaben: Chillies

#### Einfache Abstract Class:
Erstellen Sie eine abstrakte Klasse mit dem Namen Shape. Diese Klasse sollte eine abstrakte Methode area haben. Erstellen Sie dann zwei Unterklassen Circle und Rectangle, die diese abstrakte Klasse erben und die Methode area implementieren, um den Flächeninhalt zu berechnen.

#### Abstrakte Methode mit Parameter:
Erweitern Sie die vorherige Übung, indem Sie die abstrakte Methode area in der Klasse Shape einen Parameter für die Farbe der Form akzeptieren lassen. Implementieren Sie diese Funktionalität in den Unterklassen.

##### Bankkonto mit abstrakter Klasse:
Erstellen Sie eine abstrakte Klasse BankAccount, die abstrakte Methoden deposit und withdraw enthält. Erben Sie dann zwei Unterklassen, SavingsAccount und CheckingAccount, und implementieren Sie die abstrakten Methoden entsprechend.

#### Tierhierarchie mit abstrakter Klasse:
Erstellen Sie eine abstrakte Klasse Animal mit abstrakten Methoden speak und move. Erben Sie dann verschiedene Tierklassen wie Dog, Cat und Bird, und implementieren Sie die abstrakten Methoden entsprechend.

##### Formen in einer Liste:
Erstellen Sie eine Liste von verschiedenen Formen (Kreis, Rechteck, usw.), die von der abstrakten Klasse Shape erben. Rufen Sie dann die Methode area für jede Form in der Liste auf und geben Sie die Ergebnisse aus.

#### Benutzerdefinierte Exception mit abstrakter Klasse:
Erstellen Sie eine abstrakte Klasse CustomError mit einer abstrakten Methode handle_error. Erben Sie dann verschiedene benutzerdefinierte Ausnahmeklassen von CustomError und implementieren Sie die Methode handle_error für jede Klasse.

#### Abstrakte Methode in einem Interface:
Erstellen Sie eine Klasse Interface mit einer abstrakten Methode. Erben Sie dann eine andere Klasse Implementation von diesem Interface und implementieren Sie die abstrakte Methode.


TODO: Seperiert das hier doch in eine zweite Datei
