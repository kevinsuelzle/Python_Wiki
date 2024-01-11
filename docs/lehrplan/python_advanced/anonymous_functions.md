# Anonyme Funktionen

#### History
Alonzo Church formalized lambda calculus, a language based on pure abstraction, in the 1930s. Lambda functions are also referred to as lambda abstractions, a direct reference to the abstraction model of Alonzo Church’s original creation.

Lambda calculus can encode any computation. It is Turing complete, but contrary to the concept of a Turing machine, it is pure and does not keep any state.

Functional languages get their origin in mathematical logic and lambda calculus, while imperative programming languages embrace the state-based model of computation invented by Alan Turing. The two models of computation, lambda calculus and Turing machines, can be translated into each another. This equivalence is known as the Church-Turing hypothesis.

Functional languages directly inherit the lambda calculus philosophy, adopting a declarative approach of programming that emphasizes abstraction, data transformation, composition, and purity (no state and no side effects). Examples of functional languages include Haskell, Lisp, or Erlang.

By contrast, the Turing Machine led to imperative programming found in languages like Fortran, C, or Python.

The imperative style consists of programming with statements, driving the flow of the program step by step with detailed instructions. This approach promotes mutation and requires managing state.

The separation in both families presents some nuances, as some functional languages incorporate imperative features, like OCaml, while functional features have been permeating the imperative family of languages in particular with the introduction of lambda functions in Java, or Python.

Python is not inherently a functional language, but it adopted some functional concepts early on. In January 1994, map(), filter(), reduce(), and the lambda operator were added to the language.

```python 
def identity(x):
    return x
```

```python 
lambda x: x
```

```python 
lambda x: x + 1
```

You can apply the function above to an argument by surrounding the function and its argument with parentheses:
```python 
(lambda x: x + 1)(2)

```

```python 
add_one = lambda x: x + 1
add_one(2)
```

```python 
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
```

```python 
lambda x, y: x + y
```

```python 
high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)

high_ord_func(2, lambda x: x + 3)
```

#### No Statements
A lambda function can’t contain any statements. In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception. Here’s an example of adding assert to the body of a lambda:

```python 
(lambda x: assert x == 2)(2) # SyntaxError: invalid syntax
```

#### Type Annotations
```python 
lambda first: str, last: str: first.title() + " " + last.title() -> str
```
#### Arguments
Like a normal function object defined with def, Python lambda expressions support all the different ways of passing arguments. This includes:

Positional arguments
Named arguments (sometimes called keyword arguments)
Variable list of arguments (often referred to as varargs)
Variable list of keyword arguments
Keyword-only arguments
The following examples illustrate options open to you in order to pass arguments to lambda expressions:

```python 
(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1,2,3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
```

#### Decorators
A decorator can be applied to a lambda. Although it’s not possible to decorate a lambda with the @decorator syntax, a decorator is just a function, so it can call the lambda function:

```python 
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
```
add_two(), decorated with @trace on line 11, is invoked with argument 3 on line 15. By contrast, on line 18, a lambda function is immediately involved and embedded in a call to trace(), the decorator. When you execute the code above you obtain the following:

#### Closures:
A lambda can also be a closure. Here’s the same example with a Python lambda function:
```python 
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
```


#### Evaluation Time
In some situations involving loops, the behavior of a Python lambda function as a closure may be counterintuitive. It requires understanding when free variables are bound in the context of a lambda. The following examples demonstrate the difference when using a regular function vs using a Python lambda.

Test the scenario first using a regular function:

```python 
def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
```
In a normal function, n is evaluated at definition time, on line 9, when the function is added to the list: funcs.append(wrap(n)).

Now, with the implementation of the same logic with a lambda function, observe the unexpected behavior:

```python 
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
```
The unexpected result occurs because the free variable n, as implemented, is bound at the execution time of the lambda expression. The Python lambda function on line 4 is a closure that captures n, a free variable bound at runtime. At runtime, while invoking the function f on line 7, the value of n is three.

To overcome this issue, you can assign the free variable at definition time as follows:

```python 
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()
```
Testing Lambdas
Python lambdas can be tested similarly to regular functions. It’s possible to use both unittest and doctest.

unittest

The unittest module handles Python lambda functions similarly to regular functions:

```python 
import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```
LambdaTest defines a test case with three test methods, each of them exercising a test scenario for addtwo() implemented as a lambda function. The execution of the Python file lambda_unittest.py that contains LambdaTest produces the following:

```shell
$ python lambda_unittest.py
test_add_three (__main__.LambdaTest) ... FAIL
test_add_two (__main__.LambdaTest) ... ok
test_add_two_point_two (__main__.LambdaTest) ... ok

======================================================================
FAIL: test_add_three (__main__.LambdaTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "lambda_unittest.py", line 18, in test_add_three
    self.assertEqual(addtwo(3), 6)
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```
As expected, we have two successful test cases and one failure for test_add_three: the result is 5, but the expected result was 6. This failure is due to an intentional mistake in the test case. Changing the expected result from 6 to 5 will satisfy all the tests for LambdaTest.

doctest

The doctest module extracts interactive Python code from docstring to execute tests. Although the syntax of Python lambda functions does not support a typical docstring, it is possible to assign a string to the __doc__ element of a named lambda:

```python 
addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```
The doctest in the doc comment of lambda addtwo() describes the same test cases as in the previous section.

When you execute the tests via doctest.testmod(), you get the following:

```shell
$ python lambda_doctest.py
Trying:
    addtwo(2)
Expecting:
    4
ok
Trying:
    addtwo(2.2)
Expecting:
    4.2
ok
Trying:
    addtwo(3) # Should fail
Expecting:
    6
**********************************************************************
File "lambda_doctest.py", line 16, in __main__.addtwo
Failed example:
    addtwo(3) # Should fail
Expected:
    6
Got:
    5
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   1 of   3 in __main__.addtwo
3 tests in 2 items.
2 passed and 1 failed.
***Test Failed*** 1 failures.
```

#### Lambda Expression Abuses
Several examples in this article, if written in the context of professional Python code, would qualify as abuses.

If you find yourself trying to overcome something that a lambda expression does not support, this is probably a sign that a normal function would be better suited. The docstring for a lambda expression in the previous section is a good example. Attempting to overcome the fact that a Python lambda function does not support statements is another red flag.

The next sections illustrate a few examples of lambda usages that should be avoided. Those examples might be situations where, in the context of Python lambda, the code exhibits the following pattern:

It doesn’t follow the Python style guide (PEP 8)
It’s cumbersome and difficult to read.
It’s unnecessarily clever at the cost of difficult readability.


#### Raising an Exception
Trying to raise an exception in a Python lambda should make you think twice. There are some clever ways to do so, but even something like the following is better to avoid:

```python 
def throw(ex): raise ex
(lambda: throw(Exception('Something bad happened')))()
```
Because a statement is not syntactically correct in a Python lambda body, the workaround in the example above consists of abstracting the statement call with a dedicated function throw(). Using this type of workaround should be avoided. If you encounter this type of code, you should consider refactoring the code to use a regular function.

#### Cryptic Style
As in any programming languages, you will find Python code that can be difficult to read because of the style used. Lambda functions, due to their conciseness, can be conducive to writing code that is difficult to read.

The following lambda example contains several bad style choices:

```python 
(lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
```
The underscore (_) refers to a variable that you don’t need to refer to explicitly. But in this example, three _ refer to different variables. An initial upgrade to this lambda code could be to name the variables:

```python 
(lambda some_list: list(map(lambda n: n // 2, some_list)))([1,2,3,4,5,6,7,8,9,10])

```
Admittedly, it’s still difficult to read. By still taking advantage of a lambda, a regular function would go a long way to render this code more readable, spreading the logic over a few lines and function calls:

```python 
def div_items(some_list):
    div_by_two = lambda n: n // 2
    return map(div_by_two, some_list)

list(div_items([1,2,3,4,5,6,7,8,9,10]))
```
This is still not optimal but shows you a possible path to make code, and Python lambda functions in particular, more readable. In Alternatives to Lambdas, you’ll learn to replace map() and lambda with list comprehensions or generator expressions. This will drastically improve the readability of the code.

#### Python Classes
You can but should not write class methods as Python lambda functions. The following example is perfectly legal Python code but exhibits unconventional Python code relying on lambda. For example, instead of implementing __str__ as a regular function, it uses a lambda. Similarly, brand and year are properties also implemented with lambda functions, instead of regular functions or decorators:

```python 
class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'  # 1: error E731

    honk = lambda self: print('Honk!')     # 2: error E731
```

Running a tool like flake8, a style guide enforcement tool, will display the following errors for __str__ and honk:

```shell
E731 do not assign a lambda expression, use a def
```
Although flake8 doesn’t point out an issue for the usage of the Python lambda functions in the properties, they are difficult to read and prone to error because of the usage of multiple strings like '_brand' and '_year'.

Proper implementation of __str__ would be expected to be as follows:

```python 
def __str__(self):
    return f'{self.brand} {self.year}'
```
brand would be written as follows:

```python 
@property
def brand(self):
    return self._brand

@brand.setter
def brand(self, value):
    self._brand = value
```
As a general rule, in the context of code written in Python, prefer regular functions over lambda expressions. Nonetheless, there are cases that benefit from lambda syntax, as you will see in the next section.


#### Appropriate Uses of Lambda Expressions
Lambdas in Python tend to be the subject of controversies. Some of the arguments against lambdas in Python are:

Issues with readability
The imposition of a functional way of thinking
Heavy syntax with the lambda keyword
Despite the heated debates questioning the mere existence of this feature in Python, lambda functions have properties that sometimes provide value to the Python language and to developers.

The following examples illustrate scenarios where the use of lambda functions is not only suitable but encouraged in Python code.

#### Classic Functional Constructs
Lambda functions are regularly used with the built-in functions map() and filter(), as well as functools.reduce(), exposed in the module functools. The following three examples are respective illustrations of using those functions with lambda expressions as companions:


```python 
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
```
You may have to read code resembling the examples above, albeit with more relevant data. For that reason, it’s important to recognize those constructs. Nevertheless, those constructs have equivalent alternatives that are considered more Pythonic. In Alternatives to Lambdas, you’ll learn how to convert higher-order functions and their accompanying lambdas into other more idiomatic forms.

#### Key Functions
Key functions in Python are higher-order functions that take a parameter key as a named argument. key receives a function that can be a lambda. This function directly influences the algorithm driven by the key function itself. Here are some key functions:

sort(): list method
sorted(), min(), max(): built-in functions
nlargest() and nsmallest(): in the Heap queue algorithm module heapq
Imagine that you want to sort a list of IDs represented as strings. Each ID is the concatenation of the string id and a number. Sorting this list with the built-in function sorted(), by default, uses a lexicographic order as the elements in the list are strings.

To influence the sorting execution, you can assign a lambda to the named argument key, such that the sorting will use the number associated with the ID:

```python 
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lexicographic sort

sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)
```

#### UI Frameworks
UI frameworks like Tkinter, wxPython, or .NET Windows Forms with IronPython take advantage of lambda functions for mapping actions in response to UI events.

The naive Tkinter program below demonstrates the usage of a lambda assigned to the command of the Reverse button:

```python 
import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda: label.configure(text=label.cget("text")[::-1]),
)
button.grid(column=0, row=1)
window.mainloop()
```

#### Python Interpreter
When you’re playing with Python code in the interactive interpreter, Python lambda functions are often a blessing. It’s easy to craft a quick one-liner function to explore some snippets of code that will never see the light of day outside of the interpreter. The lambdas written in the interpreter, for the sake of speedy discovery, are like scrap paper that you can throw away after use.

timeit
In the same spirit as the experimentation in the Python interpreter, the module timeit provides functions to time small code fragments. timeit.timeit() in particular can be called directly, passing some Python code in a string. Here’s an example:

```python 
from timeit import timeit
timeit("factorial(999)", "from math import factorial", number=10)
```
When the statement is passed as a string, timeit() needs the full context. In the example above, this is provided by the second argument that sets up the environment needed by the main function to be timed. Not doing so would raise a NameError exception.

Another approach is to use a lambda:

```python 
from math import factorial
timeit(lambda: factorial(999), number=10)
```
This solution is cleaner, more readable, and quicker to type in the interpreter. Although the execution time was slightly less for the lambda version, executing the functions again may show a slight advantage for the string version. The execution time of the setup is excluded from the overall execution time and shouldn’t have any impact on the result.

#### Monkey Patching
For testing, it’s sometimes necessary to rely on repeatable results, even if during the normal execution of a given software, the corresponding results are expected to differ, or even be totally random.

Let’s say you want to test a function that, at runtime, handles random values. But, during the testing execution, you need to assert against predictable values in a repeatable manner. The following example shows how, with a lambda function, monkey patching can help you:

```python 
from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex
    function during testing.
    """
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_token():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_token()
```
A context manager helps with insulating the operation of monkey patching a function from the standard library (secrets, in this example). The lambda function assigned to secrets.token_hex() substitutes the default behavior by returning a static value.

This allows testing any function depending on token_hex() in a predictable fashion. Prior to exiting from the context manager, the default behavior of token_hex() is reestablished to eliminate any unexpected side effects that would affect other areas of the testing that may depend on the default behavior of token_hex().

Unit test frameworks like unittest and pytest take this concept to a higher level of sophistication.

With pytest, still using a lambda function, the same example becomes more elegant and concise :

```python 
import secrets

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_token(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"
```
With the pytest monkeypatch fixture, secrets.token_hex() is overwritten with a lambda that will return a deterministic value, feedfacecafebeef, allowing to validate the test. The pytest monkeypatch fixture allows you to control the scope of the override. In the example above, invoking secrets.token_hex() in subsequent tests, without using monkey patching, would execute the normal implementation of this function.

Executing the pytest test gives the following result:

```shell 
$ pytest test_token.py -v
============================= test session starts ==============================
platform linux -- Python 3.7.2, pytest-4.3.0, py-1.8.0, pluggy-0.9.0
cachedir: .pytest_cache
rootdir: /home/andre/AB/tools/bpython, inifile:
collected 1 item

test_token.py::test_gen_token PASSED                                     [100%]

=========================== 1 passed in 0.01 seconds ===========================
```

#### Are Lambdas Pythonic or Not?
PEP 8, which is the style guide for Python code, reads:

Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier. (Source)

This strongly discourages using lambda bound to an identifier, mainly where functions should be used and have more benefits. PEP 8 does not mention other usages of lambda. As you have seen in the previous sections, lambda functions may certainly have good uses, although they are limited.

A possible way to answer the question is that lambda functions are perfectly Pythonic if there is nothing more Pythonic available. I’m staying away from defining what “Pythonic” means, leaving you with the definition that best suits your mindset, as well as your personal or your team’s coding style.

Beyond the narrow scope of Python lambda, How to Write Beautiful Python Code With PEP 8 is a great resource that you may want to check out regarding code style in Python.

#### Conclusion
You now know how to use Python lambda functions and can:

Write Python lambdas and use anonymous functions
Choose wisely between lambdas or normal Python functions
Avoid excessive use of lambdas
Use lambdas with higher-order functions or Python key functions
If you have a penchant for mathematics, you may have some fun exploring the fascinating world of lambda calculus.

Python lambdas are like salt. A pinch in your spam, ham, and eggs will enhance the flavors, but too much will spoil the dish.


## Beispielaufgaben:

#### Beispiel 1: Überprüfen ob eine Zahl gerade ist

```python
even = lambda x: x%2==0
```

```python
even(3)
```

```python
even(4)
```
#### Beispiel 2: Erstes Zeichen eines Strings ausgeben

```python
erstes = lambda s: s[0]
```

```python
erstes('Hallo')
```


## Verständnisfragen:
Was ist eine Lambda-Funktion in Python?

- Eine spezielle Funktion für mathematische Berechnungen
- Eine anonyme Funktion
- Eine Funktion, die nur für Listen verwendet wird
- Eine Funktion, die nur in Klassen definiert werden kann

Wie wird eine Lambda-Funktion in Python erstellt?

- Mit dem Schlüsselwort lambda gefolgt von Argumenten und einem Ausdruck
- Mit dem Schlüsselwort def gefolgt von Funktionennamen und Argumenten
- Mit dem Schlüsselwort function gefolgt von Argumenten und einem Ausdruck
- Mit dem Schlüsselwort anonymous gefolgt von Argumenten und einem Ausdruck

Welche der folgenden Aussagen zur Lambda-Funktion ist korrekt?

- Lambda-Funktionen können mehrere Ausdrücke enthalten
- Lambda-Funktionen können nicht als Argumente an andere Funktionen übergeben werden
- Lambda-Funktionen können keine Variablen referenzieren, die außerhalb der Funktion definiert sind
- Lambda-Funktionen sind für komplexe Berechnungen nicht geeignet

Wofür werden Lambda-Funktionen häufig verwendet?

- Zur Definition von Klassen
- Zur Berechnung von komplexen mathematischen Ausdrücken
- Zur Erstellung von anonymen Funktionen für kurzzeitige Verwendung
- Zur Implementierung von Schleifen in Python

Wie können Lambda-Funktionen in Kombination mit der Funktion map verwendet werden?

- Zur Definition von benutzerdefinierten Sortieralgorithmen
- Zur Anwendung einer Funktion auf jedes Element einer Liste
- Zur Erstellung von Bedingungen in Schleifen
- Zur Umwandlung von Strings in Zahlen


Wie sieht die Syntax einer einfachen Lambda-Funktion aus?

- function: arguments => expression
- lambda {arguments}: {expression}
- lambda arguments: expression
- def lambda(arguments, expression)

Welche der folgenden Funktionen akzeptiert eine Lambda-Funktion als Argument?

- sort()
- sum()
- filter()
- append()

Was passiert, wenn eine Lambda-Funktion mehrere Argumente hat, aber nur eines beim Aufruf übergeben wird?

- Die Lambda-Funktion gibt einen Fehler aus.
- Die Lambda-Funktion akzeptiert nur ein Argument.
- Die Lambda-Funktion gibt den Wert des übergebenen Arguments aus.
- Die Lambda-Funktion ignoriert das übergebene Argument.

Welcher Ausdruck ist äquivalent zur Lambda-Funktion lambda x, y: x + y?

- def add(x, y): return x + y
- def add(x, y): x + y
- def add(x, y) => x + y
- def add(x, y) { return x + y }

Wie wird die Funktion reduce aus dem Modul functools mit einer Lambda-Funktion verwendet?

- reduce(lambda x, y: x + y, sequence)
- functools.reduce(lambda x, y: x + y, sequence)
- sequence.reduce(lambda x, y: x + y)
- sequence(functools.lambda x, y: x + y)



## Beispielaufgaben

#### Beispielaufgabe 1: Einen String umkehren

```python
umk = lambda s: s[::-1]
```

```python
umk('Hallo')
```

### Beispielaufgabe 2: Genau wie bei normalen Funktionen können wir mehr als einen Parameter aufnehmen

```python
add = lambda x,y: x+y
```

```python
add(3,4)
```

## Weiterführende Übungsaufgaben: Chillies

#### Addition mit Lambda:
Schreiben Sie eine Lambda-Funktion, die zwei Zahlen addiert.

#### Quadratzahlen mit Lambda:
Erstellen Sie eine Lambda-Funktion, die das Quadrat einer Zahl berechnet.

#### Filtern von geraden Zahlen:
Verwenden Sie filter und eine Lambda-Funktion, um eine Liste von ganzen Zahlen zu erstellen, die nur gerade Zahlen enthält.

#### Wortlänge sortieren:
Gegeben ist eine Liste von Wörtern. Verwenden Sie sorted und eine Lambda-Funktion, um die Liste nach der Länge der Wörter zu sortieren.

#### Potenzen mit Lambda:
Schreiben Sie eine Lambda-Funktion, die eine Zahl und einen Exponenten akzeptiert und die Potenz berechnet.

#### Umwandlung in Großbuchstaben:
Verwenden Sie map und eine Lambda-Funktion, um eine Liste von Wörtern in Großbuchstaben umzuwandeln.

#### Addition von drei Zahlen:
Schreiben Sie eine Lambda-Funktion, die drei Zahlen addiert.

#### Filtern von negativen Zahlen:
Verwenden Sie filter und eine Lambda-Funktion, um eine Liste von ganzen Zahlen zu erstellen, die nur negative Zahlen enthält.

#### Maximum von zwei Zahlen:
Schreiben Sie eine Lambda-Funktion, die das Maximum von zwei Zahlen zurückgibt.

#### Anonyme Funktionen in einer Liste:
Gegeben ist eine Liste von Lambda-Funktionen. Verwenden Sie map, um eine Liste von Ergebnissen zu erstellen, indem Sie jeder Funktion eine Zahl übergeben.
