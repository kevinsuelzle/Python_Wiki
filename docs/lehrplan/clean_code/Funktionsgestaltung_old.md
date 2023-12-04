# Funktionsgestaltung

## Gestaltung von Funktionen

Funktionen sollten

1. kurz sein
2. sich nur um eine einzige Sache kümmern: "Do One Thing!"
3. im Namen das "One Thing" klar beschreiben und in den Parametern ebenfalls sprechende Namen verwenden.
4. sich nur um eine [Abstraktionsebene](../Abstraktionsebene) kümmern.
5. wenig [Argumente](../Funktionsparameter) haben.
6. echte Fehler verarbeiten und keine Fehlerwerte an die aufrufende Funktion "hoch" geben. Das erleichtert
   die Wartung, da man sich sofort bewusst ist, wo das Problem aufgetaucht ist. Zudem bleibt der übergeordnete Code frei
   von der Fehlerverarbeitung und damit lesbarer.
7. Keine Seiteneffekte haben. (*Seiteneffekt* ist der Fachbegriff für eine Änderung des Speichers.)

#Aufagbe: Code aufsplitten
1. Teile den folgenden Code in mehrere Funktionen auf, die jeweils nur eine Sache tun.
2. Benenne die Funktionen und ihre Parameter entsprechend.

```python
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def process_mnist_dataset(url, upscale_factor, val_split, test_split):
    """
    Diese Funktion führt mehrere Schritte der Datenverarbeitung durch:
    1. Lädt den MNIST-Datensatz herunter.
    2. Teilt den Datensatz in Trainings-, Validierungs- und Testsets auf.
    3. Führt ein Upscaling und Normalisierung für jedes Bild durch.
    """
    # MNIST-Daten herunterladen
    response = requests.get(url)
    response.raise_for_status()
    mnist_data = np.load(BytesIO(response.content))
    
    # Combine x_train, x_test, y_train and y_test to one big dataset (do our own splitting)
    arr_0 = np.concatenate((mnist_data['x_train'], mnist_data['x_test']), axis=0)
    arr_1 = np.concatenate((mnist_data['y_train'], mnist_data['y_test']), axis=0)

    # Trainings- und Validierungsdaten aufteilen
    split_index_val = int(val_split * len(arr_0))
    X_train, X_val = arr_0[:split_index_val], arr_0[split_index_val:]
    y_train, y_val = arr_1[:split_index_val], arr_1[split_index_val:]

    # Testdaten aufteilen und Testdaten aus Validierungsdaten entfernen
    split_index_test = int(test_split * len(X_val))
    X_test, X_val = X_val[:split_index_test], X_val[split_index_test:]
    y_test, y_val = y_val[:split_index_test], y_val[split_index_test:]

    # Bilder verarbeiten (Upscaling und Normalisierung)
    processed_images = []
    for image in X_train:
        pil_image = Image.fromarray(image)
        upscaled_image = pil_image.resize([int(dim * upscale_factor) for dim in pil_image.size], Image.Resampling.LANCZOS)
        normalized_image = np.array(upscaled_image) / 255.0
        processed_images.append(normalized_image)
    X_train = np.array(processed_images)

    processed_images = []
    for image in X_val:
        pil_image = Image.fromarray(image)
        upscaled_image = pil_image.resize([int(dim * upscale_factor) for dim in pil_image.size], Image.Resampling.LANCZOS)
        normalized_image = np.array(upscaled_image) / 255.0
        processed_images.append(normalized_image)
    X_val = np.array(processed_images)
    
    X_val = np.array(processed_images)
    for image in X_test:
        pil_image = Image.fromarray(image)
        upscaled_image = pil_image.resize([int(dim * upscale_factor) for dim in pil_image.size], Image.Resampling.LANCZOS)
        normalized_image = np.array(upscaled_image) / 255.0
        processed_images.append(normalized_image)
    X_test = np.array(processed_images)

    return X_train, X_val, X_test, y_train, y_val, y_test

# URL des MNIST-Datensatzes
url = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'

# Test der Funktion mit spezifischen Parametern
X_train, X_val, X_test, y_train, y_val, y_test = process_mnist_dataset(url, upscale_factor=2, val_split=0.8, test_split=0.5)

# Ausgabe der Formen der Datensätze
print("X_train shape:", X_train.shape)
print("X_val shape:", X_val.shape)
print("X_test shape:", X_test.shape) 
print("y_train shape:", y_train.shape)
print("y_val shape:", y_val.shape)
print("y_test shape:", y_test.shape)
```

## Lösung
```python
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def download_mnist_data(url):
    """
    Diese Funktion lädt den MNIST-Datensatz herunter und gibt ihn zurück.
    """
    response = requests.get(url)
    response.raise_for_status()
    mnist_data = np.load(BytesIO(response.content))
    return mnist_data

def split_dataset(data, val_split, test_split):
    """
    Diese Funktion teilt den Datensatz in Trainings-, Validierungs- und Testsets auf.
    """
    arr_0 = np.concatenate((data['x_train'], data['x_test']), axis=0)
    arr_1 = np.concatenate((data['y_train'], data['y_test']), axis=0)

    split_index_val = int(val_split * len(arr_0))
    split_index_test = int(test_split * split_index_val)

    X_train, X_val, X_test = arr_0[:split_index_val], arr_0[split_index_val:split_index_val+split_index_test], arr_0[split_index_val+split_index_test:]
    y_train, y_val, y_test = arr_1[:split_index_val], arr_1[split_index_val:split_index_val+split_index_test], arr_1[split_index_val+split_index_test:]

    return X_train, X_val, X_test, y_train, y_val, y_test

def preprocess_images(images, upscale_factor):
    """
    Diese Funktion führt Upscaling und Normalisierung für Bilder durch.
    """
    processed_images = []
    for image in images:
        pil_image = Image.fromarray(image)
        upscaled_image = pil_image.resize([int(dim * upscale_factor) for dim in pil_image.size], Image.Resampling.LANCZOS)
        normalized_image = np.array(upscaled_image) / 255.0
        processed_images.append(normalized_image)
    return np.array(processed_images)

def process_mnist_dataset(url, upscale_factor, val_split, test_split):
    """
    Diese Funktion führt die gesamte Datenverarbeitung durch und gibt die aufgeteilten und vorverarbeiteten Datensätze zurück.
    """
    mnist_data = download_mnist_data(url)
    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(mnist_data, val_split, test_split)
    
    X_train = preprocess_images(X_train, upscale_factor)
    X_val = preprocess_images(X_val, upscale_factor)
    X_test = preprocess_images(X_test, upscale_factor)

    return X_train, X_val, X_test, y_train, y_val, y_test

# URL des MNIST-Datensatzes
url = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'

# Test der Funktion mit spezifischen Parametern
X_train, X_val, X_test, y_train, y_val, y_test = process_mnist_dataset(url, upscale_factor=2, val_split=0.8, test_split=0.5)

# Ausgabe der Formen der Datensätze
print("X_train shape:", X_train.shape)
print("X_val shape:", X_val.shape)
print("X_test shape:", X_test.shape) 
print("y_train shape:", y_train.shape)
print("y_val shape:", y_val.shape)
print("y_test shape:", y_test.shape)
```

# Aufgabe: Code lesbarer machen
Refaktorisiere den folgenden Python-Code, der eine Textanalyse durchführt. Der aktuelle Code nutzt unklare und verwirrende Namen, die es schwierig machen, die Funktionalität und Absicht des Codes zu verstehen. Deine Aufgabe ist es, den Code zu überarbeiten, um ihn klarer und verständlicher zu machen.
```python
def text(a):
    b = a.split()
    c = len(b)
    d = {}
    e = 0
    for f in b:
        if f in d:
            d[f] += 1
        else:
            d[f] = 1
        e += len(f)
    g = None
    h = 0
    for i, j in d.items():
        if j > h:
            h = j
            g = i
    k = e / c
    return c, g, k

l = text("Beispieltext mit einigen Wörtern. Einige Wörter wiederholen sich.")
print("Zählung:", l[0])
print("Oft:", l[1])
print("Durchschn:", l[2])
```
## Lösung
```python
def count_words(text):
    # Zerlegt den Text in einzelne Wörter
    words = text.split()
    return len(words)

def calculate_word_frequency(text):
    # Erstellt ein Wörterbuch zur Zählung der Häufigkeit jedes Wortes
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def analyze_text(text):
    # Funktionen aufrufen, um Anzahl der Wörter und Wortfrequenz zu berechnen
    word_count = count_words(text)
    word_frequency = calculate_word_frequency(text)

    # Findet das am häufigsten vorkommende Wort
    most_frequent_word = max(word_frequency, key=word_frequency.get)

    # Berechnet die durchschnittliche Wortlänge
    total_characters = sum(len(word) for word in text.split())
    average_word_length = total_characters / word_count

    return word_count, most_frequent_word, average_word_length

# Test des refaktorisierten Codes
result = analyze_text("Beispieltext mit einigen Wörtern. Einige Wörter wiederholen sich.")
print("Anzahl der Wörter:", result[0])
print("Häufigstes Wort:", result[1])
print("Durchschnittliche Wortlänge:", result[2])
```

Der Autor antwortet auf die Aufgabe, Zitat (übersetzt): "Mit nur ein paar einfachen Methodenextraktionen, etwas Umbenennung und einer kleinen Umstrukturierung
konnte ich jedoch die Absicht der Funktion in den neun Zeilen [des folgenden von Java nach Python übersetzten Codes]
erfassen."

### TODO: @Benedikt, wollen wir die Aufgabe überarbeiten?
# Aufgabe: Sehen Sie, ob Sie das in den nächsten 3 Minuten verstehen können.

```python
def render_page_with_setups_and_teardowns(page_data, is_suite):
    is_test_page = page_data.has_attribute("Test")
    if is_test_page:
        test_page = page_data.get_wiki_page()
        new_page_content = []

        include_setup_pages(test_page, new_page_content, is_suite)
        new_page_content.append(page_data.get_content())
        include_teardown_pages(test_page, new_page_content, is_suite)

        page_data.set_content(''.join(new_page_content))

    return page_data.get_html()
```

[zurück](../TheGoodPractices)