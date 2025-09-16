from typing import Optional

from pdf_suite.helper.output import Output
from .helper.percentage import Percentage
from .helper.filesize import FileSize
from pypdf import PdfWriter
from termspark import TermSpark

class Compress:
    def run(self, input: str, output: str, quality: Optional[int], max: Optional[float]) -> None:
        inputSize, inputSizeForHuman = FileSize(input).to_megabytes()
        TermSpark().set_width(40).print_left("Input size").print_right(inputSizeForHuman, "bright red").spark()

        quality = quality + 10 if quality else 100
        while True:
            quality = quality - 10
            self._to_quality(quality, input, output)

            if not max or quality <= 0 or FileSize(output).to_megabytes()[0] < max:
                break

            input = output
            print("Loading...", end='\r')

        outputSize, outputSizeForHuman = FileSize(output).to_megabytes()
        percentage = Percentage().part(inputSize - outputSize).whole(inputSize).humanize()

        TermSpark().set_width(40).print_left("Output size").spark_right([f"quality {quality} ", "gray"], [outputSizeForHuman, "pixie green"]).spark()
        TermSpark().set_width(40).print_left("Compressed by").print_right(percentage, "pixie green").spark()

        if max and outputSize > max:
            print()
            TermSpark().print_left(f" Could not compress to less than {max} MB! ", 'white', 'bright red').spark()

    def _to_quality(self, quality: int, input: str, output: str) -> None:
        writer = PdfWriter(clone_from=input)

        for page in writer.pages:
            for img in page.images:
                if img.image:
                    img.replace(img.image, quality=quality)

        with open(Output(output).path(), "wb") as f:
            writer.write(f)
