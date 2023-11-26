# Beispiele für schlechten Code in Python

```python
x = 10


def increment():
    global x
    x += 1
```

```python
def divide(a, b):
    return a / b
```

```python
my_list = [x ** 2 for x in range(20) if x % 2 == 0 if x % 3 == 0]
```

```python
a = 50
b = 100
c = a + b
```

```python
def calc(x):
    return x * 2 + 5
```

```python
# Berechnung des Quadrats von Zahlen
num1 = 4
quadrat_num1 = num1 * num1

num2 = 5
quadrat_num2 = num2 * num2

num3 = 6
quadrat_num3 = num3 * num3

print(quadrat_num1, quadrat_num2, quadrat_num3)
```

### Aufgabe: Umwandeln in sauberen Code.

```python
a1 = []
a2 = []


def copyarr():
    global a1, a2
    for i in range(len(a1)):
        a2.append(a1[i])
```

### Aufgabe: Versuche innerhalb von 3 Minuten eine grobe Vorstellung von der Funktion des folgenden Codes zu bekommen.

Entnommen aus Clean Code von Robert C. Martin

```java
    public static String testableHtml(PageData pageData, boolean includeSuiteSetup) throws Exception {
        WikiPage wikiPage = pageData.getwikiPage();
        StringBuffer buffer = new StringBuffer();
        if (pageData.hasAttribute("Test")) {
            if (includeSuiteSetup)
                WikiPage suiteSetup = PageCrawlerImpl.getInheritedPage(SuiteResponder.SUITE_SETUP_NAME, wikiPage);
            if (suiteSetup != null) {
                WikiPagePath pagePath = suitesetup.getPageCrawler().getFullPath(suiteSetup);
                String pagePathName = PathParser.render(pagePath);
                buffer.append("!include -setup .")
                        .append(pagePathName)
                        .append("\n");
            }
        }

        WikiPage setup = PageCrawlerImpl.getInheritedPage("SetUp", wikiPage);
        if (setup != null) {
            WikiPagePath setupPath = wikiPage.getPageCrawler().getFullPath(setup);
            String setupPathName = PathParser.render(setupPath);
            buffer.append("!include -setup.")
                    .append(setupPathName)
                    .append("\n");
        }
    
        buffer.append(pageData.getContent());
        if (pageData.hasAttribute("Test")) {
            WikiPage teardown = PageCrawlerImpl.getInheritedPage("TearDown", wikiPage);
            if (teardown != null) {
                WikiPagePath tearDownPath = wikiPage.getPageCrawler().getFullPath(teardown);
                String tearDownPathName = PathParser.render(tearDownPath);
                buffer.append("\n")
                        .append(" !include -teardown .")
                        .append(tearDownPathName).append("/n");
            }

            if (includeSuiteSetup) {
                WikiPage suiteTeardown = PageCrawlerImpl.getInheritedPage(SuiteResponder.SUITE_TEARDOWN_NAME, wikiPage);
                if (suiteTeardown != null) (WikiPagePath
                pagePath = suiteTeardown.getPageCrawler().getFullPath(suiteTeardown);
                String pagePathName = PathParser.render(pagePath);
                buffer.append(" !include -teardown .")
                        .append(pagePathName)
                        .append("/a");
            }
        }

        pageData.setContent(buffer.tostring());
        return pageData.getHtml();
    }
```

Zitat (übersetzt): Mit nur ein paar einfachen Methodenextraktionen, etwas Umbenennung und einer kleinen Umstrukturierung
konnte ich jedoch die Absicht der Funktion in den neun Zeilen [des folgenden Codes] erfassen.
Sehen Sie, ob Sie das in den nächsten 3 Minuten verstehen können.

```java
  public static String renderPageWithSetupsAndTeardowns ( 
            Pagedata pageData, boolean isSuite
    ) throws Exception {
        boolean isTestPage = pageData.hasAttribute("Test");
        if (isTestPage) {
            WikiPage testPage = pageData.getWikiPage();
            StringBuffer newPageContent = new StringBuffer();
            includeSetupPages(testPage, newPageContent, isSuite);
            newPageContent.append(pageData.getContent());
            includeTeardownPages(testPage, newPageContent, isSuite);
            pageData.setContent(newPageContent.toString());
        }
        return pageData.getHtmal();
    }
```

Auch wenn dieses Beispiel, ganz bewusst aus einer fremden Programmiersprache gewählt, keinen tieferen Sinn ergibt, so
ist doch klar ersichtlich,
wie viel eine gute Benennung und Gliederung von Funktionalität ausmacht.

Daraus ergeben sich folgende Erkenntnisse bezüglich der Gestaltung von Funktionen:

1. sie sollten kurz sein
2. sie sollten sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. sie sollten keine Nebeneffekte haben.
4. innerhalb einer Funktion sollte es nur eine Abstraktionsebene geben.
5. sie sollten wenig Argumente haben. Das bezieht sich auf das Testen von Funktionen.

    1. **niladic**: Funktionen ohne Argumente sind am einfachsten zu testen.
    2. **monadic**: Funktionen mit einem Argument sind noch recht einfach zu testen, da der Wertebereich nur für die
       eineVariable zu erfassen ist und es keine Kombinatorik gibt.
    3. **dyadic**: Funktionen mit zwei Argumenten sind schon schwer in ihrer Totalität zu testen. Je nach Datentyp der
       Parameter ufert der Test aus.
    4. **triadic**: gar nicht erst dran denken.
    5. **polyadic**: das muss anders gemacht werden.
       Aufgabe: Wie kann man eine Reduktion von Parametern erreichen? Wie kann eine Funktion ohne Parameter auskommen?
   
6. sie sollten eher echte Fehler verarbeiten als Fehlerwerte an die aufrufende Funktion "hoch" zu geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.
7. wenn sie eine Ausnahmebehandlung vorsehen, sollte nichts vor dem "try" stehen und nach dem "except" Block sollte auch
   kein weiterer Code mehr folgen. Ausnahme: der "finally" Block. Es kann ja sein, dass man was aufräumen muss.

### Abstraktionsebene

Code von oben nach unten lesen: Die Stepdown-Regel

Wir wollen, dass der Code wie eine Top-Down-Erzählung gelesen wird. Wir möchten, dass jede Funktion von denen auf der
nächsten Abstraktionsebene gefolgt wird, damit wir das Programm lesen können, wobei wir jeweils eine
Abstraktionsebene
absteigen, während wir die Liste der Funktionen lesen. Ich nenne das die Step-down-Regel.
Um dies anders auszudrücken, möchten wir in der Lage sein, das Programm so zu lesen, als wäre es eine Reihe von Um
zu-Absätzen, von denen jeder die aktuelle Abstraktionsebene beschreibt und auf nachfolgende Um zu-Absätze auf der
nächsten Ebene nach unten verweist.

- **Um die Setups und Teardowns einzubeziehen**, schließen wir Setups ein, dann schließen wir den Testseiten-Content
  und dann die Teardowns ein.
- **Um die Setups einzubeziehen**, schließen wir das Suite-Setup ein, wenn es sich um eine Suite handelt, dann
  schließen
  wir das reguläre Setup ein.
- **Um das Suite-Setup einzubeziehen**, durchsuchen wir die übergeordnete Hierarchie nach der Seite "SuiteSetUp" und
  fügen eine include-Anweisung mit dem Pfad dieser Seite hinzu.
- **Um den Elternteil zu suchen**...

Es stellt sich heraus, dass es für Programmierer sehr schwierig ist, zu lernen, dieser Regel zu folgen und Funktionen
zu schreiben, die auf einer einzigen Abstraktionsebene bleiben. Aber das Erlernen dieses Tricks ist auch sehr
wichtig.
Es ist der Schlüssel, um Funktionen kurzzuhalten und sicherzustellen, dass sie "eine Sache" tun. Den Code wie einen
Top-Down-Satz von Um zu-Absätzen lesen zu lassen, ist eine effektive Technik, um die Abstraktionsebene konsistent zu
halten.

