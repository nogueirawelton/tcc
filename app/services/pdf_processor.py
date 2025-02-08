import gc
import os

import pypdfium2 as pdfium


class PDFProcessor:
    def __init__(self, dpi=300, base_path="app/temp"):
        self.base_path = base_path
        self.dpi = dpi

    async def convert(self, pdf_path):
        pdf = pdfium.PdfDocument(pdf_path)
        image = pdf[0].render(scale=self.dpi / 300).to_pil()

        path = os.path.join(self.base_path, 'doc.png')
        image.save(path)

        del pdf
        gc.collect()

        return path
