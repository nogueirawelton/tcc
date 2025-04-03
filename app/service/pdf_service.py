from os.path import join
from time import time
from typing import Tuple

import fitz
import pypdfium2 as pdfium
from PIL import Image

from app.interface.pdf_converter import IPDFConverter
from app.utils.center_box import fix_bounding_box


class PDFService(IPDFConverter):
    @staticmethod
    async def convert(path: str) -> Image:
        pdf = pdfium.PdfDocument(path)

        image = pdf[0].render(1).to_pil()

        pdf.close()

        return image

    @staticmethod
    async def extract_rect_data(path_pdf: str, box: Tuple[int, int, int, int]):

        rect = fitz.Rect(fix_bounding_box(box))

        doc = fitz.open(path_pdf)
        page = doc.load_page(0)

        text = page.get_text("text", clip=rect).strip()

        return text.split("\n")[:2] if text else ["", ""]
