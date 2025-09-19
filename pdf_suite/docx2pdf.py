from docx2pdf import convert
from pdf_suite.helper.output import Output
from termspark import print

class docxToPdf:
    def run(self, input: str, output: str) -> None:
        """
        Converts DOCX document to a PDF.
        """
        convert(input, Output(output).path())
        print(' DOCX converted to PDF successfully! ', 'black', 'screaming green')
