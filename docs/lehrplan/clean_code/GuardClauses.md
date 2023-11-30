$$$ TASK 2 START: stattddessen mit GUARDS arbeiten: 
$$$ Beispiel für Code mit zu vielen if-schachtelunge und gegenbeispiel mit Guard definieren.
$$$ dann 3 Übungsaufgaben, so man verschachtelte if-schahtelungen (gerne auch mit for schleife drinne) in 
guard form bring. hier sollen sie merken, wie nütlich boolsche Algebra ist (z.B. de morgan)

```python
def f(a, b):
    if a > 10 and b > 10:
        return a + b
    else:
        if a <= 10: return a * 2
        if b <= 10: return b * 2
```

Probleme in diesem Code:

1. Funktion und Variablennamen: Die Funktion f und die Variablen a und b sind nicht aussagekräftig.
2. Einzeilige if-Anweisung: Die Verwendung einer einzeiligen if-Anweisung reduziert die Lesbarkeit.
3. Keine Konsistenz: Inkonsistente Verwendung von Einrückungen und Leerzeichen.
4. Logik: Die Logik könnte klarer und effizienter gestaltet werden.

### Verbesserter Code: Beispiel

Jetzt sehen wir uns eine verbesserte Version des obigen Codes an:

```python
def sum_or_double(a, b):
    if a > 10 and b > 10:
        return a + b
    if a <= 10:
        return a * 2
    else:
        return b * 2
```

### Diskussion: Vergleich der Beispiele

**Frage**: Welche Verbesserungen wurden gemacht?

**Frage**: Welche weiteren Verbesserungen könnten an dem verbesserten Code vorgenommen werden?

**Aktivität**: Versuchen Sie, den verbesserten Code weiter zu optimieren und diskutieren Sie Ihre Änderungen.

$$$ End Task 2