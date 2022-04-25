from typing import List
from .BaseRecognizer import BaseClassifier
import numpy as np
import cv2



class ORBClassifier(BaseClassifier):
   

    def get_features(self, image: np.ndarray) -> List:
        orb = cv2.ORB_create()
        # find the keypoints with ORB
        kp = orb.detect(image,None)
        # compute the descriptors with ORB
        kp, des = orb.compute(image, kp)

        des = cv2.resize(des, (300, 300))
        des = des.reshape(300, 300)

        return des