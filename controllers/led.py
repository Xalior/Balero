from neopixel import *

# LED strip configuration:
FRONT_LED_COUNT = 12 # Number of LED pixels.
FRONT_LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).0
FRONT_LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
FRONT_LED_DMA = 5  # DMA channel to use for generating signal (try 5)
FRONT_LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
FRONT_LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
FRONT_LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
FRONT_LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

j = 0

strip = Adafruit_NeoPixel(FRONT_LED_COUNT, FRONT_LED_PIN, FRONT_LED_FREQ_HZ, FRONT_LED_DMA, FRONT_LED_INVERT,
                          FRONT_LED_BRIGHTNESS, FRONT_LED_CHANNEL, FRONT_LED_STRIP)
strip.begin()

def main(anim_on, anim_command):
    global j

    # Handle the mode change of anim_command here and refactor this to a mode module...
    if anim_on.value == 1:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        j = j + 1
        if j > 255:
            j = 0
