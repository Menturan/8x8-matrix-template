#!/usr/bin/python3
from time import sleep

from matrix_driver import Matrix
from matrix_images import OneMatrixImage

mx = Matrix()
try:
    print("Press Ctrl+C to exit...")
    while True:
        mx.display(OneMatrixImage.MEH_SMILEY)
        sleep(0.5)
        mx.display(OneMatrixImage.HEART)
        sleep(0.5)
        mx.display(OneMatrixImage.VERY_HAPPY_SMILEY)
        sleep(0.5)
        mx.display(OneMatrixImage.SAD_SMILEY)
        sleep(0.5)
        mx.display(OneMatrixImage.HEART)
        sleep(0.5)
except KeyboardInterrupt:
    pass

