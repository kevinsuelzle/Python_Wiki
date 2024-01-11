# Guard Clauses
[15min]

```python
def can_drink(person):
    if person.age is not None:
        if person.age < 18:
            print('Nope 👶')
        elif person.age < 21:
            print('Not in the US 😨')
        else:
            print('Yes 🍺')
    else:
        print('You are not a Person 👽')
```

Der Code ist durch die Verschachtelungen schwer zu verstehen. Durch die ausschließliche Nutzung des `if`-Schlüsselworts
und den Verzicht auf `elif` und `else` lässt er sich tatsächlich vereinfachen:

```python
def can_drink(person):
    if person.age is None:
        print('You are not a Person 👽')
    if person.age < 18:
        print('Nope 👶')
    if person.age < 21:
        print('Not in the US 😨')
    print('Yes 🍺')
```

Diese Technik ausschließlich `if`-Statements zu verwenden wird **Guard Clauses** genannt.

### 1. Aufgabe 🌶🌶 
[15min]
Wandeln Sie den Code so um, dass Guard Clauses verwendet werden. Wie viele Testfälle benötigt der Code mindestens?

```python
def calculate_discount(price, discount, is_member):
    if is_member:
        if discount > 10:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if discount > 20:
            return price * 0.85
        else:
            return price
```

[Lösung](solution.md#lsung-aufgabe-1)

### 2. Aufgabe 🌶🌶
[15min]
Wandeln Sie den Code so um, dass Guard Clauses verwendet werden. Wie viele Testfälle benötigt der Code mindestens?

```python
def check_access(age, has_ticket, special_pass):
    if age > 18:
        if has_ticket:
            return "Access granted"
        else:
            return "No ticket"
    else:
        if special_pass:
            return "Access granted"
        else:
            return "Access denied"
```

[Lösung](solution.md#lsung-aufgabe-2)

### 3. Aufgabe 🌶🌶
[15min]
Wandeln Sie den Code so um, dass Guard Clauses verwendet werden. Wie viele Testfälle benötigt der Code mindestens?

```python
def user_permission_check(role, age, account_status):
    if role == "admin":
        if age >= 18:
            if account_status == "active":
                return "Zugriff gewährt"
            else:
                return "Account inaktiv"
        else:
            return "Zu jung"
    else:
        if account_status == "active":
            if age >= 18:
                return "Zugriff eingeschränkt"
            else:
                return "Zugriff verweigert"
        else:
            return "Account inaktiv"
```

[Lösung](solution.md#lsung-aufgabe-3)
