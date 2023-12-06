# Einführung in Git Teil 1

Git ist ein Versionsverwaltungssystem, um im Team gemeinsam einfach und sicher an Projekten arbeiten.

## Lernziele dieses Kapitels:
    - Du verstehst wofür GIT da ist.
    - Du hast dein eigenes Repository erzeugt.
    - Verstehe die Struktur von Git (Working Tree, Index, Repository)

## Inhaltsangabe 

#### Teil 1
1. Übersicht
2. Was ist GIT?
3. Installation von GIT
4. Die Hilfsfunktion von GIT
5. Die Konfiguration von GIT
6. Ein GIT Repository erstellen




## 1. Übersicht
In diesem Kurs besprechen wir die Befehle, die wir bei der Arbeit mit Git am häufigsten verwenden.

Wir beginnen mit der Installation und Konfiguration und erstellen dann unser erstes lokales Repository. Dabei stellen wir theoretische Konzepte stets in praktischen Anwendungen dar.

Darüber hinaus besprechen wir das Branching und erlernen auch einige fortgeschrittene Techniken wie das Ändern von Commits und das Manipulieren des Commit-Verlaufs.

## 2. Was ist GIT?
Git ist ein Versionskontrollsystem (VCS), das das Speichern und Verfolgen von Änderungen an Dateien im Laufe der Zeit ermöglicht, ohne vorherige vorherige Zwischenstände zu überschreiben. Es hilft Entwicklern, gemeinsam an Projekten zu arbeiten.

Im Gegensatz zu seinem Hauptkonkurrenten SVN implementiert Git auch ein verteiltes Workflow-System. Das bedeutet, dass jeder Entwickler, der mit Git arbeitet, über eine lokale Kopie des gesamten Repositorys verfügt. Git ermöglicht auch asynchrones Arbeiten ohne ständige Verbindung zum zentralen Repository.

#### Wofür braucht man git?

    - Speicherung, Einsicht und Wiederherstellung von verschiedenen Projektversionen. (Wie viele Projektversionen?)
    - Für Übersicht sorgen.
    - Nachverfolgbarkeit (Wer erstellte welche Änderung?) mit Begründung
    - Identitätskontrolle (der Autorenschaft von Versionen)
    - Sicherheit (Zugang gegenüber Dritten sichern)
    - Paralleles Arbeiten erlauben
    - Einzelnes Arbeiten erlauben (ungestört)
    - Offline Arbeiten ermöglichen (Unabhängigkeit vom Internet)
    - Umgang mit Speicherplatz klein halten
    - Zwischenspeichern von Versionen, an denen später gearbeitet werden soll
    - Grüne Wiesen
    - Teamgrößenunabhängigkeit
    - Kein Verlust von Dateien
    - Differenz zwischen zwei Projektversion ansehen


#### Beispiel ohne code
    - Ein Bild malen.
        1. Leeres Canvas nehmen... drauf malen.... wenns gefällt zwischenspeichern.
        2. Später woanders rummalen.
        3. Eventuell eine Änderung wieder zurück nehmen.
        4. Verschiedene Versionen malen und nebeneinander Zwischenspeichern.
        5. Mit mehreren Personen malen.
            - Jeder malt in seinem Bereich.
            - Jeder mal wie er will.... Die Kunstwerke überschneiden sich. Danach müssen die Bilder zusammengeführt werden. 
                Aber wie? Bitte keine Konflikte untereinander! :)


#### Was speichert GIT?
    - Es gibt drei Hauptarten von Objekten in git:
    - Blobs (Dateien mit Inhalt)
    - Trees (Bildet Ordnerstrukturen ab. Hat Referenzen zu Blobs und Trees)
    - Commits (Wird bei einem Commit erstellt, hat verschiedene Metainfos und Referenz zu einem Tree)
    - Annotatet Tags
    - Alle Objekte sind im .git/objects Ordner gespeichert.

## 3. Installation von GIT
Wir können Git auf den gängigsten Betriebssystemen wie Windows, Mac und Linux installieren. Tatsächlich ist Git auf den meisten Mac- und Linux-Rechnern standardmäßig installiert.

Um zu sehen, ob Git bereits installiert ist, öffnen wir ein Terminal und führen Folgendes aus:

```console
$ git version
git version 2.24.3 (Apple Git-128)
```
Darüber hinaus verfügt Git über integrierte GUI-Tools zum Festschreiben (git-gui) und Durchsuchen (gitk). Es gibt auch zahlreiche Tools oder IDE-Plugins von Drittanbietern, die das Arbeiten vereinfachen. Wir lernen es in diesem Kurs aber von Grund auf.

## 4. Die Hilfsfunktion von GIT
Bevor wir unser erstes Repository erstellen, führen wir den Befehl „git help“ aus um uns nützliche Befehle anzeigen zu lassen.

```console

$ git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
...

```
Wir können das Manual für einen bestimmten Befehl auch auf verschiedene Arten überprüfen:


```console
$ git --help init
$ git help init
$ git init --help
```

Alle drei oben genannten Varianten geben eine identische Ausgabe zurück.

Mit der Option -g können wir auch auf die Liste der internen Anleitungen zugreifen:

```console
$ git help -g
The common Git guides are:
   attributes          Defining attributes per path
   cli                 Git command-line interface and conventions
   core-tutorial       A Git core tutorial for developers
...
$ git help core-tutorial
```



## 5. Die Konfiguration von GIT
Sobald wir Git installiert haben, können wir es einfach mit dem Befehl gitconfig konfigurieren.

Git unterstützt Optionen auf verschiedenen Ebenen wie System, Global, Lokal, Tree oder Datei.


Während die Systemeinstellungen systemweit gelten und auf jeden Benutzer und alle seine Repositorys im System angewendet werden, bezieht sich die globale Ebene auf benutzerspezifische Einstellungen.

Die lokale Konfiguration ist spezifisch für das einzelne Repository und die Standardebene, die Git verwendet, wenn wir keine Option an den Befehl „git config“ übergeben.

Die Tree- und Dateiebenen sind erweiterte Konfigurationsebenen, die auf einen einzelnen Zweig oder eine einzelne Datei im Repository angewendet werden können.

Darüber hinaus löst Git den effektiven Wert einer Option auf, indem es zunächst die lokale Ebene überprüft und dann bis zur Systemebene vorgeht, wenn die Option nicht festgelegt ist.

Als Beispiel konfigurieren wir unseren Benutzernamen, der im Commit-Verlauf verwendet wird:

```console
$ git config --global user.name "Qualidy User"
```
Wir haben gerade unseren Namen bekannt gemacht.

Um eine Option für ein einzelnes Repository zu überschreiben, können wir die Flag –local in seinem Verzeichnis verwenden.

Um die Liste der wirksamen Optionen auszugeben, tippen wir:


```console
$ git config -l
user.name=Qualidy User
```

Wir können den Befehl git –help config ausführen, um Details zu allen verfügbaren Optionen zu erhalten.

## 6. Ein GIT Repository erstellen
Als nächstes müssen wir ein Repository erstellen. Hierfür haben wir zwei Alternativen: Ein neues Repository kann entweder lokal von Grund auf erstellt werden oder ein bestehendes kann geklont werden.

## 6.1 git init – Ein neues Repository erstellen

Wenn wir uns entscheiden, ein neues Repository zu initialisieren, müssen wir den Befehl git init verwenden. Es verwandelt das aktuelle Verzeichnis in ein Git-Repository und beginnt mit der Verfolgung seines Inhalts:

```console
$ mkdir simple-repo; cd simple-repo; git init
Initialized empty Git repository in /simple-repo/.git/
```

Git erstellt darin auch ein verstecktes Verzeichnis namens .git. In diesem Verzeichnis werden alle Objekte und Referenzen gespeichert, die Git im Rahmen unseres Projektverlaufs erstellt und verwendet. Diese Dateien werden bei Commits erstellt und verweisen auf bestimmte Revisionen unserer Dateien.

Danach möchten wir in den meisten Fällen unser bereits erstelltes Repository mit einem Remote-Repository verbinden. Wir verwenden den Befehl git remote, um Remote-Links für das aktuelle Repository zu verwalten:

```console
$ git remote add origin https://github.com/eugenp/tutorials.git
```

Wir haben gerade neues Remote Repository namens origin hinzugefügt und verbunden.

## 6.2 git clone – Kopiere ein externes Repository
Manchmal möchten wir zu einem vorhandenen Repository eigene Änderungen beitragen. Zuerst müssen wir das vorhandene Repository lokal herunterladen.

Der Befehl git clone kopiert das Repository in ein neues Verzeichnis:

```console
$ git clone https://github.com/eugenp/tutorials.git
Cloning into 'repo'...
```

Wenn der Vorgang abgeschlossen ist, enthält das neu erstellte Verzeichnis alle Dateien, Branches und den Verlauf des Projekts.

Darüber hinaus ist das geklonte Repository bereits konfiguriert und mit der externen Quelle verbunden:

```console
$ cd tutorials
$ git remote -v
origin	https://github.com/eugenp/tutorials.git (fetch)
origin	https://github.com/eugenp/tutorials.git (push)
```

Git verwendet diese links, um weitere Änderungen zu verwalten.


# Aufgaben:
[320min]

## 1. Neues Repository anlegen. 🌶️
Neues Repository anlegen.
Dateien erstellen, bearbeiten und dem Index hinzufügen.
Mindestens zwei Commits erstellen.

## 2. Mit Repository arbeiten. 🌶️
Den Zustand eines alten Commits wiederherstellen.
Von diesem aus neue Commits erstellen.
Untersuche Strucktur der Commits mit git log --all --graph --oneline
Passiert es dir, dass Commits plötzlich nicht mehr sichtbar sind?

## 3. Ein externes Repository klonen 🌶️🌶️
Klone ein externes Repository aus dem Internet. 
Mache eine Änderung im Code.
Commite deine Änderung.


