from .helper.percentage import Percentage
from .helper.filesize import FileSize
from pypdf import PdfWriter
from termspark import TermSpark

class Compress:
    def run(self, input: str, output: str, max: float) -> None:
        quality: int = 90

        inputSize, inputSizeForHuman = FileSize(input).to_megabytes()
        TermSpark().set_width(40).print_left("Input size").print_right(inputSizeForHuman, "bright red").spark()

        while True:
            quality = quality - 10
            writer = PdfWriter(clone_from=input)

            for page in writer.pages:
                for img in page.images:
                    if img.image:
                        img.replace(img.image, quality=quality)

            with open(output, "wb") as f:
                writer.write(f)

            if not max or quality <= 0 or FileSize(output).to_megabytes()[0] < max:
                break

            input = output
            print("Loading...", end='\r')

        outputSize, outputSizeForHuman = FileSize(output).to_megabytes()
        percentage = Percentage().part(inputSize - outputSize).whole(inputSize).humanize()

        TermSpark().set_width(40).print_left("Output size").print_right(outputSizeForHuman, "pixie green").spark()
        TermSpark().set_width(40).print_left("Compressed by").print_right(percentage, "pixie green").spark()

        if max and outputSize > max:
            print()
            TermSpark().print_left(f" Could not compress to less than {max} MB! ", 'white', 'bright red').spark()
