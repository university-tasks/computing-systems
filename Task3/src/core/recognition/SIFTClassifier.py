from typing import List

import cv2
import numpy as np
from .BaseRecognizer import BaseClassifier


class SIFTClassifier(BaseClassifier):
    def get_features(self, image: np.ndarray) -> List:
        # convert to grayscale image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # initialize SIFT object
        sift = cv2.SIFT_create()

        _, desc= sift.detectAndCompute(gray, None)

        desc = cv2.resize(desc, (300, 300))
        desc = desc.reshape(300, 300)

        return desc