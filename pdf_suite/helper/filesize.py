import os


class FileSize:
    _size: float = 0
    _unit: str = 'B'

    def __init__(self, file: str):
        self._size = os.path.getsize(file)

    def to_megabytes(self) -> tuple[float, str]:
        self._unit = 'MB'
        self._size = self._size / (1024 * 1024)

        return self._size, self.humanize()

    def humanize(self) -> str:
        return str('%.2f' % self._size) + ' ' + self._unit
