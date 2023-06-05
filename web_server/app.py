from flask import Flask, render_template, request
from scraper.color_scraper import generate_random_color
from web_server.envio.envio_email import enviar_email

import webcolors

app = Flask(__name__)

# Variables globales para almacenar el color seleccionado y la escala del LED
global_color = (0, 0, 0)
led_scale = 509  # Valor predeterminado de la escala del LED

def get_global_color():
    global global_color
    return global_color

def set_global_color(color):
    global global_color
    global_color = color

def get_led_scale():
    global led_scale
    return led_scale

def set_led_scale(scale):
    global led_scale
    led_scale = scale

def get_color_name(hex_color):
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    try:
        return webcolors.rgb_to_name(rgb)
    except ValueError:
        return "Desconocido"

@app.route("/set_color", methods=['POST'])
def set_color():
    hex_color = request.form['color'].lstrip('#')
    red, green, blue = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    set_global_color((red, green, blue))  # Actualizar la variable global con el color seleccionado
    return "Color cambiado a RGB({}, {}, {})".format(red, green, blue)

@app.route("/set_scale", methods=['POST'])
def set_scale():
    scale = int(request.form['scale'])
    set_led_scale(scale)  # Actualizar la escala del LED con el valor recibido
    return "Escala del LED actualizada"

@app.route("/set_random_color", methods=['POST'])
def set_random_color():
    color = generate_random_color()  # Generar color aleatorio
    set_global_color(color)  # Actualizar el color global con el color aleatorio
    hex_color = "#{:02x}{:02x}{:02x}".format(*color)  # Convertir color a formato hexadecimal
    return hex_color

@app.route("/send_email", methods=['POST'])
def send_email():
    hex_color = request.form['color'].lstrip('#')
    red, green, blue = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    email = request.form['email']

    # Obtener información adicional sobre el color
    color_name = get_color_name(hex_color)
    hex_value = "#" + hex_color
    rgb_values = f"RGB({red}, {green}, {blue})"

    # Enviar el correo electrónico
    subject = "Color seleccionado"
    mensaje = f"El color seleccionado es {color_name}.\n\n" \
              f"Valor hexadecimal: {hex_value}\n" \
              f"Valores RGB: {rgb_values}\n" \

    destinatario = email

    enviar_email(subject, mensaje, destinatario)

    return "Correo enviado a: " + email

@app.route("/")
def home():
    return render_template('home.html', led_scale=get_led_scale())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)