# Flask API in der Cloud
[45 min]

Eine Flask-API mit Azure Web Apps zu deployen, ermöglicht es, leistungsfähige Webanwendungen und APIs in einer skalierbaren und verwalteten Cloud-Umgebung zu hosten. Flask ist ein leichtgewichtiges und flexibles Mikro-Webframework für Python, ideal für schnelle Entwicklung und einfache Bereitstellung von Webanwendungen.

## Die Azure CLI
Die Azure Command Line Interface (CLI) ist ein Befehlszeilen-Tool. das eine schnelle, textbasierte Schnittstelle zur Ausführung von Azure-Diensten und -Operationen bietet. 

> Die Azure CLI ist sowohl für Windows als auch für Linux/MacOS muss aber vor Verwendung installiert werden.

Mit der Azure CLI kann z.B. eine virtuelle Maschine erstellt, Ressourcengruppen verwaltet oder Datenbankdienste konfiguriert werden. Ein typischer Befehl um eine neue VM in einer bestehenden Ressourcengruppe zu erstellen könnte z.B. wie folgt aussehen. 

```bash
az vm create --resource-group MyResourceGroup --name MyVM --image UbuntuLTS --generate-ssh-keys`
```

Mit etwas Übung kann fast das ganze Management der Ressourcen über das Terminal abgewickelt werden.

**Auflisten aller virtuellen Maschinen**:
Zeigt alle VMs in Ihrem Abonnement in einer tabellarischen Form an.

```bash
az vm list --output table
```

**Deployment eines ARM Templates**:
Ressourcengruppen-Deployment unter Verwendung einer ARM-Vorlagendatei durchführen.

```bash
az deployment group create --resource-group myResourceGroup --template-file template.json
```


## Live Deployment der Beispiel Flask API auf Azure
... Todo


## Aufgaben
[45 min]

### Deployment einer simplen Flask API 🌶️🌶️
Erstelle eine Simple Flask API mit GET-Route die bei Request ein "Hallo Welt!" zurückgibt. Deploye die API als Azure Web App.

### ... 🌶️🌶️🌶️
...


## Komplex-Aufgaben
[90 min]

### Inventory Management SWA 🌶️🌶️🌶️🌶️
Erstelle eine simple statische Webapp mit einem Formular um Inventaritems in die Datenbank zu schreiben. Zeige die Inventarliste in der SWA direkt an.

[Lösungen](./solutions.md)