## Install
```bash
pip install pdf-suite
```

## Features
- Merge pdf files in one.
- PDF to Images.
- Compress PDF.

## Usage

### Merge
Merges multiple PDF files into one.

```bash
pdf_suite merge -i input -o output
```

#### In order
To merge your files in a specific order, you need to pass the order you want to `--order` option.

```bash
pdf_suite merge --input input --output output --order file1,file2,file3
```

#### Output
An `ouput.pdf` file will be generated in `/output` directory.

### PDF to Images
Extract images from your PDF file.

```bash
pdf_suite pdf2img --input input.pdf --output images_directory
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
