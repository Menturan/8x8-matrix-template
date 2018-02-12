from PIL import Image
import os


class ImageConstant:
    def __init__(self, value=None):
        self.value = value

    def __get__(self, instance, owner) -> Image:
        return Image.open(os.path.dirname(__file__) + "/" + self.value)

    def __set__(self, instance, value):
        raise ValueError("You can't change a constant")


class OneMatrixImage:
    HAPPY_SMILEY = ImageConstant("images_files/smiley_happy.png")
    SAD_SMILEY = ImageConstant("images_files/smiley_sad.png")
    MEH_SMILEY = ImageConstant("images_files/smiley_meh.png")
    VERY_HAPPY_SMILEY = ImageConstant("images_files/smiley_very_happy.png")
    HEART = ImageConstant("images_files/heart.png")
