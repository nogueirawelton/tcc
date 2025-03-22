from typing import List, Tuple, TypedDict
from abc import ABC, abstractmethod


class DetectionResult(TypedDict):
    predict: str
    boxes: List[Tuple[int, int, int, int]]


class IDetector(ABC):
    @staticmethod
    @abstractmethod
    def detect(image_path: str, model_path: str, conf: float) -> DetectionResult:
        ...
