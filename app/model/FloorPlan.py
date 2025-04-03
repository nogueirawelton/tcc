from os.path import join
from typing import List

from PIL import Image

from app.service.pdf_service import PDFService
from app.service.yolo_service import YoloService


class FloorPlan:
    __document: str
    __predict: str

    def __init__(self, document: str):
        self.__document = document

    async def get_predict(self):
        image = await PDFService.convert(self.__document)
        boxes = await YoloService.detect(image, "training/runs/short/weights/best.pt", 0.5)

        rooms = []

        for box in boxes:
            name, size = await PDFService.extract_rect_data(self.__document, box)

            windows = await YoloService.detect(image.crop(box), "training/runs/det_windows/weights/best.pt", 0.5)

            if name and size:
                rooms.append({
                    "name": name,
                    "size": size,
                    "windows": len(windows)
                })

        return rooms

