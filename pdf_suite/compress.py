import os
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

        inputSize = os.path.getsize(input) / (1024 * 1024)
        outputSize = os.path.getsize(output) / (1024 * 1024)
        percentage = ((inputSize - outputSize) * 100) / inputSize
        inputSizeText = str('%.2f' % inputSize) + " MB"
        outputSizeText = str('%.2f' % outputSize) + " MB"
        percentageText = str('%.2f' % percentage) + "  %"

        TermSpark().set_width(40).print_left("From").print_right(inputSizeText, "bright red").spark()
        TermSpark().set_width(40).print_left("To").print_right(outputSizeText, "pixie green").spark()
        TermSpark().set_width(40).print_left("Compressed by").print_right(percentageText, "pixie green").spark()
