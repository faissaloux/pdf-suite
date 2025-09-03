import glob
import os
import shutil
import PyPDF2
import img2pdf
from pdf_suite.helper.file import File
from termspark import print

class Merger:
    order = []

    def merge(self, input_directory, output_directory, order):
        if order:
            self.order = order.split(',')

        files = self.__get_files(input_directory)
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

        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)

        with open(f"{output_directory}/output.pdf", 'wb') as pdfOutput:
            pdfWriter.write(pdfOutput)

        print(' files merged successfully! ', 'black', 'screaming green')

        return True

    def __get_files(self, input_directory):
        extensions = ('pdf', 'jpg', 'jpeg', 'png')
        files = []

        if (len(self.order) == 0):
            for ext in extensions:
                files.extend(File(glob.glob(f"{input_directory}/*.{ext}")))
        else:
            for file in self.order:
                for ext in extensions:
                    path = os.path.join(input_directory, f"{file}")
                    if not '.' in file:
                        path += f".{ext}"

                    if os.path.exists(path):
                        files.append(File(path))
                        break

        return files

    def __convert_images_to_pdfs(self, files):
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
