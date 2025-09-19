import os
import platform
import subprocess
from docx2pdf import convert
from pdf_suite.helper.output import Output
from termspark import print

class docxToPdf:
    def run(self, input: str, output: str) -> None:
        """
        Converts DOCX document to a PDF.
        """

        system: str = platform.system()
        if system == "Linux":
            env = os.environ.copy()
            env["HOME"] = "/tmp"

            subprocess.run([
                "libreoffice",
                "--headless",
                "--convert-to", "pdf",
                "--outdir", Output(output).dir(),
                input
            ], check=True, env=env)

            outputfile = os.path.join(Output(output).dir(), input.rsplit(os.sep, 1)[1].rsplit('.', 1)[0] + '.pdf')
            os.rename(outputfile, Output(output).path())
        elif system in ("Windows", "Darwin"):
            convert(input, Output(output).path())
        else:
            raise RuntimeError(f"Unsupported system: {system}")

        print(' DOCX converted to PDF successfully! ', 'black', 'screaming green')
