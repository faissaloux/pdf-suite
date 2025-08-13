### Install
```bash
pip install -r requirements.txt
```

### Features
- Merge pdf files in one.

### Usage

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
python main.py -i input -o output
```

#### Output
An `ouput.pdf` file will be generated in `/output` directory.
