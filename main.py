import glob
import os

from merger import Merger

INPUT_DIRECTORY = 'input'
OUTPUT_DIRECTORY = 'output'

ORDER = [
    # pdf files in order.
]

pdf_files = []

if (len(ORDER) == 0):
    pdf_files = glob.glob(f"{INPUT_DIRECTORY}/*.pdf")
else:
    for file in ORDER:
        if not file.endswith('.pdf'):
            file = file + '.pdf'

        path = os.path.join(INPUT_DIRECTORY, file)

        if os.path.exists(os.path.exists(f"{INPUT_DIRECTORY}/{file}")):
            pdf_files.append(path)

Merger.merge(pdf_files, OUTPUT_DIRECTORY)
