# Lösungen


### 1. **Typisierte Variable**
```python
alter: int = 25
```

### 2. **Typisierte Funktion**
```python
def quadrat(zahl: int) -> int:
    return zahl * zahl
```

### 3. **Mehrere Parameter**
```python
def addiere(a: float, b: float) -> float:
    return a + b
```

### 4. **Optionale Parameter**
```python
from typing import Optional

def begruessen(name: str, alter: Optional[int] = None) -> str:
    return f"Hallo {name}, Alter: {alter}" if alter is not None else f"Hallo {name}"
```

### 5. **Rückgabewert None**
```python
def drucke_hallo(name: str) -> None:
    print(f"Hallo, {name}")
```

### 6. **Listen als Parameter**
```python
def durchschnitt(zahlen: list[int]) -> float:
    return sum(zahlen) / len(zahlen)
```

### 7. **Dictionary als Rückgabewert**
```python
def erstelle_dict(key: str, value: str) -> dict[str, str]:
    return {key: value}
```

### 8. **Komplexe Typen**
```python
def verarbeite_daten(daten: list[dict[str, int]]) -> list[int]:
    return [d["wert"] for d in daten]
```

### 9. **Typisierte Tuples**
```python
def min_max(zahlen: list[int]) -> tuple[int, int]:
    return (min(zahlen), max(zahlen))
```

### 10. **Union Type Hints**
```python
from typing import Union

def id_oder_name(wert: Union[int, str]) -> Union[int, str]:
  return wert
```

