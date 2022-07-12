import os
from glob import glob
from pathlib import Path


class Input:
    def __init__(self, path: str):
        self.path = Path(path)
        if self.path.exists():
            print()
            for file in glob(f"*.jpg"):
                print(file)
