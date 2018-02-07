#!/usr/bin/python3
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image
import time
import threading

happy = Image.open("images/smiley_happy.png")
sad = Image.open("images/smiley_sad.png")
meh = Image.open("images/smiley_meh.png")
very_happy = Image.open("images/smiley_very_happy.png")
heart = Image.open("images/heart.png")

def display():
    print("Setting up display...")
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial)
    global view
    view = happy
    while True:
        device.display(view.convert(device.mode))

def main():
    global view
    while True:
        view = sad
        time.sleep(5)
        view = meh
        time.sleep(5)

if __name__ == "__main__":
    try:
        t_d = threading.Thread(target=display)
        t_d.start()
        t_m = threading.Thread(target=main)
        t_m.start()
    except KeyboardInterrupt:
        pass
    except e:
        print (e)

