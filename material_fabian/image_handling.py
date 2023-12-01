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

# Print the shapes of the resulting datasets
print("X_train shape:", X_train.shape)
print("X_val shape:", X_val.shape)
print("X_test shape:", X_test.shape) 
print("y_train shape:", y_train.shape)
print("y_val shape:", y_val.shape)
print("y_test shape:", y_test.shape)

