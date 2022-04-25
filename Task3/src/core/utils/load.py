
from typing import List
from ..config import DATABASES
import os
import cv2


def load() -> List:
    data = []
    for style in DATABASES:
        for filename in os.listdir(DATABASES[style]):
            f = os.path.join(DATABASES[style], filename)
            img = cv2.imread(f)
            data.append((img, style))
    return data