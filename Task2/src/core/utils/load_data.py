import os
from typing import List

import cv2
from ..configuration import DATABASE_CONF
from sklearn.datasets import fetch_olivetti_faces
import numpy as np


def load(database: str) -> List:
    database_data = []
    for group in range(DATABASE_CONF[database]["number_group"]):
        database_group = []
        for image in range(DATABASE_CONF[database]["number_img"]):
            print(DATABASE_CONF[database]["img_path"].format(g=group + 1, im=image + 1))
            if os.path.exists(DATABASE_CONF[database]["img_path"].format(g=group + 1, im=image + 1)):
                img = cv2.imread(
                    DATABASE_CONF[database]["img_path"].format(g=group + 1, im=image + 1),
                    -1,
                )
                database_group.append(img)

        database_data.append(database_group)

    print(np.array(database_data).shape)

    return database_data
