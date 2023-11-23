# Einführung in Clean Code

## Lernziele: Einführung

- **Grobziel**: Verstehen, was Clean Code ist und warum er wichtig ist.
- **Richtziel**: Erkennen der Merkmale von Clean Code.
- **Feinziele**:
    - Definieren von Clean Code.
    - Diskutieren der Bedeutung von Clean Code in der Softwareentwicklung.

## Was ist Clean Code?

Clean Code bezieht sich auf einen Software-Code, der leicht zu verstehen und zu ändern ist. Der Code sollte klar, präzise und so einfach wie möglich sein. Ein gut geschriebener Code kann von anderen Entwicklern leicht gelesen und bearbeitet werden, was für die langfristige Wartbarkeit und Skalierbarkeit von Softwareprojekten entscheidend ist.

### Merkmale von Clean Code:

- **Lesbarkeit**: Der Code sollte für andere Entwickler leicht verständlich sein.
- **Einfachheit**: Vermeidung unnötiger Komplexität; einfache Lösungen sind vorzuziehen.
- **Wartbarkeit**: Leicht zu ändern und zu erweitern.
- **Effizienz**: Der Code sollte nicht nur funktionieren, sondern auch effizient sein.

## Warum ist Clean Code wichtig?

1. **Wartung**: Der Großteil der Kosten eines Softwareprojekts entsteht in der Wartungsphase. Sauberer Code erleichtert die Wartung erheblich.
2. **Teamarbeit**: In einem Team ist es wichtig, dass jeder den Code der anderen verstehen und daran arbeiten kann.
3. **Qualität**: Sauberer Code führt zu weniger Fehlern und höherer Softwarequalität.
4. **Skalierbarkeit**: Projekte sind einfacher zu erweitern und anzupassen, wenn der zugrunde liegende Code sauber ist.

## Diskussion: Bedeutung von Clean Code

- **Frage**: Warum glauben Sie, ist Clean Code besonders in großen Projekten wichtig?
- **Aktivität**: Finden Sie Beispiele für schlechten Code in Ihrem eigenen Projekt und diskutieren Sie, wie dieser verbessert werden könnte.

### Beispiel für Schlechten und Guten Code in Python

#### Schlechter Code: Beispiel

Betrachten Sie das folgende Python-Beispiel, das einige typische Merkmale von schlechtem Code aufweist:

```python
def f(a, b):
    if a > 10 and b > 10: return a + b
    else:
        if a <= 10: return a * 2
        if b <= 10: return b * 2
```
Probleme in diesem Code:

1. Funktion und Variablennamen: Die Funktion f und die Variablen a und b sind nicht aussagekräftig.
2. Einzeilige if-Anweisung: Die Verwendung einer einzeiligen if-Anweisung reduziert die Lesbarkeit.
3. Keine Konsistenz: Inkonsistente Verwendung von Einrückungen und Leerzeichen.
4. Logik: Die Logik könnte klarer und effizienter gestaltet werden.

#### Verbesserter Code: Beispiel

Jetzt sehen wir uns eine verbesserte Version des obigen Codes an:

```python
def sum_or_double(a, b):
    if a > 10 and b > 10:
        return a + b
    elif a <= 10:
        return a * 2
    else:
        return b * 2
```
Verbesserungen:

1. Klare Funktions- und Variablennamen: Die Funktion sum_or_double und die Variablen a und b sind jetzt aussagekräftiger.
2. Lesbarkeit: Die if-Anweisungen sind klar und konsistent formatiert.
3. Konsistenz: Einheitliche Einrückungen und Leerzeichen verbessern die Lesbarkeit.
4. Logik: Die Logik ist jetzt einfacher und direkter.

Diskussion: Vergleich der Beispiele

**Frage**: Welche weiteren Verbesserungen könnten an dem verbesserten Code vorgenommen werden?

**Aktivität**: Versuchen Sie, den verbesserten Code weiter zu optimieren und diskutieren Sie Ihre Änderungen.

## Zusammenfassung

In dieser Einführung haben wir die Grundlagen von Clean Code und seine Bedeutung in der Softwareentwicklung besprochen. Die Fähigkeit, sauberen und effizienten Code zu schreiben, ist eine wesentliche Fähigkeit für jeden Entwickler.

---

