from fastapi import APIRouter, UploadFile

from app.utils.file_manager import FileManager
from app.services.pdf_processor import PDFProcessor


router = APIRouter()


@router.post("/")
async def root(file: UploadFile):
    fm = FileManager()
    pp = PDFProcessor()

    # 1. Save Temporary PDF
    content = await file.read()
    pdf_path = fm.save(content, file.filename)

    # 2. Do Something

    image_path = await pp.convert(pdf_path)

    # 3. Delete Files

    fm.remove(pdf_path)

    return {"message": image_path}
