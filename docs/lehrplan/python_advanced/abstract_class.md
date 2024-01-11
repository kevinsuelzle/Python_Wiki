# Abstract Class, Dataclass

## Introduction to Python Abstract Classes

In object-oriented programming, an abstract class is a class that cannot be instantiated. However, you can create classes that inherit from an abstract class.

Typically, you use an abstract class to create a blueprint for other classes.

Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract methods.

Python doesn’t directly support abstract classes. But it does offer a module that allows you to define abstract classes.

To define an abstract class, you use the abc (abstract base class) module.

The abc module provides you with the infrastructure for defining abstract base classes.

For example:

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

#### Python abstract class example
Suppose that you need to develop a payroll program for a company.

The company has two groups of employees: full-time employees and hourly employees. The full-time employees get a fixed salary while the hourly employees get paid by hourly wages for their services.

The payroll program needs to print out a payroll that includes employee names and their monthly salaries.

To model the payroll program in an object-oriented way, you may come up with the following classes: Employee, FulltimeEmployee, HourlyEmployee, and Payroll.

To structure the program, we’ll use modules, where each class is placed in a separate module (or file).

The Employee class
The Employee class represents an employee, either full-time or hourly. The Employee class should be an abstract class because there’re only full-time employees and hourly employees, no general employees exist.

The Employee class should have a property that returns the full name of an employee. In addition, it should have a method that calculates salary. The method for calculating salary should be an abstract method.

The following defines the Employee abstract class:

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
#### The FulltimeEmployee class
The FulltimeEmployee class inherits from the Employee class. It’ll provide the implementation for the get_salary() method.

Since full-time employees get fixed salaries, you can initialize the salary in the constructor of the class.

The following illustrates the FulltimeEmployee class:

```python 
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

```

The HourlyEmployee class
The HourlyEmployee also inherits from the Employee class. However, hourly employees get paid by working hours and their rates. Therefore, you can initialize this information in the constructor of the class.

To calculate the salary for the hourly employees, you multiply the working hours and rates.

The following shows the HourlyEmployee class:

```python 
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate
```

#### The Payroll class
The Payroll class will have a method that adds an employee to the employee list and print out the payroll.

Since fulltime and hourly employees share the same interfaces (full_time property and get_salary() method). Therefore, the Payroll class doesn’t need to distinguish them.

The following shows the Payroll class:

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
#### The main program
The following app.py uses the FulltimeEmployee, HourlyEmployee, and Payroll classes to print out the payroll of five employees.

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

When to use abstract classes
In practice, you use abstract classes to share the code among several closely related classes. In the payroll program, all subclasses of the Employee class share the same full_name property.

Summary
Abstract classes are classes that you cannot create instances from.
Use abc module to define abstract classes.


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
