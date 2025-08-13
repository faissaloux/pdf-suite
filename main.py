import typer

from merger import Merger

app = typer.Typer()

@app.command()
def merge(
    input: str = typer.Option('input', "--input", "-i", help="Where all your files to merge reside."),
    output: str = typer.Option('output', "--output", "-o", help="Where you gonna find the generated pdf.")
):
    Merger().merge(input, output)

if __name__ == "__main__":
    app()
