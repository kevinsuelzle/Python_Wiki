# Funktionsparameter

Man unterscheidet aufgrund der Anzahl der Parameter:

1. **nyladic**: Funktionen ohne Argumente sind am einfachsten zu testen.
2. **monadic**: Funktionen mit einem Argument sind noch recht einfach zu testen, da der Wertebereich nur für
   einen Parameter zu erfassen ist und es keine Kombinatorik gibt.
3. **dyadic**: Funktionen mit zwei Argumenten sind schon schwerer in ihrer Totalität zu testen. Je nach Datentyp der
   Parameter ufert der Test aus.
4. **triadic**: gar nicht erst dran denken.
5. **polyadic**: das muss anders gemacht werden.
   

**Aufgabe:** Wie kann man eine Reduktion von Parametern erreichen? Nennen sie Beispiele.

[zurück](../TheGoodPractices)