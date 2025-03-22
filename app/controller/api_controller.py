from fastapi import APIRouter, UploadFile

from app.model.FloorPlan import FloorPlan
from app.service.yolo_service import YoloService
from app.utils.file_manager import FileManager
from app.service.pdf_service import PDFService


router = APIRouter()


@router.post("/")
async def root(file: UploadFile):
    # 1. Save Temporary PDF

    content = await file.read()
    pdf_path = FileManager.save(content, file.filename)

    # 2. Do Something

    image_path = await PDFService.convert(pdf_path)

    results = await YoloService.detect(image_path, "training/runs/det_all3/weights/best.pt", 0.3)

    # 3. Clean Files

    FileManager.remove(pdf_path)

    # 4. Build Response

    floor_plan = FloorPlan(image_path, results['predict'])

    return floor_plan.to_dict()
