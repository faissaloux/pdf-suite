NAME = pdf_suite
PYTHON = python3

clean:
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf *_cache
	find $(NAME) -type d -name '__pycache__' -exec rm -rf {} +

install: clean
	pip install -e ."[dev]"

build: clean
	$(PYTHON) setup.py bdist_wheel

lint: mypy

mypy:
	mypy --show-error-codes $(NAME)