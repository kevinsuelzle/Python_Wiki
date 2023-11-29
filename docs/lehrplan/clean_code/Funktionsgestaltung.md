# Funktionsgestaltung

## Gestaltung von Funktionen

Funktionen sollten

1. kurz sein
2. sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. im Namen das "One Thing" klar beschreiben und in den Parametern ebenfalls sprechende Namen verwenden.
4. keine Nebeneffekte haben.
5. sich nur um eine [Abstraktionsebene](../Abstraktionsebene) kümmern.
6. wenig [Argumente](../Funktionsparameter) haben.
7. echte Fehler verarbeiten und keine Fehlerwerte an die aufrufende Funktion "hoch" geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.

## Testen von Funktionen

Tests sollen zuerst da sein und damit zunächst scheitern.
Der erste Grundsatz des Test Driven Developments (TDD).

Es ist leicht einsehbar, dass eine Funktion mit steigender Anzahl von Parametern immer schwerer zu testen ist.

Binäre Parameter deuten oft darauf hin, dass die Funktion zwei Aufgaben hat anstatt nur einer.

Funktionen mit gemischten Abstraktionsebenen sind schwerer zu testen als mit nur einer Ebene. Höhere Ebenen kommen mit
weniger Parametern aus. Bestes Beispiel dafür ist das Programm selbst, dass als Funktion des Betriebssystems angesehen
werden kann. Es wird meist ohne Parameter aufgerufen.

[zurück](../TheGoodPractices)