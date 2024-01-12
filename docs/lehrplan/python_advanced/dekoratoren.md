# Dekoratoren (Memoisation)


## Theorie:

First class function. Das konzept erlaubt es uns Funktionen wie jedes andere Objekt in Python zu betrachten.

- Wir können Funktionen als Argumente in anderen Funktionen einsetzen.
- Wir können uns Funktionen als output einer Funktion ausgeben lassen.
- Wir können Funktionen zu Variablen assignen.

Closures: 

- Erlauben es uns innere Funktionen mit Variablen aus dem Scope der äußeren Funktion auszustatten.

```python 
def outer_function():
    message = 'Hi' # local variable kann verändert werden

    def inner_function():
        print(message)

    return inner_function()

outer_function()
```

Als Nächstes lassen wir uns die Funktion ausgeben und nicht die ausgeführte Funktion. (Klammern wegnehmen)

```python 
def outer_function():
    message = 'Hi' # local variable kann verändert werden

    def inner_function():
        print(message)

    return inner_function

my_func = outer_function()

my_func()
my_func()
my_func()
```

Die Funktion erinnert sich an die local variable selbst nachdem die Funktion ausgeführt wurde. (Das ist es was ein Closure ist.)

```python 
def outer_function(msg):
    message = msg # local variable kann verändert werden

    def inner_function():
        print(message)

    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
```
Vereinfachen:

```python 
def outer_function(msg):

    def inner_function():
        print(msg)

    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
```

Das war eine kurze Wiederholung von Closures. Unser Thema Decorators ist sehr nahe an dem, was wir grade gemacht haben.

Ein Decorator ist eine Funktion, die eine andere Funktion als Argument nimmt, Funktionalitäten hinzufügt, und dann die veränderte, ursprüngliche funktion ausgibt.
(Das alles ohne den Source Code der ursprünglichen Funktion zu verändern)

Mit dem Beispiel von oben kann man jetzt einfach nur die Namen verändern:

```python 
def decorator_function(msg): 

    def wrapper_function():
        print(msg)

    return wrapper_function
```

An dieser Stelle wollen wir jetzt aber statt der Message eine andere Funktion einstzen. Dann haben wir einen Decorator! Yeah!

```python 
def decorator_function(original_function): 

    def wrapper_function():
        return original_function()

    return wrapper_function
```
Konkretes Beispiel:

```python 
def display():
    print('Display function ran!')

def decorator_function(original_function): 

    def wrapper_function():
        return original_function()

    return wrapper_function

decorated_display = decorator_function(display)

decorated_display()
```
Das Beispiel macht nichts tolles, also kommt jetzt die Veränderung rein, die wir machen wollen.

```python 
def display():
    print('Display function ran!')

def decorator_function(original_function): 

    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

decorated_display = decorator_function(display)

decorated_display()
```

Etwas mehr pythonic:

```python 
def decorator_function(original_function): 

    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

@decorator_function # <--- neue Schreibweise
def display():
    print('Display function ran!')

# display = decorator_function(display) <--- Der Teil wird durch die neue Schreibweise ersetzt.

display()
```

Einfacher zu lesen, besonders wenn man mehrere Decorators verkettet. (werden wir später sehen)

```python 
def decorator_function(original_function): 

    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

@decorator_function 
def display():
    print('Display function ran!')

@decorator_function 
def display_info(name, age):
    print('Display function ran with arguments ({}, {})'.format(name, age))

display_info('John',30)
```

Die Funktion spuckt uns einen Fehler aus. Also müssen wir noch *args und **kwargs hinzufügen.

```python 
def decorator_function(original_function): 

    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)

    return wrapper_function

@decorator_function 
def display():
    print('Display function ran!')

@decorator_function 
def display_info(name, age):
    print('Display function ran with arguments ({}, {})'.format(name, age))

display_info('John',30)

display()
```

Es folgen ein paar praktische Anwendungen von Decorators:

```python 
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger 
def display_info(name, age):
    print('Display function ran with arguments ({}, {})'.format(name, age))

display_info('John',30)

```

```python 
def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer 
def display_info(name, age):
    print('Display function ran with arguments ({}, {})'.format(name, age))

display_info('John',30)
```

Beispiel aus der library flask:

```python 
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def about():
    return "About Page"

if __name__ == "__main__":
    app.run()
```

Wir beginnen mit einem üblichen Decorator.

```python 
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Executed Before', original_function.__name__)
        result = original_function(*args, **kwargs)
        print('Executed After', original_function.__name__, '\n')
        return result
    return wrapper_function


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)
```

Nun wollen wir, dass zusätzlich dem Decorator ein Prefix mitgegeben werden kann.

```python 
def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)
```


## Beispielaufgabe

#### Decorating Functions with Parameters
The above decorator was simple and it only worked with functions that did not have any parameters. What if we had functions that took in parameters like:

```python 
def divide(a, b):
    return a/b
```

This function has two parameters, a and b. We know it will give an error if we pass in b as 0.

Now let's make a decorator to check for this case that will cause the error.

```python 
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)
```



## Verständnisfragen:

Was ist ein Decorator in Python?

- Ein grafisches Element zur Verschönerung von Benutzeroberflächen.
- Eine Funktion, die eine andere Funktion modifiziert oder erweitert.
- Ein Datentyp für die Speicherung von dekorativen Mustern.
- Ein spezielles Modul für die Verwaltung von Stildetails.

Wie wird ein Decorator in Python definiert?

- Mit dem Schlüsselwort "decorate".
- Mit dem Schlüsselwort "modifier".
- Mit dem Symbol "@" gefolgt von der Decorator-Funktion.
- Mit dem Symbol "#" gefolgt von der Decorator-Funktion.

Welchen Zweck erfüllt ein Decorator?

- Änderung der Farben in einer Python-Anwendung.
- Verbesserung der Lesbarkeit von Code.
- Hinzufügen von Bildern zu Funktionen.
- Beschleunigung der Ausführungsgeschwindigkeit.

Was passiert, wenn mehrere Decorators auf eine Funktion angewendet werden?

- Nur der letzte Decorator wird angewendet.
- Alle Decorators werden in der Reihenfolge angewendet, in der sie deklariert wurden.
- Decorators können nicht kombiniert werden.
- Nur der erste Decorator wird angewendet.

Welche Syntax wird verwendet, um einen Decorator mit Argumenten zu definieren?

- @decorator(argument)
- @decorator(argument=)
- @decorator(argument):
- @decorator und Argumente als separate Funktion.


Was ist die Hauptfunktion eines Decorators in Python?

- Die Verbesserung der grafischen Benutzeroberfläche.
- Die Änderung des Datenflusses in einer Funktion.
- Die Erstellung von dekorativen Mustern für den Code.
- Die automatische Dokumentation von Funktionen.

Wie wird ein Decorator auf eine Funktion angewendet?

- Durch Hinzufügen des Decorators vor das Schlüsselwort "def".
- Durch Deklaration des Decorators nach dem Funktionsnamen.
- Durch Voranstellen des Symbols "@" vor den Funktionskopf.
- Durch Einfügen des Decorators nach der Rückgabeanweisung.

Welche der folgenden Aussagen ist korrekt?

- Decorators können nur auf Funktionen angewendet werden.
- Decorators können nur von eingebauten Python-Funktionen verwendet werden.
- Decorators können auf Funktionen und Klassen angewendet werden.
- Decorators können nicht innerhalb von Schleifen verwendet werden.

Was ist die Rolle des functools.wraps-Decorators?

- Er fügt Funktionen Wrapping-Elemente hinzu.
- Er erleichtert das Schreiben von komplexen Decorators.
- Er stellt sicher, dass der ursprüngliche Funktionsname und die Dokumentation beibehalten werden.
- Er dekoriert Funktionen automatisch mit zusätzlichen Argumenten.

In welcher Reihenfolge werden mehrere Decorators auf eine Funktion angewendet?

- Von innen nach außen.
- Von außen nach innen.
- Zufällige Reihenfolge.
- Alphabetische Reihenfolge der Decorator-Namen.




## Weiterführende Übungsaufgaben: Chillies


#### Aufgabe 1
Write a Python program to create a decorator that logs the arguments and return value of a function.

The decorator in this code logs the function name, arguments, and return value whenever the decorated function is called.

#### Aufgabe 2
Write a Python program to create a decorator to convert the return value of a function to a specified data type.

#### Aufgabe 3
Write a Python program that implements a decorator to add logging functionality to a function.

Logging functionality refers to the capability of recording and storing information about program execution. It allows you to capture significant events, messages, and errors that occur during code execution.

