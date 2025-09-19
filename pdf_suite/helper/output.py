import os


class Output:
    _dir: str = ''
    _output: str

    def __init__(self, output: str):
        self._output = output

    def path(self) -> str:
        output_file: str = 'output.pdf'
        output_directory: str = self._output
        split: list[str] = output_directory.replace("/", os.sep).rsplit(os.sep, 1)

        if len(split) > 1 and '.' in split[1]:
            output_directory, output_file = split

        self._dir = output_directory
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)

        return os.path.join(output_directory, output_file)

    def dir(self) -> str:
        self.path()

        return self._dir
