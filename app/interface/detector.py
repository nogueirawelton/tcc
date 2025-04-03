from typing import List, Tuple, TypedDict
from abc import ABC, abstractmethod


class IDetector(ABC):
    @staticmethod
    @abstractmethod
    def detect(image_path: str, model_path: str, conf: float) -> List[Tuple[int, int, int, int]]:
        ...
