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


def get_face_xy(angle, radius):
    """
    Get x,y coordinates on face at specified angle and radius
    """
    theta = math.radians(angle)
    x = int(x0 + radius * math.cos(theta))
    y = int(y0 + radius * math.sin(theta))
    return x, y


def draw_face():
    # Outline
    #glcd.draw_rectangle(1, height - 8, width, height - 8)
    glcd.draw_circle(x0, y0, 31)
    # Ticks
    for angle in range(30, 331, 30):
        glcd.draw_line(x0, y0, *get_face_xy(angle, 29))
    # Clear center of circle
    glcd.fill_circle(x0, y0, 25, color=0)
    # Numbers
    glcd.draw_string("12", neato, x0 - 5, y0 - 29, spacing=0)
    glcd.draw_letter("3", neato, x0 + 25, y0 - 3)
    glcd.draw_letter("6", neato, x0 - 2, y0 + 23)
    glcd.draw_letter("9", neato, x0 - 29, y0 - 3)
    # Date
    glcd.draw_string(time.strftime("%b").upper(), wendy, 0, 0)
    glcd.draw_string(time.strftime("@Xalior"), broadway, 0, 31)

second = int(time.strftime("%S"))


def main():
    global second
    if second != int(time.strftime("%S")):
        glcd.clear_back_buffer()
        draw_face()
        second = int(time.strftime("%S"))
        minute = int(time.strftime("%M"))
        hour = int(time.strftime("%H"))
        glcd.draw_line(x0, y0, *get_face_xy(second * 6 + 270, 28))
        glcd.draw_line(x0, y0, *get_face_xy(minute * 6 + 270, 24))
        glcd.draw_line(x0, y0, *get_face_xy(hour * 30 - 90, 15))
        glcd.flip()
