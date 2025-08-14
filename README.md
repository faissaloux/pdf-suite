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

```bash
pdf_suite merge -i input -o output
```

#### In order
To merge your files in a specific order, you need to pass the order you want to `--order` option.

```bash
pdf_suite merge -i input -o output --order file1,file2,file3
```

#### Output
An `ouput.pdf` file will be generated in `/output` directory.

### PDF to Images
Extract images from your PDF file.

```bash
pdf_suite pdf2img --input file.pdf --output images_directory
```

#### Output
An `images_directory` directory will be generated with all images from `file.pdf`.
