# Input und Output

## Die `print`-Funktion
[45min]
Die `print`-Funktion ist eines der grundlegendsten Werkzeuge in Python. Sie wird verwendet, um Werte auf der Konsole 
auszugeben, sei es Text, Zahlen oder den Inhalt von Variablen. Ein einfacher Aufruf von `print` sieht wie folgt aus:
`print("Hallo, Welt!")`. 

Die Verwendung von Formatierungs-Strings, auch bekannt als f-Strings, macht die Arbeit mit der `print`-Funktion sehr
angenehm. Mit f-Strings können wir Werte von Variablen direkt in einen String einfügen, indem wir die Variable in 
geschweifte Klammern `{}` setzen und dem String ein `f` voranstellen.

**Beispiel**: 

```python
name = "Anna"
alter = 30
print(f"Mein Name ist {name} und ich bin {alter} Jahre alt.")
```

Diese Methode der String-Formatierung ist nicht nur effizient, sondern verbessert auch die Lesbarkeit des Codes 
erheblich. Sie ermöglicht es, dynamisch Werte in Strings einzubetten, was besonders nützlich ist, wenn es darum geht, 
komplexe Ausgaben zu generieren oder Benutzerinteraktionen zu gestalten.

## Die `input`-Funktion
[45min]
Die `input`-Funktion in Python ist ein wesentliches Werkzeug, um Benutzereingaben zu erhalten. Sie ermöglicht es einem
Programm, während der Ausführung Daten vom Benutzer zu erfragen. Wenn `input()` aufgerufen wird, hält das Programm an
und wartet auf eine Eingabe von der Tastatur. Nachdem der Benutzer seine Eingabe bestätigt hat (üblicherweise 
durch Drücken der Enter-Taste), gibt `input()` diese Eingabe als String zurück. Optional kann `input()` einen 
String als Argument erhalten, der als Eingabeaufforderung (Prompt) dient. Hier ein einfaches Beispiel:

```python
name = input("Bitte gib deinen Namen ein: ")
print(f"Hallo, {name}!")
```

In diesem Beispiel wird der Benutzer aufgefordert, seinen Namen einzugeben. Nach der Eingabe wird der eingegebene 
Name mit einer Begrüßung ausgegeben. Es ist wichtig zu beachten, dass `input()` immer einen String zurückgibt. Wenn wir 
Zahlen oder andere Datentypen erwarten, müssen wir die Eingabe entsprechend konvertieren:

```python
alter_string = input("Gib dein Alter an: ")
alter = int(alter_string)
```

Damit haben wir bereits eine Menge Grundlagen gelernt, mit denen wir kleine Programme schreiben können. Damit wir das 
nicht nur theoretisch besprechen folgen jetzt erstmal eine Reihe an Übungsaufgaben.


# Aufgaben
[40min]


### 1. **Einfache Ausgabe**: 🌶️
Verwende `print`, um "Hallo Welt" auszugeben. 
### 2. **Variable ausgeben**: 🌶️
Erstelle eine Variable `text` mit dem Wert "Python" und gib sie mit `print` aus.
### 3. **Zahlen ausgeben**: 🌶️
Gib mit `print` die Zahl 100 aus. 
### 4. **Mehrere Argumente**: 🌶️
Verwende `print`, um "Hallo" und "Welt" in derselben Zeile mit einem Leerzeichen dazwischen
auszugeben. 
### 5. **Zeilenende ändern**: 🌶️🌶️
Benutze `print`, um "Hallo", gefolgt von einem "!", ohne Zeilenumbruch auszugeben. 
### 6. **Eingabeaufforderung**: 🌶️🌶️
Verwende `input`, um den Benutzer nach seinem Namen zu fragen und speichere das Ergebnis in
einer Variablen. 
### 7. **Begrüßung**: 🌶️🌶️
Frage den Benutzer mit `input` nach seinem Namen und begrüße ihn anschließend mit `print`. 
### 8. **Numerische Eingabe**: 🌶️🌶️
Frage den Benutzer nach seinem Alter und gib es mit `print` aus. 
### 9. **Kombinierte Eingabe und Ausgabe**: 🌶️🌶️
Frage den Benutzer nach seinem Lieblingsessen und sage ihm mit `print`, dass du 
es auch magst. 
### 10. **Formatierte Ausgabe**: 🌶️🌶️
Frage den Benutzer nach seinem Namen und Alter und gib beides formatiert mit einem
f-String aus. 
### 11. **Mehrere Eingaben**: 🌶️🌶️
Frage den Benutzer nacheinander nach seinem Vornamen und Nachnamen und gib dann den
vollständigen Namen aus. 
### 12. **Rechnung mit Eingabe**: 🌶️🌶️
Bitte den Benutzer, zwei Zahlen einzugeben, addiere sie und gib das Ergebnis aus. 
### 13. **Fehlerkorrektur**: 🌶️🌶️🌶️
Frage den Benutzer nach einer Zahl, konvertiere die Eingabe in einen Integer und fange dabei 
Fehler mit einer Fehlermeldung ab. 
### 14. **Eingabe in Liste speichern**: 🌶️🌶️🌶️
Bitte den Benutzer um drei Lieblingsfarben und speichere sie in einer Liste. Gib 
dann die Liste aus. 
### 15. **Benutzereingaben vergleichen**: 🌶️🌶️🌶️
Frage den Benutzer zweimal nach einem Passwort. Gib eine Erfolgsmeldung aus, 
wenn beide Eingaben übereinstimmen, ansonsten eine Fehlermeldung.

[Lösungen](solutions.md#lösungen)

## Komplex-Aufgaben

### **Aufgabe 1: Persönliche Statistik** 🌶️🌶️🌶️

[45min]

Aufgabenstellung:

- Schreibe ein Python-Programm, das verschiedene persönliche Informationen von einem Benutzer erfragt: Name (String), Alter (Integer), Größe in Metern (Float) und Lieblingsfarben (Liste von Strings).
- Das Programm soll dann diese Informationen jeweils in einem formatierten String ausgeben.
- Für die Lieblingsfarben soll der Benutzer mehrere Farben eingeben können, getrennt durch Kommas.
- Wie können die Farben intern als eine Liste gespeichert werden?
- Das Programm soll die Anzahl der eingegebenen Lieblingsfarben berechnen und ausgeben.

[Lösungen](solutions.md#komplex-aufgabe)