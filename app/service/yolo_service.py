import os
from os.path import join
from time import time
from typing import List, Tuple

from PIL import Image
from ultralytics import YOLO

from app.interface.detector import IDetector
from app.utils.file_manager import FileManager


class YoloService(IDetector):

    @staticmethod
    async def detect(image: Image, model_path: str, conf: float) -> List[Tuple[int, int, int, int]]:
        image_path = join("app", "tmp", f"{time()}.png")
        image.save(image_path)

        model = YOLO(model_path)
        results = model.predict(image_path, save=False, conf=conf)

        boxes = []
        for box in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            boxes.append((x1, y1, x2, y2))

        FileManager.remove(image_path)

        return boxes
