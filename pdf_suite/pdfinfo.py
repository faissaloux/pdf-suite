from io import BufferedReader
from PyPDF2 import PdfReader
from termspark import TermSpark


class pdfInfo:
    _pdf_file: BufferedReader
    _reader: PdfReader

    def __init__(self, input: str):
        self._pdf_file = open(input, 'rb')
        self._reader = PdfReader(self._pdf_file)

    def pages_count(self) -> int:
        pages_count: int = len(self._reader.pages)
        TermSpark().set_width(40).print_left("Pages count").spark_right(pages_count, "gray").spark()

        return pages_count

    def __del__(self):
        self._pdf_file.close()
        self._reader = None
