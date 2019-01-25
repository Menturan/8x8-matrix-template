from time import sleep

from PIL import Image
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from matrix_images import OneMatrixImage
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(module)s.%(lineno)d:%(message)s',)

class Matrix:
    __MAX_CONTRAST = 255
    is_on = False

    def display(self, image: Image):
        logging.info("Change image...")
        if not self.is_on:
            self.device.contrast(0)
            self.device.show()
        self.__fade_out()
        view = image
        self.is_on = True
        self.device.display(view.convert(self.device.mode))
        self.__fade_in()

    def __fade_out(self):
        for i in range(self.__MAX_CONTRAST, 0, -3):
            self.device.contrast(i)
            sleep(0.01)

    def __fade_in(self):
        for i in range(0, self.__MAX_CONTRAST, 3):
            self.device.contrast(i)
            sleep(0.01)

    def turn_off_display(self):
        logging.info("Turn off display.")
        self.device.hide()
        self.is_on = False

    def __init__(self, port: int = 0, device: int = 0):
        try:
            logging.info("Setting up display...")
            serial = spi(port=port, device=device, gpio=noop())
            self.device = max7219(serial)
            self.device.clear()
            self.device.contrast(self.__MAX_CONTRAST)
            self.device.display(OneMatrixImage.HAPPY_SMILEY.convert(self.device.mode))
            self.is_on = True
        except KeyboardInterrupt:
            pass
