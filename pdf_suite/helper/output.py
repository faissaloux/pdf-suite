import os


class Output:
    def __init__(self, output: str):
        self.output = output        

    def path(self) -> str:
        output_file: str = 'output.pdf'
        output_directory: str = self.output

        if output_directory.endswith('.pdf'): 
            output_directory, output_file = output_directory.rsplit(os.sep, 1)

        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)

        return os.path.join(output_directory, output_file)
