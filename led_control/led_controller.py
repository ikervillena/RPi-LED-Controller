import board
import neopixel

PIXELS = 30

class LEDController:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, PIXELS)

    def set_led_color(self, num_leds, color):
        if num_leds < 0 or num_leds > 30:
            raise ValueError("El número de LEDs debe estar entre 0 y 30")
        self.pixels.fill((0, 0, 0))  # Apagar todos los LEDs
        for i in range(num_leds):
            self.pixels[i] = color
        self.pixels.show()
    
    def apagar(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
