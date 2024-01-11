# Weitere fortgeschrittene Themen

In dieser Einheit geht es allgeimein um Objektorientiere Programmierung in Python. 
Wir beginnen einfach mit einer Klasse und diskutieren an diesem Beispiel weiterführende Konzepte.

Wiederholiung Klasse, mit Attributen und einer Method. 
Dazu zwei instanzen der Klasse:
```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
```

Class Variables sind Variablen, welche alle Instanzen der Klasse teilen.
Wir wollen eine methode einführen, um das Gehalt der Mitarbeiter zu erhöhen.
```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp2.pay)
```

Für emp1 wurde das Gehalt erhöht, aber nicht für emp2.
Wir wünschen uns sowas wie Employee.apply_raise().
Zudem wäre es auch wünschenswert angeben zu können, um welchen Faktor wir das Gehalt erhöhen wollen.

Dazu erzeugen wir eine Class-Method 

```python 
class Employee:

    raise_amt = 1.04 # class variable
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * raise_amt) # nimmt die Variable als Faktor

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp2.pay)
```

Wir erhalten an der Stelle aber einen Fehler, da raise_amt eine Class Variable ist.

```python 
class Employee:

    raise_amt = 1.04 # class variable
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # nimmt die Class Variable als Faktor ( es ginge auch per Employee.raise_amt )

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
```
Woher kommt die Variable denn genau?
Lasst uns dazu die Instanzen und die Klasse anschauen:

```python 
print(emp1.__dict__)
```
Die Instanz enthält die Variable nicht.

```python 
print(Employee.__dict__)
```
Die Klasse enthält die Variable. Python schaut also zunächst in der Instanz nach, und falls die Variable nicht gefunden wird, wird danach in der Klasse geschaut.
Betrachten wir nun ein entscheidendes Konzept. Wir ändern das Attribut der Klasse, nachdem wir die Instanzen erzeugt haben.

```python 
class Employee:

    raise_amt = 1.04 # class variable
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # nimmt die Class Variable als Faktor ( es ginge auch per Employee.raise_amt )

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
Employee.raise_amt = 1.05
print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
emp1.raise_amt = 1.08
print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
print(amp1.__dict__)
Employee.raise_amt = 1.07
print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
print(amp1.__dict__)
```
Weiter schauen wir uns eine Variable an, die nicht sinnvoll für einzelne Instanzen ist. 
Und zwar wollen wir die Anzahl der erstellten Employees zählen.

```python 
class Employee:

    num_of_emps = 0 # class variable
    raise_amt = 1.04 # class variable
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # nimmt die Class Variable als Faktor ( es ginge auch per Employee.raise_amt )

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)
```

So wie es class variables und instance variables gibt, so gibt es auch class methods und instance methods UND static methods! :D
Üblicherweise beziehen sich methods auf die Instanz der Klasse, welche wir ja mit "self" bezeichnen.

Das heißt die Method fullname ist eine instance method.

Wir wollen jetzt aber eine class method erstellen, nämlich set_raise_amt()
Dazu nehmen wir den Decorator @classmethod

```python 
class Employee:

    num_of_emps = 0 # class variable
    raise_amt = 1.04 # class variable
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # nimmt die Class Variable als Faktor ( es ginge auch per Employee.raise_amt )

    @classmethod
    def set_raise_amt(cls, amount): # anstelle von self wird nun cls verwendet
        cls.raise_amt = amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

```

Klappt wunderbar!
Wir können class methods auch verwenden, um alternaitve Konstruktoren zu bilden. Angenommen, wir müssen neue Mitarbeiter auch aus einem einzelnen String instanziieren,
jedoch wollen wir das als method in der Klasse haben, und nicht jedes mal vorher umwandeln müssen.

```python 
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay) # alte Art und Weise
new_emp_1 = Employee.from_string(emp_str_1) # neue Art und Weise

print(new_emp_1.email)
print(new_emp_1.pay)
```

Jetzt kommen static methods. Anders als class und instance methods, welche cls oder self als Argument entgegennehmen, kommen sie ohne aus.
Sie sind daher wie normale Funktionen, beziehen sich vom Kontext her inhaltlich aber möglicherweise auf die Klasse, weshalb wir sie auch damit verbinden wollen.

```python 
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
```

Ob es sich um einen Werktag handelt ist logisch irgendwie verbunden mit Employees, allerdings hängt das Ergebnis nicht von der Klasse oder einer Instanz ab, weshalb wir 
die Funktion als static method erstellen wollen.


#### Vererbung

Folgender code erzeugt eine Developer class, welche alle Eigenschaften einer Employee class erbt.
```python 
class Developer(Employee): 
    pass

emp_1 =  Developer('Corey', 'Schafer', 50000)
```

Sehr Aufschlussreich ist auch:

```python 
class Developer(Employee): 
    pass

print(help( Developer ) )
```

```python 
class Developer(Employee): 
    raise_amt = 1.10

emp_1 =  Developer('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.apply_raise

print(emp_1.pay)
print(emp_2.pay)
```

Man kann also gezielt Änderungen an Unterklassen vornehmen, ohne die Klasse zu ändern.

Wollen wir nun weitere Eigenschaften (zb Programmiersprache) definieren, welche die ursprüngliche Klasse nicht hat, müssen wir den Developer nun mit einer __init__() method versehen.
Dennoch soll ja alles von Employee geerbt werden. Das sieht dann so aus:

```python 
class Developer(Employee): 
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang): # hier taucht nun das neue prog_lang auf
        super().__init__(first, last, pay) # dadurch müssen wir die Attribute nicht neu definieren, sondern nehmen sie aus der "Oberklasse"
        self.prog_lang = prog_lang

dev_1 =  Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.prog_lang)
```

Auf folgende Art und Weise kann man einen Manager erstellen, der eine Liste der zugeordneten Mitarbeiter enthält.
```python 
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
```

Probiere ruhig etwas mit dem Code herum.


Weiter gibt es noch hilfreiche Funktionen zb isinstance()
```python 
print( isinstance(mgr_1, Manager))
print( isinstance(mgr_1, Employee))
print( isinstance(mgr_1, Developer))
```

```python 
print( issubclass(Manager, Employee))
```

#### special methods
Als Motivation betrachten wir mal folgende beiden Beispiele:
```python 
print( 1 + 2)
print('a' + 'b')
```

Obwohl beide Male ein + verwendet wird, ist das Verhalten in beiden Fällen anders.
Mithilfe von special Methods können wir dieses Verhalten definieren.

Double Underscores werden auch "dunder" genannt.

__unit__() ist auch so eine special method.

```python 
repr(emp_1)
str(emp_1)
```
Wird so verwendet:
```python 
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname() , self.email)



emp_1 = Employee('Corey', 'Schafer', 50000)

print(emo_1) 

print(repr(emp_1)) # ist das gleiche wie print(emp_1.__repr__())
print(str(emp_1)) # ist das gleiche wie print(emp_1.__str__())
```
Die Methods __init__() , __repr__() und __str()__() werden am häufigsten verwendet...

Was genau macht nun print(1+2) ??

```python 
print( int.__add__(1,2))
```
Strings benutzen ihre eigene __add__() method!
```python 
print( str.__add__('a','b'))
```

Wir können uns auch eine eigene für unsere Employees bauen:
```python 
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname() , self.email)

    def __add__(self, other):
        return self.pay + other.pay

    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)
```
Direkt mal ausprobieren! :)

```python 
print( emp_1 + emp_2 )
```

TODO: Dieser Link hier ist nicht anklickbar im Wiki nachher. Du musst das über []() machen. Bitte auch an anderer Stelle prüfen.

Es gibt noch mehr special methods: https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
zB

```python 
print( len('test') )
print( 'test'.__len__())
```

#### Property Decorators

TODO: Bitte schau noch mal mit der Rechtschreibung. Vor allem Groß-/Kleinschreibung trifft häufig auf.

Damit kann man eine method schreiben, den Wert aber wie ein attrubute abrufen.

Zum Beispiel wollen wir email in Employee ersetzen:
```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

```
.... und zwar durch:

```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
    
    def email(): 
        return self.first + '.' + self.last + '@email.com'

emp_1 =  Employee('Corey', 'Schafer', 50000)
```
Jetzt können wir den Wert aber nur als method abrufen:

```python 
print(emp_1.email())
```

Durch den Property Decorator können wir den Wert aber auch als Attribut abrufen:

```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last


    @property
    def email(): 
        return self.first + '.' + self.last + '@email.com'

emp_1 =  Employee('Corey', 'Schafer', 50000)

print(emp_1.email())
```

Ebenso mit fullname:

```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last


    @property
    def email(): 
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 =  Employee('Corey', 'Schafer', 50000)

print(emp_1.email())
```

Ein spannender Fehler:
```python 
emp_1.fullname = 'Britney Spears'
```

Das wird leider nicht funktionieren, denn dafür benötigen wir einen setter!
```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last


    @property
    def email(): 
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self, name):
        print('Deleted name!')
        self.first = None
        self.last = None

emp_1 =  Employee('Corey', 'Schafer', 50000)

```

Jetzt klappt unser Vorhaben:

```python 
emp_1.fullname = 'Britney Spears'

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
```

Weiter gehts mit dem Deleter:
```python 
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last


    @property
    def email(): 
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self, name):
        print('Deleted name!')
        self.first = None
        self.last = None

emp_1 =  Employee('Corey', 'Schafer', 50000)

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname

```

## Beispielaufgaben:
1. Klassen und Instanzmethoden:

Erstellen Sie eine Klasse namens "Auto". Die Klasse sollte eine Instanzmethode namens "fahren" haben, die eine Entfernung als Parameter akzeptiert und ausgibt, dass das Auto diese Entfernung zurückgelegt hat.

Beispiel:

```python 
class Auto:
    def fahren(self, entfernung):
        print(f"Das Auto ist {entfernung} Kilometer gefahren.")
Erstellen Sie dann eine Instanz der Klasse und rufen Sie die Methode "fahren" mit einer beliebigen Entfernung auf.
```

2. Klassenvariable und statische Methode:

Fügen Sie der Klasse "Auto" eine Klassenvariable "anzahl_autos" hinzu, die die Gesamtanzahl der erstellten Autos verfolgt. Erstellen Sie auch eine statische Methode namens "gesamtanzahl_autos", die die aktuelle Anzahl der Autos zurückgibt.

Beispiel:

```python 
class Auto:
    anzahl_autos = 0

    def __init__(self):
        Auto.anzahl_autos += 1

    @staticmethod
    def gesamtanzahl_autos():
        return Auto.anzahl_autos
```

Erstellen Sie dann mehrere Instanzen der Klasse und rufen Sie die statische Methode auf, um die Gesamtanzahl der Autos zu überprüfen.


## Verständnisfrage:
Was ist der Hauptunterschied zwischen einer Klassenmethode und einer Instanzmethode in Python?

- Klassenmethoden haben Zugriff auf Instanzattribute, Instanzmethoden nicht.
- Instanzmethoden haben Zugriff auf Klassenattribute, Klassenmethoden nicht.
- Klassenmethoden haben Zugriff auf Instanzattribute, Instanzmethoden auf Klassenattribute.
- Instanzmethoden und Klassenmethoden haben denselben Zugriff auf Attribute.

Wie wird eine Instanzmethode in Python deklariert?

- Mit dem Schlüsselwort instance vor der Methodendefinition.
- Mit dem Schlüsselwort def gefolgt von der Methode und dem self Parameter.
- Mit dem Schlüsselwort instance gefolgt von der Methode und dem self Parameter.
- Mit dem Schlüsselwort method vor der Methodendefinition.

Welches Schlüsselwort wird in Python verwendet, um eine Klassenmethode zu deklarieren?

- classmethod
- staticmethod
- method
- classfunc

Wie wird der erste Parameter einer Instanzmethode in Python genannt?

- self
- this
- obj
- instance

Was ist der Hauptzweck von statischen Methoden in Python?

- Zugriff auf Klassenattribute
- Zugriff auf Instanzattribute
- Kein Zugriff auf Klassen- oder Instanzattribute
- Zugriff auf globale Variablen

Was ist die Hauptmotivation für die Verwendung von Klassenmethoden in Python?

- Sie können nur innerhalb der Klasse aufgerufen werden.
- Sie können auf Klassenattribute zugreifen, aber nicht auf Instanzattribute.
- Sie ermöglichen die Erstellung von Instanzen der Klasse.
- Sie sind effizienter als Instanzmethoden.

Wie wird eine statische Methode in Python deklariert?

- Mit dem Schlüsselwort staticmethod vor der Methodendefinition.
- Mit dem Schlüsselwort def gefolgt von der Methode und dem self Parameter.
- Mit dem Schlüsselwort static vor der Methodendefinition.
- Mit dem Schlüsselwort method gefolgt von der Methode und dem self Parameter.

Kann eine Instanzmethode auf Klassenattribute zugreifen?

- Ja, immer.
- Nein, niemals.
- Nur wenn die Methode statisch ist.
- Nur wenn die Methode eine Klassenmethode ist.

Wie wird eine Instanzmethode aufgerufen?

- ClassName.method_name()
- instance.method_name()
- method_name(instance)
- method_name(ClassName)

Welche Art von Methoden werden in der Regel für die Initialisierung von Instanzen verwendet?

- Klassenmethoden
- Statische Methoden
- Konstruktoren
- Destruktoren



## Weiterführende Übungsaufgaben: Chillies

#### Vererbung und Überschreibung:

Erstellen Sie eine Unterklasse "Elektroauto", die von der Klasse "Auto" erbt. Fügen Sie eine Instanzmethode "ladezeit" hinzu, die angibt, wie lange das Elektroauto zum Aufladen benötigt.

Beispiel:

```python 

class Elektroauto(Auto):
    def ladezeit(self, stunden):
        print(f"Das Elektroauto benötigt {stunden} Stunden zum Aufladen.")
```

Erstellen Sie eine Instanz der Klasse "Elektroauto" und rufen Sie die Methoden "fahren" und "ladezeit" auf.

Diese Übungsaufgaben sollten Ihnen helfen, Ihr Verständnis für Klassen, Instanzmethoden und statische Methoden in Python zu vertiefen. Wenn Sie weitere Fragen haben oder weitere Übungen wünschen, lassen Sie es mich einfach wissen!


#### Eigenschaften und Setter-Methode:

Erstellen Sie eine Klasse "Person". Jede Person sollte einen Namen und ein Alter haben. Implementieren Sie eine Eigenschaft (Property) namens "alter", die den Zugriff auf das Alter der Person ermöglicht. Erstellen Sie außerdem eine Setter-Methode namens "set_alter", die das Alter überprüft und es nur setzt, wenn es größer als 0 ist.

Beispiel:

```python 
class Person:
    def __init__(self, name, alter):
        self._name = name
        self._alter = alter

    @property
    def alter(self):
        return self._alter

    def set_alter(self, neues_alter):
        if neues_alter > 0:
            self._alter = neues_alter
        else:
            print("Ungültiges Alter. Das Alter muss größer als 0 sein.")
```
