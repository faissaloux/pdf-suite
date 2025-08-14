from ..compress import Compress
from ..merger import Merger
from ..pdf2img import pdfToImage
import typer

class CommandLine:
    app = typer.Typer()

    def main(self):
        self.app()

    @app.command()
    def merge(
        input: str = typer.Option('input', '--input', '-i', help='Where all your files to merge reside.'),
        output: str = typer.Option('output', '--output', '-o', help='Where you gonna find the generated pdf.'),
        order: str = typer.Option(None, '--order', help='Order of your pdf files.'),
    ):
        Merger().merge(input, output, order)

    @app.command()
    def pdf2img(
        input: str = typer.Option(help='PDF file that you want to convert to image.'),
        output: str = typer.Option(help='Where you gonna find the extracted images.'),
    ):
        pdfToImage().run(input, output)

    @app.command()
    def compress(
        input: str = typer.Option('input', '--input', '-i', help='PDF file that you want to compress.'),
        output: str = typer.Option('output', '--output', '-o', help='Path where you will find the compressed PDF file.'),
        max: str = typer.Option(None, '--max', '-m', help='Maximum size (MB) you tolerate for the compressed file.'),
    ):
        Compress().run(input, output, max)
