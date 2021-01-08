from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    global pt
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {pt.x, pt.y}


import os

path = os.getcwd()
for root, dirs, files in os.walk(path):

    list_of_files = []
    for name in files:
        if name.endswith((".png")):
            list_of_files.append(name)
    try:
        largest = max(list_of_files)
        if largest.endswith(".png"):
            largest = largest[:-4]
        global newnomb1
        newnomb1 = largest
    except:
        newnomb1 = 0


print("The largest .png file in the current directory = " + str(newnomb1))
from PIL import ImageGrab
import keyboard

while True:
    try:
        if keyboard.is_pressed("print_screen"):
            # https://buildmedia.readthedocs.org/media/pdf/pynput/latest/pynput.pdf

            pos = queryMousePosition()
            print(pos)

            ratiod1 = 0.2
            ratiod2 = 0.3
            magicnumberw = ratiod1 * 1920
            magicnumberh = ratiod1 * 1080
            magicnumberw2 = ratiod2 * 1920
            magicnumberh2 = ratiod2 * 1080
            image = ImageGrab.grab(
                bbox=(
                    pt.x - magicnumberw,
                    pt.y - magicnumberh,
                    pt.x + magicnumberw2,
                    pt.y + magicnumberh2,
                )
            )
            newnomb1 = int(newnomb1) + 1
            image.save(str(newnomb1) + ".png")

            pass
        else:
            pass
    except:
        break