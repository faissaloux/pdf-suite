from typing import Any, Optional
import zipfile
from typing_extensions import Self  # For Python <3.11.
import fitz
import os
from termspark import print

from pdf_suite.helper.output import Output

class pdfToImage:
    _pdfFile: Any
    _page: Optional[int]
    _output_folder: str

    def run(self, pdf_path: str, output_folder: str, zipped: bool):
        """
        Extracts all images from a PDF and saves them to a specified folder.
        """
        self._output_folder = output_folder

        self._pdfFile = fitz.open(pdf_path)

        if self._page:
            self._extract_images_from_page(self._page)
        else:
            for page_index in range(len(self._pdfFile)):
                self._extract_images_from_page(page_index + 1)

        self._pdfFile.close()

        if zipped:
            self._zip_output()

    def page(self, page: int) -> Self:
        self._page = page

        return self

    def _extract_images_from_page(self, page_number: int) -> None:
        if page_number > len(self._pdfFile):
            print(f" Page {page_number} not found! Only {len(self._pdfFile)} disponible. ", 'white', 'guardsman red')
            exit(1)

        pdf_page = self._pdfFile[page_number - 1]
        image_list = pdf_page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = self._pdfFile.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_filename = os.path.join(self._output_folder, f"page{page_number}_img{img_index + 1}.{image_ext}")
            with open(Output(image_filename).path(), "wb") as f:
                f.write(image_bytes)

    def _zip_output(self) -> None:
        zip_file = os.path.join(self._output_folder, "output.zip")
        with zipfile.ZipFile(Output(zip_file).path(), "w") as zipf:
            for image in os.listdir(self._output_folder):
                if not '.zip' in image:
                    image_path = os.path.join(self._output_folder, image)
                    zipf.write(image_path, arcname=os.path.basename(image_path))

        for file in os.listdir(self._output_folder):
            if not '.zip' in file:
                os.remove(os.path.join(self._output_folder, file))
