import os


class File:
    def __init__(self, file_path):
        self.path = file_path
        self.name = self.path.split(os.sep)[-1]
        self.extension = self.path.split('.')[-1] if '.' in self.path else None

    def set_extension(self, extension):
        self.path += f".{extension}"
        self.extension = extension

    def is_image(self):
        return self.extension in ('jpg', 'jpeg', 'png')

    def exists(self):
        return os.path.exists(self.path)
