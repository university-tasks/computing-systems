from typing import Callable, List, Tuple
from .utils.dist import dist

import numpy as np


class Classifier:
    def __init__(self, method: Callable) -> None:
        self.method = method
        self.train_data: List = []

    def __get_features(self, image: List) -> List:
        return self.method(image, self.param)[1]

    def __search(self, test: np.array) -> Tuple:
        d_min = float("inf")
        template_min = None
        template_group = None
        for train, group in self.train_data:
            d = dist(train, test)
            if d < d_min:
                d_min = d
                template_min = train
                template_group = group
        return template_min, template_group

    def fit(self, X: List, y: List, param: int) -> None:
        self.param = param
        train_data = []
        for index, image in enumerate(X):
            train_data.append((self.__get_features(image), y[index]))
        self.train_data = train_data

    def predict(self, images: List) -> List:
        predicted_groups = []
        for image in images:
            image_features = self.__get_features(image)
            _, group_num = self.__search(image_features)
            predicted_groups.append(group_num)
        return predicted_groups

    def accuracy(self, true_answers: List, predicted_answers: List) -> float:
        if len(true_answers) != len(predicted_answers):
            raise Exception("Arguments have different length")
        number_true = 0
        for index, ta in enumerate(true_answers):
            if ta == predicted_answers[index]:
                number_true += 1
        if len(predicted_answers) == 0:
            return 0

        return number_true / len(predicted_answers)
