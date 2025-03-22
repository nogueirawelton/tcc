import os
from os.path import join
from time import time
from ultralytics import YOLO

from app.interface.detector import DetectionResult, IDetector


class YoloService(IDetector):

    @staticmethod
    async def detect(image_path, model_path: str, conf: float) -> DetectionResult:
        model = YOLO(model_path)
        results = model.predict(join("app", image_path), save=True, conf=conf)

        boxes = []
        for box in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            boxes.append((x1, y1, x2, y2))

        path = f'public/predicts/{time()}.png'
        results[0].save(join("app", path))

        return {
            "predict": path,
            "boxes": boxes
        }
