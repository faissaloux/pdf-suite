import fitz
from typing import Any

class Thumbnail:
    _pdf_file: Any

    def extract(self, input: str, output: str):
        self._pdf_file = fitz.open(input)
        page = self._pdf_file.load_page(0)
        zoom = 1

        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        pix.save(output)

    def __del__(self):
        self._pdf_file.close()
        self._reader = None
