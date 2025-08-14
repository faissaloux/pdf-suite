import glob
import os
import PyPDF2
from termspark import print

class Merger:
    ORDER = [
        # pdf files in order.
    ]

    def merge(self, input_directory, output_directory):
        pdf_files = self.__get_pdf_files(input_directory)

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

    def __get_pdf_files(self, input_directory):
        pdf_files = []

        if (len(self.ORDER) == 0):
            pdf_files = glob.glob(f"{input_directory}/*.pdf")
        else:
            for file in self.ORDER:
                if not file.endswith('.pdf'):
                    file = file + '.pdf'

                path = os.path.join(input_directory, file)

                if os.path.exists(os.path.exists(f"{input_directory}/{file}")):
                    pdf_files.append(path)

        return pdf_files
