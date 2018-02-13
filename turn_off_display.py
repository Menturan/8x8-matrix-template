#!/usr/bin/python3
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219

print("Switching off matrix at 0.0.")
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
device.cleanup()
