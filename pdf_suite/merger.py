import glob
import os
import shutil
import PyPDF2
import img2pdf
from pdf_suite.helper.file import File
from pdf_suite.helper.output import Output
from termspark import print

class Merger:
    order: list[str] = []

    def merge(self, input_directory: str, output: str, order: str) -> bool:
        if order:
            self.order = order.split(',')

        files: list[File] = self.__get_files(input_directory)
        files = self.__convert_images_to_pdfs(files)

        if (len(files) == 0):
            print(' No files to merge! ', 'white', 'guardsman red')

            return False

        pdfWriter = PyPDF2.PdfWriter()

        for file in files:
            with open(file.path, 'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                for pageNum in range(0, len(pdfReader.pages)):
                    pageObj = pdfReader.pages[pageNum]
                    pdfWriter.add_page(pageObj)

        with open(Output(output).path(), 'wb') as pdfOutput:
            pdfWriter.write(pdfOutput)

        print(' files merged successfully! ', 'black', 'screaming green')

        return True

    def __get_files(self, input_directory: str) -> list[File]:
        extensions: tuple[str, ...] = ('pdf', 'jpg', 'jpeg', 'png')
        files: list[File] = []

        if (len(self.order) == 0):
            for extension in extensions:
                for file_path in glob.glob(f"{input_directory}/*.{extension}"):
                    files.append(File(file_path))
        else:
            for path in self.order:
                file: File = File(os.path.join(input_directory, f"{path}"))

                for extension in extensions:
                    if not file.extension:
                        file.set_extension(extension)

                    if file.exists():
                        files.append(file)
                        break

        return files

    def __convert_images_to_pdfs(self, files: list[File]) -> list[File]:
        if not os.path.isdir('.temp'):
            os.makedirs('.temp')

        for index, file in enumerate(files):
            if file.is_image():
                pdf_file_path = os.path.join('.temp', f"{file.name}-{index}.pdf")
                with open(pdf_file_path, 'wb') as pdf_file:
                    pdf_file.write(img2pdf.convert(file.path))

                    files[index] = File(pdf_file_path)

        return files

    def __del__(self):
        if os.path.isdir('.temp'):
            shutil.rmtree('.temp')
