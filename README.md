## Install
```bash
pip install pdf-suite
```

## Features
- Merge pdf files in one.
- PDF to Images.

## Usage

### Merge
Merges multiple PDF files into one.

#### In order
To merge your files in a specific order, specify your files in the order you want in `ORDER` array in `merger.py` file.

```python
ORDER = [
    'file1.pdf',
    'file2.pdf',
    'file3.pdf',
]
```

#### Run
```bash
pdf_suite merge -i input -o output
```

#### Output
An `ouput.pdf` file will be generated in `/output` directory.

### PDF to Images
Extract images from your PDF file.

#### Run
```bash
pdf_suite pdf2img --input file.pdf --output images_directory
```

#### Output
An `images_directory` directory will be generated with all images from `file.pdf`.
