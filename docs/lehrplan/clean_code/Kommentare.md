# Kommentare

```python
def calc(x):
    return x * 2 + 5
```

Mal abgesehen von der [Benennung](../Benennungskonventionen) sind Kommentare sehr wichtig, um die Absicht hinter dem
Code zu erklären, insbesondere in Fällen, in denen die Logik nicht offensichtlich ist.

```python
"""
Sammlung von Funktionen um ....    
"""


def calculate_adjusted_value(x):
    """
    Berechnet den angepassten Wert durch Verdopplung und Addition von 5
    
    oder
    
    Die binäre Verschiebung um ein Bit nach links wird hier durch die Multiplikation mit 2 erreicht. 
    Der Offset von 5 Bytes ist technisch erforderlich weil ...
    """
    return x * 2 + 5
```

[zurück](../TheGoodPractices)
