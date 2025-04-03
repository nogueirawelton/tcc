from os.path import join

import cv2
from fastapi import APIRouter, UploadFile

from app.model.FloorPlan import FloorPlan
from app.service.ocr_service import OCRService
from app.service.yolo_service import YoloService
from app.utils.file_manager import FileManager
from app.service.pdf_service import PDFService


router = APIRouter()


@router.post("/")
async def root(file: UploadFile):
    # 1. Save Temporary PDF

    content = await file.read()
    doc = FileManager.save(content, file.filename)

    # 2. Do Something

    floor_plan = FloorPlan(doc)
    predict = await floor_plan.get_predict()

    # 4. Build Response

    return predict
