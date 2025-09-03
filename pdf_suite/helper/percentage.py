class Percentage:
    def part(self, value):
        self._part = value

        return self

    def whole(self, value):
        self._whole = value

        return self

    def humanize(self) -> str:
        perc = (self._part * 100) / self._whole

        return str('%.2f' % perc) + '  %'
