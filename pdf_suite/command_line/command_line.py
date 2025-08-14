from ..merger import Merger
from ..pdf2img import pdfToImage
import typer

class CommandLine:
    app = typer.Typer()

    def main(self):
        self.app()

    @app.command()
    def merge(
        input: str = typer.Option('input', "--input", "-i", help="Where all your files to merge reside."),
        output: str = typer.Option('output', "--output", "-o", help="Where you gonna find the generated pdf.")
    ):
        Merger().merge(input, output)

    @app.command()
    def pdf2img(
        input: str = typer.Option(help="PDF file that you want to convert to image."),
        output: str = typer.Option(help="Where you gonna find the extracted images.")
    ):
        pdfToImage().run(input, output)
