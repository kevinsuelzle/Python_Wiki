# Lösung


## Lists, Tupels, Sets, Dictionaries

Hier sind die Lösungen zu den gestellten Übungsaufgaben zu Listen, Tupeln, Sets und Dictionaries in Python:

1. **Liste erstellen**

```python
liste = [i for i in range(1, 11)]
```

2. **Tupel zu Liste**

```python
tupel = (1, 2, 3)
liste = list(tupel)
```


5. **Liste invertieren**

```python
liste = liste[::-1]
```

6. **Tupel aus Listen**

```python
tupel = tuple(liste[:3])
```


9. **Liste von Tupeln**

```python
liste_von_tupeln = [(i, i ** 2) for i in range(1, 6)]
```

1

12. **Listenelemente filtern**

```python
gerade_zahlen = [i for i in liste if i % 2 == 0]
```

13. **Schlüssel aus Dictionary entfernen**

```python
del dictionary["a"]
```

15. **Duplikate aus Liste entfernen**

```python
liste_ohne_duplikate = list(set([1, 2, 2, 3, 3, 4, 4, 5]))
```