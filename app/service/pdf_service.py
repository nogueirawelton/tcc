import os
from os.path import join
from time import time
import pypdfium2 as pdfium
from app.interface.pdf_converter import IPDFConverter


class PDFService(IPDFConverter):
    @staticmethod
    async def convert(path: str) -> str:
        pdf = pdfium.PdfDocument(path)

        image = pdf[0].render(3).to_pil()

        path = f'public/uploads/{time()}.png'
        image.save(join("app", path))

        pdf.close()

        return path
