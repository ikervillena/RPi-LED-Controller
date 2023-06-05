import threading
import time
import RPi.GPIO as GPIO

from sensors.sound_sensor import SoundSensor
from led_control.led_controller import LEDController
from web_server.app import app, get_global_color, get_led_scale
from scraper.color_scraper import generate_random_color

BUTTON_PIN = 16
LED_PIN = 5
LONG_PRESS_DURATION = 2

lock = threading.Lock()

global server_active
server_active = True

def handle_led(sensor, led_controller):
    global modo_servidor
    global modo_ruido
    while server_active:
        # Si el servidor Flask está activo se obtienen el color y la escala
        if modo_servidor:
            with lock:
                led_color = get_global_color()  # Obtener el color global seleccionado
                led_scale = get_led_scale() # Obtener la escala del led seleccionada
        else:
            led_color = generate_random_color()
            led_scale = 20

        # Si el modo ruido está activado se obtiene el número de leds que hay que encender
        if modo_ruido:
            value = sensor.read_adc()
            num_leds = int(value * 30 / led_scale)  # Ajusta la sensibilidad según tus necesidades
        if num_leds > 30 or not modo_ruido:
            num_leds = 30
        led_controller.set_led_color(num_leds, led_color)  # Utilizar el color global
        if modo_ruido:
            time.sleep(0.2)
        else:
            time.sleep(0.8)

def handle_button(channel):
    global modo_servidor
    global modo_ruido
    start_time = time.time()
    while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        if time.time() - start_time >= LONG_PRESS_DURATION:
            # Comportamiento cuando se MANTIENE PULSADO el boton durante 2 segundos
            #GPIO.output(LED_PIN, not GPIO.input(LED_PIN))
            modo_servidor = not modo_servidor
            if modo_servidor:
                print("Modo servidor Flask activado")
            else:
                print("Modo servidor Flask desactivado (colores aleatorios)")
            return
    
    # Comportamiento cuanto el botón se PULSA SIMPLEMENTE, sin manterlo pulsado
    modo_ruido = not modo_ruido
    if modo_ruido:
        print("Modo ruido activado")
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print("Modo ruido desactivado")
        GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == '__main__':
    sensor = SoundSensor()
    led_controller = LEDController()
    global modo_ruido
    global modo_servidor
    modo_ruido = True
    modo_servidor = True
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=handle_button, bouncetime=300)

    # Crear y ejecutar el hilo para gestionar el Led
    led_thread = threading.Thread(target=handle_led, args=(sensor, led_controller))
    led_thread.start()

    # Iniciar servidor Flask
    app.run(host='0.0.0.0', port=8000)

    # Después de hacer CTRL + C, cuando se cierra el servidor Flask
    print("Servidor cerrado")
    server_active = False
    led_controller.apagar()
    led_thread.join()
    print("Hilo del led finalizado")
