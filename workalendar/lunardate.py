import datetime
import warnings


class LunarDate:

    def __init__(self, y, m, d):
        self.date = datetime.date(y, m, d)

    def toSolarDate(self):
        warnings.warn(
            'lunardate support is not available, see: '
            'https://github.com/peopledoc/workalendar/issues/346')
        return self.date
