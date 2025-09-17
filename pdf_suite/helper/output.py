import os


class Output:
    def __init__(self, output: str):
        self._output = output

    def path(self) -> str:
        output_file: str = 'output.pdf'
        output_directory: str = self._output
        split: list[str] = output_directory.rsplit('/', 1)

        if '.' in split[1]:
            output_directory, output_file = split

        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)

        return os.path.join(output_directory, output_file)
