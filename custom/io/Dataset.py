from os import listdir
from os.path import isfile

from PIL import Image

from .Input import *


class Dataset:
    def __init__(self):
        pass

    def load(self, path: str, extension=".png"):
        self.input = Input(path)
        print(f"Loading dataset from {self.input.path.absolute()}")
        # image = Image.open(path)
        # print(image.getdata())

        # print(path)
        return self
