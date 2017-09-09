import math
import time

import lib.lcd.xglcd_font as font
from lib.lcd import st7565

neato = font.XglcdFont('./fonts/Neato5x7.c', 5, 7)
arcadepix = font.XglcdFont('./fonts/ArcadePix9x11.c', 9, 11)
bally = font.XglcdFont('./fonts/Bally5x8.c', 5, 8)
ballyLG = font.XglcdFont('./fonts/Bally7x9.c', 7, 9)
broadway = font.XglcdFont('./fonts/Broadway17x15.c', 17, 15)
fixed = font.XglcdFont('./fonts/FixedFont5x8.c', 5, 8)
robotron = font.XglcdFont('./fonts/Robotron7x11.c', 7, 11)
wendy = font.XglcdFont('./fonts/Wendy7x8.c', 7, 8)

glcd = st7565.Glcd(rgb=[21, 20, 16])
glcd.init()
x0, y0 = 63, 31
width = ((x0 + 1) * 2) - 1
height = ((y0 + 1) * 2) - 1

second = int(time.strftime("%S"))  # Used to keep track if we need to redraw the clock...


def get_face_xy(angle, radius):
    """
    Get x,y coordinates on face at specified angle and radius
    """
    theta = math.radians(angle)
    x = int(x0 + radius * math.cos(theta))
    y = int(y0 + radius * math.sin(theta))
    return x, y


def keypad():
    return


def draw_button(x, y, button, label = ""):
    glcd.draw_string(button, arcadepix, x+2, y+1)
    glcd.draw_string(label, fixed, x+14, y+3)
    glcd.draw_rectangle(x, y, 12, 12)

def draw():
    # Outline
    glcd.draw_line(0, height - 8, width, height - 8)
    # Time
    glcd.draw_string(time.strftime("%H:%M:%S").upper(), wendy, 0, height - 7)
    # Date
    glcd.draw_string(time.strftime("%D").upper(), wendy, width - 38, height - 7)
    # Title
    glcd.draw_string("MAIN", wendy, 0, 0)
    glcd.draw_line(0, 8, width, 8)
    # Option
    draw_button(0, 10, "A", "LCD")
    draw_button(64, 10, "B", "LEDs")
    draw_button(0, 24, "C", "Keypad")
    draw_button(64, 24, "D", "Settings")
    #

    # Default Options
    draw_button(0, 42, "*", "back")
    draw_button(64, 42, "#", "help")
    # for i in range(0, 9):
    #     draw_button(i*14, 42, str(i))

def main():
    keypad()
    global second
    if second != int(time.strftime("%S")):
        glcd.clear_back_buffer()
        draw()
        # second = int(time.strftime("%S"))
        # minute = int(time.strftime("%M"))
        # hour = int(time.strftime("%H"))
        # glcd.draw_line(x0, y0, *get_face_xy(second * 6 + 270, 28))
        # glcd.draw_line(x0, y0, *get_face_xy(minute * 6 + 270, 24))
        # glcd.draw_line(x0, y0, *get_face_xy(hour * 30 - 90, 15))
        glcd.flip()
