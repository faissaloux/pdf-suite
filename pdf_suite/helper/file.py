import os


class File:
    def __init__(self, file_path):
        self.path = file_path
        self.name = self.path.split(os.sep)[-1]
        self.ext = self.path.split('.')[-1]

    def is_image(self):
        return self.ext in ('jpg', 'jpeg', 'png')
