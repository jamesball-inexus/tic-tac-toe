class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, string):
        position = cls.parse_string(string)
        return cls(*position)

    @staticmethod
    def parse_string(string):
        try:
            return tuple((int(point) for point in string.split(',')))
        except ValueError:
            raise
