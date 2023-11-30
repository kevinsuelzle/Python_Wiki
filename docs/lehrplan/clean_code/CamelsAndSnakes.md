# Kamele und Schlangen

Ein Ausflug in Benennungskonventionen.

## CamelCase

CamelCase ist eine Benennungskonvention, bei der jedes neue Wort innerhalb eines Identifikators mit einem Großbuchstaben beginnt. Es gibt zwei Hauptvarianten:

### UpperCamelCase (oder PascalCase)
- Jedes Wort, einschließlich des ersten, beginnt mit einem Großbuchstaben.
- Häufig verwendet in Sprachen wie Java und C# für Klassen- und Typnamen.
- Beispiel: `ProduktListe`, `KundenDatenbank`

### lowerCamelCase
- Das erste Wort beginnt mit einem Kleinbuchstaben, alle folgenden Wörter mit Großbuchstaben.
- Oft verwendet in Sprachen wie Java und JavaScript für Methoden- und Variablennamen.
- Beispiel: `produktListe`, `kundenDatenbank`

## snake_case

Bei snake_case werden Wörter durch Unterstriche getrennt und komplett in Kleinbuchstaben geschrieben. Diese Konvention ist besonders in der Python-Community beliebt.

- Wird für Variablen, Funktionen und Methodennamen verwendet.
- Beispiel: `produkt_liste`, `kunden_datenbank`

## Kebab-Case

Kebab-Case ist eine Variante, bei der Wörter durch Bindestriche getrennt werden. Es wird hauptsächlich in URLs und CSS-Klassennamen verwendet.

- Beispiel: `produkt-liste`, `kunden-datenbank`

## Wann welche Konvention verwenden?

$$$ Den folgenden Teil bitte durch die PEP Namenskonventionen ersetzen

- **Java**: Verwenden Sie UpperCamelCase für Klassennamen und lowerCamelCase für Methoden und Variablen.
- **C#**: Ähnlich wie Java, UpperCamelCase für Klassen und lowerCamelCase für Methoden und Variablen.
- **Python**: Verwenden Sie snake_case für fast alles, außer Klassennamen, die UpperCamelCase folgen.
- **JavaScript**: Tendiert zu lowerCamelCase, aber manchmal sieht man auch snake_case.

Ganz allgemein kann die Benennung auch nach Firmenvorschrift erfolgen.

## Diskussion und Übungen

- **Frage**: Warum ist es wichtig, sich an die Benennungskonventionen einer Sprache zu halten?
- **Übung**: Überprüfen Sie ein Stück Code und identifizieren Sie, ob die Benennungskonventionen korrekt angewendet wurden. Versuchen Sie, den Code entsprechend zu korrigieren.
