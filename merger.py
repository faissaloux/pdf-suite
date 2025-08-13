import os
import PyPDF2
from termspark import print

class Merger:
    def merge(pdf_files, output_directory):
        if (len(pdf_files) == 0):
            print(' No PDF files to merge! ', 'white', 'guardsman red')

            return False

        pdfWriter = PyPDF2.PdfWriter()

        for filename in pdf_files:
            with open(filename, 'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                for pageNum in range(0, len(pdfReader.pages)):
                    pageObj = pdfReader.pages[pageNum]
                    pdfWriter.add_page(pageObj)

        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)

        with open(f"{output_directory}/output.pdf", 'wb') as pdfOutput:
            pdfWriter.write(pdfOutput)

        print(' PDF files merged successfully! ', 'black', 'screaming green')

        return True
