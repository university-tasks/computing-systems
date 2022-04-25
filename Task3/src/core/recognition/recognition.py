from typing import Counter, List, Tuple

import numpy as np
from .classifiers import classifiers


def recognition(image: List) -> Tuple[dict, List]:
    print("PREDICTING")

    marks = {}
    descriptors = []

    for name, classifier in classifiers.items():
        mark_with_feature = classifier.predict(image)
        marks[name] = mark_with_feature[0][0]
        descriptors.append(classifier.plot(mark_with_feature[0][1]))

    

    print(f"MARKS: {marks}")

    return marks, descriptors
