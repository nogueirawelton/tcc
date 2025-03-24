import fitz  # PyMuPDF
from typing import List, Tuple, Dict


class OCRService:

    @staticmethod
    def reduzir_box(x1, y1, x2, y2, margem=0.05):
        largura = x2 - x1
        altura = y2 - y1

        if largura < 10 or altura < 10:
            return None

        x1 += int(largura * margem)
        y1 += int(altura * margem)
        x2 -= int(largura * margem)
        y2 -= int(altura * margem)

        return x1, y1, x2, y2

    @staticmethod
    def _extrair_texto_pdf(path_pdf: str, boxes: List[Tuple[int, int, int, int]] = None) -> List[Dict[str, any]]:
        resultados = []

        # ✅ Abre o PDF
        doc = fitz.open(path_pdf)

        for num_pagina in range(len(doc)):
            pagina = doc.load_page(num_pagina)

            # ✅ Extrai o texto com as bounding boxes
            textos = pagina.get_text("blocks")

            for (x1, y1, x2, y2, texto, _, _) in textos:
                if texto.strip():
                    if boxes:
                        for (bx1, by1, bx2, by2) in boxes:
                            # ✅ Verifica se a bounding box externa cobre o texto detectado
                            if bx1 <= x1 and by1 <= y1 and bx2 >= x2 and by2 >= y2:
                                resultados.append({
                                    "texto": texto.strip(),
                                    "coords": (int(x1), int(y1), int(x2), int(y2)),
                                    "pagina": num_pagina + 1
                                })
                    else:
                        resultados.append({
                            "texto": texto.strip(),
                            "coords": (int(x1), int(y1), int(x2), int(y2)),
                            "pagina": num_pagina + 1
                        })

        doc.close()

        return resultados

    @staticmethod
    def extrair_texto(path_pdf: str, boxes: List[Tuple[int, int, int, int]] = None) -> List[Dict[str, any]]:
        resultados = []

        if path_pdf:
            print(f"📄 Extraindo texto do PDF: {path_pdf}")
            # ✅ Extrai diretamente do PDF usando PyMuPDF
            resultados_pdf = OCRService._extrair_texto_pdf(path_pdf, boxes)
            resultados.extend(resultados_pdf)
            print(f"✅ {len(resultados_pdf)} textos extraídos diretamente do PDF")

        return resultados
