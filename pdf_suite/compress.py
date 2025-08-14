from pdf_suite.helper.percentage import Percentage
from .helper.filesize import FileSize
from pypdf import PdfWriter
from termspark import TermSpark

class Compress:
    def run(self, input, output):
        writer = PdfWriter(clone_from=input)

        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality=80)

        with open(output, "wb") as f:
            writer.write(f)

        inputSize, inputSizeForHuman = FileSize(input).to_megabytes()
        outputSize, outputSizeForHuman = FileSize(output).to_megabytes()
        percentage = Percentage().part(inputSize - outputSize).whole(inputSize).humanize()

        TermSpark().set_width(40).print_left("From").print_right(inputSizeForHuman, "bright red").spark()
        TermSpark().set_width(40).print_left("To").print_right(outputSizeForHuman, "pixie green").spark()
        TermSpark().set_width(40).print_left("Compressed by").print_right(percentage, "pixie green").spark()
