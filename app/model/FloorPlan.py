from typing import List


class FloorPlan:
    __image: str
    __predict: str

    def __init__(self, image_path: str, predict_path: str):
        self.__image = image_path
        self.__predict = predict_path

    def to_dict(self):
        return {
            "image": self.__image,
            "predict": self.__predict
        }
