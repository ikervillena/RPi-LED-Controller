import requests
from bs4 import BeautifulSoup
from PIL import ImageColor

def generate_random_color():
    url = "http://www.shodor.org/~ishaanr/PHP/colorgenerator.php"

    # Realizar la solicitud HTTP a la página web
    response = requests.get(url)

    # Analizar el HTML de la página web
    soup = BeautifulSoup(response.content, 'html.parser')

    # Obtener el valor HEX del elemento <p> que contiene el código de color
    hex_element = soup.find('p')
    hex_value = hex_element.text

    # Convertir el valor HEX a RGB
    rgb_value = ImageColor.getrgb(hex_value)

    return rgb_value
