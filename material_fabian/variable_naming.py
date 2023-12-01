def func(a, b, c, d):
    x = a + b
    y = c * d
    z = x - y
    return z

def calculate_difference(addend1, factor1, factor2, subtractor):
    # Berechnung der Summe von addend1 und factor1
    sum_result = addend1 + factor1
    
    # Berechnung des Produkts von factor2 und subtractor
    product_result = factor2 * subtractor
    
    # Berechnung der Differenz zwischen sum_result und product_result
    difference = sum_result - product_result
    
    # Rückgabe des Ergebnisses
    return difference

def calculate_area(l, w):
    a = l * w
    return a

length = 10
width = 5
result = calculate_area(length, width)
print("The area is:", result)

def calculate_rectangle_area(length, width):
    area = length * width
    return area

rectangle_length = 10
rectangle_width = 5
resulting_area = calculate_rectangle_area(rectangle_length, rectangle_width)
print("The area is:", resulting_area)

import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

# Initialer Code mit schwer verständlichen Variablennamen
def func_a(url_b):
    res_c = requests.get(url_b)
    img_d = Image.open(BytesIO(res_c.content))
    ax_e = plt.subplot(111)
    ax_e.imshow(img_d)
    ax_e.axis('off')
    plt.show()

# Beispiel-URL für ein Bild
url_f = 'https://banner2.cleanpng.com/20180402/ioq/kisspng-python-logo-clojure-javascript-9-5ac25c2686ca38.9179638515226870145521.jpg'
func_a(url_f)

# Verbesserter Code mit verständlichen Variablennamen
def show_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    axis = plt.subplot(111)
    axis.imshow(image)
    axis.axis('off')
    plt.show()

# Beispiel-URL für ein Bild
url = 'https://banner2.cleanpng.com/20180402/ioq/kisspng-python-logo-clojure-javascript-9-5ac25c2686ca38.9179638515226870145521.jpg'
show_image(url)


import requests
from bs4 import BeautifulSoup

def show_webpage_content(url):
    response = requests.get(url)
    print(response.text)

def find_and_display_element(url, element_id):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find(id=element_id)
    print(element)

def display_website_structure(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for header in soup.find_all(['h1', 'h2', 'h3']):
        print(header.text.strip())
    for paragraph in soup.find_all('p'):
        print(paragraph.text.strip())

# Testen der Funktionen mit einer Beispiel-URL
test_url = 'https://openai.com'
show_webpage_content(test_url)
# print all element ids
find_and_display_element(test_url, 'Careers at OpenAI')
display_website_structure(test_url)

import requests
from bs4 import BeautifulSoup

def funktion_alpha(url_parameter):
    variable_a = requests.get(url_parameter)
    print(variable_a.text)

def funktion_beta(url_parameter, id_parameter):
    variable_a = requests.get(url_parameter)
    variable_b = BeautifulSoup(variable_a.text, 'html.parser')
    variable_c = variable_b.find(id=id_parameter)
    print(variable_c)

def funktion_gamma(url_parameter):
    variable_a = requests.get(url_parameter)
    variable_b = BeautifulSoup(variable_a.text, 'html.parser')
    for h in variable_b.find_all(['h1', 'h2', 'h3']):
        print(h.text.strip())
    for p in variable_b.find_all('p'):
        print(p.text.strip())

# Testen der Funktionen mit einer Beispiel-URL
beispiel_url = 'https://openai.com'
funktion_alpha(beispiel_url)
# print all element ids
funktion_beta(beispiel_url, 'Careers at OpenAI')
funktion_gamma(beispiel_url)
