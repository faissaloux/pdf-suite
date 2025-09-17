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
        self=None,  # type: ignore
        input: str = typer.Option('input', '--input', '-i', help='Where all your files to merge reside.'),
        output: str = typer.Option('output', '--output', '-o', help='Where you gonna find the generated pdf.'),
        order: str = typer.Option(None, '--order', help='Order of your pdf files.'),
    ) -> None:
        Merger().merge(input, output, order)

    @app.command()
    def pdf2img(
        self=None,  # type: ignore
        input: str = typer.Option(help='PDF file that you want to convert to image.'),
        output: str = typer.Option(help='Where you gonna find the extracted images.'),
        page: int = typer.Option(None, '--page', '-p', help='The page number that you want.'),
    ) -> None:
        if page <= 0:
            raise ValueError("page should be greater than 0")

        pdfToImage().page(page).run(input, output)

    @app.command()
    def compress(
        self=None,  # type: ignore
        input: str = typer.Option('input', '--input', '-i', help='PDF file that you want to compress.'),
        output: str = typer.Option('output.pdf', '--output', '-o', help='Path where you will find the compressed PDF file.'),
        quality: int = typer.Option(None, '--quality', '-q', help='Quality of the compressed file.'),
        max: str = typer.Option(None, '--max', '-m', help='Maximum size (MB) you tolerate for the compressed file.'),
    ) -> None:
        if not quality and not max:
            raise TypeError("At least one of the two should be provided: quality or max")

        if quality and max:
            raise TypeError("Only one of the two should be provided: quality or max")

        if quality and quality <=0:
            raise ValueError("quality should be greater than 0")

        Compress().run(
            input,
            output,
            int(quality) if quality else None,
            float(max) if max else None
        )
