## Install
```bash
pip install pdf-suite
```

## Features
- Merges multiple PDF files / images into one PDF file.
- PDF to Images.
- Compress PDF.
- Convert DOCX to PDF.

## Usage

### Merge
Merges multiple PDF files / images into one PDF file (output.pdf).

```bash
pdf_suite merge -i input -o output.pdf
```

#### In order
To merge your files in a specific order, you need to pass the order you want to `--order` option.

```bash
pdf_suite merge --input input --output output.pdf --order file1.pdf,file2,file3.jpg
```

#### Output
An `ouput.pdf` file will be generated in `/output` directory.

### PDF to Images
Extract images from your PDF file.

```bash
pdf_suite pdf2img --input input.pdf --output images_directory
```

Zip extracted images from your PDF file using `--zip`.

```bash
pdf_suite pdf2img --input input.pdf --output images_directory --zip
```

You can also extract images from specific page.

```bash
pdf_suite pdf2img --input input.pdf --output images_directory --page 2
```

#### Output
An `images_directory` directory will be generated with all images from `file.pdf`.

### Compress PDF
Compress a PDF file.

```bash
pdf_suite compress --input input.pdf --output output.pdf
```

#### Compress to a maximum size
You can specify the maximum size (MB) you need.

```bash
pdf_suite compress --input input.pdf --output output.pdf --max 2
```

`input.pdf` will be compressed to `output.pdf` with less than 2MB.

#### Output
A compressed PDF file `output.pdf` will be generated for you.

### Convert DOCX to PDF
Convert DOCX document to a PDF.

```bash
pdf_suite docx2pdf --input input.docx --output output.pdf
```