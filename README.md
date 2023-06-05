# Proyecto RPi LED Controller

## Descripción
Este proyecto consiste en un sistema de iluminación LED reactivo al sonido. Utiliza un sensor de sonido para captar la intensidad del sonido ambiente y enciende una tira de LEDs en función de esa intensidad. Además, se puede controlar el color y la escala de los LEDs a través de un servidor web.

## Funcionalidades
- El sistema se compone de los siguientes componentes:
    - Raspberry Pi.
    - Sensor de sonido.
    - Tira de LEDs.
    - Servidor Flask para controlar la iluminación desde una interfaz web.
- El sensor de sonido captura la intensidad del sonido ambiente y la convierte en una señal analógica.
- La tira de LEDs se enciende y apaga en función de la intensidad del sonido capturada por el sensor.
- El color y la escala de los LEDs se pueden controlar a través de una interfaz web proporcionada por un servidor Flask.
- El servidor Flask permite seleccionar el color de los LEDs utilizando un selector de colores y ajustar la escala de brillo de los LEDs mediante un control deslizante.
- Además, se puede generar un color aleatorio utilizando un scraper.
- Pulsando el pulsador se puede activar/desactivar el modo ruido.
- Pulsando duante 2 segundos el pulsador se puede activar/desactivar el modo servidor.
## Requisitos
- Raspberry Pi.
- Sensor de sonido.
- Tira de LEDs.
- Bibliotecas Python: RPi.GPIO, smbus, neopixel, requests, BeautifulSoup, PIL, Flask, webcolors.

## Instrucciones de uso
1. Conecta el sensor de sonido a la Raspberry Pi.
2. Conecta la tira de LEDs a la Raspberry Pi.
3. Instala las bibliotecas Python requeridas.
4. Clona el repositorio desde GitHub.
5. Ejecuta el archivo `main.py`.
6. Accede a la interfaz web desde tu navegador utilizando la dirección IP de la Raspberry Pi y el puerto 8000.
7. Utiliza el selector de colores y el control deslizante para controlar el color y la escala de los LEDs.
8. Puedes generar un color aleatorio haciendo clic en el botón "Cambiar color aleatoriamente".
9. Si deseas recibir información sobre el color seleccionado por correo electrónico, ingresa tu dirección de correo electrónico y haz clic en el botón "Enviar información del color seleccionado".
